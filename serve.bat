@ECHO OFF
REM Expose generated HTML documentation via a local HTML server

pushd %~dp0%build\html
python -m http.server
popd
