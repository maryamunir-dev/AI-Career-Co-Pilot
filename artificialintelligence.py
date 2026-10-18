import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def analyze_resume(resume_text, user_goal):
    prompt = f"""
    You are a Senior Software Engineer and Expert Hiring Manager.
    Evaluate the following resume content based strictly on the user's targeted career goal.
    
    Targeted Career Goal: {user_goal}
    Resume Content: {resume_text}
    
    Strict Rules:
    1. Extract ONLY relevant technical skills that match the target career goal.
    2. Identify real gaps by comparing the resume skills with market requirements for a {user_goal}.
    3. Generate a structured step-by-step learning roadmap ONLY for the missing fields.
    4. Provide 3-5 high-quality expected technical interview questions based on the missing or required skills.
    5. Remove irrelevant tools[excel for backend, etc]
    6. Return the output ONLY as a valid JSON object. Do not include markdown code blocks like ```json or any conversational text.

     Expected JSON Format:
    {{
        "skills": ["List of matching skills found in resume"],
        "missing_skills": ["List of critical skills missing for the targeted role"],
        "roadmap": ["Step 1...", "Step 2...", "Step 3..."],
        "interview_questions": ["Question 1?", "Question 2?", "Question 3?"]
    }}
    """

    try:
        
        model = genai.GenerativeModel("gemini-3.8-flash")
        
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        

        raw_content = response.text.strip()
        parsed_json = json.loads(raw_content)
        return parsed_json

    except json.JSONDecodeError:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": "Google AI returned an invalid response format. Please try again."
        }
        
    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": f"Google AI Generation Failed: {str(e)}"
        }
