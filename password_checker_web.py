import streamlit as st
import re

def check_password_strength(password):
    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        tips.append("Include numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        tips.append("Use special characters like !@#.")

    if password.lower() in ['123456', 'password', 'qwerty', '111111', 'abc123']:
        tips.append("Avoid common passwords like '123456'.")
        score = 0

    return score, tips

# Streamlit App
st.set_page_config(page_title="Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    score, suggestions = check_password_strength(password)

    st.markdown(f"### ✅ Strength Score: {score} / 6")
    
    if score >= 5:
        st.success("🟢 Strong password!")
    elif score >= 3:
        st.warning("🟡 Medium password. Consider improving:")
    else:
        st.error("🔴 Weak password. Please improve:")

    for tip in suggestions:
        st.markdown(f"- {tip}")
