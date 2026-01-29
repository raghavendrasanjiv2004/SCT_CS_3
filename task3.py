import re
import getpass

common_passwords = [
    "password", "123456", "12345678", "qwerty",
    "abc123", "password123", "admin", "letmein"
]

def password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    
    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    
    if len(set(password)) < len(password) * 0.6:
        suggestions.append("Avoid repeated characters")

    
    if password.lower() in common_passwords:
        return "Very Weak Password", suggestions

   
    if score <= 3:
        return "Weak Password", suggestions
    elif score <= 5:
        return "Medium Password", suggestions
    else:
        return "Strong Password", []


password = getpass.getpass("Enter password to check strength: ")

strength, tips = password_strength(password)

print("\nPassword Strength:", strength)

if tips:
    print("Suggestions:")
    for tip in tips:
        print("-", tip)
