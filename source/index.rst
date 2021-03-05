GLOBIOM_FABLE
=============

.. image:: images/logo.png
   :width: 154

This website provides FABLE consortium members using GLOBIOM for partial
equilibrium modeling with documentation, links to code repositories,
a graphical user interface, and training presentations.

About GLOBIOM
-------------

The `Global Biosphere Management Model <http://www.globiom.org>`_ (GLOBIOM) has been developed
and used by the International Institute for Applied Systems Analysis (IIASA) since the late
2000s. The partial-equilibrium model represents various land use-based activities, including
agriculture, forestry and bioenergy sectors. The model is built following a bottom-up
setting based on detailed grid-cell information, providing the biophysical and technical
cost information. This detailed structure allows a rich set of environmental parameters to
be taken into account. Its spatial equilibrium modeling approach represents bilateral
trade based on cost competitiveness. The model was initially developed for impact
assessment of climate change mitigation policies in land-based sectors,
including biofuels, and nowadays is also increasingly being implemented for agricultural
and timber markets foresight, and economic impact analysis of climate change and adaptation,
and a wide range of sustainable development goals.

GLOBIOM Documentation
---------------------
The `model documentation <GLOBIOM_Documentation_20180604.pdf>`_ provides a detailed description
of the main features of the GLOBIOM model, as present in the standard global version.

FABLE Training Presentations
----------------------------
| `Introduction to GLOBIOM <presentations/GLOBIOM_Introduction.pdf>`_
| `GLOBIOM <presentations/GLOBIOM_FABLE.pdf>`_, an overview for FABLE.
| `Introduction to SSP scenarios <presentations/SSP_Scenarios_Intro.pdf>`_
| `Running a first baseline <presentations/Running_first_baseline.pdf>`_
| `Equations, Variables, Calibration <presentations/GLOBIOM_Equations_Variables_Calibration.pdf>`_
| `Baseline Development <presentations/Baseline_Development.pdf>`_
| `The GLOBIOM Data Folder <presentations/GLOBIOM_Data_Folder.pdf>`_
| `A GUI for GLOBIOM <presentations/A_GUI_for_GLOBIOM.pdf>`_
| `GUI Baseline & FAOSTAT Comparison <presentations/GUI_Baseline_FAOSTAT_Comparison.pdf>`_
| `Running GLOBIOM Scenarios with Excel <presentations/Running_GLOBIOM_Scenarios_with_Excel.pdf>`_

GLOBIOM resources
-----------------

**Note**: the below links to the repositories are accessible only after having signed-in to your
GitHub account, and after having requested and received access to the repositories.

GLOBIOM for FABLE is provided via three GitHub repositories:

* The `GLOBIOM_FABLE repository <https://github.com/iiasa/GLOBIOM_FABLE>`_ holds the model.
  For further detail, `see the README <https://github.com/iiasa/GLOBIOM_FABLE/blob/master/README.md>`_.
* The `GLOBIOM_FABLE_Data repository <https://github.com/iiasa/GLOBIOM_FABLE_Data>`_ contains the
  source data and pre-compilation scripts. To learn more,
  `see its README <https://github.com/iiasa/GLOBIOM_FABLE_Data/blob/master/README.md>`_.
* The `GLOBIOM_GUI repository <https://github.com/iiasa/GLOBIOM_GUI>`_ provides a graphical user
  interface (GUI) for running GLOBIOM and analyzing results. Installation instructions are found
  `here <https://github.com/iiasa/GLOBIOM_GUI/blob/master/README.md>`_.
  See the `GUI page <https://iiasa.github.io/GLOBIOM/GUI.html>`_ to learn how to use the GUI.

GLOBIOM is implemented primarily in `GAMS <https://www.gams.com/products/introduction/>`_. To run the
model, you need a GAMS installation with a license that allows use of the CONOPT and CPLEX solvers.

In addition, GLOBIOM includes scripts written in the Open Source R language. To learn how to install
and configure R for GLOBIOM, see the `R page <https://iiasa.github.io/GLOBIOM/R.html>`_.

Top-Level GAMS Scripts
----------------------

.. toctree::
   :maxdepth: 1

   Data/0_executebatch_total
   Model/0_executebatch

Important GAMS Scripts
----------------------

.. toctree::
   :maxdepth: 1

   Model/1_loaddata
   Model/2_activesets
   Model/3_precompute
   Model/3b_calibtrade
   Model/4_model
   Model/5_precompute_scen
   Model/6_scenarios
   Model/7_output

Search
------

* :ref:`search`

Acknowledgement
---------------

This documentation was generated using the `GAMS stub project on Github <https://github.com/iiasa/gams_stub>`_.
