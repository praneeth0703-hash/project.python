from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox

# Generate or load a secret key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        return generate_key()

# Encryption function
def encrypt_file(filepath, key):
    with open(filepath, "rb") as file:
        data = file.read()
    f = Fernet(key)
    encrypted = f.encrypt(data)
    with open(filepath + ".encrypted", "wb") as file:
        file.write(encrypted)

# Decryption function
def decrypt_file(filepath, key):
    with open(filepath, "rb") as file:
        data = file.read()
    f = Fernet(key)
    decrypted = f.decrypt(data)
    original_path = filepath.replace(".encrypted", "_decrypted")
    with open(original_path, "wb") as file:
        file.write(decrypted)

# GUI Interface
def choose_file_encrypt():
    file_path = filedialog.askopenfilename()
    if file_path:
        key = load_key()
        encrypt_file(file_path, key)
        messagebox.showinfo("Success", "File encrypted successfully!")

def choose_file_decrypt():
    file_path = filedialog.askopenfilename()
    if file_path:
        key = load_key()
        try:
            decrypt_file(file_path, key)
            messagebox.showinfo("Success", "File decrypted successfully!")
        except:
            messagebox.showerror("Error", "Decryption failed! Wrong key or file.")

# Set up the UI
root = tk.Tk()
root.title("Secure File Encryptor")

tk.Label(root, text="Secure File Encryption & Decryption", font=("Helvetica", 14)).pack(pady=10)
tk.Button(root, text="Encrypt a File", command=choose_file_encrypt, width=30).pack(pady=5)
tk.Button(root, text="Decrypt a File", command=choose_file_decrypt, width=30).pack(pady=5)

root.mainloop()