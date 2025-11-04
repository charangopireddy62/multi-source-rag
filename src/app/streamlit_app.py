import streamlit as st
from datetime import datetime

st.title("🧠 Multi-Source RAG Project")
st.write("✅ Environment setup successful!")
st.write(f"Last checked: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.info("You’re ready for Phase 1 — Ingest and Chunk PDF data.")
