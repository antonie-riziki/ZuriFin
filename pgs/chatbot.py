
#!/usr/bin/env python3

import africastalking
import streamlit as st 
import google.generativeai as genai
import os
import sys 


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

    model = genai.GenerativeModel("gemini-2.0-flash", 

        system_instruction = '''
            You are ZuriFin, a smart, friendly, and culturally aware financial assistant available via SMS. 
            You help users with money matters like budgeting, saving, investing, debt, credit scores, and retirement planning. 

            You also support **tool calling** for actions like sending money via M-Pesa, checking balances, or retrieving transaction info. 
            If a user explicitly asks to send money or perform an action, respond by calling the right tool instead of replying with text. 
            
            For example:
            - "Send 500 to John" → trigger lipa_na_mpesa tool
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
            ZuriFin: {"action":"lipa_na_mpesa", "amount":200}
            
            ''')

    # Generate AI response

    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=0.1, 
      )
    
    )

    # text = response.text.strip()

    # # Try to parse tool call
    # try:
    #     data = json.loads(text)
    #     if "action" in data and data["action"] == "lipa_na_mpesa":
    #         return lipa_na_mpesa(data["amount"], data["recipient"])
    # except Exception:
    #     # Not a tool call, just return text
    #     return text

    # return text
    
    return response.text





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



