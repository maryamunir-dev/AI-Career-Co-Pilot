# 🤖 AI Career Co-Pilot

### Your Personal AI-Powered Career Assistant 🚀

AI Career Co-Pilot is an intelligent career assistance platform designed to bridge the gap between your current skills and your dream job.

By analyzing resumes and understanding target job roles, it helps users identify skill gaps, discover what they need to learn, build personalized learning roadmaps, and prepare for technical interviews.

**The goal is simple:** turn your career goals into a clear, actionable learning path with the power of AI.



## ✨ Features

- **User Authentication:** Sign-up and login pages for users.
- **Dashboard:** A dedicated dashboard interface.
- **AI Integration:** Google Gemini integration for AI-powered functionality.
- **Resume Processing:** Support for extracting text from PDF and DOCX documents.
- **Database Integration:** Database models and connectivity using SQLAlchemy and MySQL-compatible database services.
- **History Page:** A dedicated interface for viewing history.
- **Custom UI:** Styled with CSS for a clean web interface.

## 🛠️ Tech Stack

- **Language:** Python
- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Database:** TiDB / MySQL-compatible database
- **ORM:** SQLAlchemy
- **AI:** Google Gemini
- **PDF Processing:** PyPDF2
- **DOCX Processing:** python-docx

## 📁 Project Structure

```text
AI-Career-Co-Pilot/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── history.html
│   ├── login.html
│   └── signup.html
│
├── .gitignore
├── app.py
├── artificialintelligence.py
├── database.py
├── models.py
└── requirements.txt
```



## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/maryamunir-dev/AI-Career-Co-Pilot.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Career-Co-Pilot
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Configure the required database connection details and Gemini API key using environment variables. Keep secret keys and database credentials private.

### 6. Run the Application

```bash
python app.py
```

Open the local URL displayed in your terminal to access the application.

## 🔐 Security

- Store API keys and database credentials securely in environment variables.
- Never commit secret keys, passwords, or sensitive configuration files to GitHub.

## 🎯 Project Goal

The goal of AI Career Co-Pilot is to explore how artificial intelligence, web technologies, and database systems can be combined to build useful career development tools.


---

*Built with Python, Flask, and AI to explore smarter career assistance.*
