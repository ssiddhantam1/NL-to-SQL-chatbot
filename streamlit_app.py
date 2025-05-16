import streamlit as st
import os
import tempfile
from models.text2sql import nl_to_sql
from utils import get_db_engine, run_sql_query

st.set_page_config(page_title="NL→SQL Chatbot", page_icon="🤖")
st.title("Natural Language Database Chatbot 🤖")
st.write(
    "Upload your own SQLite database (.db) and ask questions in natural language!"
)

# File uploader for database
uploaded_db = st.file_uploader("Upload a SQLite .db file", type=["db"])

# Store uploaded DB path in session state
if uploaded_db:
    # Create a temp file to save the uploaded database
    temp_db_fd, temp_db_path = tempfile.mkstemp(suffix=".db")
    with os.fdopen(temp_db_fd, 'wb') as f:
        f.write(uploaded_db.read())
    st.session_state.db_path = temp_db_path
    st.success("Database uploaded and loaded!")

# Default to sample db if no upload
db_path = st.session_state.get('db_path', "db/sample.db")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask your question:")

if st.button("Submit") and user_input:
    # 1. NL to SQL
    sql_query = nl_to_sql(user_input)
    # 2. Run SQL
    try:
        engine = get_db_engine(f"sqlite:///{db_path}")
        result = run_sql_query(engine, sql_query)
    except Exception as e:
        result = str(e)
    # 3. Store and display
    st.session_state.history.append({
        "question": user_input,
        "sql": sql_query,
        "result": result
    })

st.markdown("---")
for chat in reversed(st.session_state.history):
    st.markdown(f"**You:** {chat['question']}")
    st.markdown(f"**SQL:** `{chat['sql']}`")
    if isinstance(chat['result'], str):
        st.error(chat['result'])
    else:
        st.dataframe(chat['result'])