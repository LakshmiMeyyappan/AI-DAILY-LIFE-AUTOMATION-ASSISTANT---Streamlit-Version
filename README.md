AI Daily Work Assistant

This project is a simple AI-based daily work assistant built using CrewAI and Python.
It analyzes daily developer activity and generates an intelligent summary and next-day plan.

The project supports:

Local execution for real daily usage

Streamlit Cloud deployment for demo and global access

What This Project Does

The assistant:

Collects daily work activity (files, git, terminal, VS Code)

Uses multiple AI agents (CrewAI) to analyze the data

Generates a daily work report

Creates a minimal next-day plan

Can optionally generate a voice briefing

Why CrewAI Is Used

CrewAI is used to implement agent-based AI.

Each agent has a specific responsibility:

Analyze work activity

Summarize completed tasks

Plan next actions

Agents collaborate to produce a single intelligent output.

Project Structure
AI DAILY WORK ASSISTANT
│
├── app.py                  # Streamlit Cloud entry point
├── main.py                 # Local automation runner
│
├── agents.py
├── tasks.py
├── crew_runner.py
│
├── morning_runner.py
├── report_generator.py
├── voice_generator.py
│
├── file_activity_collector.py
├── git_collector.py
├── terminal_collector.py
├── vscode_collector.py
│
├── requirements.txt
├── README.md
└── .gitignore

How the Project Works

main.py
Runs the assistant locally and decides:

Morning → generate briefing

Evening → generate daily report

app.py
Used only for Streamlit Cloud to demonstrate the project.

Running Locally

Install dependencies:

pip install -r requirements.txt


Run the project:

python main.py

Running with Streamlit (Demo Mode)
streamlit run app.py


This mode is mainly used for:

Mentor review

Recruiter demo

Portfolio showcase

API Key Setup

The project uses a Groq API key.

Local:

Create a file named api_key.txt and paste your key.

Streamlit Cloud:

Add the key in App Settings → Secrets:

GROQ_API_KEY="your_api_key_here"

Files Not Included in GitHub

For security and cleanliness, these are excluded:

Virtual environment folders

API key files

Generated reports

Executable (.exe) files

Purpose of This Project

This project was built as:

A realistic AI automation project

A learning exercise for agentic AI

A career restart portfolio project

Author

Lakshmi Meyyappan
AI / ML Engineer