# Lesson 3: Experiment Tracking with MLflow

This lesson demonstrates how to track experiments using **MLflow**, applied to a **logistic regression model** for air quality classification.

##  Objective
Track hyperparameters, metrics, and model versions for reproducibility and experiment comparison.

##  Files
- `mlflow-Experiment Tracking.ipynb`: Notebook for model training and MLflow tracking.
- `air_quality.csv`: Dataset with environmental features.
- `requirements.txt`: Required packages.

##  How to Use
1. Clone the repo:
   ```bash
   git clone https://github.com/AmmarMohanna/oreilly-mlops-bootcamp.git
   cd oreilly-mlops-bootcamp//Day1/lesson-3-mlflow

2. Install dependencies and start Jupyter or run in google collab:

    ```bash
    pip install -r requirements.txt
    jupyter notebook

3. Open and run the notebook.

    * Train a logistic regression model
    * Log parameters, metrics, and model artifacts using MLflow


4. Start MLflow tracking UI in another terminal:
    ```bash
    mlflow ui
    
Visit http://localhost:5000 to monitor your experiments.
