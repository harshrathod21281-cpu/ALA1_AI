"""
QueryBee - Streamlit web interface for the GMIU College Help Chatbot.
Run locally :  streamlit run app.py
"""

import streamlit as st
from chatbot import get_response, WELCOME, BOT_NAME

st.set_page_config(page_title="QueryBee - GMIU Help Chatbot", page_icon="🐝")

QUICK_QUESTIONS = [
    "About GMIU",
    "Courses offered",
    "How to apply?",
    "Documents required",
    "Scholarships",
    "Hostel facility",
    "Bus facility",
    "Placement statistics",
    "Contact details",
]


def fmt(text):
    """Keep line breaks when showing text in Streamlit markdown."""
    return text.replace("\n", "  \n")


# ---------- Session state (stores the chat history) ----------
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": WELCOME}]
if "pending" not in st.session_state:
    st.session_state.pending = None

# ---------- Sidebar ----------
with st.sidebar:
    st.title("🐝 QueryBee")
    st.caption("GMIU College Help Chatbot")
    st.markdown("**Quick questions**")
    for q in QUICK_QUESTIONS:
        if st.button(q, use_container_width=True):
            st.session_state.pending = q
    st.divider()
    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = [{"role": "assistant", "content": WELCOME}]
        st.session_state.pending = None
        st.rerun()
    st.caption("Rule-based chatbot built with Python if-else rules.")
    st.caption("Made by Rathod Harsh P. (Diploma IT)")

# ---------- Main page ----------
st.title("🐝 QueryBee")
st.caption("Ask me anything about Gyanmanjari Innovative University (GMIU), Bhavnagar")

typed = st.chat_input("Type your question here...")
prompt = typed or st.session_state.pending
st.session_state.pending = None

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append(
        {"role": "assistant", "content": get_response(prompt)}
    )

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🐝" if msg["role"] == "assistant" else None):
        st.markdown(fmt(msg["content"]))