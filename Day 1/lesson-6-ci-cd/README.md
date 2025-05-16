
# Lesson 6: CI/CD Pipeline with GitHub Actions

This lesson extends the ML pipeline by automating build, test, and deploy using **CI/CD** via **GitHub Actions**.

##  Objective
Integrate a CI/CD pipeline that:
- Runs tests
- Builds Docker image
- Deploys the Flask API automatically

##  Files
- All files from `lesson-5-ml-pipeline`
- `.github/workflows/`: CI/CD workflows for GitHub Actions
- `tests/`: Unit test scripts

## Jobs Defined
1. **Test (CI)**
    * Checkout code
    * Set up Python
    * Install dependencies
    * Run unit tests using pytest

2. **Deploy (CD)**: 

    * Triggered only if tests pass
    * Build Docker image for FastAPI app
    * Run the app in a Docker container
    * Send a test request to verify the app is live
##  How to Use
1. Clone the repo:
   ```bash
   git clone https://github.com/AmmarMohanna/oreilly-mlops-bootcamp.git
   cd oreilly-mlops-bootcamp/Day1/lesson-6-ci-cd
2. Push code to **GitHub**.
3. GitHub Actions will automatically:
   - Run tests on each push
   - Build the Docker image

