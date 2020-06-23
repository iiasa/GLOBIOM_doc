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

How GLOBIOM works
-----------------
GLOBIOM's analytical process captures the multiple interrelationships between the different
systems involved in provision of agricultural and forestry products, for example, population
dynamics, ecosystems, technology, and climate.

GLOBIOM is a global, recursively dynamic, and partial equilibrium model. It integrates the
agricultural, bioenergy, and forestry sectors and draws on comprehensive socioeconomic and
geospatial data.  It accounts for the 18 most globally important crops, a range of livestock
production activities, forestry commodities, first- and second-generation bioenergy, and
water. Production is spatially explicit and takes into account land, management, and weather
characteristics.

.. image:: _images/sectors.svg

The market equilibrium is solved by maximizing the sum of producer and consumer surplus
subject to resource, technological, and political constraints. Using the year 2000 as the
baseline, GLOBIOM simulates demand and supply quantities, bilateral trade flows, and prices
for commodities and natural resources at 10-year-step intervals up to 2050. This gives
planners a basis for setting future land use and, more importantly, for identifying possible
shortfalls in food and biomass supplies.

Model documentation
-------------------
The `model documentation <https://iiasa.github.io/GLOBIOM/GLOBIOM_Documentation_20180604.pdf>`_
provides a detailed description of the main features of the GLOBIOM model, as present in the
standard global version.

GLOBIOM resources
-----------------

Model code
^^^^^^^^^^
An Open Source version of GLOBIOM is under preparation. External collaborators are given access
to an open-source pre-release version of GLOBIOM hosted on GitHub in `this repository
<https://github.com/iiasa/GLOBIOM_Prerelease_Model>`_.

Development
^^^^^^^^^^^
The `GLOBIOM wiki <https://github.com/iiasa/GLOBIOM/wiki>`_ provides background and guidelines
for GLOBIOM development with an IIASA-specific focus. The GitHub `issue tracker
<https://github.com/iiasa/GLOBIOM/issues>`_ and `project boards
<https://github.com/iiasa/GLOBIOM/projects>`_ support collaborative development for team
members. These links work if you are signed in to GitHub and are a member of the
``iiasa/GLOBIOM`` GitHub team, or have been given collaborator access.

GUI
^^^
The `GLOBIOM_GUI repository <https://github.com/iiasa/GLOBIOM_GUI>`_ provides a graphical user
interface (GUI) for running GLOBIOM and analyzing results. Installation instructions are found
`here <https://github.com/iiasa/GLOBIOM_GUI/blob/master/README.md>`_.
See the :doc:`GUI` to learn how to use the GUI.

R
^
In addition to GAMS, GLOBIOM includes scripts written in the Open Source R language.
How to install and configure R for GLOBIOM is explained on `this R page <R>`_. In
addition, R packages and examples for analysis and preperation of GLOBIOM data are
available on GitHub:

* `globiomvis <https://iiasa.github.io/globiomvis>`_, an R package and examples for
  visualizing GLOBIOM data.

* `mapspam2globiom <https://iiasa.github.io/mapspam2globiom>`_, an R package and examples
  to facilitate the creation of country level crop distribution maps that are input to
  GLOBIOM.

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
