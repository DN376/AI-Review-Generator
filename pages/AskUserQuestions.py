# This file asks the user to describe the different aspects of the store. They have 2 options:
# 1. They are given a list of adjectives / keywords with to select
# 2. They are given a text box where they can type their own response
# After this, the response will be sent to CreateAIReviews.py for the reviews to be generated.
import random
from streamlit_extras.stateful_button import button
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# if any session variables aren't loaded, send user back to the starting page
if ('userOptions' not in st.session_state or
        'userInput' not in st.session_state or
        'storeName' not in st.session_state):
    switch_page("GreetingPage")


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
    canProceed = True
    if "Food & Drink" in userOptions:  # "Food & Drink" Option
        order = displayMenu("What did you order?", "Order",
                            ["Pearl Milk Tea", "Brown Sugar Oolong Milk Tea with 2J", "Mango Smoothie",
                             "Peach Green Tea with QQ Jelly", "3J Earl Grey Milk Tea", "Oreo Coffee Milk Tea",
                             "Milk Foam Wintermelon Drink", "Wintermelon Milk Tea with Grass Jelly",
                             "Milk Foam Green Tea",
                             "Original Bubble Waffle", "Pearl Bubble Waffle"])
        fndOptions = showQuestions("How would you describe our store's food and drink?", "Food & Drink",
                                   ["Flavourful", "Refreshing", "Bold", "Yummy", "Excellent", "Delicious",
                                    "Tasty", "Sweet", "Many Options", "Balanced"])
        # st.write(order)
        # st.write(fndOptions)
        if order == "" or fndOptions == "" or fndOptions is None:
            canProceed = False

    if "Atmosphere" in userOptions:  # Atmosphere
        atmoOptions = showQuestions("How would you describe our store's atmosphere?", "Atmosphere",
                                    ["Cozy", "Quiet", "Fun", "Great Music", "Clean", "Chic", "Casual",
                                     "Free Wifi", "Comfy", "Excellent"])
        # st.write(atmoOptions)
        if atmoOptions == "" or atmoOptions is None:
            canProceed = False
    if "Staff" in userOptions:  # Staff
        staffOptions = showQuestions("How would you describe our store's staff?", "Staff",
                                     ["Polite", "Friendly", "Fast Service", "Helpful", "Excellent", "Kind",
                                      "Patient", "Offered Free Samples", "Great Manager", "Impressive"])
        # st.write("staffOptions -->" + str(staffOptions))
        if staffOptions == "" or staffOptions is None:
            canProceed = False

    # Writes the customer's order (Debugging only !!)
    # st.write(fndOptions)
    # st.write(order)
    # st.write(atmoOptions)
    # st.write(staffOptions)

    # for the aspects the user has decided to review, make sure they have feedback on that aspect.
    # Otherwise, checks that there is no feedback for that aspect.
    if canProceed:
        # Only when the user has given feedback on everything they said they would do we let them proceed.
        # Saves the feedback to use for generating the reviews
        userInput = order + fndOptions + atmoOptions + staffOptions
        st.session_state['userInput'] = userInput
        if st.button("Generate the Reviews! 🌟", type="primary"):
            switch_page("CreateAIReviews")


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
def showQuestions(question, aspect, options):
    # Displays the interface for feedback.
    feedbackTraits = ""
    traits = ''
    st.header(question)
    st.write(":red[*required]")
    selectedAttributes = st.container(border=True)
    allAttributes = st.container(border=True)
    # selectedAttributes.write("This is where the attributes the user selected go")
    # allAttributes.write("This is where all possible attributes go")

    # Display all possible attributes (options)
    gaveTraits = False
    userSelection = set()
    index = 0
    NUM_ATTRIBUTES_PER_LINE = 5
    numRows = (len(options) + NUM_ATTRIBUTES_PER_LINE - 1) // NUM_ATTRIBUTES_PER_LINE
    for i in range(numRows):
        cols = allAttributes.columns(NUM_ATTRIBUTES_PER_LINE)
        for j in range(min(NUM_ATTRIBUTES_PER_LINE, len(options) - index)):
            with cols[j]:
                option = options[index]
                key = aspect + option
                # st.write(key)
                if button(option, key, key=key + "."):
                    # if cols[j].button(option, key):
                    gaveTraits = True
                    userSelection.add(option)
                else:
                    userSelection.discard(option)
                index += 1
    # selectedAttributes.write(st.session_state)
    for option in userSelection:
        traits += (option + ", ")
    traits = traits[:len(traits) - 2] + "."  # Separates the Keywords by comma and adds a period to the end.
    if traits != ".":
        feedbackTraits += aspect.title() + " Keywords: " + traits
        # selectedAttributes.write("You've Selected: " + traits)

    gaveFeedback = False
    feedbackWritten = ""
    feedbackTitle = aspect.title() + " Feedback: "
    if feedbackTitle not in st.session_state:
        st.session_state[feedbackTitle] = ""
    text = st.text_input(label="Or write your own feedback here!", placeholder="Write here!", key=aspect)
    # For some reason, when the user hasn't input anything into the text box, text is set as True.
    # This contradicts Streamlit documentation AND the previous code (it should be None).
    # I don't know why this happens, but it's a simple fix, so: ???
    if text != "" and text is not True:
        feedbackWritten += feedbackTitle + text
        st.session_state[feedbackTitle] = feedbackWritten
    if text == "":
        st.session_state[feedbackTitle] = ""
    if st.session_state[feedbackTitle] != "":
        gaveFeedback = True
    feedbackWritten = st.session_state[feedbackTitle]
    if gaveTraits or gaveFeedback:
        if gaveTraits != gaveFeedback:
            return feedbackTraits + feedbackWritten
        else:
            st.write(":red[Cannot select keywords AND write a custom response!]")


def displayMenu(question, aspect, options):
    order = ""
    traits = ''
    st.header(question)
    optionsSelected = st.multiselect(label=":red[*required]", options=options)
    for option in optionsSelected:
        traits += (option + ", ")
    traits = traits[:len(traits) - 2] + "."  # Separates the Keywords by comma and adds a period to the end.
    if traits != ".":
        order += aspect.title() + " Keywords: " + traits
    return order


def dropdown(question):
    st.expander()


def textForDropdown():
    return ""


main()
