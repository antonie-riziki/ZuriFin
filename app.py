import streamlit as st

reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/thumb_up:")
signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/thumb_down:")
home_page = st.Page("./pgs/main.py", title="home page", icon=":material/house:")
chatbot_page = st.Page("./pgs/chatbot.py", title="chatbot", icon=":material/chat:")


pg = st.navigation([reg_page, signin_page, home_page, chatbot_page])



st.set_page_config(
    page_title="ZuriFin",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': "a Financial Advisor Bot over SMS is perfect for 2G users in Africa and ties beautifully with financial literacy, inclusion, and low-tech accessibility"
    }
)


pg.run()



