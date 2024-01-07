import streamlit as st
import cohere
from dotenv import load_dotenv
import os

STORE_NAME = "Gong Cha Davisville"
COHERE_API_KEY = os.getenv('COHERE_API_KEY')

def main():
    st.set_page_config(page_title="Leave a review!", page_icon=":sparkles:")
    st.title("Thank you for your patronage at " + STORE_NAME + "!")
    st.header("Use our guide to automatically create a review.")
    order = st.multiselect(
    'What did you order today? :red[*required]',
    ['Pearl Milk Tea', 'Bubble Waffle', 'Milk Tea'])
    opinion = st.multiselect(
        'How was the experience? Choose 1 or 2 words from this list :red[*required]',
        ['Cozy Atmosphere', 'Friendly Staff', 'Clean Store', 'Yummy Food', 'Quick Service']
    )
    # other = st.text_input('Anything else? (optional)', placeholder="Type here!")
    # st.write(str(order))
    if len(order) != 0 and len(opinion) != 0 and st.button("Generate Review!", type="primary"):
        st.spinner("Generating Review...")
        co = cohere.Client(COHERE_API_KEY)
        reviews = co.generate(
            prompt= """Generate a review for """ + STORE_NAME + """ (limited to 50 words or less) as if you are a customer. 
            Do not include any phrases that rate the experience numerically such as 'would give it X/5 stars'. 
            Do not imply any specific information about the customer in the review, as you have no information about them. 
            Do not imply that you are creating these reviews.
            The customer ordered these items: """ + str(order) + """ \n The customer described their experience as: """ + str(opinion),
            num_generations = 3,
            temperature=1.0
        )
        st.write("Review #1: ")
        st.write(reviews.generations[0].text)
        st.write("Review #2: ")
        st.write(reviews.generations[1].text)
        st.write("Review #3: ")
        st.write(reviews.generations[2].text)




    
main()