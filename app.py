import streamlit as st
import pickle
import numpy as np

 # 1. Load the trained model
try:
  

# 2. App Title and Description
st.title("Gold Price Prediction App")
st.write("""
This app predicts the **GLD (Gold Price)** based on financial market metrics.
""")

st.sidebar.header("Input Features")

# 3. Input fields matching the model's expected features: ['SPX', 'USO', 'SLV', 'EUR/USD']
def user_input_features():
    spx = st.sidebar.number_input("SPX Index (S&P 500)", min_value=0.0, value=1447.16, step=1.0)
    uso = st.sidebar.number_input("USO (United States Oil Fund)", min_value=0.0, value=78.47, step=0.1)
    slv = st.sidebar.number_input("SLV (Silver ETF)", min_value=0.0, value=15.18, step=0.1)
    eur_usd = st.sidebar.number_input("EUR/USD Exchange Rate", min_value=0.0, value=1.47, step=0.01)

    # Pack features into a numpy array for prediction
    features = np.array([[spx, uso, slv, eur_usd]])
    return features

input_data = user_input_features()

# Display the input values back to the user
st.subheader("Current Input Parameters")
st.write(f"**SPX:** {input_data[0][0]} | **USO:** {input_data[0][1]} | **SLV:** {input_data[0][2]} | **EUR/USD:** {input_data[0][3]}")

# 4. Predict Button and Output
if st.button("Predict Gold Price"):
    try:
        # If you scaled your training data using StandardScaler, your inputs should technically
        # be transformed here using scaler.transform(input_data) before prediction.
        prediction = model.predict(input_data)

        st.success(f"### Predicted GLD Price: ${prediction[0]:.2f}")
    except NameError:
        st.error("Model could not be loaded. Prediction aborted.")
