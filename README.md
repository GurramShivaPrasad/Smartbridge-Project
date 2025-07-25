# Smartbridge-Project
# 🧬 Revolutionizing Liver Care: Predicting Liver Cirrhosis using Advanced Machine Learning

A machine learning-based web application for early prediction of liver cirrhosis using structured clinical and laboratory data. This tool provides healthcare professionals with a non-invasive, real-time diagnostic aid through a simple web interface.

---

## 🚀 Project Overview

This project leverages a trained XGBoost classifier to predict liver cirrhosis based on patient data such as blood test results and clinical parameters. The interface is built using Flask, and predictions are made in real time when a user submits the form.

---

## 🎯 Objective

To create a fast, accurate, and non-invasive diagnostic system that helps healthcare providers detect liver cirrhosis early using machine learning.

---

## 🧪 Features

- ✅ Real-time prediction using a trained **XGBoost** model  
- 📝 Web-based form for medical parameter input  
- 📊 Prediction output: **Yes (Cirrhosis)** / **No (No Cirrhosis)**  
- 🧼 Clean dataset with numeric-only features  
- 🧠 Achieved **100% accuracy** on test data (based on available dataset)

---

## 📊 Dataset Overview

The dataset includes numeric medical features such as:

- **Demographics**: Age, Alcohol Consumption (duration & quantity)
- **Blood Parameters**: Hemoglobin, RBC, WBC, Platelet count, PCV, MCH, MCHC
- **Liver Enzymes**: ALP, SGOT (AST), SGPT (ALT)
- **Proteins and Bilirubin**: Albumin, Total Protein, Total Bilirubin
- **Cholesterol**: TCH, TG, LDL, HDL
- **Target**: `0 = Cirrhosis`, `1 = No Cirrhosis`

## 🛠 Tech Stack

| Component  | Technology           |
|------------|----------------------|
| ML Model   | XGBoost              |
| Backend    | Python, Flask        |
| Frontend   | HTML                 |
| Tools      | Jupyter Notebook, VS Code |
| Dataset    | CSV Format (from Kaggle) |


## ⚙️ How to Run the Project
```bash
1. Clone the Repository
git clone https://github.com/GurramShivaPrasad/Smartbridge-Project.git
cd liver-cirrhosis-predictor

2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate

3. Install Required Packages
pip install -r requirements.txt

4. Run the Flask App
python app.py
```
---

## 🧪 Sample Workflow

Open the web form.

Enter patient values (e.g., age, hemoglobin, ALT levels).

Click Submit.

Receive prediction:

Yes = Patient at risk of Cirrhosis

No = No Cirrhosis detected

---

## 👩‍💻 Contributor

Gurram Shiva Prasad – Developer & Designer

---

## 📜 License

This project is licensed under the MIT License.

---

> Machine learning powered web application designed to predict liver cirrhosis in real time using clinical and laboratory data,fast,and accurate tool to support early diagnosis and improve patient outcomes using machine learning.


