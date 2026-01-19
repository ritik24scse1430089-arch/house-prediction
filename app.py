import streamlit as st
import joblib
import numpy as np
model = joblib.load("house_price.pkl")
st.title("Student Pass/Fail Prediction System")
living_area = st.number_input("Living Area", min_value=0.0, max_value=40.0, value=10.0)
numbers of floor = st.number_input("Floor Number", min_value=0.0, max_value=100.0,value=75.0)
if st.button("Predict Result"):
 input_data = np.array([[living area, number of floor]])
 prediction = model.predict(input_data)
 if prediction[0] == 1:
  st.success("Prediction: PASS")
 else:
  st.error("Prediction: FAIL")