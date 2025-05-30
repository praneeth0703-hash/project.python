import re
import math
import tkinter as tk

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset += 32
    entropy = len(password) * math.log2(charset) if charset else 0
    return entropy

def check_password():
    password = entry.get()
    if len(password) < 8:
        result.set("Password too short! (min 8 characters)")
        return
    entropy = calculate_entropy(password)
    if entropy < 28:
        strength = "Very Weak"
    elif entropy < 36:
        strength = "Weak"
    elif entropy < 60:
        strength = "Moderate"
    elif entropy < 128:
        strength = "Strong"
    else:
        strength = "Very Strong"
    result.set(f"Password Strength: {strength}\nEntropy: {entropy:.2f} bits")

root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter your password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)
tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)
result = tk.StringVar()
tk.Label(root, textvariable=result, fg="blue").pack(pady=5)

root.mainloop()
