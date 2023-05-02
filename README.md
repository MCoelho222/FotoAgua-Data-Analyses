# Functions for processing and plot data from FotoAgua project

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

