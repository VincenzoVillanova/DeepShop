import streamlit as st
import requests
import re
import csv
import io
from uuid import uuid4

st.set_page_config(page_title="DeepShop 🛒🤖", layout="centered")

API_URL = "http://127.0.0.1:1234/v1/chat/completions"  
HEADERS = {"Content-Type": "application/json"}  

USER_ICON = "👨🏻‍💻"
BOT_ICON = "🤖"

def get_bot_response(message):
    payload = {
        "model": "deepseek-r1-distill-llama-8b",
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7
    }
    try:
        response = requests.post(API_URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        response_data = response.json()
        content = response_data.get("choices", [{}])[0].get("message", {}).get("content", "Errore nella risposta")
        content = re.sub(r"</?think>.*?</?think>|</?think>", "", content, flags=re.DOTALL).strip()
        return content
    except Exception as e:
        return f"**Errore:** {str(e)}"

def parse_questions(response_text):
    questions = []
    seen = set()
    for match in re.finditer(r'\d+\.\s*"(.*?)"', response_text):
        question = match.group(1)
        if question not in seen:
            seen.add(question)
            questions.append(question)
    return questions

def clean_response(response_text):
    return re.sub(r'\n?\d+\.\s*".*?"\s*\n?', '', response_text).strip()

def parse_markdown_table(markdown_text):
    lines = markdown_text.strip().splitlines()
    rows = []
    for line in lines:
        line = line.strip()
        if not line or re.match(r"^\|[-\s|]+$", line):
            continue
        if line.startswith("|") and line.endswith("|"):
            line = line[1:-1]
        row = [col.strip() for col in line.split("|")]
        rows.append(row)
    return (rows[0], rows[1:]) if rows else (None, None)

def convert_markdown_to_csv(markdown_text):
    output = io.StringIO()
    writer = csv.writer(output, delimiter=";")
    for line in markdown_text.strip().splitlines():
        line = line.strip()
        if not line or re.match(r"^\|[-\s|]+$", line):
            continue
        if line.startswith("|") and line.endswith("|"):
            line = line[1:-1]
        columns = [col.strip() for col in line.split("|")]
        writer.writerow(columns)
    return output.getvalue()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "suggestions" not in st.session_state:
    st.session_state.suggestions = {}
if "input_key" not in st.session_state:
    st.session_state.input_key = 0
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

st.title("DeepShop 🛒🤖")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=USER_ICON if msg["role"] == "user" else BOT_ICON):
        st.markdown(msg["content"])
        
        if msg["role"] == "assistant" and msg["id"] in st.session_state.suggestions:
            cols = st.columns(2)
            questions = st.session_state.suggestions[msg["id"]]
            for i, q in enumerate(questions):
                with cols[i % 2]:
                    st.button(
                        q,
                        key=f"sugg_{msg['id']}_{i}",
                        on_click=lambda q=q: st.session_state.update({
                            "user_input": q,
                            "input_key": st.session_state.input_key + 1
                        })
                    )   
        
        if msg["role"] == "assistant" and "|" in msg["content"]:
            csv_content = convert_markdown_to_csv(msg["content"])
            st.download_button(
                label="📥 Scarica Tabella CSV",
                data=csv_content,
                file_name="bot_response.csv",
                mime="text/csv",
                key=f"download_{msg['id']}"
            )

current_input = st.chat_input(
    "Scrivi un messaggio...",
    key=f"chat_input_{st.session_state.input_key}",
)

if st.session_state.user_input:
    current_input = st.session_state.user_input
    st.session_state.user_input = ""  

if current_input:
    user_msg = {
        "role": "user",
        "content": current_input,
        "id": str(uuid4())
    }
    st.session_state.messages.append(user_msg)
    
    with st.spinner("⏳ Sto pensando..."):
        raw_bot_response = get_bot_response(current_input)
        cleaned_bot_response = clean_response(raw_bot_response)
        questions = parse_questions(raw_bot_response)
    
    bot_msg = {
        "role": "assistant",
        "content": cleaned_bot_response,
        "id": str(uuid4())
    }
    st.session_state.messages.append(bot_msg)
    
    if questions:
        st.session_state.suggestions[bot_msg["id"]] = questions
    
    st.rerun()