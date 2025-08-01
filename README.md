# SMART_IRRIGATION_AICTE_SHELL_INTERNSHIP
This is an AICTE Shell Internship Cycle 2 Code.
This project was developed as part of the **AICTE Shell Internship – Cycle 2** under the **Smart Agriculture** theme. It demonstrates how **Machine Learning (ML)** can be applied to optimize irrigation systems using environmental sensor data.

## 🧠 Project Overview

The system predicts whether each sprinkler in a farm zone should be turned **ON** or **OFF**, based on real-time sensor values such as soil moisture, humidity, temperature, and more. A **trained classification model** processes inputs from **20 sensors**, simulates decision-making, and outputs recommendations in a clean and simple web interface built using **Streamlit**.

This AI-powered solution helps conserve water, reduce human effort, and promote sustainable agriculture practices — making it ideal for both small and large-scale farms.

---

## 🔧 Features

- 🚀 **Machine Learning-Based Prediction:** Classifies ON/OFF sprinkler decisions based on 20 real-time sensor values.
- 🎛️ **Interactive Streamlit UI:** Sliders allow simulation of sensor inputs in a user-friendly interface.
- 🧮 **Pre-trained Model Integration:** Uses `Joblib` to load a trained Random Forest model for fast predictions.
- 📊 **Visual Feedback:** Displays parcel-wise sprinkler status clearly with labels and emojis.
- 📦 **Modular & Scalable:** Designed to support real-time IoT integration in future versions.

---

## 📂 Project Highlights

- ✅ **Internship Program:** AICTE Shell Internship (Cycle 2)  
- 🏷️ **Domain:** Smart Agriculture  
- 🖥️ **Platform:** Streamlit web application  
- 🧪 **Algorithm Used:** Random Forest Classifier  
- 📁 **Model Format:** `.pkl` (Joblib serialized model)  
- 🛠️ **Technologies:** Python, NumPy, Pandas, Scikit-learn, Streamlit  

---

## 📌 Technical Summary

- The dataset was cleaned and normalized by removing invalid/false indexes and scaling all sensor inputs between **0 and 1**.
- Several algorithms like Logistic Regression, Decision Trees, and Random Forests were evaluated, and **Random Forest** was selected based on its accuracy, robustness, and ability to handle high-dimensional input.
- The system uses 20 sensor values per input instance, reshaped into a 1x20 array before being fed into the model for prediction.
- Sprinkler status (ON/OFF) is shown for each **parcel (zone)** using a clean, emoji-enhanced display to improve readability and accessibility.

---

## 🔮 Future Scope

- 🌐 **Live Sensor Integration:** Connect to IoT soil/moisture sensors for real-time automatic predictions.
- 🧠 **Advanced Models & Tuning:** Incorporate algorithms like XGBoost, CatBoost, or Neural Networks, and implement hyperparameter tuning (e.g., GridSearchCV).
- ☁️ **Cloud Deployment:** Host on platforms like AWS, Heroku, or Streamlit Cloud for remote farm access.
- 🔁 **Adaptive Learning:** Enable models that learn and improve based on user feedback and long-term soil behavior.

---

## 🙌 Acknowledgment

This project was created as part of the **AICTE Shell Internship – Cycle 2** with the aim of addressing real-world problems in agriculture through artificial intelligence.

