Using R with GLOBIOM
====================
In addition to using `GAMS <https://www.gams.com/>`_, GLOBIOM includes scripts written in the open-source
`R language <https://en.wikipedia.org/wiki/R_(programming_language)>`_. In addition separate
`GLOBIOM-specific R packages`_ provide data handling scripts and examples. Therefore, to use all features
of GLOBIOM, you need to have R installed.

Installing R and required packages
----------------------------------
R can be installed via the `R Project website <https://www.r-project.org/>`_. If you find
yourself using R a lot, the `R Studio integrated development environment <https://www.rstudio.com/>`_
is highly recommended.

The R scripts included with GLOBIOM require additional R packages. These can be installed from the
R console using ``install.packages("package")``. R Studio provides a convenient package manager that
makes installing/removing packages even easier.

Instead of installing individual packages, we recommend to simply install the `tidyverse <https://www.tidyverse.org/>`_
package collection.

The one required package that needs special treatment is GDXRRW, a package to read/write GDX files from R. Please
see the `GDXRRW installation instructions <https://support.gams.com/gdxrrw:interfacing_gams_and_r>`_ for details.
**Beware**, on Windows installing the source package will not work unless you have a compiler installed, install
a binary package instead. Binary packages are provided for specific operating systems and R versions, carefully
select the appropriate package for download.

Setting environment variables
-----------------------------
To invoke R from GAMS, GLOBIOM relies on the ``Rscript`` command being available. Check that you can
invoke ``Rscript`` from the command line/shell. If you can, then GAMS too can find ``Rscript``.
If you cannot, add the directory holding the ``Rscript`` binary/executable of your R installation to
your ``PATH`` environment variable.

GDXRRW needs to load GDX libraries from a GAMS system directory. GLOBIOM makes sure that it can,
but if you want to use GDXRRW in your own scripts, issue ``help(igdx)`` in the R console and read carefully
(after having installed and loaded the package). One of the methods described in that help page involves setting
the ``R_GAMS_SYSDIR`` environment variable and passing an empty string as a first ``gamsSysDir`` parameter to
``igdx()``.  To learn about setting environment variables, see below.

The GAMS installation directory can typically be found at:

* ``C:\GAMS\win64\xy.z`` on Windows.
* ``/opt/gams/gams`` on Linux.
* ``/Applications/GAMSxy.z`` on MacOS.

Windows 10
^^^^^^^^^^
On Windows 10, you can edit ``PATH`` by searching for "env" in the Start Menu and selecting either **Edit environment
variables for your account** or, if you have administrator rights, **Edit the system environment variables** and also
clicking the **Environment Variables...** button in the dialog that opens. Next, select the ``Path`` variable from the
bottom (System variables) or top (User variables) list, click the **Edit** button, and then click **New** to add an
entry with the directory where Rscript is located. This is typically something like ``C:\Program Files\R\R-3.6.2\bin\x64``.
Determine the right location with the File Explorer, and make sure to pick the ``x64`` subdirectory holding the
64-bit executables if you have a 64-bit Windows installation.

Linux and MacOS
^^^^^^^^^^^^^^^
Assuming bash is your default shell, you can set an environment variable with the ``export`` command.
To make a command execute each time you start a new session, add it to the ``~/.profile`` or ``~/.bash_profile``
script. For MacOS, use the former. For Linux the preferred script depends on your distribution.

For example, to add the GAMS system directory to the search path on Linux use:
    ``export PATH="/opt/gams/gams:$PATH"``

Since profile scripts execute on starting a session, you need to log out and back in for your edits to be
picked up.

GLOBIOM-specific R packages
---------------------------
Beyond the R scripts included with GLOBIOM, additional R packages and examples for analysis
and preperation of GLOBIOM data are available on GitHub:

* `globiomvis <https://iiasa.github.io/globiomvis>`_, an R package and examples for
  visualizing GLOBIOM data.

* `mapspam2globiom <https://iiasa.github.io/mapspam2globiom>`_, an R package and examples
  to facilitate the creation of country level crop distribution maps that are input to
  GLOBIOM.

Please see the websites of these packages for further details.
