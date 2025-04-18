import re

def check_password_strength(password):
    strength = "Strength: "

    if len(password) < 6:
        level = "Weak"
        color = "red"
    elif re.search(r'[A-Z]', password) and re.search(r'\d', password) and len(password) >= 8:
        level = "Strong"
        color = "#66CDAA"
    else:
        level = "Medium"
        color = "orange"

    return f"{strength}{level}", color