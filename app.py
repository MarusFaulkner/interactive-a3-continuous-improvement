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

st.divider()

st.header("1. Define the Problem")

st.write(
    "A synthetic medical-device final assembly process is experiencing "
    "an increase in units failing final functional inspection."
)

col1, col2 = st.columns(2)

with col1:
    target_fpy = st.number_input(
        "Target First-Pass Yield (%)",
        min_value=0.0,
        max_value=100.0,
        value=98.0,
        step=0.1
    )

with col2:
    current_fpy = st.number_input(
        "Current First-Pass Yield (%)",
        min_value=0.0,
        max_value=100.0,
        value=91.0,
        step=0.1
    )

gap = target_fpy - current_fpy

st.subheader("Performance Gap")

st.metric(
    "FPY Gap",
    f"{gap:.1f} percentage points"
)
