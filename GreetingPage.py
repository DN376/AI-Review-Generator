
# This is the entrypoint file and the start screen for users (Frontend)!
# This'll be fairly barebones. as It's just a screen and a button to proceed to the next pages
import streamlit as st

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
    st.session_state['userOptions'] = []
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
    st.title("Thank you for your patronage at " + STORE_NAME + "!")
    st.header("Use our guide to automatically create a review.")

    # Makes a button that, when pressed, sends the user to the next screen.
    st.page_link("pages/ChooseStoreAspects.py", label="Let's make an incredible review together!", icon="🧋")


main()
