import streamlit as st
import joblib
import numpy as np
import tflite_runtime.interpreter as tflite

# Load scaler
scaler = joblib.load("scaler.pkl")

# Load TFLite model
interpreter = tflite.Interpreter(model_path="nids_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

st.set_page_config(page_title="Nexus NIDS", page_icon="🛡️")
st.title("🛡️ Nexus Network Intrusion Detection")
st.markdown("---")

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

if submit:
    input_data = np.zeros((1, 41), dtype=np.float32)

    input_data[0, 0] = duration
    input_data[0, 4] = src_bytes
    input_data[0, 5] = dst_bytes
    input_data[0, 11] = logged_in
    input_data[0, 22] = count

    if count > 100 and logged_in == 0:
        input_data[0, 24] = 0.9
        input_data[0, 28] = 0.1
        input_data[0, 32] = 255

    protocol_map = {"tcp": 1, "udp": 2, "icmp": 3}
    input_data[0, 1] = protocol_map[protocol]

    scaled_input = scaler.transform(input_data).astype(np.float32)

    interpreter.set_tensor(input_details[0]["index"], scaled_input)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]["index"])
    prob = float(prediction[0][0])

    if prob > 0.5:
        st.error(f"🚨 INTRUSION DETECTED! (Confidence: {prob*100:.2f}%)")
        st.warning("Action Recommended: Block IP address and inspect packet headers.")
    else:
        st.success(f"✅ TRAFFIC NORMAL (Safety Score: {(1-prob)*100:.2f}%)")
        st.info("Network integrity verified. No immediate threats found.")
