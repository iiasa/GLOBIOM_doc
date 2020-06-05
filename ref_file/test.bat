:<<BATCH
@echo off
:: DOS/Windows batch commands can go below here
gams set.gms reference=default
gams parameter.gms reference=default
gams combined.gms reference=default
gams parent.gms reference=default
exit /b :: end batch script processing
BATCH
# Platform-agnostic script.
# Put batch commands above and functionally-identical Linux/MacOS shell
# commands terminated by a # below. Save this script with CR+LF end-of-line
# breaks. The trailing # makes the shell ignore the CR.
gams set.gms reference=default #
gams combined.gms reference=default #
gams parent.gms reference=default #
