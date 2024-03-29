import streamlit as st
# import clipboard
from streamlit_extras.switch_page_button import switch_page
from st_copy_to_clipboard import st_copy_to_clipboard
from streamlit_extras.stateful_button import button
import textwrap as tw

if 'NUM_REVIEWS' not in st.session_state:
    switch_page("GreetingPage")


def on_copy_click(text):
    st.markdown(f'<button id="copy-button" onclick="copyToClipboard(\'{text}\')">Copy Text</button>', unsafe_allow_html=True)
    st.markdown("""
        <script>
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text)
                .then(function() {
                    alert("Text copied to clipboard: " + text);
                })
                .catch(function(error) {
                    alert("Failed to copy text: " + error);
                });
        }
        </script>
    """, unsafe_allow_html=True)


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
    NUM_REVIEWS = st.session_state["NUM_REVIEWS"]
    for i in range(NUM_REVIEWS):
        st.write("Review #" + str(i + 1) + ":")
        st.write("🌟🌟🌟🌟🌟")
        review_text = st.session_state["review#" + str(i + 1)]
        # st.write(review_text)
        copyKey = str(i) + "COPY_BUTTON"
        st.code("\n".join(
            tw.wrap(
                review_text,
                width=80,
            )
        ), None)

    st.link_button("Give us a review on Google!",
                   "https://www.google.com/search?client=firefox-b-d&q=gong+cha+davisville#lrd=0x882b3320b8abb05b:0xbff654876b9a8f56,3,,,,")


main()