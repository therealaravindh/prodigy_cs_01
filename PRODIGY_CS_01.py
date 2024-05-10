import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_decrypt():
    message = entry_message.get()
    shift = int(entry_shift.get())
    if choice.get() == 1:
        result = encrypt(message, shift)
        messagebox.showinfo("Encryption Result", f"Encrypted message: {result}")
    elif choice.get() == 2:
        result = decrypt(message, shift)
        messagebox.showinfo("Decryption Result", f"Decrypted message: {result}")


root = tk.Tk()
root.title("Caesar Cipher Encryptor/Decryptor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_message = tk.Label(frame, text="Enter message:")
label_message.grid(row=0, column=0, sticky="w")

entry_message = tk.Entry(frame, width=40)
entry_message.grid(row=0, column=1, padx=5, pady=5)

label_shift = tk.Label(frame, text="Enter shift value:")
label_shift.grid(row=1, column=0, sticky="w")

entry_shift = tk.Entry(frame, width=10)
entry_shift.grid(row=1, column=1, padx=5, pady=5)

choice = tk.IntVar()
choice.set(1)

encrypt_radio = tk.Radiobutton(frame, text="Encrypt", variable=choice, value=1)
encrypt_radio.grid(row=2, column=0, padx=5, pady=5)

decrypt_radio = tk.Radiobutton(frame, text="Decrypt", variable=choice, value=2)
decrypt_radio.grid(row=2, column=1, padx=5, pady=5)

encrypt_button = tk.Button(frame, text="Encrypt/Decrypt", command=encrypt_decrypt)
encrypt_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()
