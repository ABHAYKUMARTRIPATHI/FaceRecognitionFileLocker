import tkinter as tk
from tkinter import filedialog, messagebox
from face_authenticator import authenticate_user
from encryptor import encrypt_file, decrypt_file

def start_gui():
    root = tk.Tk()
    root.title("Face Recognition File Locker")
    root.geometry("400x300")

    def lock_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            if authenticate_user():
                encrypt_file(file_path)
                messagebox.showinfo("Success", "File locked (encrypted) successfully.")
            else:
                messagebox.showerror("Access Denied", "Face not recognized.")

    def unlock_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            if authenticate_user():
                decrypt_file(file_path)
                messagebox.showinfo("Success", "File unlocked (decrypted) successfully.")
            else:
                messagebox.showerror("Access Denied", "Face not recognized.")

    tk.Button(root, text="🔐 Lock File", command=lock_file, width=30).pack(pady=20)
    tk.Button(root, text="🔓 Unlock File", command=unlock_file, width=30).pack(pady=20)

    root.mainloop()