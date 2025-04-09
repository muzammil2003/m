import os
import sys
import tkinter as tk
from tkinter import ttk, font, messagebox
import subprocess


class ModernLoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Translator - Login")
        self.root.geometry("1000x600")
        self.root.minsize(800, 600)
        
        # Set background color
        self.root.configure(bg="#f5f5f7")
        
        # Try to load the icon
        try:
            self.icon = tk.PhotoImage(file="icon.png")
            self.root.iconphoto(False, self.icon)
        except tk.TclError:
            print("Icon not found. Using default icon.")
        
        # Configure custom fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.heading_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=12)
        self.text_font = font.Font(family="Helvetica", size=11)
        self.button_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.small_font = font.Font(family="Helvetica", size=9)
        
        # Create the main container
        self.create_layout()
    
    def create_layout(self):
        # Create a two-column layout
        self.main_frame = tk.Frame(self.root, bg="#f5f5f7")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel (decorative)
        self.left_panel = tk.Frame(self.main_frame, bg="#3a7ebf", width=500)
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Make sure the left panel maintains its size
        self.left_panel.pack_propagate(False)
        
        # Add decorative elements to left panel
        self.create_left_panel()
        
        # Right panel (login form)
        self.right_panel = tk.Frame(self.main_frame, bg="#ffffff", padx=40, pady=20)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Create login form in right panel
        self.create_login_form()
    
    def create_left_panel(self):
        # Create a container for centered content
        center_frame = tk.Frame(self.left_panel, bg="#3a7ebf")
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Try to load app icon
        try:
            logo = tk.PhotoImage(file="icon.png")
            # Scale down if needed
            logo = logo.subsample(2, 2)
            logo_label = tk.Label(center_frame, image=logo, bg="#3a7ebf")
            logo_label.image = logo  # Keep a reference
            logo_label.pack(pady=(0, 20))
        except Exception:
            # Create a decorative circle if icon not available
            canvas = tk.Canvas(center_frame, width=120, height=120, bg="#3a7ebf", highlightthickness=0)
            canvas.create_oval(10, 10, 110, 110, fill="#ffffff", outline="")
            canvas.create_text(60, 60, text="VT", fill="#3a7ebf", font=("Helvetica", 36, "bold"))
            canvas.pack(pady=(0, 20))
        
        # App name
        app_name = tk.Label(
            center_frame, 
            text="Voice Translator", 
            font=self.title_font, 
            fg="#ffffff", 
            bg="#3a7ebf"
        )
        app_name.pack(pady=(0, 10))
        
        # Tagline
        tagline = tk.Label(
            center_frame, 
            text="Break language barriers in real-time", 
            font=self.label_font, 
            fg="#e0e0e0", 
            bg="#3a7ebf"
        )
        tagline.pack(pady=(0, 30))
        
        # Features list
        features_frame = tk.Frame(center_frame, bg="#3a7ebf", padx=20)
        features_frame.pack(anchor=tk.W)
        
        features = [
            "✓ Real-time voice translation",
            "✓ Support for 15+ languages",
            "✓ Preserve tone and emotion",
            "✓ Easy-to-use interface"
        ]
        
        for feature in features:
            feature_label = tk.Label(
                features_frame, 
                text=feature, 
                font=self.label_font, 
                fg="#ffffff", 
                bg="#3a7ebf",
                anchor="w",
                pady=5
            )
            feature_label.pack(anchor=tk.W)
    
    def create_login_form(self):
        # Create a container for centered content
        form_container = tk.Frame(self.right_panel, bg="#ffffff")
        form_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.8)
        
        # Welcome text
        welcome_label = tk.Label(
            form_container, 
            text="Welcome Back", 
            font=self.heading_font, 
            fg="#333333", 
            bg="#ffffff"
        )
        welcome_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Subtitle
        subtitle_label = tk.Label(
            form_container, 
            text="Sign in to continue to Voice Translator", 
            font=self.label_font, 
            fg="#666666", 
            bg="#ffffff"
        )
        subtitle_label.pack(anchor=tk.W, pady=(0, 30))
        
        # Username/Email field
        username_label = tk.Label(
            form_container, 
            text="Username or Email", 
            font=self.label_font, 
            bg="#ffffff", 
            fg="#333333",
            anchor="w"
        )
        username_label.pack(fill="x", pady=(0, 5))
        
        # Create a frame for the input with bottom border only
        username_frame = tk.Frame(form_container, bg="#ffffff")
        username_frame.pack(fill="x", pady=(0, 20))
        
        self.username_entry = tk.Entry(
            username_frame, 
            font=self.text_font, 
            bg="#ffffff", 
            fg="#333333",
            bd=0,  # No border
            highlightthickness=0  # No highlight
        )
        self.username_entry.pack(fill="x", ipady=8, side=tk.TOP)
        
        # Add a separator line below the entry
        username_separator = tk.Frame(username_frame, height=2, bg="#e0e0e0")
        username_separator.pack(fill="x", side=tk.TOP)
        
        # Password field
        password_label = tk.Label(
            form_container, 
            text="Password", 
            font=self.label_font, 
            bg="#ffffff", 
            fg="#333333",
            anchor="w"
        )
        password_label.pack(fill="x", pady=(0, 5))
        
        # Create a frame for the input with bottom border only
        password_frame = tk.Frame(form_container, bg="#ffffff")
        password_frame.pack(fill="x", pady=(0, 5))
        
        self.password_entry = tk.Entry(
            password_frame, 
            font=self.text_font, 
            bg="#ffffff", 
            fg="#333333",
            bd=0,  # No border
            highlightthickness=0,  # No highlight
            show="•"  # Show dots instead of actual password
        )
        self.password_entry.pack(fill="x", ipady=8, side=tk.TOP)
        
        # Add a separator line below the entry
        password_separator = tk.Frame(password_frame, height=2, bg="#e0e0e0")
        password_separator.pack(fill="x", side=tk.TOP)
        
        # Error message placeholder (hidden by default)
        self.error_label = tk.Label(
            form_container, 
            text="", 
            font=self.small_font, 
            bg="#ffffff", 
            fg="#e74c3c",  # Red color for error
            anchor="w"
        )
        self.error_label.pack(fill="x", pady=(5, 0))
        
        # Remember me and forgot password in the same row
        options_frame = tk.Frame(form_container, bg="#ffffff")
        options_frame.pack(fill="x", pady=(10, 20))
        
        # Remember me checkbox
        self.remember_var = tk.BooleanVar()
        remember_check = tk.Checkbutton(
            options_frame, 
            text="Remember me", 
            variable=self.remember_var,
            font=self.small_font,
            bg="#ffffff",
            fg="#666666",
            activebackground="#ffffff",
            selectcolor="#ffffff"
        )
        remember_check.pack(side=tk.LEFT)
        
        # Forgot password link
        forgot_password = tk.Label(
            options_frame, 
            text="Forgot password?", 
            font=self.small_font, 
            bg="#ffffff", 
            fg="#3a7ebf",
            cursor="hand2"
        )
        forgot_password.pack(side=tk.RIGHT)
        forgot_password.bind("<Button-1>", self.forgot_password)
        
        # Login button with hover effect
        self.login_button = tk.Button(
            form_container, 
            text="Sign In", 
            font=self.button_font, 
            bg="#3a7ebf", 
            fg="white",
            activebackground="#2a5d8f",
            activeforeground="white",
            relief=tk.FLAT,
            command=self.login,
            cursor="hand2",
            padx=10,
            pady=10
        )
        self.login_button.pack(fill="x", pady=(10, 20))
        
        # Bind hover events for button
        self.login_button.bind("<Enter>", self.on_enter)
        self.login_button.bind("<Leave>", self.on_leave)
        
        # Don't have an account section
        signup_frame = tk.Frame(form_container, bg="#ffffff")
        signup_frame.pack(pady=(20, 0))
        
        no_account_label = tk.Label(
            signup_frame, 
            text="Don't have an account? ", 
            font=self.small_font, 
            bg="#ffffff", 
            fg="#666666"
        )
        no_account_label.pack(side=tk.LEFT)
        
        signup_link = tk.Label(
            signup_frame, 
            text="Sign up", 
            font=self.small_font, 
            bg="#ffffff", 
            fg="#3a7ebf",
            cursor="hand2"
        )
        signup_link.pack(side=tk.LEFT)
        signup_link.bind("<Button-1>", self.signup)
    
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
        subprocess.Popen([sys.executable, 'main.py', '--no-login'])
    
    def forgot_password(self, event):
        messagebox.showinfo(
            "Forgot Password", 
            "Please contact the administrator to reset your password."
        )
    
    def signup(self, event):
        messagebox.showinfo(
            "Sign Up", 
            "This is a demo application. Please contact the administrator to create an account."
        )


# Function to start the login page
def start_login():
    login_root = tk.Tk()
    login_app = ModernLoginPage(login_root)
    login_root.mainloop()


# If this file is run directly, start the login page
if __name__ == "__main__":
    start_login()