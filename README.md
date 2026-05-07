# GLOBIOM_doc
Scripts and templates for GLOBIOM documentation generation. The `master` branch provides ReST page templates and serves to generate pages from the Trunk GAMS source files. The generated HTML is committed to the `gh-pages` branch of the [GLOBIOM](https://github.com/iiasa/GLOBIOM) meta repository. That `gh-pages` branch stores the content of the [GLOBIOM documentation site](https://iiasa.github.io/GLOBIOM/).

For detailed instructions see the [page on updating the GLOBIOM documentation site](https://github.com/iiasa/GLOBIOM/wiki/Updating-the-GLOBIOM-documentation-site) on the GLOBIOM wiki (access required).

## Setup

To set up a Python virtual environment with the required dependencies for building the documentation:

1. Ensure you have Python 3.6+ installed.

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Building the Documentation

To build the HTML documentation:

```bash
make html
```

The generated HTML will be in the `build/html` directory.

## Extracting Documentation from GAMS Sources

The `get_dependencies_and_docs.py` script extracts reStructuredText comments and dependency information from GAMS source files. It expects the GLOBIOM source tree to be in the parent directory (`../`). Run it with:

```bash
python get_dependencies_and_docs.py
```

This will generate reStructuredText files in the `source/` directory based on the GAMS scripts.
