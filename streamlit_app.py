import streamlit as st
import os
from datetime import datetime
from crew_runner import run_nightly_process
from morning_runner import run_morning

st.set_page_config(page_title="AI Daily Work Assistant", layout="centered")

st.title("🌅 AI Daily Work Assistant")

# Load secret key from Streamlit Cloud
if "GROQ_API_KEY" not in os.environ:
    st.error("GROQ API Key not found. Please add it in Streamlit Secrets.")
    st.stop()

current_hour = datetime.now().hour
st.caption(f"Current Time: {datetime.now().strftime('%H:%M')}")

if current_hour >= 16:
    st.subheader("📊 End of Day Analysis")
    with st.spinner("Analyzing today's work..."):
        run_nightly_process()
    st.success("Daily report generated successfully.")
else:
    st.subheader("🎧 Morning Briefing")
    with st.spinner("Preparing your intelligent plan for today..."):
        run_morning()
    st.success("Morning briefing ready.")

st.info("This assistant runs automatically based on time.")
