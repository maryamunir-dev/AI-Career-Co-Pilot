from flask import Flask, render_template, request, redirect, session
from database import Base, engine, SessionLocal
import models
import PyPDF2
import docx
import json
from artificalintelign import analyze_resume
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

Base.metadata.create_all(bind=engine)

@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    database = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = database.query(models.User).filter_by(email=email).first()
        if existing_user:
            database.close()
            return "User already exists"

        new_user = models.User(email=email, password=password)
        database.add(new_user)
        database.commit()
        database.close()
        return redirect("/login")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    database = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = database.query(models.User).filter_by(email=email, password=password).first()
        database.close()

        if user: 
            session["user"] = user.email
            return redirect("/dashboard")
        else:
            return "Invalid credentials! <a href='/login'>Try Again</a>"

    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":
        user_role = request.form.get("role")
        resume_text = request.form.get("resume")
        uploaded_file = request.files.get("file")

        if uploaded_file and uploaded_file.filename != "":
            filename = uploaded_file.filename.lower()
            
            if filename.endswith(".pdf"):
                try:
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    extracted_text = ""
                    for page in pdf_reader.pages:
                        extracted_text += page.extract_text() or ""
                    resume_text = extracted_text
                except Exception as e:
                    result = {"error": f"Failed to parse PDF: {str(e)}"}

            elif filename.endswith(".docx"):
                try:
                    doc = docx.Document(uploaded_file)
                    extracted_text = "\n".join([p.text for p in doc.paragraphs])
                    resume_text = extracted_text
                except Exception as e:
                    result = {"error": f"Failed to parse DOCX: {str(e)}"}
            else:
                result = {"error": "Unsupported format! Please upload PDF or DOCX."}

        if resume_text and user_role and not result:
            try:
                result = analyze_resume(resume_text, user_role)

                if "error" not in result:
                    database = SessionLocal()
                    current_user = database.query(models.User).filter_by(email=session["user"]).first()
                    
                    if current_user:
                        new_report = models.Reports(
                            user_id=current_user.id,
                            resume_text=resume_text[:200],
                            result=json.dumps(result)
                        )
                        database.add(new_report)
                        database.commit()
                    database.close()
                    
                
                    return render_template("dashboard.html", user=session["user"], result=result)

            except Exception as e:
                result = {"error": f"AI error: {str(e)}"}

    return render_template("dashboard.html", user=session["user"], result=result)


@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")

    database = SessionLocal()
    current_user = database.query(models.User).filter_by(email=session["user"]).first()
    
    parsed_reports = []
    
    if current_user:
        user_reports = database.query(models.Reports).filter_by(user_id=current_user.id).all()
        for r in user_reports:
            try:
                ai_result = json.loads(r.result) if r.result else {}
            except Exception:
                ai_result = {}
                
            parsed_reports.append({
                "resume": r.resume_text or "No preview content",
                "result": ai_result
            })
            
    database.close()
    return render_template("history.html", reports=parsed_reports)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
