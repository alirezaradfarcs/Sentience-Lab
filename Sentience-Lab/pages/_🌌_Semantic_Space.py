import streamlit as st
import plotly.express as px
from modules.geometry import GeometryEngine

st.set_page_config(page_title="Semantic Space", layout="wide")
st.title("🌌 Semantic Geometry")
geo_engine = GeometryEngine('gpt2')
text = st.text_area("Enter complex text:", "King - Man + Woman = Queen. The cat sat on the mat.")
if st.button("Project to 3D"):
    with st.spinner("Calculating PCA..."):
        df = geo_engine.get_3d_projection(text)
        fig = px.scatter_3d(df, x='x', y='y', z='z', text='Token', color='z', template="plotly_dark", opacity=0.8)
        st.plotly_chart(fig, use_container_width=True)
