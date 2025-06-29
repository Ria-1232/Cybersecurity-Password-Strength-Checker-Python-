import re

# Common weak passwords (you can expand this list)
weak_passwords = ['123456', 'password', 'qwerty', '111111', 'abc123']

def check_password_strength(password):
    score = 0
    tips = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 12 characters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add uppercase letters.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Add lowercase letters.")

    # Check for digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        tips.append("Include numbers.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        tips.append("Use special characters like !@#.")

    # Check if it's a common weak password
    if password.lower() in weak_passwords:
        tips.append("Avoid common passwords like '123456'.")
        score = 0  # force score to weak

    return score, tips

# Main program
if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    user_password = input("Enter a password to check: ")

    strength, suggestions = check_password_strength(user_password)

    print("\n✅ Strength Score:", strength, "/ 6")

    if strength >= 5:
        print("🟢 Strong password!")
    elif strength >= 3:
        print("🟡 Medium password. Consider improving:")
    else:
        print("🔴 Weak password. Please improve:")

    for tip in suggestions:
        print("- " + tip)
