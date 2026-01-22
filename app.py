import streamlit as st
from dotenv import load_dotenv
import os
import openai

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="AI SQL Query Generator",
    page_icon="🧠",
    layout="centered"
)

from openai import OpenAI
load_dotenv(dotenv_path=".env")
st.write("API KEY FOUND:", os.getenv("OPENAI_API_KEY") is not None)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ------------------ FUNCTIONS ------------------
def build_prompt(question, db_type):
    return f"""
You are an expert SQL developer.

Convert the following natural language question into a correct and optimized {db_type} SQL query.

Rules:
- Use standard {db_type} syntax
- Assume a typical relational database
- Do NOT invent table names unless necessary (use generic names like orders, customers, products)

Also provide:
1. SQL Query
2. Step-by-step explanation in simple English
3. Assumptions made

Question:
{question}

Output format (strict):
SQL Query:
<query>

Explanation:
<explanation>

Assumptions:
<assumptions>
"""


def generate_sql(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert SQL developer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


# ------------------ UI ------------------
st.title("🧠 AI SQL Query Generator & Explainer")

st.write("Convert **English questions → SQL queries** with clear explanations.")

question = st.text_area(
    "Enter your question in plain English:",
    placeholder="Example: Get top 5 products by revenue last month"
)

db_type = st.selectbox(
    "Select Database Type:",
    ["MySQL", "PostgreSQL", "SQL Server", "SQLite"]
)

generate_btn = st.button("🚀 Generate SQL")

# ------------------ OUTPUT ------------------
if generate_btn:
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating SQL using GenAI..."):
            prompt = build_prompt(question, db_type)
            output = generate_sql(prompt)

        st.subheader("📌 Generated Result")
        st.markdown(output)

