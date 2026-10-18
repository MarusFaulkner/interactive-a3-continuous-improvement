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

device_under_test = st.selectbox(
    "Device Under Test",
    [
        "Electrosurgical Generator",
        "Patient Monitoring Device",
        "Medical Imaging Controller",
        "Surgical Energy Controller"
    ]
)

specific_failure = st.selectbox(
    "Specific Functional Failure",
    [
        "Monopolar Output Failure",
        "Bipolar Output Failure",
        "Neutral Electrode Interface Failure",
        "Cable / Connection Failure",
        "Output Power Below Specification",
        "Output Power Above Specification",
        "Spark Test Failure"
    ]
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

categorized_failures = sum(failure_data.values())

if categorized_failures != units_failed:
    st.warning(
        f"Failure count mismatch: {categorized_failures} categorized failures "
        f"do not match {units_failed} total units failed."
    )
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

st.divider()

st.header("3. Root Cause Analysis — 5 Whys")

st.write(
    f"Investigate why **{specific_failure}** is occurring. "
    "Each answer should be supported by process evidence before it is "
    "treated as a confirmed cause."
)

# Track previous 5 Whys answers for flow validation
if "previous_whys" not in st.session_state:
    st.session_state.previous_whys = {
        "why_1": "",
        "why_2": "",
        "why_3": "",
        "why_4": "",
        "why_5": ""
    }
why_1 = st.text_area(
    f"Why 1 — Why is {specific_failure} occurring?",
    placeholder="Enter the first potential cause...",
    key="why_1"
)

why_2 = st.text_area(
    f'Why 2 — Why did "{why_1.strip()}" occur?',
    placeholder="Investigate the cause behind Why 1...",
    key="why_2"
)

why_3 = st.text_area(
    f'Why 3 — Why did "{why_2.strip()}" occur?',
    placeholder="Investigate the cause behind Why 2...",
    key="why_3"
)

why_4 = st.text_area(
    f'Why 4 — Why did "{why_3.strip()}" occur?',
    placeholder="Investigate the cause behind Why 3...",
key="why_4"
)

why_5 = st.text_area(
    f'Why 5 — Why did "{why_4.strip()}" occur?',
    placeholder="Investigate the cause behind Why 4...",
    key="why_5"
)

current_whys = {
    "why_1": why_1,
    "why_2": why_2,
    "why_3": why_3,
    "why_4": why_4,
    "why_5": why_5
}
st.divider()

st.subheader("5 Whys Flow Validation")

if all([
    why_1.strip(),
    why_2.strip(),
    why_3.strip(),
    why_4.strip(),
    why_5.strip()
]):
    st.success("All five Why levels are complete. Review the cause-and-effect chain before confirming the potential root cause.")
else:
    st.warning(
        "5 Whys analysis incomplete. Complete all five levels before identifying a potential root cause."
    )
