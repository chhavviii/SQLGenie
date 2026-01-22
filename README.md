# SQLGenie (Gen AI Project)
A GenAI-powered web application that converts **natural language questions into SQL queries** and explains them in simple, human-readable English using Large Language Models (LLMs).

This project demonstrates **prompt engineering, LLM integration, and real-world SQL reasoning**, making it ideal for **GenAI / Data / Analytics intern roles**.

---

## 🚀 Features

- 🔤 Converts English questions into SQL queries  
- 🧩 Supports multiple SQL dialects (MySQL, PostgreSQL, SQL Server, SQLite)  
- 📘 Provides step-by-step query explanation  
- 📌 Clearly states assumptions made by the AI  
- ⚡ Simple and clean Streamlit web interface  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web UI
- **OpenAI API (LLM)**  
- **Prompt Engineering**
- **python-dotenv** – Environment variable management

---

## 📁 Project Structure
ai-sql-generator/
│
├── app.py
├── requirements.txt
├── .env
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/chhavviii/SQLGenie.git
cd SQLGenie
```
### 2️⃣ Create & Activate Virtual Environment
``` bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
``` bash
pip install -r requirements.txt
```
### 4️⃣ Add OpenAI API Key
``` bash
OPENAI_API_KEY=sk-your-api-key-here
```

### 5️⃣ Run the Application
``` bash
streamlit run app.py
```

## 🧪 Example Inputs
Find average order value per customer

Get top 5 products by revenue last month

Show total revenue per month for the last year
