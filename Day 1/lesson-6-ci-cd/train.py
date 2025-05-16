import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

from data_pipeline.preprocessing import load_and_preprocess_data  

def train():
    X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess_data()

    mlflow.set_experiment("Income_Classification")
    with mlflow.start_run():

        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train, y_train)

        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)

        mlflow.log_param("model_type", "RandomForest")
        mlflow.log_metric("accuracy", acc)

        for label, scores in report.items():
            if isinstance(scores, dict):  
                mlflow.log_metric(f"{label}_precision", scores["precision"])
                mlflow.log_metric(f"{label}_recall", scores["recall"])

        # Save model and preprocessor
        joblib.dump(clf, "model/rf_model.pkl")
        joblib.dump(preprocessor, "model/preprocessor.pkl")
        mlflow.sklearn.log_model(clf, "model")

if __name__ == "__main__":
    train()
