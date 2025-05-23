# 🤖 ATS Resume Analyzer

**AI-powered Resume Evaluator using Streamlit + Gemini AI**

This tool helps job seekers evaluate and optimize their resumes against job descriptions using Google Gemini's powerful natural language capabilities. Get ATS compatibility insights, keyword suggestions, skill gap analysis, and resume scoring — all in one place.

---

## 🔍 Features

✅ Upload your resume in **PDF** format  
✅ Paste a **job description**  
✅ Get **AI-powered analysis**:
- Overall Resume Assessment
- Skills Gap & Learning Path
- Keyword Optimization
- Resume Score out of 100
- Recruiter-focused insights

---

## 🛠️ Built With

- [Streamlit]– Python web app framework
- [Google Gemini AI] – LLM for content generation
- [pdf2image] – Convert PDFs to images
- [Pillow (PIL)]– Image handling
- `dotenv`, `base64`, `io`, `os`

---

## 🚀 Live Demo

🔗 [Try the App Online]([https://your-deployment-link.com](https://ats-resume-analyzer-z.streamlit.app/))  

---

## 🧑‍💻 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/MohammedTawfikEldeeb/ATS-Resume-Analyzer.git
cd ATS-Resume-Analyzer
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Set up your environment**
   Create a .env file in the project root and add:
```bash
GEMINI_API_KEY=your_google_gemini_api_key
```
4. **Run the Streamlit app**
```bash
streamlit run app.py
```



