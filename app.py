import streamlit as st
import tensorflow as tf
import joblib
import numpy as np

# 1. Load the "Brain" and the "Cleaning Rules"
model = tf.keras.models.load_model('nids_model.h5')
scaler = joblib.load('scaler.pkl')

# 2. Page Setup
st.set_page_config(page_title="Nexus NIDS", page_icon="🛡️")
st.title("🛡️ Nexus Network Intrusion Detection")
st.markdown("---")

# 3. Create the Input Form
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        duration = st.number_input("Duration", min_value=0.0)
        src_bytes = st.number_input("Source Bytes", min_value=0)
        count = st.number_input("Count (Connections)", min_value=0)
    with col2:
        dst_bytes = st.number_input("Destination Bytes", min_value=0)
        logged_in = st.selectbox("Logged In? (1=Yes, 0=No)", [0, 1])
        protocol = st.selectbox("Protocol Type", ["tcp", "udp", "icmp"])

    submit = st.form_submit_button("Analyze Traffic")

# 4. The Prediction Logic
if submit:
    # Initialize all 41 features used during training
    input_data = np.zeros((1, 41))
    
    # Map UI inputs to feature columns
    input_data[0, 0] = duration     # duration
    input_data[0, 4] = src_bytes    # src_bytes
    input_data[0, 5] = dst_bytes    # dst_bytes
    input_data[0, 11] = logged_in   # logged_in
    input_data[0, 22] = count       # count

    # Demo simulation
    if count > 100 and logged_in == 0:
        input_data[0, 24] = 0.9   # serror_rate
        input_data[0, 28] = 0.1   # same_srv_rate
        input_data[0, 32] = 255   # dst_host_count

    # Optional protocol mapping
    # tcp=1, udp=2, icmp=3 (adjust if your training used different encoding)
    protocol_map = {"tcp": 1, "udp": 2, "icmp": 3}
    input_data[0, 1] = protocol_map[protocol]

    # Scale + predict
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)
    prob = float(prediction[0][0])

    # Show results
    if prob > 0.5:
        st.error(f"🚨 INTRUSION DETECTED! (Confidence: {prob*100:.2f}%)")
        st.warning("Action Recommended: Block IP address and inspect packet headers.")
    else:
        st.success(f"✅ TRAFFIC NORMAL (Safety Score: {(1-prob)*100:.2f}%)")
        st.info("Network integrity verified. No immediate threats found.")
