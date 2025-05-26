# 📊 Fitness-Tracker Dashboard

A secure, interactive Streamlit web app that allows individual users to log their personal progress (e.g., health, habits, mood, fitness) over time, store it in a PostgreSQL database, and visualize trends using custom charts and tables.

---

## 🔧 Features

- 🔐 **User Authentication** (Sign up / Log in)
- 🧠 **Password Hashing** with `bcrypt`
- 📥 **User Input Validation** (prevent bad data)
- 🗃️ **PostgreSQL Database** hosted on **Supabase**
- 📈 **Custom Charts & Tables** (user-specific)
- ☁️ **Hosted on Streamlit Cloud**
  
---

## 📦 Tech Stack

| Tool        | Purpose                     |
|-------------|-----------------------------|
| `Streamlit` | Web app framework           |
| `Supabase`  | PostgreSQL DB hosting       |
| `psycopg2`  | PostgreSQL connection       |
| `bcrypt`    | Password hashing            |
| `pandas`    | Data analysis & cleaning    |
| `plotly`    | Charting                    |

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/progress-tracker-app.git
cd progress-tracker-app
