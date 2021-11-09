Using R with GLOBIOM
====================
In addition to using `GAMS <https://www.gams.com/>`_, GLOBIOM includes scripts written in the open-source
`R language <https://en.wikipedia.org/wiki/R_(programming_language)>`_. Also, separate
`GLOBIOM-specific R packages`_ provide data handling scripts and examples. Therefore, to use all features
of GLOBIOM, you need to have R installed.

Installing R and required packages
----------------------------------
R can be installed via the `R Project website <https://www.r-project.org/>`_. If you find
yourself using R a lot, the `RStudio <https://www.rstudio.com/>`_ integrated development
environment is highly recommended.

The R scripts included with GLOBIOM require additional R packages. These can be installed from the
R console using ``install.packages("package")``. R Studio provides a convenient package manager that
makes installing/removing packages even easier.

To install required packages, please follow [this guidance](https://github.com/iiasa/xl2gdx#dependencies).

Setting environment variables
-----------------------------
To set the environment variables decribed in the guidance linked above, it is helpful
to know that the GAMS installation directory can typically be found at:

* ``C:\GAMS\xy`` on Windows.
* ``/opt/gams/gams`` on Linux.
* ``/Applications/GAMSxy.z`` on MacOS.

Windows 10
^^^^^^^^^^
On Windows 10, you can type "env" in the search field of the Start Menu and select either
**Edit environment variables for your account**
or, if you have administrator rights or have the administrator password,
**Edit the system environment variables** and also clicking the **Environment Variables...**
button in the dialog that opens.

**Beware:** applications that are already running when you change environment variables will not see the
changes and have to be restarted for the changes to take effect.

**Beware:** if you edit the user variables (the top list) after having authenticated with the administrator
password, they will apply to the administrator user account, not to your regular user account.

Linux and MacOS
^^^^^^^^^^^^^^^
Assuming bash is your default shell, you can set an environment variable with the ``export`` command.
To make a command execute each time you start a new session, add it to the ``~/.profile`` or ``~/.bash_profile``
script. For MacOS, use the former. For Linux the preferred script depends on your distribution.

For example, to add the GAMS system directory to the search path on Linux use:
    ``export PATH="/opt/gams/gams:$PATH"``

**Note:** since profile scripts execute on starting a session, you need to log out and back in for your edits
to be picked up.

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
