# ❤️ Heart Disease Prediction System

A **Machine Learning–based web application** that predicts the likelihood of heart disease based on patient data.  
This project uses a trained Logistic Regression model integrated with a Flask web interface.

---

## 📋 Overview

The Heart Disease Prediction System is designed to assist healthcare professionals and patients in identifying potential heart disease risks early.  
Users can input medical data through an intuitive web form, and the system provides instant feedback on whether the data indicates a **healthy heart** or a **defective heart**.

---

## 🚀 Features

- 🧠 **Machine Learning Model** (Logistic Regression) for binary classification  
- 💻 **Flask Web Interface** with modern responsive design  
- 📊 User-friendly data entry form with 13 key health indicators  
- 📈 Real-time predictions displayed directly on the web page  
- 🌐 Separate pages for About, Prediction, and Contact  

---

## 🧩 Input Features

| Feature | Description |
|----------|-------------|
| age | Age of the patient |
| sex | Sex (0 = Female, 1 = Male) |
| cp | Chest Pain Type (0–3) |
| trestbps | Resting blood pressure (mm Hg) |
| chol | Serum cholesterol (mg/dl) |
| fbs | Fasting blood sugar > 120 mg/dl (1 = True, 0 = False) |
| restecg | Resting electrocardiographic results (0–2) |
| thalach | Maximum heart rate achieved |
| exang | Exercise induced angina (1 = Yes, 0 = No) |
| oldpeak | ST depression induced by exercise |
| slope | The slope of the peak exercise ST segment |
| ca | Number of major vessels (0–3) colored by fluoroscopy |
| thal | Thalassemia (3 = Normal, 6 = Fixed defect, 7 = Reversible defect) |

---

## 🧠 Model Information

- **Model type:** Logistic Regression  
- **Training Dataset:** Heart Disease Dataset (Cleveland UCI Repository)  
- **Trained using:** `scikit-learn`  
- **File name:** `LRv1.pkl`

The model was trained to predict whether a patient has heart disease (1) or not (0) using the 13 features above.

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | HTML5, CSS3 |
| Backend | Flask (Python) |
| Machine Learning | scikit-learn, numpy, joblib |
| Deployment | Localhost / Flask Server |

---

## ⚙️ Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Heart-Disease-Prediction.git
   cd Heart-Disease-Prediction

2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the Flask app:
python app.py

5. Open your browser and go to:
http://127.0.0.1:5000

📞 Contact

Developer: Ahmed Ghonime
📧 Email: ahmedghonime@gmail.com

💼 LinkedIn: linkedin.com/in/ahmed-ghonime

🐙 GitHub: github.com/Ahmed-M-Gh

🧾 License

This project is open-source and available under the MIT License
.

📸 Screenshots
🏠 Home Page

A modern welcome screen with project introduction and navigation.

📊 Prediction Page

Interactive form that collects user input and displays real-time results.

ℹ️ About Page

Describes the model, its training process, and how it assists in medical decision-making.