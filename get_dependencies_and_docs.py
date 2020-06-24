#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Recursively determine the execute and $include dependencies as of a
whitelist of manually executed GAMS scripts. Report any problems encountered
and, for each GAMS script in this dependency tree, generate a reStructuredText
file containing dependency links as well as any ***-delimited reStructuredText
doc-comments in the script. The reStructuredText text files can subsequently be
fed to Sphinx to generate a variety of document formats.

When a GAMS script starts with with *** delimited reStructuredText comment,
this first comment is output as a header before any dependency links. This
header comment is therefore a good place to provide a brief synopsis of
what the script is for.

BEWARE: the parser is a quick-and-dirty regexp implementation that does not
handle the full GAMS syntax. As such it is not guaranteed to catch all
dependencies. In particular %variable% expansion in paths is not handled.

NOTE: absolute paths are not handled, paths should be relative to the current directory (CD)
of the containing script. What constitutes the CD of a script is inferred as follows:
* Top-level scripts are ASSUMED to have their containing directory as CD.
* $included scripts have the CD of the including script as CD.
* executed scripts have the CD of the executing script as CD when no cDir or curDir parameter is set.
* executed scripts have the CD of the executing script joined with the cDir/curDir parameter as CD.

NOTE: execute statements that are commented-out with a leading * are parsed
and the executed file is added to the dependency tree. This is done because it is
common practice to comment-out execute statements, e.g. in 0_executebatch.gms.

BEWARE: $include and execute statements that are block-commented out through $ONTEXT
and $OFFTEXT are NOT included in the dependency scan. Before running this script,
pay particular attention to the 0_executebatch* scripts and remove any block
comments that deactivate sets of execute/execute_abort statements.
"""
__author__ = "Albert Brouwer"

import errno
import os
import re
import shutil
from fileinput import FileInput

GENERATE_REST = True
WARN_MULTI_CD_INCLUDE = False
LINK_EXECUTED_BY = False # Causes recursion overrun

ROOT = '..' # directory containing GLOBIOM branch/tag/trunk
if not os.path.exists(ROOT):
    raise RuntimeError(f"Root directory at '{ROOT}' does not exist")

# Whitelist of manually executed scripts
MANUALLY_EXECUTED_SCRIPTS = [
    "Data/0_executebatch_total.gms",
    "Model/0_executebatch.gms",
]

rest_pattern                   = re.compile('[*] (.*)$')
ontext_pattern                 = re.compile('\$ontext\s*$', re.IGNORECASE)
offtext_pattern                = re.compile('\$offtext\s*$', re.IGNORECASE)
quoted_include_path_pattern    = re.compile('\$(bat)?include\s+"([^"]+)"\s', re.IGNORECASE) # match early
quoted_if_include_path_pattern = re.compile('\$if\s.*\s\$(bat)?include\s+"([^"]+)"\s', re.IGNORECASE) # match early
include_path_pattern           = re.compile('\$(bat)?include\s+(\S+)\s', re.IGNORECASE)
if_include_path_pattern        = re.compile('\$if\s.*\s\$(bat)?include\s+(\S+)\s', re.IGNORECASE)
execute_gams_pattern           = re.compile("""(\*)?\s*execute(\.async)?\s+["']gams\s+(\S+)(\s.*)""", re.IGNORECASE)
execute_abort_pattern          = re.compile("""(\*)?\s*execute_(abort)\(\s*["']gams\s+(\S+)(\s.*)""", re.IGNORECASE)
cdir_pattern                   = re.compile('\s+cdir=(\S+)[\s"]', re.IGNORECASE)
curdir_pattern                 = re.compile('\s+curdir=(\S+)[\s"]', re.IGNORECASE)
file_put_pattern               = re.compile("""\s*files?\s+\S+\s+/\s*"?'?(\S.*\S)'?"?\s*/""", re.IGNORECASE)

def ScriptDict(cd):
    """Instantiate a dictionary for holding GAMS script info"""
    return {
        'scanned': False,
        'cd': cd,
        '$includes': [],
        'missing_$includes': [],
        '$included_by': [],
        'executes': [],
        'commented_executes': [],
        'missing_executes': [],
        'executed_by': [],
        'files': [],
        'rest_header': '',
        'rest': '',
    }

def Missing(line_number, line, missing_path):
    """ Instantiate a dictionary for holding info on a potentially missing file: not in repo, but might be generated"""
    return {
        'line_number': line_number,
        'line': line,
        'path': missing_path,
    }

def mkdir(d):
    """Make a directory if it doesn't already exist"""
    if not os.path.exists(d):
        try:
            os.makedirs(d)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def join_and_normalize(path1, path2):
    """Platform-agnostic %X%-substitution-aware path join and normalization"""
    path1 = path1.replace('\\', '/').replace('%X%', '/')
    path2 = path2.replace('\\', '/').replace('%X%', '/')
    joined_path = os.path.join(path1, path2).replace('\\', '/')
    return os.path.normpath(joined_path).replace('\\', '/')
                
def parse_directives(script_paths_dict, path, script_dict, line, line_number):
    """Parse $include, execute, and file/put directives and update the
    dependency tree as encoded in script_paths_dict"""
    if '$include' in line.lower():
        # Handle $include directive
        match = quoted_include_path_pattern.match(line)
        if not match:
            match = quoted_if_include_path_pattern.match(line)
            if not match:
                match = include_path_pattern.match(line)
                if not match:
                    match = if_include_path_pattern.match(line)
        if not match:
            if (line[:8].lower() == '$include' or line[:3].lower() == '$if'):
                raise RuntimeError(f"Unmatchable include in {path}: {line}")
            else:
                # Presumably commented out
                return
        include_path = join_and_normalize(script_dict['cd'], match.group(2))
        if include_path.find('%') >= 0:
            print(f"WARNING: cannot handle %variable% expansion in $include statement on line {line_number} of file {path}:")
            print(f"    {line}", end='')
        else:
            if not os.path.exists(os.path.join(ROOT, include_path)):
                if os.path.exists(os.path.join(ROOT, include_path+'.gms')):
                    print(f"WARNING: path is missing a .gms extension in $include statement on line {line_number} of file {path}:")
                    print(f"    {line}", end='')
                    include_path += '.gms'
            if not os.path.exists(os.path.join(ROOT, include_path)):
                script_dict['missing_$includes'].append(Missing(line_number, line, include_path))
            else:
                if include_path[-4:].lower() == '.csv':
                    return
                elif include_path[-4:].lower() == '.gms':
                    if include_path not in script_dict['$includes']:
                        script_dict['$includes'].append(include_path)
                    if include_path in script_paths_dict:
                        if WARN_MULTI_CD_INCLUDE and script_paths_dict[include_path]['cd'] != script_dict['cd']:
                            print(f"WARNING: file {include_path} $included from another current directory on line {line_number} of file {path}:")
                            print(f"    current current directory: {script_dict['cd']}")
                            print(f"    earlier current directory: {script_paths_dict[include_path]['cd']}")
                    else:
                        script_paths_dict[include_path] = ScriptDict(script_dict['cd']) # an $included script runs with the current directory of the $including script
                    if path not in script_paths_dict[include_path]['$included_by']:
                        script_paths_dict[include_path]['$included_by'].append(path)
                else:
                    print(f"ERROR: file {include_path} with unknown extension $included on line {line_number} of file {path}:")
    else:
        # Handle execute directive
        match = execute_gams_pattern.match(line)
        if not match:
            match = execute_abort_pattern.match(line)
        if match:
            # Executing script's CD is inherited or modified by cDir or curDir relative paths.
            cd = script_dict['cd']
            # Extract any cDir or curDir parameter and joins it with the executing script's CD.
            options = match.group(4)
            cd_match = cdir_pattern.search(options)
            if not cd_match:
                cd_match = curdir_pattern.search(options)
            if cd_match:
                cd = join_and_normalize(cd, cd_match.group(1))
            # Determine the normalized path of the script being executed
            execute_path = join_and_normalize(cd, match.group(3))
            if execute_path.find('%') >= 0:
                print(f"WARNING: cannot handle %variable% expansion in GAMS file execute statement on line {line_number} of file {path}:")
                print(f"    {line}", end='')
            else:
                if execute_path[-4:].lower() == '.gms':
                    if os.path.exists(os.path.join(ROOT, execute_path)):
                        if match.group(1):
                            # Execute statement is commented out
                            if execute_path not in script_dict['executes']:
                                if execute_path not in script_dict['commented_executes']:
                                    script_dict['commented_executes'].append(execute_path)
                        else:
                            # Execute statement not commented out
                            if execute_path not in script_dict['executes']:
                                script_dict['executes'].append(execute_path)
                            if execute_path in script_dict['commented_executes']:
                                script_dict['commented_executes'].remove(execute_path)
                        if execute_path in script_paths_dict:
                            if script_paths_dict[execute_path]['cd'] != cd:
                                print(f"WARNING: file {execute_path} executed from another current directory on line {line_number} of file {path}")
                                print(f"    current current directory: {cd}")
                                print(f"    earlier current directory: {script_paths_dict[execute_path]['cd']}")
                        else:
                            script_paths_dict[execute_path] = ScriptDict(cd)
                        if path not in script_paths_dict[execute_path]['executed_by']:
                            script_paths_dict[execute_path]['executed_by'].append(path)
                    else:
                        # If not commented-out, complain about non-existence of executed file
                        if not match.group(1):
                            script_dict['missing_executes'].append(Missing(line_number, line, execute_path))
                else:
                    # If not commented-out, complain about lack of .gms extension
                    if not match.group(1):
                        print(f"ERROR: .gms extensionless file {execute_path} executed from line {line_number} of file {path}")
        # Handle file directive
        match = file_put_pattern.match(line)
        if match:
            file_put_path = join_and_normalize(script_dict['cd'], match.group(1))
            if file_put_path.find('%') >= 0:
                print(f"WARNING: cannot handle %variable% expansion in GAMS file put statement on line {line_number} of file {path}:")
                print(f"    {line}", end='')
            else:
                if path not in script_dict['files']:
                    script_dict['files'].append(file_put_path)
                                
def scan_script(path, script_paths_dict):
    """Scan a GAMS script, extract any reStructured text, and update dependency tree
    as encoded in script_paths_dict"""
    script_dict = script_paths_dict[path]
    with open (os.path.join(ROOT, path), 'rt', encoding='ISO-8859-1') as gams_file:
        line_number = 0
        rest_comment = False
        rest_header = False
        block_comment = False
        for line in gams_file:
            line_number += 1
            # Extract reStructuredText comments
            if rest_comment:
                match = rest_pattern.match(line.rstrip())
                if match:
                    # Some text on the line after the *
                    if rest_header:
                        script_dict['rest_header'] += match.group(1)+'\n'
                    else:
                        script_dict['rest'] += match.group(1)+'\n'
                elif line.rstrip() == '*':
                    # No text on the line after the *
                    if rest_header:
                        script_dict['rest_header'] += '\n'
                    else:
                        script_dict['rest'] += '\n'
                else:
                    # Something other than a line starting with a single *
                    if rest_header:
                        script_dict['rest_header'] += '\n'
                        rest_header = False
                    else:
                        script_dict['rest'] += '\n'
                    rest_comment = False
            else:
                if line.rstrip() == '***':
                    rest_comment = True
                    if line_number == 1:
                        rest_header = True
            # Extract dependencies outside block comments
            if block_comment:
                if offtext_pattern.match(line):
                    block_comment = False
                    continue
            else:
                if ontext_pattern.match(line):
                    block_comment = True
                    continue
                # Not inside a block comment
                parse_directives(script_paths_dict, path, script_dict, line, line_number)
    script_dict['scanned'] = True

if __name__ == '__main__':
    # Walk the source tree and collect the paths of GAMS files in a dictionary
    gams_paths_dict = {}
    for dirpath, dirs, files in os.walk(ROOT):
        for file in files:
            if file[-4:].lower() == '.gms':
                # Found a GAMS file
                gams_rel_file_path = os.path.relpath(os.path.join(dirpath, file), start=ROOT).replace('\\', '/')
                gams_paths_dict[gams_rel_file_path] = True
    # Check whitelisted scripts for existence
    bad_whitelist = False
    for path in MANUALLY_EXECUTED_SCRIPTS:
        if path not in gams_paths_dict:
            bad_whitelist = True
            print(f"NON-EXISTENT: {path}")
    if bad_whitelist:
        raise RuntimeError("ERROR: non-existent scripts present in MANUALLY_EXECUTED_SCRIPTS whitelist.")
    # Seed script_paths_dict that will hold the parse tree with the whitelist of manually executed scripts.
    print("----------------------- Starting from Manually-Executed Script Whitelist")
    script_paths_dict = {}
    for path in MANUALLY_EXECUTED_SCRIPTS:
        cd,dummy = os.path.split(path)
        if path in script_paths_dict:
            raise RuntimeError(f"ERROR: script {path} whitelisted multiple times!")
        script_paths_dict[path] = ScriptDict(cd)
        print(path)
    # Recursively scan and collect scripts $included or executed
    print("----------------------- Dependency Scan and Doc Extract under Whitelist")
    while True:
        any_scanned = False
        for path in script_paths_dict.keys():
            if not script_paths_dict[path]['scanned']:
                scan_script(path, script_paths_dict)
                any_scanned = True
                break
        if not any_scanned:
            break
    # Create a dictionary of GAMS file put paths
    gams_put_file_dict = {}
    for path,script_dict in script_paths_dict.items():
        for file_put_path in script_dict['files']:
            if file_put_path[-4:].lower() == '.gms':
                gams_put_file_dict[file_put_path] = True
    # List GAMS files not caught in the dependency net
    print("----------------------- Report GAMS files not $included or executed starting from MANUALLY_EXECUTED_SCRIPTS")
    for path in sorted(gams_paths_dict.keys()):
        if path not in script_paths_dict:
            print(path)
    # Throw an error for GAMS files that are missing but executed
    print("----------------------- Report executed GAMS files that are missing")
    for path in sorted(script_paths_dict.keys()):
        for missing in script_paths_dict[path]['missing_executes']:
            print(f"ERROR: missing execute GAMS file on line {missing['line_number']} of file {path}:")
            print(f"    {missing['line']}", end='')
            print(f"    missing file: {missing['path']}")
    # Throw an error for GAMS files that are missing but included
    print("----------------------- Report $included GAMS files that are missing")
    for path in sorted(script_paths_dict.keys()):
        for missing in script_paths_dict[path]['missing_$includes']:
            print(f"ERROR: missing $included GAMS file on line {missing['line_number']} of file {path}:")
            print(f"    {missing['line']}", end='')
            print(f"    missing file: {missing['path']}")
    # Report white-listed scripts that are not top-level.
    print("----------------------- Report Non-Top-Level Whitelisted Scripts")
    for path in MANUALLY_EXECUTED_SCRIPTS:
        script_dict = script_paths_dict[path]
        if script_dict['$included_by']:
            print(f"Whitelisted script {path} is $included")
            for by_path in script_dict['$included_by']:
                print(f"    {by_path}")
        if script_dict['executed_by']:
            print(f"Whitelisted script {path} is executed by:")
            for by_path in script_dict['executed_by']:
                print(f"    {by_path}")
    # Add-to-list top-level scripts
    topLevelScriptPaths = []
    for path,script_dict in script_paths_dict.items():
        if not (script_dict['$included_by'] or script_dict['executed_by']):
            topLevelScriptPaths.append(path)
    # Check if all top-level scripts are whitelisted
    for path in topLevelScriptPaths:
        assert path in MANUALLY_EXECUTED_SCRIPTS
    # Report totals
    print("----------------------- Report Totals")
    # Count unique $include children and parents
    include_children = 0
    include_parents  = 0
    for path,script_dict in script_paths_dict.items():
        include_children += len(script_dict['$includes'])
        include_parents  += len(script_dict['$included_by'])
    print(f"$include children: {include_children}, $include parents: {include_parents}")
    # Count unique execute children and parents
    execute_children = 0
    execute_parents  = 0
    for path,script_dict in script_paths_dict.items():
        execute_children += len(script_dict['executes'])
        execute_children += len(script_dict['commented_executes'])
        execute_parents  += len(script_dict['executed_by'])
    print(f"(commented) execute children: {execute_children}, execute parents: {execute_parents}")
    print(f"Source tree holds {len(gams_paths_dict)} GAMS scripts in total.")
    print(f"Dependency-located {len(script_paths_dict)} GAMS scripts starting from and including MANUALLY_EXECUTED_SCRIPTS.")
    # Generate reStructuredText
    if GENERATE_REST:
        print("----------------------- Removing old reStructuredText")
        # Delete any previously-generated subdirectories of the source directory
        for dirpath, dirs, files in os.walk('source'):
            for d in dirs:
                if d not in  ['_static', '_templates']:
                    shutil.rmtree(os.path.join(dirpath, d))
        # Generate the index
        print("----------------------- Generating reStructuredText index")
        prior_lines = [
            "Top-Level GAMS Scripts",
            "----------------------",
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "",
        ]
        substitute_lines = ['   '+path[:-4] for path in sorted(topLevelScriptPaths)] 
        post_line = ""
        # Update the source tree
        with FileInput(files=["source/source_tree.rst"], inplace=True) as f:
            prior = 0
            post = False
            for line in f:
                line = line.rstrip('\r\n') # strips any repetition of either
                if post:
                    print(line, end='\n')
                else:
                    if prior < len(prior_lines):
                        # Prior lines not matched yet
                        print(line, end='\n')
                        if line == prior_lines[prior]:
                            # Another match in the sequence
                            prior += 1
                        else:
                            # A mismatch, revert back to 0 and match as of start
                            prior = 0
                            if line == prior_lines[prior]:
                                prior += 1
                    elif line != post_line:
                        # Forget lines-to-be-substituted, before post line
                        continue
                    else:
                        # Found the post line, output substitution and post line
                        post = True
                        for sub in substitute_lines:
                            print(sub, end='\n')
                        print(line, end='\n')
        # Generate reStructuredText for every GAMS script caught in the dependency tree
        print("----------------------- Generating reStructuredText for GAMS tree")
        for path,script_dict in script_paths_dict.items():
            rest_path = os.path.join('source', path[:-4] + '.rst')
            mkdir(os.path.dirname(rest_path))
            with open(rest_path, 'w', newline='') as rest_file:
                # Write path/title
                rest_file.write('#'*len(path) + '\n')
                rest_file.write(path + '\n')
                rest_file.write('#'*len(path) + '\n')
                rest_file.write('\n')
                # Write header
                if script_dict['rest_header'] or script_dict['rest']:
                    rest_file.write(script_dict['rest_header'])
                else:
                    rest_file.write('Not documented.\n\n')
                # Link execute dependencies, if any
                if script_dict['executes']:
                    rest_file.write('********\n')
                    rest_file.write('Executes\n')
                    rest_file.write('********\n')
                    rest_file.write('\n')
                    rest_file.write('.. toctree::\n')
                    rest_file.write('   :maxdepth: 1\n')
                    rest_file.write('\n')
                    for execute_path in sorted(script_dict['executes']):
                        rest_file.write('   ' + os.path.relpath(execute_path[:-4], os.path.dirname(path)).replace('\\', '/') + '\n')
                    rest_file.write('\n')
                # Link commented-out execute dependencies, if any
                if script_dict['executes']:
                    rest_file.write('******************************************\n')
                    rest_file.write('Commented-out executes of existing scripts\n')
                    rest_file.write('******************************************\n')
                    rest_file.write('\n')
                    rest_file.write('.. toctree::\n')
                    rest_file.write('   :maxdepth: 1\n')
                    rest_file.write('\n')
                    for execute_path in sorted(script_dict['commented_executes']):
                        rest_file.write('   ' + os.path.relpath(execute_path[:-4], os.path.dirname(path)).replace('\\', '/') + '\n')
                    rest_file.write('\n')
                # Link executing scripts, if any
                if LINK_EXECUTED_BY and script_dict['executed_by']:
                    rest_file.write('***********\n')
                    rest_file.write('Executed by\n')
                    rest_file.write('***********\n')
                    rest_file.write('\n')
                    rest_file.write('.. toctree::\n')
                    rest_file.write('   :maxdepth: 1\n')
                    rest_file.write('\n')
                    for execute_path in sorted(script_dict['executed_by']):
                        rest_file.write('   ' + os.path.relpath(execute_path[:-4], os.path.dirname(path)).replace('\\', '/') + '\n')
                    rest_file.write('\n')
                # Link include dependencies, if any
                if script_dict['$includes']:
                    rest_file.write('********\n')
                    rest_file.write('Includes\n')
                    rest_file.write('********\n')
                    rest_file.write('\n')
                    rest_file.write('.. toctree::\n')
                    rest_file.write('   :maxdepth: 1\n')
                    rest_file.write('\n')
                    for include_path in sorted(script_dict['$includes']):
                        rest_file.write('   ' + os.path.relpath(include_path[:-4], os.path.dirname(path)).replace('\\', '/') + '\n')
                    rest_file.write('\n')
                # Write remaining extracted reStructuredText, if any
                if script_dict['rest']:
                    rest_file.write('********\n')
                    rest_file.write('Comments\n')
                    rest_file.write('********\n')
                    rest_file.write('\n')
                    rest_file.write(script_dict['rest'])
