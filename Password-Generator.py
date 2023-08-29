import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=50)
        
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=50)
        
        self.complexity_label = tk.Label(root, text="Password Complexity:")
        self.complexity_label.pack(pady=50)
        
        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")
        
        self.complexity_radio_low = tk.Radiobutton(root, text="Low", variable=self.complexity_var, value="Low")
        self.complexity_radio_medium = tk.Radiobutton(root, text="Medium", variable=self.complexity_var, value="Medium")
        self.complexity_radio_high = tk.Radiobutton(root, text="High", variable=self.complexity_var, value="High")
        
        self.complexity_radio_low.pack()
        self.complexity_radio_medium.pack()
        self.complexity_radio_high.pack()
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=30)
        
        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack()
        
        self.generated_password = tk.StringVar()
        self.generated_password_label = tk.Label(root, textvariable=self.generated_password, font=("Helvetica", 40, "bold"))
        self.generated_password_label.pack()
        
    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()
        
        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(length))
        self.generated_password.set(password)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
