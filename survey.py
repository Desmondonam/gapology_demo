import streamlit as st

def display_survey():
    st.header("Survey Form")
    st.write("Please fill in the survey to identify performance gaps.")

    role = st.selectbox("Are you an:", ["Employee", "Team Leader"])
    knowledge_gap = st.slider("Rate your knowledge of your role (1 = Low, 5 = High)", 1, 5)
    importance_gap = st.slider("Rate your understanding of priorities (1 = Low, 5 = High)", 1, 5)
    action_gap = st.slider("Rate the effectiveness of actions taken to achieve goals (1 = Low, 5 = High)", 1, 5)
    comments = st.text_area("Additional Comments")

    if st.button("Submit"):
        return {
            "role": role,
            "knowledge_gap": knowledge_gap,
            "importance_gap": importance_gap,
            "action_gap": action_gap,
            "comments": comments
        }
    return None
