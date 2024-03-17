# In this page, users are asked what they want to review: Food & Drink, Atmosphere, and People/Staff.
# This will then lead users to AskUserQuestions.py, which asks the questions.
# TODO: Instead of manually setting options, retrieve this from a file (likely .csv)
import streamlit as st


def main():
    # Sets basic configuration of website
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

    # options is the aspects of the store that the user can decide to review. They have to select at least one aspect
    # to review, but they can choose any.
    options = ["Food & Drink", "Atmosphere", "Staff"]
    # userOptions is which aspects the user will review in the next screen.
    # A list of booleans where True = will review, False = won't review
    userOptions = []
    # TODO: Change these to buttons instead of checkboxes & line them up horizontally
    for option in options:
        userOptions.append(st.checkbox(option))
    st.text("")
    counter = 0
    # Makes sure that the user has chosen at least one option before letting them move on
    for op in userOptions:
        if op:
            counter += 1
    if counter != 0:
        st.session_state['userOptions'] = userOptions
        st.page_link("pages/AskUserQuestions.py", label="Next", icon="🌟")


main()
