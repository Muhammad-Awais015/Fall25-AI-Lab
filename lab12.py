import pickle
import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder

# Flask App
app = Flask(__name__)

# Load the pre-trained model
model_svr = pickle.load(open("model_svr.pkl", "rb"))

# Load the processed dataset to extract unique values for dropdowns
processed_data = pd.read_csv("processed_data.csv")

# Define the categorical and numeric columns
categorical_columns = ['Region', 'Season']
numeric_columns = ['CO2_ppm', 'Humidity_%', 'Pressure_hPa', 'WindSpeed_km_h','PollutionIndex', 'HeatIndex', 'Rainfall_mm']

# Define the exact feature order used during model training
model_feature_order = ['CO2_ppm', 'Humidity_%', 'Pressure_hPa', 'WindSpeed_km_h','PollutionIndex', 'HeatIndex', 'Rainfall_mm', 'Region', 'Season']

# Initialize label encoders for categorical columns
label_encoders = {'Region': LabelEncoder(),'Season': LabelEncoder()}

# Fit label encoders on the categorical columns in the processed data
for col in categorical_columns:
    label_encoders[col].fit(processed_data[col])

# Home Page Route
@app.route("/")
def index():
    # Fetch unique values for dropdowns from processed_data.csv
    sample_data = {
        'Region': processed_data['Region'].unique(),
        'Season': processed_data['Season'].unique()
    }
    return render_template("index.html", sample_data=sample_data)

# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    # Read numeric values
    input_data = {
        col: float(request.form.get(col)) for col in numeric_columns
    }
    
    # Read & encode categorical values
    for col in categorical_columns:
        val = request.form.get(col)
        input_data[col] = label_encoders[col].transform([val])[0]

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Ensure the input data has the same feature order as the model
    input_df = input_df[model_feature_order]

    # Make prediction
    predicted_temp = model_svr.predict(input_df)[0]

    # Fetch unique values for dropdowns from processed_data.csv (for the form)
    sample_data = {'Region': processed_data['Region'].unique(),'Season': processed_data['Season'].unique()}
    
    # Pass both sample_data and predicted_price to the template
    return render_template("index.html",sample_data=sample_data,predicted_temp=round(predicted_temp, 2))


if __name__ == "__main__":
    app.run(debug=True)
