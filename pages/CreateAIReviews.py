# This acts as a small loading screen for generating the reviews.
# TODO: Ask Anh Nhan abt loading screen: loading & generating text, OR loading and then making text
# The frontend shows a small loading screen for users while handling prompt generation and AI responses.
import os
from st_copy_to_clipboard import st_copy_to_clipboard
import cohere
from dotenv import load_dotenv
import streamlit as st
import clipboard
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stateful_button import button

# if any session variables aren't loaded, send user back to the starting page
if ('userOptions' not in st.session_state or
        'userInput' not in st.session_state or
        'storeName' not in st.session_state):
    switch_page("GreetingPage")

load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
# TODO: find if ChatGPT or Cohere is better for this application. Currently, we're using Cohere because it's cheaper for
#  testing purposes, but if ChatGPT's model is better than we should switch
systemMsg = """You are an assistant that helps customers write reviews for the store named """ + st.session_state[
    'storeName'] + """. 
    You will be given the customers' feedback and write a review based on what they say.
    The user will give feedback using keywords for different aspects of the store and will also occasionally add their own responses.
    Only use the custom responses if they are appropriate in the context of writing a review. If the feedback is negative, try to frame it as positively as possible.
    Limit your response to 50 to 100 words. Answer in a consistent style to the previous responses."""
# TODO: Implement techniques to imrpove the model.
#  Currently, we use few shot prompting (having an example), we have a clear prompt, & ask the model to adapt a persona.
#  Things we should implement: (List, try to expand)
#       - Clear delimiters for customer input (i.e """[input]""")
#       - Use a fine-tuning approach instead of few-shot prompting
#  (See https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results)

# fewShotUser & fewShotAssistant are an example of the target input & output for the model. This (few-shot prompting)
# improves the model's answers. Using multiple answers should further improve results.
fewShotUser = """Ordered: Mango Smoothie, Bubble Waffle.
Food & Drink Keywords: Delicious.
Atmosphere Keywords: Clean.
Staff Keywords: Friendly, Great Service.
Staff Feedback: My kids enjoyed it and they want to come back tomorrow.
Tone: Casual."""
fewShotAssistant = """I went for the first time today, the service was great, the staff is friendly. 
I ordered a mango smoothie and a waffle (it was delicious). 
The restaurant was clean. My kids enjoyed the time we spent there and they want to come back tomorrow."""


# TODO: actually finish changing the copy/past function (clipboard/pyperclip instead of st_copy_to_clipboard)
def on_copy_click(text):
    # st.session_state.copied.append(text)
    clipboard.copy(text)


def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)


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
    # Initializes the model (the API key is contained in a .env file so that it remains secret)
    co = cohere.Client("WYbq1RzI3MniGl2xfq6iG0vKC6JeIPUptalaJwcZ")
    NUM_REVIEWS = 3  # The number of reviews that will be generated
    st.session_state["NUM_REVIEWS"] = NUM_REVIEWS
    # Displays a "Loading" bar & shows it to the user. Review number changes as reviews are created.
    my_bar = st.progress(0, "Generating Review #1, Please Wait!")
    toneIndicators = ["Casual", "Formal", "Use lots of emojis"]
    for i in range(NUM_REVIEWS):
        my_bar.progress((i / NUM_REVIEWS), text="Generating Review#" + str(i + 1) + ", Please wait!")
        # st.write("Review #" + str(i + 1) + ":")
        # TODO: tweak some of the AI features (e.g temperature, max_tokens, etc.)
        response = co.chat(
            chat_history=[
                {"role": "USER", "message": fewShotUser},
                {"role": "CHATBOT", "message": fewShotAssistant}
            ],
            message=st.session_state['userInput']+"\nTone: "+toneIndicators[i],
            preamble=systemMsg,
            temperature=0.5
        )
        st.session_state["review#"+str(i+1)] = response.text
        # st.write("🌟🌟🌟🌟🌟")
        # Displays the review for the customer to choose. By pressing the clipboard button for anny of these reviews,
        # they will copy it and a button will appear leading to a Google Review page.
        # TODO: Potentially link to Yelp or other review sites?
        # st.write(response.text)
        # copyKey=str(i)+"COPY_BUTTON"
        # button("Copy this review!", copyKey+".", on_click=on_copy_click(response.text), key=copyKey)
    my_bar.empty()
    st.balloons()
    # st.write(st.session_state["review#1"])
    # st.write()
    # st.write(st.session_state["review#2"])
    # st.write()
    # st.write(st.session_state["review#3"])
    # nav_to("http://localhost:8502/DisplayEndReviews")
    switch_page("DisplayEndReviews")
    # if st.session_state['copy0'] or st.session_state['copy1'] or st.session_state['copy2']:


main()
