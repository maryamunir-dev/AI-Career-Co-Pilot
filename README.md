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


## 📸 Project Screenshots

### 🔒 User Authentication (Signup / Login)
*Secure gateway for users to create an account and log in safely:*

<img width="1822" height="901" alt="login-auth-screen png" src="https://github.com/user-attachments/assets/ead26903-be43-4226-8b3f-8da3901ba94a" />
<img width="1867" height="896" alt="signup-auth-screen png" src="https://github.com/user-attachments/assets/deecf52d-c089-4637-894a-67cd23655747" />


### 📊 Main Application Dashboard
*The dashboard interface where users can paste or upload their resumes for AI-powered analysis:*

<img width="1843" height="900" alt="dashboard-screen png" src="https://github.com/user-attachments/assets/77a57257-9232-4aef-981b-c3279f879b23" />


### 🧪 Real-time Resume Analysis Result
*AI-generated results showing relevant skills, skill gaps, and personalized career recommendations using the Gemini API:*

<img width="1145" height="536" alt="analysis-screen png" src="https://github.com/user-attachments/assets/d2788781-7212-42a3-8fee-32a693c0dec3" />

### 📜 Saved Analysis History
*The history page displaying previous resume analyses, identified skill gaps, and personalized learning roadmaps saved in the database:*

<img width="1887" height="908" alt="history-screen png" src="https://github.com/user-attachments/assets/3b635e4f-7acc-4c0e-92ab-294eacc408dd" />

---

*Built with Python, Flask, and AI to explore smarter career assistance.*
---
