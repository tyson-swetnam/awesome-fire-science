# awesome-fire-science
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

List of resources for working with data and doing wildfire science 

****

# Table of Contents

## Free and Open Source Software (FOSS)

Free and Open Source Software (FOSS) reduce the digital divide and allow everyone to work with open data. 

Popular Integrated Development Environments (IDE) for data science:

   * [Project Jupyter](https://jupyter.org/) - Browser based computational notebooks, focused on Python, but any computer kernel can be installed as add-ons 
   * [RStudio](https://www.rstudio.com/) - IDE for the popular statistical computing language R
   * [QGIS](https://qgis.org/en/site/) - Quantum GIS, an open source alternative to ESRI ArcGIS
      * [GDAL](https://gdal.org/) - powerful tool for manipulating raster (2D) data
      * [PDAL](https://pdal.io/) - powerful tool for manipulating point cloud (3d) data
      * [GRASS-GIS](https://grass.osgeo.org/) - US Army Corps of Engineers GIS with numerous topographic and hyrdological algorithms
      * [SAGA-GIS](http://www.saga-gis.org/) - European GIS with numerous topographic and hydrological algorithms
   * [VS Code](https://code.visualstudio.com/) - Microsoft's free Visual Studio Code is the most popular and fully featured code editor in the world   

## Self-Paced Data Science Training

Explore these resources for gaining essential data science skills
   
   * [Carpentries](https://carpentries.org/) - Basic data science skills
   * [CyVerse Learning](https://learning.cyverse.org) - Life science data science skills
   * [EarthLab](https://www.earthdatascience.org/) - Earth science data science skills
   * [geemap](https://geemap.org/) - Google Earth Engine Maps with over 360 free notebooks
   * [JoVE](https://www.jove.com/) - videos of science protocols (e.g. [fire history](https://www.jove.com/t/61698/using-tree-rings-to-reconstruct-fire-history-information-from)) 
   * [Protocols.io](https://www.protocols.io/) - Methods for doing science
   * [WholeTale](https://wholetale.org/) - create and publish your own transparent and reproducible research

## Open Data

Data should be open, and follow the [FAIR](https://www.go-fair.org/fair-principles/) and [CARE](https://www.go-fair.org/fair-principles/) data principles

   * [3DEP](https://usgs.entwine.io/) - USGS 3DEP lidar point clouds on AWS
   * [Ameriflux](https://ameriflux.lbl.gov/) - eddy covariance data
   * [CZO](https://czo-archive.criticalzone.org/national/data/) - Critical Zone Observatory data (archived on HydroShare).
   * [eBird](https://ebird.org/science/use-ebird-data) - citizen science for ornithology
   * [EcoSML](https://ecosml.org/) - NASA supported Ecological Spectral Model Library (EcoSML), a useful tool for finding spectral models.
   * [Earth Null School](https://earth.nullschool.net/) - dynamic vizualizations of Earth model and weather data
   * [Environmental Data Initiative](https://environmentaldatainitiative.org/) - access to LTER and LTAR datasets online
   * [ESRI Fire Maps](https://www.esri.com/en-us/disaster-response/disasters/wildfires) - Access wildfire data, live feeds, technology, and resources
   * [HydroShare](https://www.hydroshare.org/) - CUASHI's online collaboration environment for sharing data, models, and code
   * [Landfire](https://landfire.gov/version_alerts.php) - geospatial data and databases that describe vegetation, wildland fuel, and fire regimes across the United States
   * [NASA LANCE](https://earthdata.nasa.gov/earth-observation-data/near-real-time) - Land, Atmosphere Near real-time Capability for EOS (LANCE)
   * [National Phenology Network](https://www.usanpn.org/usa-national-phenology-network) - citizen science data for vegetation phenology
   * [National Weather Service](https://www.weather.gov/fire/)
   * [NEON](https://www.neonscience.org/data-samples) - National Ecological Observation Network (NEON) data and API
   * [NeotomaDB](https://www.neotomadb.org/data) - Neotoma paleo ecology database
   * [NIFC Statistics](https://www.nifc.gov/fire-information/statistics)
   * [NIFC Wildland Fire Data](https://data-nifc.opendata.arcgis.com/)
   * [OpenTopography](https://opentopography.org/) - NSF supported lidar and global elevation data 
   * [Paleo Data Search](https://www.ncdc.noaa.gov/paleo-search/) - Paleo data archives
   * [PaleoFire DB](https://www.paleofire.org/index.php) - Global paleofire databse
   * [RAMMB](https://rammb2.cira.colostate.edu/) - Regional and Mesoscale Meteorology Branch (RAMMB) GOES-16/17 image animations. 
   * [RealEarth](https://www.ssec.wisc.edu/realearth/) - EOS data visualization
   * [WFDSS](https://wfdss.usgs.gov/wfdss/WFDSS_Data.shtml) - Wildfire decision support system GIS data for fire modelling
   * [WIFIRE](https://wifire.ucsd.edu/) - ML and AI for wildland fire support centered in California, also supporting data
  
### Google Earth Engine (GEE) 

Most major Earth Observation System (EOS) datasets (e.g. ESA, NASA) are available on cloud and in [Google Earth Engine](https://earthengine.google.com/). 

A curated list of community data sets in GEE:
   * [![GEE Community Datasets](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://samapriya.github.io/awesome-gee-community-datasets) - Another awesome list of free datasets in GEE.
      * [Landfire Mosaics LF v2.0.0](https://samapriya.github.io/awesome-gee-community-datasets/projects/landfire/)
      * [United States Drought Monitor](https://samapriya.github.io/awesome-gee-community-datasets/projects/usdm/)
      * [Global Fire Atlas (2003-2016)](https://samapriya.github.io/awesome-gee-community-datasets/projects/gfa/)

### Microsoft Planetary Computer

Microsoft has just launched a sort-of-competitor to GEE called [Planetary Computer](https://planetarycomputer.microsoft.com/). It is based on the Python language and supports Project Jupyter and distributed computing across Azure. 

   * [Planetary Computer Data Catalog](https://planetarycomputer.microsoft.com/catalog)

### NASA data special agreements

   * [Planet Labs](https://www.planet.com/markets/nasa/) has signed a special use agreement with NASA to provide their data to researchers and academics. 

## Free and Open Source Software

Using open source software allows other researchers to reproduce your work and increases access to your work as part of a [research object](https://en.wikipedia.org/wiki/Research_Object) or data cube.

### Python (Jupyter)
 
   * [Pangeo](https://pangeo.io/) - community platform for big data geoscience
   * [GEEMap](https://geemap.org/) - collection of python notebooks for running Google Earth Engine
   * [Example Planetary Computer Jupyter Notebooks](https://github.com/microsoft/PlanetaryComputerExamples)

### RStudio
   * [Forest Analysis in R App](https://atkinsjeff.shinyapps.io/ForestAnalysisInR/) - Shiny App with list of available packages for forestry analyses.
      * [BurnR](https://github.com/ltrr-arizona-edu/burnr) - Fire history analysis tools for R
      * [dplR](https://github.com/AndyBunn/dplR) - dendrochronology R tools
      * [lidR](https://jean-romain.github.io/lidRbook/) - lidar package for R

### Geospatial Software

   * [CSIRO Data61](https://data61.csiro.au/en/Our-Research/Our-Work/Safety-and-Security/Disaster-Management/) - CSIRO fire modelling software
   * [ESA STEP](http://step.esa.int/main/) - Scientific Toolbox Exploitation Platform 
   * [FRAMES](https://www.frames.gov/) - Fire Research and Management Exchange System
   * [USFS RMRS](https://www.fs.usda.gov/rmrs/wildland-fire-management-research-development-application-program) - Rocky Mountain Research Station fire data and tools

### General purpose software
   
   * [CyberDuck](https://cyberduck.io) - 3rd party software for getting data to and from the internet
   * [VS Code](https://code.visualstudio.com/) - Visual Studio Code is currently the most widely used code developer platform 

## Cyberinfrastructure

Existing investments in research cyberinfrastructure are available for free to all US based researchers. These resources can be used by non-US researchers under certain conditions. 

Commercial cloud resources are available to all at a $$$.

### Free Cloud and HPC resources

   * [XSEDE](https://portal.xsede.org/) - NSF supported cyberinfrastructure network (HPC, HTC, research clouds)
   * [CyVerse](https://cyverse.org) - NSF supported cyberinfrastructure for life sciences
   * [CloudBank](https://www.cloudbank.org/) - NSF supported cloud access

   * [Azure](https://www.microsoft.com/en-us/education/higher-education/academic-research) - free credits for research on Microsoft Azure
   * [Google Cloud](https://edu.google.com/programs/credits/research/?modal_active=none) - free credits for research on Google Cloud
   * [AWS](https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/) - free credits for research on Amazon Web Services
