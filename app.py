import streamlit as st
from survey import display_survey
from analysis import analyze_data, display_results
from metrics import get_gapology_metrics

def main():
    st.title("Gapology App")
    st.sidebar.title("Navigation")
    options = ["Home", "Gapology Metrics", "Take Survey", "View Results"]
    choice = st.sidebar.radio("Go to", options)

    if choice == "Home":
        st.write("Welcome to the Gapology App!")
        st.write("Identify and close performance gaps in your organization.")
    elif choice == "Gapology Metrics":
        metrics = get_gapology_metrics()
        for metric, description in metrics.items():
            st.subheader(metric)
            st.write(description)
    elif choice == "Take Survey":
        user_data = display_survey()
        if user_data:
            st.session_state["survey_data"] = user_data
    elif choice == "View Results":
        if "survey_data" in st.session_state:
            analyze_data(st.session_state["survey_data"])
            display_results(st.session_state["survey_data"])
        else:
            st.warning("No survey data available. Please complete the survey first.")

if __name__ == "__main__":
    main()
