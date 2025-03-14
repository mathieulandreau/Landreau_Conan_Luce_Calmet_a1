# Article 1 : Observation and LES modeling of an offshore atmospheric undular bore generated during sea-breeze initiation near a peninsula

This project contains all the files to reproduce the simulation results and the figures presented in this paper, including:
- the modified version of WRF (as a submodule)
- WPS files used to link the chosen datasets and fix an ERA5 issue
- the input files for the simulation
- the Python post-processing library py\_wrf\_arps (as a submodule)
- the Python post-processing notebooks to draw the figures

## Install

to install this project with the submodules, use the following:
```
git clone --recurse-submodules linkToTheProject
```

## WRFstats
It is a submodule, all informations are in its own README.md

## py\_wrf\_arps
It is also a submodule

## Input
Contains
- **namelist.wps** : namelist of wps
- **namelist.input** : namelist of WRF 
- **namelist_rst_real.input**, **namelist_rst.input** : WRF namelist of the restart run. The simulation has been run in two parts (first until May 18 and then until May 18)
- **LAI_modif.py** : This script is called between ./real.exe and ./wrf.exe to add the higher resolution LAI and VEGRA field (see article 1)
- **slurm.job**, **slurm_LAI.job**, **slurm_real.job** : sbatch programs to run on the cluster
- **tslist** : list of the timeseries locations
- **wrfio_d0X.txt** : list the desired and undesired output variables

How to use :
- link namelist.wps in the WPS working directory
- run WPS
- link all the other files in the WRF working directory
- run real
- run LAI modif: you need to install py\_wrf\_arps first, to download the , if you skip this part, the monthly MODIS LAI and VEGFRA are used
- run WRF

### LAI modif
Before runnin LAI modif, you need to:
- download the LAI and VEGFRA datasets (e.g. on [WEkEO](https://wekeo.copernicus.eu/))
- install py\_wrf\_arps first
if you skip this part, the monthly MODIS LAI and VEGFRA are used instead of the high-resolution LAI and VEGFRA datasets

## WPS files
Other important high-resolution datasets have been used (land-use, topography). References to these datasets can be found in the paper. 
To use them in WPS, the GEOGRID\_CLC\_EUDEM.TBL must be used

In addition, the METGRID\_ERA5.TBL.ARW solves a 

## Postproc
Contains
- **1430_18_article1_GW_carac2.ipynb**
- **1430_18_article1_GW_stats4-5_v2.ipynb**
- **1430_18_article1.ipynb** : Figures 
- **1430_19_GW_var.ipynb**

How to use
- These scripts need the py\_wrf\_arps library to run, the version of py\_wrf\_arps is written in the first cell
- You need to activate the conda environment first with the yaml file given in py\_wrf\_arps
- Also, the different paths (in py\_wrf\_arps) in lib/manage\_path and in class\_proj must be modified to your specific folders

