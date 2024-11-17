import customtkinter as ctk
from datetime import datetime
import random
import string

# Set appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PasswordGenerator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Password Generator")
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        self.window.iconbitmap("icon.ico")
        # Title
        self.title_label = ctk.CTkLabel(self.window, text="Password Generator", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        # Length selection
        self.length_frame = ctk.CTkFrame(self.window)
        self.length_frame.pack(pady=10)
        
        self.length_label = ctk.CTkLabel(self.length_frame, text="Password Length:")
        self.length_label.pack(side="left", padx=10)
        
        self.length_var = ctk.StringVar(value="12")
        self.length_entry = ctk.CTkEntry(self.length_frame, textvariable=self.length_var, width=50)
        self.length_entry.pack(side="left")

        # Checkboxes for password criteria
        self.uppercase_var = ctk.BooleanVar(value=True)
        self.uppercase_check = ctk.CTkCheckBox(self.window, text="Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_check.pack(pady=5)

        self.lowercase_var = ctk.BooleanVar(value=True)
        self.lowercase_check = ctk.CTkCheckBox(self.window, text="Lowercase Letters", variable=self.lowercase_var)
        self.lowercase_check.pack(pady=5)

        self.numbers_var = ctk.BooleanVar(value=True)
        self.numbers_check = ctk.CTkCheckBox(self.window, text="Numbers", variable=self.numbers_var)
        self.numbers_check.pack(pady=5)

        self.symbols_var = ctk.BooleanVar(value=True)
        self.symbols_check = ctk.CTkCheckBox(self.window, text="Symbols", variable=self.symbols_var)
        self.symbols_check.pack(pady=5)

        # Generate button
        self.generate_button = ctk.CTkButton(self.window, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Password display
        self.password_display = ctk.CTkTextbox(self.window, height=100, width=300)
        self.password_display.pack(pady=10)

        # Credit label
        self.credit_label = ctk.CTkLabel(self.window, text="Made by SireenDev", font=("Arial", 12))
        self.credit_label.pack(pady=20)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                self.password_display.delete("1.0", "end")
                self.password_display.insert("1.0", "Please enter a positive number")
                return
        except ValueError:
            self.password_display.delete("1.0", "end")
            self.password_display.insert("1.0", "Please enter a valid number")
            return

        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.numbers_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += string.punctuation

        if not characters:
            self.password_display.delete("1.0", "end")
            self.password_display.insert("1.0", "Please select at least one character type")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.delete("1.0", "end")
        self.password_display.insert("1.0", password)

        # Save password with timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("generated_passwords.txt", "a") as file:
            file.write(f"{password} - {current_time}\n")

if __name__ == "__main__":
    app = PasswordGenerator()
    app.window.mainloop()
