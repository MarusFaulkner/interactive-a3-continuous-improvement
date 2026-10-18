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

st.divider()

st.header("2. Current Condition")

st.write(
    "Document what is currently happening in the process before "
    "attempting to identify the root cause."
)



col1, col2 = st.columns(2)

with col1:
    units_inspected = st.number_input(
        "Units Inspected",
        min_value=1,
        value=200,
        step=1
    )

with col2:
    units_failed = st.number_input(
        "Units Failed",
        min_value=0,
        value=18,
        step=1
    )

st.subheader("Failure Data")

col1, col2, col3 = st.columns(3)

with col1:
    functional_failures = st.number_input(
        "Functional Test Failures",
        min_value=0,
        value=8,
        step=1
    )

    connector_failures = st.number_input(
        "Connector Alignment Issues",
        min_value=0,
        value=4,
        step=1
    )

with col2:
    torque_failures = st.number_input(
        "Fastener Torque Failures",
        min_value=0,
        value=3,
        step=1
    )

    cosmetic_failures = st.number_input(
        "Cosmetic Defects",
        min_value=0,
        value=2,
        step=1
    )

with col3:
    documentation_failures = st.number_input(
        "Labeling / Documentation Errors",
        min_value=0,
        value=1,
        step=1
    )

failure_data = {
    "Functional Test Failure": functional_failures,
    "Connector Alignment Issue": connector_failures,
    "Fastener Torque Failure": torque_failures,
    "Cosmetic Defect": cosmetic_failures,
    "Labeling / Documentation Error": documentation_failures
}
leading_failure = max(failure_data, key=failure_data.get)

failure_rate = (units_failed / units_inspected) * 100

st.subheader("Observed Performance")

st.metric(
    "Observed Failure Rate",
    f"{failure_rate:.1f}%"
)

leading_failure_count = failure_data[leading_failure]

st.write(
    f"Leading observed failure: **{leading_failure} "
    f"({leading_failure_count} failures)**"
)
