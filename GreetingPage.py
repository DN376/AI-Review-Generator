# Haii!! :3
# This is the entrypoint file and the start screen for users (Frontend)! This'll be fairly barebones.
import streamlit as st

# This sets the name of the store (Can be changed for different customers)
# TODO: Instead of manually setting STORE_NAME, retrieve this from a file (likely .csv but it'll have formatting)
STORE_NAME = "Gong Cha Davisville"

# Sets a few variables that will carry across different pages.
# userOptions is the aspects of the store the user decides to review (e.g food, staff, etc.)
# userInput is the feedback that the user gives (might not be used? We'll see...)
# TODO: make sure that holding the variables like this doesn't introduce some security vulnerabilities
if 'userOptions' not in st.session_state:
    st.session_state['userOptions'] = []
if 'userInput' not in st.session_state:
    st.session_state['userInput'] = """"""
if 'storeName' not in st.session_state:
    st.session_state['storeName'] = STORE_NAME

# Sets the greetings page for when the user joins the site (scanning the QR Code).
# This should only contain a button to reach the next page, the header, and some background decor
def main():
    st.session_state['storeName'] = STORE_NAME
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
    st.title("Thank you for your patronage at " + STORE_NAME + "!")
    st.header("Use our guide to automatically create a review.")
    st.page_link("pages/ChooseStoreAspects.py", label="Let's make an incredible review together!", icon="🧋")


main()
