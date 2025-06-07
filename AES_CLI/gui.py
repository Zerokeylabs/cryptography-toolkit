# gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import pyperclip

def pad(text):
    return text + b" " * (16 - len(text) % 16)

def encrypt_file():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return

    key = key_entry.get().encode('utf-8')
    if len(key) != 16:
        messagebox.showerror("Key Error", "Key must be exactly 16 characters!")
        return

    with open(filepath, 'rb') as f:
        data = pad(f.read())

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(data)

    outpath = filedialog.asksaveasfilename(defaultextension=".enc")
    if outpath:
        with open(outpath, 'wb') as f:
            f.write(encrypted)
        messagebox.showinfo("Success", "File encrypted!")

def decrypt_file():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return

    key = key_entry.get().encode('utf-8')
    if len(key) != 16:
        messagebox.showerror("Key Error", "Key must be exactly 16 characters!")
        return

    with open(filepath, 'rb') as f:
        encrypted = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted).rstrip(b" ")

    outpath = filedialog.asksaveasfilename(defaultextension=".txt")
    if outpath:
        with open(outpath, 'wb') as f:
            f.write(decrypted)
        messagebox.showinfo("Success", "File decrypted!")

def update_count(event=None):
    count_label.config(text=f"{len(key_entry.get())}/16 chars")

def generate_key():
    raw_key = get_random_bytes(16)
    key = base64.urlsafe_b64encode(raw_key)[:16].decode('utf-8')
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)
    update_count()
    pyperclip.copy(key)
    messagebox.showinfo("Key Generated", f"New key copied to clipboard:\n\n{key}")

# GUI Setup
root = tk.Tk()
root.title("AES File Encryptor (16-char Key)")
root.geometry("400x250")

tk.Label(root, text="Enter 16-character Key:").pack(pady=5)

key_entry = tk.Entry(root, width=30, show="*")
key_entry.pack(pady=5)
key_entry.bind("<KeyRelease>", update_count)

count_label = tk.Label(root, text="0/16 chars")
count_label.pack()

tk.Button(root, text="Generate Key", command=generate_key).pack(pady=5)
tk.Button(root, text="Encrypt File", command=encrypt_file).pack(pady=10)
tk.Button(root, text="Decrypt File", command=decrypt_file).pack(pady=5)

root.mainloop()
