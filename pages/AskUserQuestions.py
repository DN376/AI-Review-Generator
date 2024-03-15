# This file asks the user to describe the different aspects of the store. They have 2 options:
# 1. They are given a list of adjectives / keywords with to select
# 2. They are given a text box where they can type their own response
# After this, the response will be sent to CreateAIReviews.py for the reviews to be generated.

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
    st.header("Answer these questions below!")
    userOptions = st.session_state['userOptions']
    order = ""
    fndOptions = ""
    atmoOptions = ""
    staffOptions = ""

    # st.write(userOptions)
    # TODO: Change UserOptions to be more than 3 options and many more adjectives
    #  (it needs to match the assumed .csv file) That's gonna be pretty hard... (<_<)

    if userOptions[0]:  # "Food & Drink" Option
        order = showQuestions("What did you order?", "Order",
                              ["Pearl Milk Tea", "Brown Sugar Oolong Milk Tea with 2J", "Mango Smoothie",
                               "Peach Green Tea with QQ Jelly", "3J Earl Grey Milk Tea", "Oreo Coffee Milk Tea",
                               "Milk Foam Wintermelon Drink", "Wintermelon Milk Tea with Grass Jelly",
                               "Milk Foam Green Tea",
                               "Original Bubble Waffle", "Pearl Bubble Waffle"],
                              False)
        fndOptions = showQuestions("How would you describe our store's food and drink?", "Food & Drink",
                                   ["Flavourful", "Refreshing", "Bold", "Yummy", "Excellent", "Delicious",
                                    "Tasty", "Sweet", "Many Options", "Balanced"], True)

    if userOptions[1]:  # Atmosphere
        atmoOptions = showQuestions("How would you describe our store's atmosphere?", "Atmosphere",
                                    ["Cozy", "Quiet", "Fun", "Great Music", "Clean", "Chic", "Casual",
                                     "Free Wifi", "Comfy", "Excellent"], True)
    if userOptions[2]:  # Staff
        staffOptions = showQuestions("How would you describe our store's staff?", "Staff",
                                     ["Polite", "Friendly", "Fast Service", "Helpful", "Excellent", "Kind",
                                      "Patient", "Offered Free Samples", "Great Manager", "Impressive"], True)
    st.write(fndOptions)
    st.write(order)
    st.write(atmoOptions)
    st.write(staffOptions)
    if ((fndOptions != "") == userOptions[0] and
            (order != "") == userOptions[0] and
            (atmoOptions != "") == userOptions[1] and
            (staffOptions != "") == userOptions[2]):
        userInput = order + fndOptions + atmoOptions + staffOptions
        st.session_state['userInput'] = userInput
        st.page_link("pages/CreateAIReviews.py", label="Next", icon="🌟")


# This function displays the questions for the user: Attributes (multiselect) or their custom message.
# Returns the feedback of the user as a string
# TODO: Moderate the custom user messages. They must be in English, be about the restaurant itself,
#  and if it's a negative message it needs to be turned into a positive-ish message.
def showQuestions(question, header, options, customAllowed):
    feedback = ""
    st.header(question)
    traits = ''
    for option in options:
        if st.checkbox(option, key=option + header):
            traits += (option + ", ")
    traits = traits[:len(traits) - 2] + "."
    if traits != ".":
        feedback += header.title() + " Keywords: " + traits

    if customAllowed:
        text = st.text_input(label="Or", placeholder="You can also write here! (optional)", key=header)
        if text != "":
            feedback += header.title() + " Feedback: " + text
    return feedback


main()
