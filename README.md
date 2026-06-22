# Simulation & Analysis

Coursework and simulation models for the Simulation Analysis course (NEU, Sem 2). The repository contains discrete-event simulation experiments built in Python and Jupyter, grouped into two topics: queueing systems (M/M/C) and time-to-failure (TTF) reliability models.

## Contents

### `MMC-queue/` — Queueing simulations
Models of multi-server queueing systems and a call-center capacity study.

| File | Description |
| --- | --- |
| `mmc.ipynb` | M/M/C system simulation using the Excel/spreadsheet method. |
| `mmc_event.ipynb` | M/M/1 queue simulation built with an event-graph approach. |
| `CallCenterSim.ipynb` | Call-center simulation (financial vs. contact reps, optional cross-training) with Erlang service times. |
| `hw5.ipynb` | Homework 5 worksheet. |

### `TTF/` — Time-to-failure reliability models
Discrete-event simulations of a component system that fails and is repaired over time, with replications and confidence-interval analysis.

| File | Description |
| --- | --- |
| `TTF_Rep.py` | Standalone TTF simulation: 100 replications, reporting average failure time and average number of functional components. |
| `q1.ipynb` | TTF system simulation (Problem 1). |
| `q3.ipynb` | Modified TTF system: 100 replications with 95% confidence intervals for expected failure time and average functional components. |

### `data/`
| File | Description |
| --- | --- |
| `CallCounts.xls` | Call-count data used by the call-center simulation. |
| `data - problem6.txt` | Observed time data (Python list) used in analysis problems. |

## Requirements

- Python 3
- Jupyter
- `numpy`, `scipy`, `pandas`, `matplotlib`, `statsmodels`

```bash
pip install jupyter numpy scipy pandas matplotlib statsmodels
```

## Usage

Run the standalone script:

```bash
python TTF/TTF_Rep.py
```

Or open any notebook:

```bash
jupyter notebook
```

