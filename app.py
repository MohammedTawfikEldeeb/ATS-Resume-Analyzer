# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Import packages
import streamlit as st
import os
from PIL import Image
import pdf2image
import io
import base64
import google.generativeai as genai


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        response = model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

# Function to process uploaded PDF
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            images = pdf2image.convert_from_bytes(uploaded_file.read(), dpi=200)
            first_page = images[0]

            
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()
                }
            ]
            return pdf_parts
        except Exception as e:
            raise RuntimeError(f"Error processing PDF file: {e}")
    else:
        raise FileNotFoundError("No file uploaded.")


st.set_page_config(page_title="ATS Resume Expert")
st.header("🤖 ATS Resume Analyzer")
st.markdown("Upload your resume and provide a job description to receive AI-powered feedback.")


input_text = st.text_area("Job Description", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    st.success("✅ PDF uploaded successfully!")

# Buttons
submit1 = st.button("Tell me about Resume")
submit2 = st.button("How can I improve my skills")
submit3 = st.button("What keywords are missing")
submit4 = st.button("Resume Score")



input_prompt1 = """You are an experienced Technical Human Resource Manager with deep knowledge of ATS systems. Your task is to review the provided resume against the job description. Please provide:

1. **Overall Assessment**: Professional evaluation of profile alignment
2. **Strengths**: Key strengths that match the role
3. **Weaknesses**: Areas that need improvement
4. **ATS Compatibility**: Formatting and structure assessment
5. **Recruiter Perspective**: What would catch a recruiter's attention

Format your response with clear sections and actionable insights.""",

input_prompt2 = """As a seasoned Technical Recruiter and Career Advisor, provide a comprehensive skills analysis:

1. **Current Skills Assessment**: Evaluate existing skills from the resume
2. **Critical Skill Gaps**: Identify missing skills for the target role
3. **Priority Learning Path**: Rank skills by importance and urgency
4. **Recommended Resources**: Specific courses, certifications, or training
5. **Timeline Suggestion**: Realistic timeline for skill development

Focus on technical, analytical, and soft skills relevant to the position.""",

input_prompt3 ="""You are an ATS Optimization Expert. Conduct a thorough keyword analysis:

1. **Missing Keywords**: Essential terms not found in the resume
2. **Keyword Density**: Current keyword usage assessment
3. **Industry-Specific Terms**: Relevant technical vocabulary
4. **Action Verbs**: Powerful verbs to include
5. **Optimization Strategy**: How to naturally integrate keywords

Provide specific examples of where and how to incorporate these keywords.""",

input_prompt4 = """You are an ATS and HR Evaluation Specialist. Provide a detailed scoring analysis:

1. **Overall Score**: X/100 with clear justification
2. **Category Breakdown**:
   - Keyword Relevance: X/25
   - Format & Structure: X/25
   - Content Quality: X/25
   - ATS Compatibility: X/25
3. **Specific Improvements**: Actionable steps to increase score
4. **Competitive Analysis**: How it compares to typical candidates
5. **Priority Fixes**: Most impactful changes to make first

Include specific examples and before/after suggestions.""",

if submit1 or submit2 or submit3 or submit4:
    if uploaded_file is not None:
        try:
            pdf_content = input_pdf_setup(uploaded_file)

            if submit1:
                response = get_gemini_response(input_text, pdf_content, input_prompt1)
            elif submit2:
                response = get_gemini_response(input_text, pdf_content, input_prompt2)
            elif submit3:
                response = get_gemini_response(input_text, pdf_content, input_prompt3)
            elif submit4:
                response = get_gemini_response(input_text, pdf_content, input_prompt4)

            st.subheader("📝 AI Response")
            st.write(response)

        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please upload your resume.")
