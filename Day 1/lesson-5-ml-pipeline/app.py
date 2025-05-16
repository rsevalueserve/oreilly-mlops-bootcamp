from flask import Flask, request, jsonify
import mlflow.sklearn
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
import joblib

app = Flask(__name__)


# Use your actual run_id as a string
experiment_id = "143003826376354799"
run_id = "e681d08cc4c6447f859d63f01a1d15a3"
model_uri = f"mlruns/{experiment_id}/{run_id}/artifacts/model"
model = mlflow.sklearn.load_model(model_uri)

preprocessor = joblib.load("model/preprocessor.pkl") 
 
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Check if the input is in JSON format
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided or invalid format"}), 400

        # Convert the data to a pandas DataFrame
        data = pd.DataFrame([data])


        # Apply preprocessing to input data
        processed_data = preprocessor.transform(data)
        
        # Make the prediction
        prediction = model.predict(processed_data)

        # Map prediction back to label
        label_map = {0: " <=50K", 1: " >50K"}
        predicted_label = label_map[int(prediction[0])]

        # Return the prediction
        return jsonify({"prediction": predicted_label})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
