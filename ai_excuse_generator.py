import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="🎭 AI Excuse Generator", page_icon="🎭")
st.title("🎭 AI Excuse Generator")
st.caption("Get AI-generated excuses using Gemini 1.5 Flash!")

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")  

        situation = st.selectbox("📌 Choose a situation", ["Late to class", "Missed a deadline", "Forgot homework", "Skipped meeting", "Overslept"])
        tone = st.selectbox("🎨 Choose a tone", ["Funny", "Serious", "Apologetic", "Creative"])
        extra = st.text_area("📝 Extra details (optional)")

        if st.button("🎬 Generate Excuse"):
            with st.spinner("Cooking up an excuse..."):
                prompt = f"Write a {tone.lower()} excuse for this situation: {situation}. Extra context: {extra if extra else 'None'}"
                response = model.generate_content(prompt)
                st.success("🎉 Here's your excuse:")
                st.markdown(f"> {response.text}")

    except Exception as e:
        st.error(f"❌ Something went wrong:\n\n{e}")
else:
    st.warning("🚨 GEMINI_API_KEY not found. Please add it to your `.env` file or environment variables.")
