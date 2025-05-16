
# lesson-5-kubernetes-hpa

## Autoscaling the Age Detection API using Kubernetes Horizontal Pod Autoscaler (HPA)

This lesson shows how to set up **Horizontal Pod Autoscaling (HPA)** for the `detect-age-api` to automatically scale the number of pods based on CPU usage.

---

## Objectives

* Configure HPA to auto-scale pods between 1 and 10 replicas
* Use `metrics-server` to track real-time CPU usage
* Simulate traffic to trigger autoscaling

---

## Prerequisites

* A Kubernetes cluster (Minikube, Docker Desktop, etc.)
* `kubectl` configured for your cluster
* Working deployment from `lesson-2-kubernetes-basics`

---

## Project Structure

* `k8s-deployment.yml`: Deployment manifest for the API
* `hpa.yaml`: HPA manifest (based on CPU utilization)

---

## How to use

1. **Navigate to the lesson folder:**

   ```bash
   cd oreilly-mlops-bootcamp/Day2/lesson-5-kubernetes-hpa
   ```

2. **Ensure the age detection API is already deployed (from lesson 1):**

   ```bash
   kubectl apply -f k8s-deployment.yml
   ```

3. **Install metrics-server (if not already installed):**

   ```bash
   kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.5.1/components.yaml
   ```

4. **Apply the HPA:**

   ```bash
   kubectl apply -f hpa.yaml
   ```

5. **Check HPA status:**

   ```bash
   kubectl get hpa
   kubectl describe hpa detect-age-api-hpa
   ```

6. **Simulate load to trigger autoscaling:**

   ```bash
   kubectl run loadgen --restart=Never --image=busybox:1.28 -- \
     /bin/sh -c "while true; do wget -q -O- http://detect-age-api:5000/detect_age; done"
   ```

7. **Monitor scaling:**

   ```bash
   kubectl get pods
   kubectl get hpa
   ```

---

## Clean Up

```bash
kubectl delete -f hpa.yaml
kubectl delete -f ../lesson-1-kubernetes-basics/k8s-deployment.yml
```
