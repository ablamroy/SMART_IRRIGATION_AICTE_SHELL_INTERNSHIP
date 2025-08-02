import streamlit as st
import numpy as np
import joblib  

# 🌿 Introductory Content 
st.set_page_config(page_title="Smart Sprinkler System", layout="centered")
st.title("🌾 Smart Sprinkler System")
st.markdown("""
Welcome to the **AI-powered Smart Sprinkler System** demo!  
This tool helps you simulate smart irrigation decisions using machine learning based on 20 sensor readings from a farm field.
Each sensor input is expected to be **scaled between 0 and 1**, where:

- `0.0` → low reading (e.g., very dry soil)
- `1.0` → high reading (e.g., fully moist soil)

**Try adjusting the sliders below to simulate field conditions and click 'Predict Sprinklers' to see the results!**
""")

# Sidebar – Quick Reference
st.sidebar.header("Project Info")
st.sidebar.markdown("""
- **Internship:** AICTE Smart Agriculture  
- **Module:** Sprinkler Automation  
- **Model Type:** ML Classifier (Joblib format)  
- **Inputs:** 20 Scaled Features  
- **Outputs:** 20 ON/OFF States  
""")

# Load the trained model
model = joblib.load("Farm_Irrigation_System.pkl")  
st.title("Smart Sprinkler System")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")
# Collect sensor inputs (scaled values)
sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)
    
# Predict button
if st.button("Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### Prediction:")
    for i, status in enumerate(prediction):
        st.write(f"Sprinkler {i} (parcel_{i}): {'ON' if status == 1 else 'OFF'}")

# Additional Features

# Data Privacy Note
st.markdown("""
#### 🔒 Data Privacy & Ethics
This system respects data privacy norms.  
In real-world use, all sensor data is securely stored and anonymized to protect farmers' identity and crop data.
""")

# Summary / Footer
st.divider()
st.markdown("""
#### Summary
This dashboard simulates a **real-time AI irrigation advisor**. You can test various environmental conditions and see how smart models optimize water usage — a step toward precision farming.

---
👨‍💻 *Developed for AICTE Internship Project on Smart Agriculture by Abram Roy Thomas*  
""")
