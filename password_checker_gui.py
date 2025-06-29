import tkinter as tk
from tkinter import messagebox
import re

# List of weak passwords
weak_passwords = ['123456', 'password', 'qwerty', '111111', 'abc123']

# Password strength function
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

    if password.lower() in weak_passwords:
        tips.append("Avoid common passwords like '123456'.")
        score = 0

    return score, tips

# GUI function
def evaluate_password():
    password = entry.get()
    strength, suggestions = check_password_strength(password)

    result_text = f"Strength Score: {strength}/6\n"

    if strength >= 5:
        result_text += "🟢 Strong password!"
        result_label.config(fg="green")
    elif strength >= 3:
        result_text += "🟡 Medium password. Consider improving:"
        result_label.config(fg="orange")
    else:
        result_text += "🔴 Weak password. Please improve:"
        result_label.config(fg="red")

    result_label.config(text=result_text)

    # Show suggestions
    tips_text = "\n".join(f"• {tip}" for tip in suggestions)
    tips_label.config(text=tips_text)

# Set up GUI window
window = tk.Tk()
window.title("🔐 Password Strength Checker")
window.geometry("400x300")
window.config(bg="#f0f0f0")

# Widgets
tk.Label(window, text="Enter your password:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
entry = tk.Entry(window, width=30, show="*", font=("Arial", 12))
entry.pack()

tk.Button(window, text="Check Strength", command=evaluate_password, font=("Arial", 12), bg="#007acc", fg="white").pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
result_label.pack()

tips_label = tk.Label(window, text="", font=("Arial", 10), bg="#f0f0f0", justify="left", wraplength=350)
tips_label.pack(pady=10)

# Run the app
window.mainloop()
