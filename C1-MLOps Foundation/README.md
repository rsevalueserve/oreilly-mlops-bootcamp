
# c1-mlops-foundation

This repository contains hands-on exercises for the **MLOps Foundation** course. The exercises cover a variety of topics in machine learning operations, including Git version control, MLflow for model tracking, and Docker for deployment. Below are details of the hands-on activities and the structure of the repository.

## Repository Structure

### 2.2. Hands-on git
- **Description**: In this hands-on exercise, we implement a simple Random Forest model on the famous **Iris dataset**. We also use **Git** for version control to manage the code and track changes.
- **Files**:
  - `app.py`: Python script to train a random forest model on the Iris dataset.
  - `iris_model.pkl`: Pickled model for saving the trained Random Forest model.
  - `requirements.txt`: List of Python dependencies required for the Random Forest model.

### 3.3. Hands-on mlflow
- **Description**: This notebook demonstrates how to use **MLflow** to track and manage the development of a classification model for **air quality prediction**. The dataset includes various environmental features, such as temperature, humidity, pollutant levels (PM2.5, PM10, NO2, SO2, CO), and proximity to industrial areas and population density. The goal is to classify air quality into categories like "Good", "Moderate", or "Hazardous" using a **Logistic Regression model**. We use **MLflow's tracking server** and **model registry** to manage the model and different versions of it.
- **Files**:
  - `Hands-on_mlflow_Experiment_Tracking_and_Model_Management.ipynb`: Jupyter notebook with the code for training the logistic regression model, logging experiments with MLflow, and evaluating model performance.
  - `air_quality.csv`: Dataset used for training and testing the air quality prediction model.
  - `requirements.txt`: List of Python dependencies required for running the MLflow tracking server and model management.

### 4.2. Hands-on docker
- **Description**: This hands-on exercise involves building and deploying an **Age Detection model** using **Flask** and **Docker**. The application takes an image and returns the predicted age. It is containerized with a Dockerfile, making it easy to deploy the model in any environment.
- **Files**:
  - `app.py`: Flask application for serving the age detection model.
  - `Dockerfile`: Dockerfile to containerize the Flask app for easy deployment.
  - `requirements.txt`: List of Python dependencies required for the Flask application.
  - `model/`: Directory containing the trained age detection model.
  - `images/`: Directory containing images to test model.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/c1-mlops-foundation.git
   cd c1-mlops-foundation
   ```

2. **For Hands-on Git**:
   - Follow the videos to use Git commands with `app.py`.

3. **For Hands-on MLflow**:
   - Open `Hands-on_mlflow_Experiment_Tracking_and_Model_Management.ipynb` in Jupyter Notebook and run the code to track and manage the development of the air quality classification model using MLflow.
   - Make sure to run MLflow in the background by executing the following command in the terminal:
     ```bash
     mlflow ui
     ```
   - This will start the MLflow tracking server, and you can access the UI by navigating to `http://localhost:5000` 
     in your web browser to monitor experiments and log metrics.


4. **For Hands-on Docker**:
   - To build and run the Age Detection app using Docker:
     ```bash
     docker build -t age-detection-app .
     docker run -p 5000:5000 age-detection-app
     ```
     - The Flask app will be available at `http://localhost:5000`.

## Prerequisites

- **Python 3.x**
- **Docker** (for Hands-on Docker)
- **Jupyter Notebook** (for Hands-on MLflow)
- **Git** (for version control)
- **MLflow** (for Hands-on MLflow)

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. If you have suggestions or issues, please open an issue on GitHub.
