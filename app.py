import streamlit as st
import pandas as pd
import pickle

# Load the full pipeline (Preprocessing + Model)
with open("model_rf.pkl", "rb") as f:
    pipeline = pickle.load(f)

with open("fert.pkl", "rb") as f:
    fert = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="Crop Prediction System", page_icon="🌾", layout="wide")
st.title("🌾 Crop Prediction System")

st.sidebar.header("📌 Enter Soil & Environmental Parameters")

# Numeric Inputs
temperature = st.sidebar.number_input("🌡 Temperature (°C)", min_value=0.0, max_value=100.0, value=25.0)
moisture = st.sidebar.number_input("💧 Moisture (%)", min_value=0.0, max_value=1.0, value=0.5)
rainfall = st.sidebar.number_input("🌧 Rainfall (mm)", min_value=0.0, max_value=500.0, value=200.0)
pH = st.sidebar.number_input("🧪 Soil pH Level", min_value=0.0, max_value=14.0, value=7.0)
nitrogen = st.sidebar.number_input("🟢 Nitrogen (mg/kg)", min_value=0.0, max_value=200.0, value=50.0)
phosphorous = st.sidebar.number_input("🔴 Phosphorous (mg/kg)", min_value=0.0, max_value=200.0, value=50.0)
potassium = st.sidebar.number_input("🟡 Potassium (mg/kg)", min_value=0.0, max_value=200.0, value=50.0)
carbon = st.sidebar.number_input("🌾 Carbon Content (%)", min_value=0.0, max_value=10.0, value=1.0)
fertilizer = st.sidebar.selectbox("🌿 Fertilizer Type", ['Compost', 'Balanced NPK Fertilizer', 'Water Retaining Fertilizer', 'Organic Fertilizer', 'Gypsum', 'Lime', 'DAP', 'Urea', 'Muriate of Potash', 'General Purpose Fertilizer'])

# Categorical Inputs
soil = st.sidebar.selectbox("🌍 Soil Type", ['Loamy Soil', 'Peaty Soil', 'Acidic Soil', 'Neutral Soil', 'Alkaline Soil'])

# Prepare input data
input_data = pd.DataFrame([{
    "Temperature": temperature,
    "Moisture": moisture,
    "Rainfall": rainfall,
    "PH": pH,
    "Nitrogen": nitrogen,
    "Phosphorous": phosphorous,
    "Potassium": potassium,
    "Carbon": carbon,
    "Soil": soil,
    "Fertilizer": fertilizer
}])

# Prediction
st.markdown("---")
st.subheader("🌾 Predicted Crop")

try:
    prediction = pipeline.predict(input_data)  # Uses full pipeline
    st.success(f"✅ Recommended Crop: **{prediction[0]}**")
except Exception as e:
    st.error(f"⚠️ Error making prediction: {e}")

st.markdown("---")
st.markdown("<h4 style='text-align: center;'>🌿 Developed with ❤️ for Smart Farming 🌿</h4>", unsafe_allow_html=True)
