import os
import tkinter as tk
from tkinter import ttk, font, messagebox
import sys

# No PIL dependency - we'll use tkinter's built-in PhotoImage instead


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Translator - Login")
        self.root.geometry("800x600")
        
        # Try to load the icon
        try:
            self.icon = tk.PhotoImage(file="icon.png")
            self.root.iconphoto(False, self.icon)
        except tk.TclError:
            print("Icon not found. Using default icon.")
        
        # Set background color
        self.root.configure(bg="#f0f5ff")
        
        # Configure custom fonts
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=12)
        self.text_font = font.Font(family="Helvetica", size=11)
        self.button_font = font.Font(family="Helvetica", size=11, weight="bold")
        self.small_font = font.Font(family="Helvetica", size=9)
        
        # Create the login form
        self.create_login_form()
    
    def _create_text_header(self, parent_frame):
        """Create a text-only header when PIL is not available"""
        # Create a decorative element instead of an image
        decorative_frame = tk.Frame(parent_frame, bg="#3a7ebf", width=60, height=60)
        decorative_frame.pack(pady=10)
        
        # Make the frame maintain its size
        decorative_frame.pack_propagate(False)
    
    def create_login_form(self):
        # Main container with gradient effect
        main_frame = tk.Frame(self.root, bg="#f0f5ff")
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # App logo/name at the top
        logo_frame = tk.Frame(main_frame, bg="#f0f5ff")
        logo_frame.pack(pady=(0, 20))
        
        # Try to load logo image using tkinter's built-in PhotoImage
        try:
            # Note: tkinter's PhotoImage only supports GIF, PGM, PPM, and PNG formats
            logo_photo = tk.PhotoImage(file="icon.png")
            
            # Create a smaller version of the image (if needed)
            # This is a simple approach - not as good as PIL's resize but works
            logo_photo = logo_photo.subsample(3, 3)  # Reduce by factor of 3
            
            logo_label = tk.Label(logo_frame, image=logo_photo, bg="#f0f5ff")
            logo_label.image = logo_photo  # Keep a reference
            logo_label.pack()
        except Exception as e:
            print(f"Could not load logo image: {e}")
            # Fallback to text-only header
            self._create_text_header(logo_frame)
        
        # App name
        app_name = tk.Label(
            logo_frame, 
            text="Voice Translator", 
            font=self.title_font, 
            fg="#3a7ebf", 
            bg="#f0f5ff"
        )
        app_name.pack(pady=(10, 0))
        
        # Login form with shadow effect and rounded corners (simulated)
        login_frame = tk.Frame(
            main_frame, 
            bg="white", 
            padx=40, 
            pady=30,
            highlightbackground="#d0d0d0",
            highlightthickness=1,
        )
        login_frame.pack(padx=20, pady=20)
        
        # Add shadow effect with multiple frames
        shadow_frame = tk.Frame(
            main_frame,
            bg="#e0e0e0",
            highlightbackground="#e0e0e0",
            highlightthickness=1
        )
        shadow_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=322, height=362, x=3, y=3)
        
        # Place the login frame on top of the shadow
        login_frame.lift()
        
        # Username/Email field
        username_label = tk.Label(
            login_frame, 
            text="Username or Email", 
            font=self.label_font, 
            bg="white", 
            fg="#333333",
            anchor="w"
        )
        username_label.pack(fill="x", pady=(0, 5))
        
        self.username_entry = tk.Entry(
            login_frame, 
            font=self.text_font, 
            bg="#f8f8f8", 
            fg="#333333",
            relief=tk.SOLID,
            bd=1,
            highlightthickness=1,
            highlightbackground="#e0e0e0"
        )
        self.username_entry.pack(fill="x", ipady=8, pady=(0, 15))
        
        # Password field
        password_label = tk.Label(
            login_frame, 
            text="Password", 
            font=self.label_font, 
            bg="white", 
            fg="#333333",
            anchor="w"
        )
        password_label.pack(fill="x", pady=(0, 5))
        
        self.password_entry = tk.Entry(
            login_frame, 
            font=self.text_font, 
            bg="#f8f8f8", 
            fg="#333333",
            relief=tk.SOLID,
            bd=1,
            highlightthickness=1,
            highlightbackground="#e0e0e0",
            show="•"  # Show dots instead of actual password
        )
        self.password_entry.pack(fill="x", ipady=8, pady=(0, 5))
        
        # Error message placeholder (hidden by default)
        self.error_label = tk.Label(
            login_frame, 
            text="", 
            font=self.small_font, 
            bg="white", 
            fg="#e74c3c",  # Red color for error
            anchor="w"
        )
        self.error_label.pack(fill="x", pady=(5, 10))
        
        # Forgot password link
        forgot_password = tk.Label(
            login_frame, 
            text="Forgot password?", 
            font=self.small_font, 
            bg="white", 
            fg="#3a7ebf",
            cursor="hand2"
        )
        forgot_password.pack(anchor="e", pady=(0, 15))
        forgot_password.bind("<Button-1>", self.forgot_password)
        
        # Login button with hover effect
        self.login_button = tk.Button(
            login_frame, 
            text="Login", 
            font=self.button_font, 
            bg="#3a7ebf", 
            fg="white",
            activebackground="#2a5d8f",
            activeforeground="white",
            relief=tk.FLAT,
            command=self.login,
            cursor="hand2",
            padx=10,
            pady=8
        )
        self.login_button.pack(fill="x", pady=(10, 0))
        
        # Bind hover events for button
        self.login_button.bind("<Enter>", self.on_enter)
        self.login_button.bind("<Leave>", self.on_leave)
    
    def on_enter(self, event):
        self.login_button.config(bg="#5294d4")
    
    def on_leave(self, event):
        self.login_button.config(bg="#3a7ebf")
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Simple validation
        if not username or not password:
            self.error_label.config(text="Please enter both username and password")
            return
        
        # For demo purposes, accept any non-empty credentials
        # In a real app, you would validate against a database
        
        # Clear the login window
        self.root.destroy()
        
        # Start the main application by running main.py with --no-login flag
        # This avoids circular imports
        import subprocess
        subprocess.Popen([sys.executable, 'main.py', '--no-login'])
    
    def forgot_password(self, event):
        messagebox.showinfo(
            "Forgot Password", 
            "Please contact the administrator to reset your password."
        )


# Function to start the login page
def start_login():
    login_root = tk.Tk()
    login_app = LoginPage(login_root)
    login_root.mainloop()


# If this file is run directly, start the login page
if __name__ == "__main__":
    start_login()