
import africastalking
import streamlit as st 
import google.generativeai as genai


from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

sms = africastalking.SMS
airtime = africastalking.Airtime
voice = africastalking.Voice

def send_response(phone_number, reply_sms):

    recipients = [f"+254{str(phone_number)}"]

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"{reply_sms}";

    # Set your shortCode or senderId
    sender = 20880
    # keyword = "Test11"

    try:
        
        response = sms.send_premium(message, recipients, sender)

        print(response)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    # st.toast(f"OTP Sent Successfully")


# def welcome_message(first_name, phone_number, site_id):

#     recipients = [f"+254{str(phone_number)}"]

#     print(recipients)
#     print(phone_number)

#     # Set your message
#     message = f"Greetings {first_name}, welcome to our site. Lets build together. Remember to stay safe. Incase of emergency call 07xxxxxxx \nSite ID: {site_id}";

#     # Set your shortCode or senderId
#     sender = 20880

#     try:
#         response = sms.send(message, recipients, sender)

#         print(response)

#     except Exception as e:
#         print(f'Houston, we have a problem: {e}')

#     st.toast(f"Account Created Successfully")


