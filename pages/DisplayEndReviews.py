import streamlit as st
import clipboard
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stateful_button import button

if 'NUM_REVIEWS' not in st.session_state:
    switch_page("GreetingPage")


def on_copy_click(text):
    # st.session_state.copied.append(text)
    clipboard.copy(text)


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
    copied = False
    NUM_REVIEWS = st.session_state["NUM_REVIEWS"]
    for i in range(NUM_REVIEWS):
        st.write("Review #" + str(i + 1) + ":")
        st.write("🌟🌟🌟🌟🌟")
        review = st.session_state["review#" + str(i + 1)]
        st.write(review)
        copyKey = str(i) + "COPY_BUTTON"
        copied = button("Copy this review!", copyKey + ".", on_click=on_copy_click(review), key=copyKey)

    if copied:
        st.link_button("Give us a review on Google!",
                       "https://www.google.com/search?client=firefox-b-d&q=gong+cha+davisville#lrd=0x882b3320b8abb05b:0xbff654876b9a8f56,3,,,,")


main()