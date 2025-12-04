import streamlit as st
import plotly.express as px
from modules.brain_scanner import BrainScanner

st.set_page_config(page_title="Layer CT Scan", layout="wide")
st.title("🧬 Neural Layer CT Scan")
scanner = BrainScanner('gpt2')
text = st.text_input("Input Stimulus:", "The concept of self is an illusion.")
if st.button("Scan Neural Layers"):
    with st.spinner("Extracting hidden states..."):
        df_layers, tokens = scanner.scan_layers(text)
        fig = px.line(df_layers, x="Layer", y="Activation Variance", markers=True, title="Neural Activation Energy", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
