import streamlit as st

st.set_page_config(
    page_title="Interactive A3 Continuous Improvement",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Interactive A3 Continuous Improvement")
st.caption(
    "A structured problem-solving application for analyzing manufacturing "
    "problems, identifying root causes, implementing countermeasures, "
    "and evaluating results."
)

st.info(
    "This application uses synthetic manufacturing scenarios for "
    "educational and portfolio purposes."
)

st.divider()

st.subheader("A3 Problem-Solving Process")

st.write(
    "Problem → Current Condition → Root Cause → Countermeasures → "
    "Implementation → Results → Standardize & Sustain"
)
