# This acts as a small loading screen for generating the reviews.
# The frontend shows a small loading screen for users while handling prompt generation and AI responses.
import os
from st_copy_to_clipboard import st_copy_to_clipboard
import cohere
from dotenv import load_dotenv
import streamlit as st
import clipboard

load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
# TODO: find if ChatGPT or Cohere is better for this (the $200 credit for Cohere makes testing cheaper).
systemMsg = """You are an assistant that helps customers write reviews for the store named """ + st.session_state[
    'storeName'] + """. 
    You will be given the customers' feedback and write a review based on what they say.
    The user will give feedback using keywords for different aspects of the store and will also occasionally add their own responses.
    Only use the custom responses if they are appropriate in the context of writing a review. If the feedback is negative, try to frame it as positively as possible.
    Limit your response to 50 to 100 words. Answer in a consistent style to the previous responses."""
# TODO: Implement few-shot prompting (get an example review & feed it in)
fewShotUser = """Ordered: Mango Smoothie, Bubble Waffle.
Food & Drink Keywords: Delicious.
Atmosphere Keywords: Clean.
Staff Keywords: Friendly, Great Service.
Staff Feedback: My kids enjoyed it and they want to come back tomorrow."""
fewShotAssistant = """I went for the first time today, the service was great, the staff is friendly. 
I ordered a mango smoothie and a waffle (it was delicious). 
The restaurant was clean. My kids enjoyed the time we spent there and they want to come back tomorrow."""


def on_copy_click(text):
    st.session_state.copied.append(text)
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
    # st.write(fewShotUser)
    # st.write(st.session_state['userInput'])
    co = cohere.Client(COHERE_API_KEY)
    NUM_REVIEWS = 3
    my_bar = st.progress(0, "Generating Review #1, Please Wait!")
    for i in range(NUM_REVIEWS):
        my_bar.progress((i/NUM_REVIEWS), text="Generating Review#"+str(i+1)+", Please wait!")
        st.write("Review #"+str(i+1)+":")
        response = co.chat(
            chat_history=[
                {"role": "USER", "message": fewShotUser},
                {"role": "CHATBOT", "message": fewShotAssistant}
            ],
            message=st.session_state['userInput'],
            preamble_override=systemMsg,
            temperature=0.45
        )
        st.write("🌟🌟🌟🌟🌟")
        st.write(response.text)
        st_copy_to_clipboard(response.text, key="copy"+str(i))
    my_bar.empty()
    st.balloons()
    if st.session_state['copy0'] or st.session_state['copy1'] or st.session_state['copy2']:
        st.link_button("Give us a review on Google!", "https://www.google.com/search?client=firefox-b-d&q=gong+cha+davisville#lrd=0x882b3320b8abb05b:0xbff654876b9a8f56,3,,,,")


main()