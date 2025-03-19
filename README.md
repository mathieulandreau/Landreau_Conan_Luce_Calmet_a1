# Article 1 : Observation and LES modeling of an offshore atmospheric undular bore generated during sea-breeze initiation near a peninsula

This project contains all the files to reproduce the simulation results and the figures presented in the article :
Landreau, Mathieu, Boris Conan, Benjamin Luce, et Isabelle Calmet. 2025. « Observation and LES modeling of an offshore atmospheric undular bore generated during sea-breeze initiation near a peninsula ». https://hal.science/hal-04996636.

This includes:
- the modified version of WRF (WRFstats as a submodule)
- WPS files used to link the chosen datasets and fix an ERA5 issue
- the WRF namelist input files for the simulation
- the Python post-processing library py\_wrf\_arps (as a submodule)
- the Python post-processing notebooks to draw the figures
- the LiDAR data used to draw the figures

This project does not contains the AROME data used for the comparison (Figures 3 to 5 in the paper). Please contact Météo-France if you need these data.

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
- **namelist_rst_real.input**, **namelist_rst.input** : WRF namelist of the restart run. The simulation has been run in two parts (first until May 18, 0800 UTC and then until May 19)
- **LAI_modif.py** : This script is called between ./real.exe and ./wrf.exe to add the higher resolution LAI and VEGRA field (see article 1)
- **slurm.job**, **slurm_LAI.job**, **slurm_real.job** : sbatch programs to run on the cluster
- **tslist** : list of the timeseries locations
- **wrfio_d0X.txt** : list the desired and undesired output variables

How to use :
- link namelist.wps in the WPS working directory
- run WPS
- link all the other files in the WRF working directory
- run real
- run LAI modif: you need to install py\_wrf\_arps first. If you skip this part, the monthly MODIS LAI and VEGFRA are used
- run WRF

### LAI modif
If you skip this part, the monthly MODIS LAI and VEGFRA are used instead of the high-resolution LAI and VEGFRA datasets.
Before running LAI modif, you need to:
- install py\_wrf\_arps first
- download the LAI and VEGFRA datasets (e.g. on [WEkEO](https://wekeo.copernicus.eu/))

## WPS files
Other important high-resolution datasets have been used (land-use, topography). References to these datasets can be found in the paper. 
To use them in WPS, the GEOGRID\_CLC\_EUDEM.TBL must be used

In addition, the METGRID\_ERA5.TBL.ARW solves an issue about the sea-surface temperature forcing with ERA5. [https://forum.mmm.ucar.edu/threads/issue-with-era5-sst-fields.12525/](https://forum.mmm.ucar.edu/threads/issue-with-era5-sst-fields.12525/)

## Postproc
Contains
- **1430_18_article1_GW_carac2.ipynb**: Figures 13 and 14 
- **1430_18_article1_GW_stats4-5_part1.ipynb**: Calculate and save GW caracteristics, run before the next one
- **1430_18_article1_GW_stats4-5_v2.ipynb**: Figures 15, 16c, 17b, 18
- **1430_19_GW_var.ipynb**: Figure 16a, 16b
- **1430_18_article1.ipynb**: Every other Figures

How to use
- These scripts need the py\_wrf\_arps library to run, the version of py\_wrf\_arps is written in the first cell
- You need to activate the conda environment first with the yaml file given in py\_wrf\_arps
- Also, the different paths (in py\_wrf\_arps) in lib/manage\_path and in class\_proj must be modified to your specific folders

