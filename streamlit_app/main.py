import streamlit as st
from utils.api_client import analyze_query
from components.chat import render_chat
from components.chart import render_chart

# 🔥 Page Config
st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide"
)

# 🔥 Custom Styling (Premium Look)
st.markdown("""
<style>
.big-title {
    font-size: 32px;
    font-weight: bold;
    color: #4CAF50;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">📊 AI Multi-Agent Data Analyst</p>', unsafe_allow_html=True)

st.caption("Ask questions about your data and get instant insights + charts")

# Render chat history
render_chat()

# Input box
query = st.chat_input("Ask your question...")

if query:
    # User message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    # Call API
    response = analyze_query(query)

    insight = response.get("insight", "")
    chart_path = response.get("chart_path", "")

    # Assistant message
    with st.chat_message("assistant"):
        st.markdown(insight)

        # Show chart
        render_chart(chart_path)

    # Save response
    st.session_state.messages.append({
        "role": "assistant",
        "content": insight
    })