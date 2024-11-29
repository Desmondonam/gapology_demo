import streamlit as st
import pandas as pd

def analyze_data(data):
    st.header("Analyzing Gaps")
    avg_score = sum([data["knowledge_gap"], data["importance_gap"], data["action_gap"]]) / 3
    if avg_score < 3:
        st.error("Significant gaps identified! Immediate action required.")
    elif avg_score < 4:
        st.warning("Moderate gaps detected. Consider improvements.")
    else:
        st.success("No significant gaps detected.")

def display_results(data):
    st.header("Survey Results")
    results_df = pd.DataFrame([data])
    st.dataframe(results_df)
