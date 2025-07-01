from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

import pandas as pd

# Load CSV dataset
df = pd.read_csv("liver_dataset.csv")

# View the first few rows
print(df.head())

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # List of expected feature keys from the form
        feature_keys = [
            'Age',
            'Durationofalcoholconsumptionyears',
            'Quantityofalcoholconsumptionquartersday',
            'Hemoglobingdl',
            'PCV',
            'MCVfemtoliterscell',
            'TotalCount',
            'Polymorphs',
            'Lymphocytes',
            'Monocytes',
            'Eosinophils',
            'Basophils',
            'PlateletCountlakhsmm',
            'Directmgdl',
            'Indirectmgdl',
            'TotalProteingdl',
            'Albumingdl',
            'Globulingdl',
            'ALPhosphataseUL',
            'SGOTASTUL',
            'SGPTALTUL'
        ]

        # Extract and validate inputs
        input_values = []
        for key in feature_keys:
            value = request.form.get(key)
            if value is None or value.strip() == '':
                return render_template("error.html", message=f"Missing input: {key}")
            try:
                input_values.append(float(value))
            except ValueError:
                return render_template("error.html", message=f"Invalid number format for: {key}")

        # Make prediction
        final_input = np.array(input_values).reshape(1, -1)
        prediction = model.predict(final_input)[0]

        result = (
            "✅ Patient is **not likely** to have liver cirrhosis."
            if prediction == 1 else
            "⚠️ Patient is **likely** to have liver cirrhosis."
        )

        return render_template("result.html", prediction=result)

    except Exception as e:
        return render_template("error.html", message=f"Unexpected Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
