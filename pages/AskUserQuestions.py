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
    #  In the future, userOptions may be longer than 3 entries & options will have to be read from a .csv .

    # Also, the "Order" aspect is linked to "Food & Drink" due to a request from GongCha -- We only ask
    # what the customer ordered when they want to comment on the food & drinks.
    # TODO: Give the user the option to specify tone for their review (e.g formal, slang, etc.)
    if userOptions[0]:  # "Food & Drink" Option
        order = showQuestions("What did you order?", "Order",
                              ["Pearl Milk Tea", "Brown Sugar Oolong Milk Tea with 2J", "Mango Smoothie",
                               "Peach Green Tea with QQ Jelly", "3J Earl Grey Milk Tea", "Oreo Coffee Milk Tea",
                               "Milk Foam Wintermelon Drink", "Wintermelon Milk Tea with Grass Jelly",
                               "Milk Foam Green Tea",
                               "Original Bubble Waffle", "Pearl Bubble Waffle"], False)
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

    # Writes the customer's order (Debugging only !!)
    # st.write(fndOptions)
    # st.write(order)
    # st.write(atmoOptions)
    # st.write(staffOptions)

    # for the aspects the user has decided to review, make sure they have feedback on that aspect.
    # Otherwise, checks that there is no feedback for that aspect.
    if ((fndOptions != "") == userOptions[0] and
            (order != "") == userOptions[0] and
            (atmoOptions != "") == userOptions[1] and
            (staffOptions != "") == userOptions[2]):
        # Only when the user has given feedback on everything they said they would do we let them proceed.
        # Saves the feedback to use for generating the reviews
        userInput = order + fndOptions + atmoOptions + staffOptions
        st.session_state['userInput'] = userInput
        st.page_link("pages/CreateAIReviews.py", label="Generate the Reviews!", icon="🌟")


# This function displays the questions for the user: Attributes (multiselect) or their custom message.
# header is the aspect of the store (e.g Food & Drink, Staff, etc.)
# question is the question the store wants to ask (e.g "What did you order?", "How was our staff?", etc.)
# options is a list of keywords that the user can select (many attributes can be selected at once,
# but at least one must be selected for feedback to be valid).
# customAllowed is whether or not the user is allowed to type their custom feedback.
# Returns the feedback of the user as a string.
# TODO: Moderate the custom user messages. They must be in English, be about the restaurant itself,
#  and if it's a negative message it needs to be turned into a positive-ish message.

# The feedback will look like this for any aspect:
#   [Aspect] Keywords: [Selected Keyword 1], [Selected Keyword 2],..., [Final Selected Keyword].
#   [Aspect] Feedback: [If custom feedback is allowed, the user feedback will be placed here].
def showQuestions(question, aspect, options, customAllowed):
    # Displays the interface for feedback.
    feedback = ""
    st.header(question)
    traits = ''
    for option in options:
        # Displays possible keywords customers can use to describe the store. Users can select multiple keywords at
        # once, and any selected keywords are added to feedback

        if st.checkbox(option, key=option + aspect):
            traits += (option + ", ")
    traits = traits[:len(traits) - 2] + "."  # Separates the Keywords by comma and adds a period to the end.
    if traits != ".":
        feedback += aspect.title() + " Keywords: " + traits

    if customAllowed:
        text = st.text_input(label="Or write your own feedback here! (optional)", placeholder="Write here!", key=aspect)
        if text != "":
            feedback += aspect.title() + " Feedback: " + text
    return feedback


main()
