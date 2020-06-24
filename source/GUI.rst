Graphical User Interface
========================
The `GLOBIOM_GUI repository <https://github.com/iiasa/GLOBIOM_GUI>`_ provides a graphical user
interface (GUI) for running GLOBIOM and analyzing results. Installation instructions are found
`here <https://github.com/iiasa/GLOBIOM_GUI/blob/master/README.md>`_.

The GUI provides a user-friendly way to run GLOBIOM and perform interactive
analysis of the model output. One or more output GDX files resulting from
GLOBIOM scenario runs can be loaded for charting, mapping, tabulation and
comparison.

The GUI is an optional add-on to GLOBIOM: those who prefer more in-depth
control can still choose to run GLOBIOM from the GAMS IDE or GAMS Studio as
before, or perform analysis using R or some other tool of choice.

Post installation
-----------------
After `installation via GitHub <https://github.com/iiasa/GLOBIOM_GUI/blob/master/README.md>`_,
the GUI window should open when running the ``globiom.bat`` script located in the
``GUI`` directory. If this fails, run the script from the command prompt or
terminal so that you can read the error message, check whether you have
configured a valid path in ``GGIG_java_path.txt``.

The first time you launch the GUI, default settings are used. You can adjust
the settings to match your system via the settings dialog that opens via the
**Settings >> Edit settings** menu item.

Adjust the following settings in particular:

* **User name** in the **User Settings** tab.

* **Path to GAMS.exe** in the **GAMS and R** tab.
  Point it to the ``gams`` or ``gams.exe`` binary/executable in your GAMS
  installation directory.

* **Path to r.exe** in the **GAMS and R** tab. Point it to the ``Rscript`` or
  ``Rscript.exe`` binary/executable of your R installation so as to be able to
  run R scripts from the GUI. Beware, on Windows the 64-bit R executables are
  in a ``x64`` subdirectory of a ``bin`` directory that holds the 32-bit
  executables. You typically will want the former, not the latter. For more
  information see :doc:`R`.

* Make sure that the **Output set with meta information to include file**
  checkbox in the **Other options** tab is not checked.

Managing the GUI settings
-------------------------
The GUI stores its settings in the ``settings.ini`` file in the ``GUI``
directory. This ``.ini`` file contains the settings you enter via the
configuration dialog, but also per-task or per-analysis-view window state.
This is convenient, but sometimes you will want to return those to a default
state. To clear all per-task settings, select the **Settings >> Remove
task-specific settings** menu item. To clear all analysis view settings,
select **Settings >> Remove view-specific settings**.

To revert all settings to their defaults, exit the GUI and delete the
``settings.ini`` file. The next time you start the GUI (via ``globiom.bat``),
default settings are loaded.

To backup and restore settings, use the **Settings >> Save current settings to
ini file** and **Settings >> Load current settings from ini file** menu items.

High-DPI diplays
----------------
When you have a high-DPI diplay, the GUI may display with a tiny font and
widgets. In this case, trying a higher Java version (9 or higher) may resolve
the issue. This is untested. Alternatively, if you use Windows 10, you can try
the following quick fix:

1. Find ``java.exe`` you installed.
2. Right click -> **Properties**
3. Go to **Compatibility** tab
4. Check **Override high DPI scaling behavior**.
5. Choose **System** for **Scaling performed by**.

Further reading
---------------
For an overview, see the `A GUI for GLOBIOM <presentations/A_GUI_for_GLOBIOM.pdf>`_
presentation.

To learn more about the powerful interactive analysis capabilities of the GUI,
please see the `GGIG User Guide <http://www.ilr.uni-bonn.de/em/rsrch/ggig/GGIG_user_Guide.pdf>`_.
To open an offline copy of the User Guide from the GUI, select the **Help >> GGIG User
Guide** menu item.

Acknowledgments
----------------
The GLOBIOM GUI is based on `GGIG <http://www.ilr.uni-bonn.de/em/rsrch/ggig/ggig_e.htm>`_,
the Gams Graphical Interface Generator. We are grateful for the generous
guidance and assistance concerning GGIG provided by Wolfgang Britz and
Torbjörn Jansson.
