# MLflow Experiment Tracking - Air Quality Classification

This lesson demonstrates MLflow experiment tracking using a Jupyter notebook for air quality classification.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Jupyter Notebook
```bash
jupyter notebook
```

### 3. Open the Notebook
Open `mlflow- Experiment Tracking.ipynb` in your browser.

### 4. Fix the Connection Issue (IMPORTANT)
Before running the notebook cells, add this code in a new cell at the beginning:

```python
import mlflow
mlflow.set_tracking_uri("file:./mlruns")
```

### 5. Run All Cells
Execute all cells in the notebook. The experiment will be logged locally in the `mlruns` folder.

## View Your Experiments

After running the notebook, you can view your experiments:

```python
import mlflow
import pandas as pd

# View all experiments
experiments = mlflow.search_experiments()
for exp in experiments:
    print(f"Experiment: {exp.name}")
    
    # View runs in this experiment
    runs = mlflow.search_runs(experiment_ids=[exp.experiment_id])
    for idx, run in runs.iterrows():
        print(f"  Run ID: {run['run_id']}")
        print(f"  Accuracy: {run.get('metrics.accuracy', 'N/A')}")
```

## Optional: Web UI
```bash
mlflow ui --port 5001
```
Then open: http://localhost:5001

## Files
- `mlflow- Experiment Tracking.ipynb`: Main notebook
- `air_quality.csv`: Dataset
- `requirements.txt`: Dependencies
