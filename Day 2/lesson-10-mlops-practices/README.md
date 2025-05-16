
# lesson-10-mlops-practices

## End-to-End MLOps: Model Registry, Monitoring & Kubernetes Deployment

This project demonstrates a full MLOps pipeline using the UCI Adult Income dataset. It integrates **MLflow**, **Flask**, **Prometheus**, **Grafana**, and **Kubernetes** to create a scalable and monitorable ML deployment.

---

## Objectives

* Train and version models using **MLflow**
* Serve predictions using a **Flask API**
* Monitor performance with **Prometheus** and **Grafana**
* Deploy everything with **Kubernetes**

---

## Prerequisites

* Python 3.x
* Docker + Docker Hub account
* A Kubernetes cluster (e.g., Docker Desktop with K8s enabled)
* `kubectl` configured
* MLflow installed
* Prometheus & Grafana Docker images

---

## Project Structure

Sure! Here's a shorter version of each item (3–4 words each) for a concise overview:

---

##  Project Structure 


* **`app.py`** – Serves predictions + metrics
* **`dockerfile`** – Container build instructions
* **`requirements.txt`** – Required Python packages
* **`data/`** – Raw + new datasets
* **`data_pipeline/`** – Data cleaning + encoding
* **`train.py`** – Model training + logging
* **`test/`** – Unit + API testing
* **`k8s-deployment.yaml`** – Flask deployment + service
* **`monitoring-deployment.yaml`** – Monitoring stack deployment

---

## How to Use

1. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

2. **Train & Register Your Model (MLflow)**

    Start the MLflow UI:

    ```bash
    mlflow ui
    ```

    Visit `http://localhost:5000`.

    Train and register a model:

    ```bash
    python train.py
    ```

3. **Build and Push Docker Image**

    ```bash
    docker login
    docker build -t yourdockerhub/income-flask-app:latest .
    docker push yourdockerhub/income-flask-app:latest
    ```


4. **Kubernetes Deployment**

    Deploy Flask app, Prometheus, and Grafana:

    ```bash
    kubectl apply -f monitoring-deployment.yaml
    kubectl apply -f k8s-deployment.yaml
    ```
6. **Test the API**

| Service    | URL                                              |
| ---------- | ------------------------------------------------ |
| Flask API  | [http://localhost:30800/predict](http://localhost:30800/predict) |
| Prometheus | [http://localhost:30909](http://localhost:30909) |
| Grafana    | [http://localhost:30009](http://localhost:30009) |


7. **Monitoring**

* Login: `admin / admin`
* Add Data Source:

  * Type: **Prometheus**
  * URL: `http://prometheus-service:9090`
* Create Dashboards:

  * `predict_requests_total`
  * `predict_exceptions_total`
  * `predict_request_latency_seconds`


## Summary

You’ve built an end-to-end MLOps pipeline that includes:

* **Model training + versioning** with MLflow
* **Prediction serving** with Flask
* **Real-time monitoring** with Prometheus
* **Live dashboards** with Grafana
* **Production-grade deployment** via Kubernetes


