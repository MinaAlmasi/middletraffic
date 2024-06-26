# Forecasting Bus Passenger Occupancy using Time Series Analysis
<p align="center">
  Anton Drasbæk Schiønning (<strong><a href="https://github.com/drasbaek">@drasbaek</a></strong>) &
  Mina Almasi (<strong><a href="https://github.com/MinaAlmasi">@MinaAlmasi</a></strong>)<br>
  <em>Data Science, Prediction, and Forecasting (F24)</em>
  <br>
  Aarhus University, Cognitive Science MSc.
  <br>
</p>
<hr>

## 🚌 About 
This repository contains scripts for developing a pipeline to forecast passenger occupancy at various bus stops on Midttrafik's route 1A in Aarhus. We trained several *NeuralProphet models* (via grid search), a *SARIMA* model, and three baselines. The main analysis was focused on the bus stop *Nørreport*. 

To run the pipeline, see the [Setup](#️-setup) and [Usage](#-usage) sections. Note that the initial preprocessing of `1A` cannot be reproduced as the file is not shareable. However, data for the five processed bus stops is available in the `data` folder, allowing the rest of the pipeline to be run.

### Project Overview
The repository is structured as such: 
| Folder/File               | Description |
|---------------------------|-------------|
| `data/`                   | Contains five bus stops from 1A (raw and aggregated).|
| `raw_data/`               | Empty folder where the raw data can be placed for the initial processing to run. |
| `plots/`                  | Plots used in the paper and appendix. |
| `results/`                | Evaluation results and forecasts for the main analysis. |
| `src/`                    | Python code related to the project. |


For a greater overview of the Python code, see the [src/README.md](src/README.md).

## 💻 Technical Requirements
Grid search and model training was run via  Ubuntu 22.04.3, Python 3.10.12 (UCloud, Coder Python 1.87.2). Other analysis work such as plotting was done locally on a Macbook Pro ‘13 (2020, 2 GHz Intel i5, 16GB of ram). Python's [venv](https://docs.python.org/3.10/library/venv.html) need to be installed for the code to run as intended. 

Code should also work on Python 3.12 although this cannot be guaranteed for all parts of the pipeline.


*Please also note that the advanced models were computionally intensive and were run on a 64 machine on UCloud*. 

## 🛠️ Setup
Prior to running the code, run the command below to create a virtual environment (`env`) and install necessary packages within it: 
```
bash setup.sh
```

##  🚀 Usage 
To run any script in the `src` folder, you can type specify the script's path in the terminal (with the `env` active):
```bash
# activate env
source env/bin/activate

# run script
python src/neural-prophet/test_prophet.py

# quit env 
deactivate
```
See also [src/README.md](src/README.md) for the scripts overview. Note that you cannot run most files in `process_data` as the raw data is not available on Git.

## 🌟 Acknowledgements 
This work was only possible thanks to our data provider, Midttrafik.