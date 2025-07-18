import streamlit as st
import pandas as pd
import africastalking
import os
import requests
import google.generativeai as genai

from streamlit_lottie import st_lottie


from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

sms = africastalking.SMS
airtime = africastalking.Airtime



# import streamlit as st
# if st.button("Log in"):
#     st.login("auth0")
# if st.experimental_user.is_logged_in:
#     if st.button("Log out"):
#         st.logout()
#     st.write(f"Hello, {st.experimental_user.name}!")



from streamlit_carousel import carousel

@st.dialog("Login")
def sign_in_form():
    with st.form(key="user_login"):
        username = st.text_input('Username:')
        password = st.text_input("Password: ", type="password")

        submit_personal_details = st.form_submit_button("Submit", use_container_width=True)


sign_in_form()









# test_items = [
#     dict(
#         title="Slide 1",
#         text="A tree in the savannah",
#         img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
#         link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819",
#     ),
#     dict(
#         title="Slide 2",
#         text="A wooden bridge in a forest in Autumn",
#         img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
#         link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel",
#     ),
#     dict(
#         title="Slide 3",
#         text="A distant mountain chain preceded by a sea",
#         img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
#         link="https://github.com/thomasbs17/streamlit-contributions/tree/master",
#     ),
#     dict(
#         title="Slide 4",
#         text="PANDAS",
#         img="pandas.webp",
#     ),
#     dict(
#         title="Slide 4",
#         text="CAT",
#         img="cat.jpg",
#     ),
# ]

# carousel(items=test_items)

