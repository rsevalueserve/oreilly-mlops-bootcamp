
# lesson-2-kubernetes-basics

##  Deploying a Dockerized Age Detection Model with Kubernetes

This lesson demonstrates how to deploy a pre-built age detection model (served via a Flask API) on a local Kubernetes cluster using **Deployments** and **Services**.

---

##  Objectives

* Deploy the Dockerized age detection API on Kubernetes
* Create Kubernetes `Deployment` and `Service` resources
* Expose the API externally using `NodePort`

---

##  Prerequisites

* Docker Desktop (with Kubernetes enabled) or Minikube
* kubectl
* Postman (for testing)

---

##  Project Structure

* `Dockerfile`: Container image for the Flask API
* `k8s-deployment.yml`: Kubernetes manifest (Deployment + Service)

---

## How to use 
1. **Clone the repo:**
   ```bash
   git clone https://github.com/AmmarMohanna/oreilly-mlops-bootcamp.git
   cd oreilly-mlops-bootcamp/Day2/lesson-2-kubernetes-basics

2. **Pull or Build Docker Image**

    Option A – Pull:

    ```bash
    docker pull mariamhsein/age_detect:latest
    ```

    Option B – Build locally:

    ```bash
    docker build -t detect-face-api:latest .
    ```


3. **Deploy to Kubernetes:**

    ```bash
    kubectl apply -f k8s-deployment.yml
    ```

4. **Test the API:**

    Send a POST request via Postman to:

    ```
    http://localhost:30600/detect_age
    ```





