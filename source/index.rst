GLOBIOM 
=======

.. image:: _images/logo.png
   :width: 154
   
This site provides documentation for the GLOBIOM model, links to GLOBIOM resources, and
helps you find your way in the model's GAMS code. GAMS script descriptions and dependency
links that match the Trunk version of the GLOBIOM model are provided.

About GLOBIOM 
-------------

The `Global Biosphere Management Model <http://www.globiom.org>`_ (GLOBIOM) has been developed
and used by the International Institute for Applied Systems Analysis (IIASA) since the late
2000s. The partial-equilibrium model represents various land use-based activities, including
agriculture, forestry and bioenergy sectors. The model is built following a bottom-up
setting based on detailed grid-cell information, providing the biophysical and technical
cost information. This detailed structure allows a rich set of environmental parameters to
be taken into account. Its spatial equilibrium modelling approach represents bilateral
trade based on cost competitiveness. The model was initially developed for impact 
assessment of climate change mitigation policies in land-based sectors,
including biofuels, and nowadays is also increasingly being implemented for agricultural 
and timber markets foresight, and economic impact analysis of climate change and adaptation,
and a wide range of sustainable development goals.

Model documentation
-------------------
The `model documentation <https://iiasa.github.io/GLOBIOM/GLOBIOM_Documentation_20180604.pdf>`_
provides a detailed description of the main features of the GLOBIOM model, as present in the
standard global version.

GLOBIOM resources
-----------------

GUI
^^^
The `GLOBIOM_GUI repository <https://github.com/iiasa/GLOBIOM_GUI>`_ provides a graphical user
interface (GUI) for running GLOBIOM and analyzing results. Installation instructions are found
`here <https://github.com/iiasa/GLOBIOM_GUI/blob/master/README.md>`_.
See the :doc:`GUI` to learn how to use the GUI.

R
^
`globiomvis <https://iiasa.github.io/globiomvis>`_, an R package and examples for visualizing
GLOBIOM data.

`mapspam2globiom <https://iiasa.github.io/mapspam2globiom>`_, an R package and examples to
facilitate the creation of country level crop distribution maps that are input to GLOBIOM.

GLOBIOM itself includes scripts written in the Open Source R language. To learn how to install
and configure R for GLOBIOM, see the :doc:`R` page.

Development
^^^^^^^^^^^
The `GLOBIOM wiki <https://github.com/iiasa/GLOBIOM/wiki>`_ provides background and guidelines
for GLOBIOM development with an IIASA-specific focus. The GitHub `issue tracker
<https://github.com/iiasa/GLOBIOM/issues>`_ and `project boards
<https://github.com/iiasa/GLOBIOM/projects>`_ support collaborative development for team
members. These links work if you are signed in to GitHub and are a member of the
``iiasa/GLOBIOM`` GitHub team, or have been given collaborator access.

Model code
^^^^^^^^^^
An Open Source version of GLOBIOM is under preparation. External collaborators are given access
to an open-source pre-release version of GLOBIOM hosted on GitHub in `this repository
<https://github.com/iiasa/GLOBIOM_Prerelease_Model>`_.

FABLE
^^^^^
FABLE consortium members using GLOBIOM for partial equilibrium modeling have been provided with
code repositories, documentation, a graphical user interface, and training presentations. These
are all described and linked on a separate `GLOBIOM FABLE website
<https://iiasa.github.io/GLOBIOM_FABLE>`_.

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
   Model/6_scenarios_msg
   Model/6_scenarios_limpopo
   Model/6_scenarios_msg_limpopo
   Model/7_output

Index and Search
----------------

* :ref:`search`

Acknowledgement
---------------

This documentation was generated using the `GAMS stub project on Github <https://github.com/iiasa/gams_stub>`_.
