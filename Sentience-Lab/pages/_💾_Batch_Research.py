import streamlit as st
import pandas as pd
from modules.brain_scanner import BrainScanner

st.set_page_config(page_title="Batch Research", layout="wide")
st.title("💾 Batch Research Protocol")
uploaded_file = st.file_uploader("Upload CSV (Column name must be 'prompt')", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if 'prompt' in df.columns and st.button("Run Analysis"):
        scanner = BrainScanner('distilgpt2')
        results = []
        progress = st.progress(0)
        for i, text in enumerate(df['prompt']):
            ent = scanner.get_token_entropy(str(text))['Entropy'].mean()
            results.append({"Prompt": text, "Avg_Entropy": ent})
            progress.progress((i + 1) / len(df))
        st.dataframe(pd.DataFrame(results))
