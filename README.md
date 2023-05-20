# Functions for process and plot data from FotoAgua project

The FotoAgua project is a partnership between the sanitation company of the State of Paraná (SANEPAR) and the Federal University of Paraná (UFPR). The goal is to evaluate the impacts from a floating photovoltaic power plant over the water quality of Passaúna reservoir, which is a public supply reservoir of the city of Curitiba, in the state of Paraná, in the south of Brazil. Four automatic sensors (miniDOTs) were installed in the reservoir, 2 underneath the photovoltaic system (surface and bottom), and 2 at a reference point away from the system (surface and bottom). The sensors provide measurements at each 5 minutes, since october 27, 2022. The data is retrieved each month from the memory card of the sensor in CSV format. The sensors generate a CSV for each day, with measurements of dissolved oxygen and water temperature.

These code can:
* **concatenate daily CSV files into one file**;
* **perform the Mann-Whitney non-parametric test to compare data from different sensors**;
* **plot data**.

## Floating Photovoltaic Power Plant at Passaúna Reservoir

<div style="text-align: center;">
<img src=images/210408_usina_passauna_2.jpeg alt="Floating Photovoltaic Power Plant at Passaúna Reservoir"/>
</div>

## MiniDOT plot example

<div style="text-align: center;">
<img src=images/minidot_oct-22_fev-23.svg alt="Floating Photovoltaic Power Plant at Passaúna Reservoir"/>
</div>

## Hypothesis testing example

### Dissolved Oxygen

| Hypothesis | Surface | Bottom |
|----------|----------|----------|
|LR = PV1 | False (stat: -71.7, p-valor: 0.0) | False (stat: 163.3, p-valor: 0.0) |
|LR > PV1 | True | False |
|LR < PV1 | False | True |

### Temperature

| Hypothesis | Surface | Bottom |
|----------|----------|----------|
|LR = PV1 | False (stat: 3.77, p-valor: 8.03e-05) | False (stat: 106.9, p-valor: 0.0) |
|LR > PV1 | False | False |
|LR < PV1 | True | True |

## Acronyms for the measurement locations

* **LR** = lake reference
* **PV1** = photovoltaic system

# First Steps

In the root of the project you must create 4 folders and 4 sub-folders in the minidit_data folder

1. minidot_concat
2. minidot_data
    1. lr_sup
    2. lr_fundo
    3. pv1_sup
    4. pv1_fundo
3. minidot_graphs
4. minidot_stats

## Folders purpose

* **minidot_concat**: receives the concatenated files
* **minidot_data**: stores the daily CSV files from miniDOT sensors in sub-folders
  * **lr_fundo**: stores the daily CSV files from the bottom sensor at LR
  * **lr_sup**: stores the daily CSV files from the surface sensor at LR
  * **pv1_fundo**: stores the daily CSV files from the bottom sensor at PV1 
  * **pv1_sup**: stores the daily CSV files from the surface sensor at PV1
* **minidot_graphs**: receives the figures saved by the plot function
* **minidot_stats**: receives the CSV with the hypotheses test results

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
#### Hypothesis testing

```
python minidot_tests.py
```

