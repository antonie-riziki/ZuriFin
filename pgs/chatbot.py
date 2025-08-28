
#!/usr/bin/env python3

import africastalking
import streamlit as st 
import google.generativeai as genai
import os


sys.path.insert(1, './models')

from dotenv import load_dotenv

load_dotenv()


from lipanampesa import lipa_na_mpesa

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

sms = africastalking.SMS

def get_gemini_response(prompt):

    model = genai.GenerativeModel("gemini-2.5-flash", 

        system_instruction = '''
            You are ZuriFin, a smart, friendly, and culturally aware financial assistant available via SMS. 
            You help users with money matters like budgeting, saving, investing, debt, credit scores, and retirement planning. 

            You also support **tool calling** for actions like sending money via M-Pesa, checking balances, or retrieving transaction info. 
            If a user explicitly asks to send money or perform an action, respond by calling the right tool instead of replying with text. 
            For example:
            - "Send 500 to John" → trigger stk_push tool
            - "Check my balance" → trigger balance_check tool
            - "Show last 5 transactions" → trigger transactions tool

            Tone & Response Rules:
            - Be warm, supportive, and non-judgmental.
            - Keep replies short (under 160 chars) for SMS.
            - Use clear, simple language. Avoid jargon.
            - Encourage good money habits and long-term thinking.
            - Be conversational: greet by name if given, ask short clarifying questions.
            - Always fit the style of an SMS chat: short, friendly, and actionable.

            Example SMS Responses:
            User: I need help saving money.
            ZuriFin: Sure! How much are you aiming to save each month?

            User: I earn 10K. How should I budget it?
            ZuriFin: Try 50% needs, 30% wants, 20% savings. Want a breakdown?

            User: I'm in debt.
            ZuriFin: Don’t worry, we’ll fix this. How much do you owe, and to who?

            User: Send 200 to Mary.
            ZuriFin: (trigger stk_push tool with {amount:200, recipient:"Mary"})
            '''
                )

    # Generate AI response

    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=0.1, 
      )
    
    )
    
    return response.text


def send_response(phone_number, reply_sms):

    recipients = [f"+254{str(phone_number)}"]

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"{reply_sms}";

    # Set your shortCode or senderId
    sender = 20880
    keyword = "Test 11"

    try:
        
        response = sms.send_premium(message, recipients, sender, keyword, retry_duration_in_hours=1)

        print(response)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')



# def handle_incoming_sms(phone_number, user_message):
#     try:
#         # 1. Get AI-generated response from Gemini
#         ai_response = get_gemini_response(user_message)

#         # 2. Clean/trim AI response for SMS (just in case)
#         trimmed_response = ai_response.strip()[:20]

#         # 3. Send response via Africa's Talking SMS
#         send_response(phone_number, trimmed_response)

#     except Exception as e:
#         print(f"Error handling SMS: {e}")



# handle_incoming_sms(phone_number="743158232", user_message="How can I save money?")


# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("How may I help?"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    chat_output = get_gemini_response(prompt)
    
    # Append AI response
    with st.chat_message("assistant"):
        st.markdown(chat_output)

    st.session_state.messages.append({"role": "assistant", "content": chat_output})



