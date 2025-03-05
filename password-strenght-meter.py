import re

# Password Strength Meter
def check_password_strength(password):
    score = 0  # Password ki overall strength ko measure karta hai.
    feedback = []  # Weak passwords ko improve karne ke liye help karta hai

    # Length Check
    if len(password) >= 8:  # Password ki length check karta hai, minimum 8 characters
        score += 1
    else:
        feedback.append("\u274C Password should be at least 8 characters long.") #\u274C Error Messages ya Negative Feedback dikhane ke liye.

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):  # Upper aur lowercase letters check karta hai
        score += 1
    else:
        feedback.append("\u274C Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):  # Password me numbers check karta hai
        score += 1
    else:
        feedback.append("\u274C Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):  # Password me special characters check karta hai
        score += 1
    else:
        feedback.append("\u274C Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:  # Strong password condition
        return "strong", "\u2705 Strong Password!"
    elif score == 3:  # Moderate password condition
        return "moderate", "\u26A0\uFE0F Moderate Password - Consider adding more security features."
    else:  # Weak password condition
        return "weak", feedback

# Login Form
def login():
    print("\U0001F510 Welcome to the Login Form!")
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    strength, message = check_password_strength(password)

    if strength == "strong":
        print("\nRedirecting to the next page...\n")
        print(f"\U0001F389 Welcome {name}!")
        print("Welcome Neha Khan Apps!")
    elif strength == "moderate":
        print("\nPassword is moderate. Please improve it.")
        print(message)
    else:
        print("\nPassword is weak. Please improve it using the suggestions below:")
        for suggestion in message:
            print("  -", suggestion)

# Execute Login Function
if __name__ == "__main__":
    login()
