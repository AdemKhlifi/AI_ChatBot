import streamlit as st 
import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)

#-------------PAGE CONFIG----------------#
st.set_page_config(
    page_title="AI ChatBot",
    page_icon="logo.png",
    layout="wide"
)

#-------------SIDEBAR----------------#
with st.sidebar : 
    st.title("⚙️ Settings")
    btnClear=st.button("🗑️ Clear Chat")
    if btnClear :
        st.success("Chat cleared ✅") 
        st.session_state.messages=[]
        st.rerun()
    btnAbout=st.button("ℹ️ About")
    if "show_about" not in st.session_state : 
        st.session_state.show_about=False
    if btnAbout : 
        st.session_state.show_about= not st.session_state.show_about
    if st.session_state.show_about :
        st.info("AI Student Assistant is an AI-powered chatbot built with Python, Streamlit, and Google Gemini. It is designed to help students learn programming, understand computer science concepts, solve coding problems, and improve their problem-solving skills through interactive conversations. " \
        "This project was developed as a learning experience to explore modern AI technologies and build practical software engineering skills.")
    btnMe=st.button("👨‍💻 About Me")
    if "DevAbt" not in st.session_state : 
        st.session_state.DevAbt=False
    if btnMe : 
        st.session_state.DevAbt = not st.session_state.DevAbt
    if st.session_state.DevAbt : 
        st.info("Hello! I'm Adem Khlifi, 20 Years Old, a Computer Science student passionate about Artificial Intelligence, software development, and emerging technologies.I created this AI Student Assistant as a personal project to explore Generative AI, Large Language Models, and how AI can be integrated into real-world applications.Through this project, I aim to improve my programming skills, learn more about AI engineering, and build useful tools that help students learn and solve problems more efficiently.")
    Menu_Choices=st.selectbox("✨ Menu", options=["✨Gemini 3.5 Flash","✨Gemini 3.1 Flash-Lite"])
    if Menu_Choices=="✨Gemini 3.5 Flash" :
        st.success("You have selected Gemini 3.5 Flash model ✅")
        model="gemini-3.5-flash"
    elif Menu_Choices=="✨Gemini 3.1 Flash-Lite" :
        st.success("You have selected Gemini 3.1 Flash-Lite model ✅")
        model="gemini-3.1-flash-lite"


#-------------MAIN PAGE----------------#
st.title("🧠 AI ChatBot")
st.write("Welcome ! Im Here To Answer Your Questions.")
st.logo("logo.png")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages :
    st.chat_message(message["role"]).write(message["content"])

question=st.text_input("What is your question ?")
botton=st.button("SEND")
if botton and question: 
    st.session_state.messages.append({"role":"user", "content":question})
    with st.spinner("💭 Thinking... ") :
        response=client.models.generate_content(
            model=model,
            contents=question
        )
    answer=response.text

    st.session_state.messages.append({"role":"assistant", "content":answer})
    st.rerun()

    

    
