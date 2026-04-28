import streamlit as st
import os

def render_chart(chart_path):
    if chart_path and os.path.exists(chart_path):
        st.image(chart_path, caption="Generated Chart", use_container_width=True)