# TODO: Merge w/ ChooseStoreAspects.py
# TODO: Generate the QR Code
# TODO: move this to mobile
# This is the entrypoint file and the start screen for users (Frontend)!
# This'll be fairly barebones. as It's just a screen and a button to proceed to the next pages
import streamlit as st
from streamlit_extras.stateful_button import button

# This sets the name of the store (Can be changed for different customers)
# TODO: Instead of manually setting STORE_NAME, retrieve this from a file (likely .csv but it'll have formatting)
# TODO: Create a README file and flesh out the github repo a bit more.
# TODO: Turn this file into an app using Docker (Using the Streamlit Cloud doesn't work here (T_T) )
STORE_NAME = "Gong Cha Davisville"

# Sets a few variables that will carry across different pages.
# userOptions is the aspects of the store the user decides to review (e.g food, staff, etc.)
# userInput is the feedback that the user gives
# storeName is the name of the business/store. This helps personalize the review & website
# TODO: make sure that holding the variables like this doesn't introduce some security vulnerabilities
if 'userOptions' not in st.session_state:
    st.session_state['userOptions'] = set()
if 'userInput' not in st.session_state:
    st.session_state['userInput'] = """"""
if 'storeName' not in st.session_state:
    st.session_state['storeName'] = STORE_NAME

# Sets the greetings page for when the user joins the site (scanning the QR Code).
# This should only contain a button to reach the next page, the header, and some background decor.
# TODO: Add the option to have a background photo, css theming, etc. This will likely be dependent
#  on customer
def main():
    st.session_state['storeName'] = STORE_NAME
    # Sets the basic appearance of the website: icon, title, etc.
    # TODO: Try to find a better way of hiding the sidebar. I'm unsure if lines 33-35 are the best way to do this.
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
    st.title("Thank you for your time at " + st.session_state['storeName'] + "!")
    st.header("Use our guide to automatically create a review.")
    st.header("First, choose what to review:")
    st.text("")

    # options is the aspects of the store that the user can decide to review. They have to select at least one aspect
    # to review, but they can choose any.
    options = ["Food & Drink", "Atmosphere", "Staff"]
    # userOptions is which aspects the user will review in the next screen.
    # A list of booleans where True = will review, False = won't review
    userOptions = set()
    # TODO: Change these to buttons instead of checkboxes & line them up horizontally
    for option in options:
        if button(option, key=option):
            userOptions.add(option)
        else:
            userOptions.discard(option)

    st.text("")
    counter = 0
    # Makes sure that the user has chosen at least one option before letting them move on
    userOptions
    # userOptions = list(st.session_state['userOptions'])
    for op in userOptions:
        if op:
            counter += 1
    if counter != 0:
        st.session_state['userOptions'] = list(userOptions)
        st.write("")
        st.page_link("pages/AskUserQuestions.py", label="Let's make an incredible review together!", icon="🧋")



main()
