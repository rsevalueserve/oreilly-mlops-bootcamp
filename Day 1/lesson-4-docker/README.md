

# Lesson 4: Dockerized Age Detection App

This lesson involves building and deploying an **Age Detection** ML model with **Flask** and **Docker**.

##  Objective
Wrap an ML model in a **Flask API**, containerize it with **Docker**, and run it locally.

##  Files
- `app.py`: Flask app for age prediction.
- `Dockerfile`: Builds the container image.
- `requirements.txt`: Dependencies for the Flask app.
- `model/`: Folder containing trained model files.
- `images/`: Sample images for testing.

##  How to Use
1. Clone the repo:
   ```bash
   https://github.com/AmmarMohanna/oreilly-mlops-bootcamp.git
   cd oreilly-mlops-bootcamp/Day1/lesson-4-docker

2. Build the Docker image:

    ```bash
    docker build -t age-detection-app .

3. Run the container:
    ```bash
    docker run -p 5000:5000 age-detection-app

Access the API at http://localhost:5000

