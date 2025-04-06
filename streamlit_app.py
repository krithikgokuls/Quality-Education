# streamlit_app.py
import streamlit as st

# Backend logic copied here
learning_paths = {
    "Math": ["Algebra Basics", "Linear Equations", "Quadratic Equations", "Geometry", "Probability"],
    "Science": ["Introduction to Physics", "Newton's Laws", "Simple Machines", "Electricity", "Magnetism"]
}

def generate_learning_path(subject, level):
    path = learning_paths.get(subject, [])
    if level == "Beginner":
        return path[:3]
    elif level == "Intermediate":
        return path[1:4]
    elif level == "Advanced":
        return path[2:]
    return path

# Frontend
st.title("EduBridge - Personalized Learning Path")

name = st.text_input("Enter your name")
subject = st.selectbox("Choose Subject", ["Math", "Science"])
level = st.selectbox("Your Skill Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Plan"):
    path = generate_learning_path(subject, level)
    st.success(f"Hello {name}, here is your learning plan:")
    for i, topic in enumerate(path, 1):
        st.write(f"{i}. {topic}")
