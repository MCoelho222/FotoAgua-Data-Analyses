# Functions for processing and plot data from FotoAgua project

The FotoAgua project is a partnership between the sanitation company of the State of Paraná (SANEPAR) and the Federal University of Paraná (UFPR). The goal is to evaluate the impacts from a floating photovoltaic power plant over the water quality of Passaúna reservoir, which is a public supply reservoir of the city of Curitiba, in the state of Paraná, in the south of Brazil. Four automatic sensors (miniDOTs) were installed in the reservoir, 2 underneath the photovoltaic system (surface and bottom), and 2 at a reference point away from the system (surface and bottom). The sensors provide measurements at each 5 minutes, since october 27, 2022. The data is retrieved each month from the memory card of the sensor in CSV format. The sensors generate a CSV for each day, with measurements of dissolved oxygen and water temperature.

# Acronyms for the measurement locations

LR = lake reference
PV1 = photovoltaic system

# Folder names and meaning

-minidot_data: stores the daily CSV files from miniDOT sensors in sub-folders
    -lr_fundo: stores the daily CSV files from the bottom sensor at LR
    -lr_sup: stores the daily CSV files from the surface sensor at LR
    -pv1_fundo: stores the daily CSV files from the bottom sensor at PV1 
    -pv1_sup: stores the daily CSV files from the surface sensor at PV1

## Creating virtual environment and installing packages

```
python -m venv venv
```
```
venv/Scripts/activate
```
```
pip install -r requirements.txt
```

## Preparing data

### MIniDOT

1. Copy the files from minidot sensor (**do not change the name of the files**) into the correspondent sub-folder of the **minidot_data** folder;
2. After running the concatenating function, the files will be stored in the folder **minidot_concat**.

#### Concatenating

```
python minidot_concat.py
```

#### Plotting

```
python minidot_plot.py
```

