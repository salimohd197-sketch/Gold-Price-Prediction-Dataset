import streamlit as st
import pickle
import numpy as np

# Page configuration
st.set_page_config(page_title="Gold Price Prediction", layout="centered")

# App header
st.title("Gold Price Prediction App")
st.write("Enter the required details below to predict the gold price.")

# 1. Load the model safely
@st.cache_resource
def load_model():
    try:
        # Apni pickle file ka sahi naam yahan check karlein
        with open('gold_price_model.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

model = load_model()

# 2. UI and Prediction Logic
if model is None:
    st.error("Error: 'gold_price_model.pkl' file nahi mili! Please check your GitHub repository.")
else:
    st.success("Model loaded successfully!")
    
    st.subheader("Enter Features:")
    
    # NOTE: Apne model ke mutabiq input fields ko tabdeel (change) karlein
    # Agar aapka model 4 inputs leta hai, to humne misal ke taur par yeh likha hai:
    spx = st.number_input("SPX Index", value=0.0)
    uso = st.number_input("USO (Oil Price)", value=0.0)
    slv = st.number_input("SLV (Silver Price)", value=0.0)
    eur_usd = st.number_input("EUR/USD Ratio", value=0.0)
    
    if st.button("Predict Gold Price"):
        # Inputs ko array mein convert karna
        features = np.array([[spx, uso, slv, eur_usd]])
        
        # Prediction calculation
        prediction = model.predict(features)
        
        # Display output
        st.metric(label="Predicted Gold Price", value=f"${prediction[0]:.2f}")
