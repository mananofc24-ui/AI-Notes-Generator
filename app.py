import streamlit as st
import mysql.connector
import os
from PyPDF2 import PdfReader
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN") 

client = InferenceClient(token=HF_TOKEN)

def db_connect():
    return mysql.connector.connect(
        host='mysql',
        user='root',
        password='root',
        database='ai_notes',
        port=3306
    )

# Persistent storage for notes
if 'notes' not in st.session_state:
    st.session_state['notes'] = ""

st.title('AI Notes Generator')
menu = st.sidebar.selectbox('Menu', ["Register", "Login"])

# --- DB LOGIC ---
if menu == "Register":
    u = st.text_input("Username")
    p = st.text_input("Password", type='password')
    if st.button('Register'):
        try:
            d = db_connect(); c = d.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS users(username VARCHAR(50), password VARCHAR(50))")
            c.execute("INSERT INTO users VALUES(%s, %s)", (u, p))
            d.commit(); st.success("Registered!")
        except Exception as e: st.error(f"Error: {e}")

if menu == "Login":
    u = st.text_input("Username")
    p = st.text_input("Password", type='password')
    if st.button("Login"):
        d = db_connect(); c = d.cursor()
        c.execute("SELECT * FROM users WHERE username=%s AND password=%s", (u, p))
        if c.fetchone():
            st.session_state['u'] = u
            st.success("Logged in!")
        else: st.error("Invalid")

# --- CORE APP ---
if "u" in st.session_state:
    f = st.file_uploader("Upload PDF", type=['pdf'])
    if f:
        reader = PdfReader(f)
        text = "".join([page.extract_text() for page in reader.pages])
        
        if st.button("Generate AI Notes"):
            with st.spinner("AI is working..."):
                try:
                    # Using the most stable direct API call possible
                    response = client.text_generation(
                        model="mistralai/Mistral-7B-Instruct-v0.3",
                        prompt = f"Make concise notes from the following notes:\n{text[:3000]}",
                        max_new_tokens=500
                    )
                    st.session_state['notes'] = response
                except Exception as e:
                    st.error(f"AI Error: {e}")

    if st.session_state['notes']:
        st.subheader("Result:")
        st.write(st.session_state['notes'])
        st.download_button("Download Notes", st.session_state['notes'], "notes.txt")
