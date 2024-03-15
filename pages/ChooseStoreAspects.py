# In this page, users are asked what they want to review: Food & Drink, Atmosphere, and People/Staff.
# This will then lead users to AskUserQuestions.py, which asks the questions.
# TODO: Instead of manually setting options, retrieve this from a file (likely .csv)
import streamlit as st


def main():
    st.set_page_config(page_title="Leave a review!", page_icon=":sparkles:", initial_sidebar_state="collapsed")
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
    st.header("Choose What to Review:")
    st.text("")
    st.text("")

    options = ["Food & Drink", "Atmosphere", "Staff"]
    userOptions = []
    #TODO: Change these to buttons instead of checkboxes
    for option in options:
        userOptions.append(st.checkbox(option))
    st.text("")
    st.session_state['userOptions'] = userOptions
    counter = 0
    # Makes sure that the user has chosen at least one option before letting them move on
    for op in userOptions:
        if op:
            counter += 1
    if counter != 0:
        st.page_link("pages/AskUserQuestions.py", label="Next", icon="🌟")


main()
