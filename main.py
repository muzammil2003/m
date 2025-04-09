import os
import threading
import tkinter as tk
from gtts import gTTS
from tkinter import ttk, font
import speech_recognition as sr
from playsound import playsound
from deep_translator import GoogleTranslator
from google.transliteration import transliterate_text
from database import Database  # Add this import


# Create an instance of Tkinter frame or window
win = tk.Tk()

# Initialize database
db = Database()  # Add this line

# Set the geometry of tkinter frame
win.geometry("800x650")
win.title("Real-Time Voice🎙️ Translator🔊")
icon = tk.PhotoImage(file="icon.png")
win.iconphoto(False, icon)

# Set a gradient background color
win.configure(bg="#f0f5ff")  # Light blue background

# Configure custom fonts
title_font = font.Font(family="Helvetica", size=14, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
text_font = font.Font(family="Georgia", size=11)
button_font = font.Font(family="Helvetica", size=10, weight="bold")

# Create a title frame with a different background
title_frame = tk.Frame(win, bg="#3a7ebf", pady=10)
title_frame.pack(fill=tk.X)

# Add a title label
title_label = tk.Label(
    title_frame, 
    text="Real-Time Voice Translator", 
    font=("Helvetica", 18, "bold"), 
    fg="white", 
    bg="#3a7ebf"
)
title_label.pack(pady=5)

# Create a main content frame
content_frame = tk.Frame(win, bg="#f0f5ff", padx=20, pady=10)
content_frame.pack(fill=tk.BOTH, expand=True)

# Create a container frame for text boxes
text_container = tk.Frame(content_frame, bg="#f0f5ff")
text_container.pack(fill=tk.BOTH, expand=True, anchor=tk.CENTER)

# Create labels and text boxes for the recognized and translated text
input_frame = tk.Frame(text_container, bg="#f0f5ff")
input_frame.pack(side=tk.LEFT, expand=True, padx=10, pady=10, anchor=tk.CENTER)

input_label = tk.Label(
    input_frame, 
    text="Recognized Text ⮯", 
    font=label_font, 
    bg="#f0f5ff", 
    fg="#3a7ebf"
)
input_label.pack(pady=(0, 5), anchor=tk.CENTER)

# Create a frame to hold the text widget and scrollbar with enhanced styling
input_text_frame = tk.Frame(input_frame, bg="#ffffff", bd=2, relief=tk.GROOVE, highlightthickness=1, highlightbackground="#3a7ebf")
input_text_frame.pack(expand=True, fill=tk.BOTH)

# Add vertical scrollbar with improved style
input_scrollbar_y = ttk.Scrollbar(input_text_frame, orient=tk.VERTICAL, style="Custom.Vertical.TScrollbar")
input_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)

# Larger text box with vertical scrollbar only
input_text = tk.Text(
    input_text_frame, 
    height=20,  # Increased height
    width=55,   # Increased width
    font=text_font,
    bg="#ffffff",
    fg="#333333",
    wrap=tk.WORD,  # Word wrap enabled, no horizontal scrolling
    yscrollcommand=input_scrollbar_y.set
)
input_text.pack(expand=True, fill=tk.BOTH)

# Connect scrollbar to the text widget
input_scrollbar_y.config(command=input_text.yview)

output_frame = tk.Frame(text_container, bg="#f0f5ff")
output_frame.pack(side=tk.RIGHT, expand=True, padx=10, pady=10, anchor=tk.CENTER)

output_label = tk.Label(
    output_frame, 
    text="Translated Text ⮯", 
    font=label_font, 
    bg="#f0f5ff", 
    fg="#3a7ebf"
)
output_label.pack(pady=(0, 5), anchor=tk.CENTER)

# Create a frame to hold the text widget and scrollbar with enhanced styling
output_text_frame = tk.Frame(output_frame, bg="#ffffff", bd=2, relief=tk.GROOVE, highlightthickness=1, highlightbackground="#3a7ebf")
output_text_frame.pack(expand=True, fill=tk.BOTH)

# Add vertical scrollbar with improved style
output_scrollbar_y = ttk.Scrollbar(output_text_frame, orient=tk.VERTICAL, style="Custom.Vertical.TScrollbar")
output_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)

# Larger text box with vertical scrollbar only
output_text = tk.Text(
    output_text_frame, 
    height=20,  # Increased height
    width=55,   # Increased width
    font=text_font,
    bg="#ffffff",
    fg="#333333",
    wrap=tk.WORD,  # Word wrap enabled, no horizontal scrolling
    yscrollcommand=output_scrollbar_y.set
)
output_text.pack(expand=True, fill=tk.BOTH)

# Connect scrollbar to the text widget
output_scrollbar_y.config(command=output_text.yview)

# Create a dictionary of language names and codes
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Spanish": "es",
    "Chinese (Simplified)": "zh-CN",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "German": "de",
    "French": "fr",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Punjabi": "pa"
}

language_names = list(language_codes.keys())

# Style the combobox and scrollbar
style = ttk.Style()
style.configure("TCombobox", 
                fieldbackground="#e8f0ff", 
                background="#ffffff",
                foreground="#333333")

# Configure scrollbar style with more advanced customization
style.configure("Custom.Vertical.TScrollbar", 
                background="#3a7ebf",
                troughcolor="#e8f0ff",
                relief="flat",
                thickness=16,
                arrowsize=0)  # Remove arrow buttons

# Create a custom element layout that removes the arrow buttons
style.layout('Custom.Vertical.TScrollbar', 
             [('Vertical.Scrollbar.trough',
               {'children': [('Vertical.Scrollbar.thumb', 
                             {'expand': '1', 'sticky': 'nswe'})],
                'sticky': 'ns'})])

# Map different states for the scrollbar thumb
style.map("Custom.Vertical.TScrollbar",
         background=[('pressed', '#2a5d8f'), ('active', '#5294d4'), ('!active', '#3a7ebf')])

# Create dropdown menus for the input and output languages
lang_frame = tk.Frame(content_frame, bg="#e8f0ff", padx=10, pady=15, bd=2, relief=tk.GROOVE)
lang_frame.pack(fill=tk.X, pady=10)

# Use a container frame to center the language selection elements
lang_container = tk.Frame(lang_frame, bg="#e8f0ff")
lang_container.pack(anchor=tk.CENTER, expand=True)

input_lang_frame = tk.Frame(lang_container, bg="#e8f0ff")
input_lang_frame.pack(side=tk.LEFT, padx=20)

input_lang_label = tk.Label(
    input_lang_frame, 
    text="Select Input Language:", 
    font=label_font, 
    bg="#e8f0ff", 
    fg="#333333"
)
input_lang_label.pack(pady=(0, 5))

input_lang = ttk.Combobox(input_lang_frame, values=language_names, width=20, font=("Helvetica", 10))
def update_input_lang_code(event):
    selected_language_name = event.widget.get()
    selected_language_code = language_codes[selected_language_name]
    # Update the selected language code
    input_lang.set(selected_language_code)
input_lang.bind("<<ComboboxSelected>>", lambda e: update_input_lang_code(e))
if input_lang.get() == "": input_lang.set("auto")
input_lang.pack(pady=5)

# Create a more stylish arrow with a circular background
arrow_frame = tk.Frame(lang_container, bg="#e8f0ff", padx=15)
arrow_frame.pack(side=tk.LEFT)

# Create a canvas for the circular arrow button with extra space for shadow
arrow_canvas = tk.Canvas(arrow_frame, width=44, height=44, bg="#e8f0ff", highlightthickness=0)
arrow_canvas.pack()

# Add a subtle shadow effect
shadow = arrow_canvas.create_oval(4, 4, 42, 42, fill="#cccccc", outline="")

# Draw a blue circle on the canvas
circle = arrow_canvas.create_oval(2, 2, 40, 40, fill="#3a7ebf", outline="")

# Add the arrow symbol on top of the canvas
arrow = arrow_canvas.create_text(21, 21, text="➡", font=("Arial", 16, "bold"), fill="white")

# Add hover effect with animation
def on_enter(e):
    arrow_canvas.itemconfig(circle, fill="#5294d4")
    # Make the arrow slightly larger on hover
    arrow_canvas.itemconfig(arrow, font=("Arial", 18, "bold"))

def on_leave(e):
    arrow_canvas.itemconfig(circle, fill="#3a7ebf")
    # Return arrow to original size
    arrow_canvas.itemconfig(arrow, font=("Arial", 16, "bold"))

# Add click effect
def on_click(e):
    arrow_canvas.itemconfig(circle, fill="#2a5d8f")
    # Schedule return to hover state after 150ms
    arrow_canvas.after(150, lambda: arrow_canvas.itemconfig(circle, fill="#5294d4"))

arrow_canvas.bind("<Enter>", on_enter)
arrow_canvas.bind("<Leave>", on_leave)
arrow_canvas.bind("<Button-1>", on_click)

output_lang_frame = tk.Frame(lang_container, bg="#e8f0ff")
output_lang_frame.pack(side=tk.LEFT, padx=20)

output_lang_label = tk.Label(
    output_lang_frame, 
    text="Select Output Language:", 
    font=label_font, 
    bg="#e8f0ff", 
    fg="#333333"
)
output_lang_label.pack(pady=(0, 5))

output_lang = ttk.Combobox(output_lang_frame, values=language_names, width=20, font=("Helvetica", 10))
def update_output_lang_code(event):
    selected_language_name = event.widget.get()
    selected_language_code = language_codes[selected_language_name]
    # Update the selected language code
    output_lang.set(selected_language_code)
output_lang.bind("<<ComboboxSelected>>", lambda e: update_output_lang_code(e))
if output_lang.get() == "": output_lang.set("en")
output_lang.pack(pady=5)

keep_running = False

def update_translation():
    global keep_running

    if keep_running:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak Now!\n")
            audio = r.listen(source)
            
            try:
                speech_text = r.recognize_google(audio)
                speech_text_transliteration = transliterate_text(speech_text, lang_code=input_lang.get()) if input_lang.get() not in ('auto', 'en') else speech_text
                input_text.insert(tk.END, f"{speech_text_transliteration}\n")
                input_text.see(tk.END)
                if speech_text.lower() in {'exit', 'stop'}:
                    keep_running = False
                    return
                
                translated_text = GoogleTranslator(source=input_lang.get(), target=output_lang.get()).translate(text=speech_text_transliteration)

                # Save translation to database
                db.save_translation(
                    speech_text_transliteration,
                    translated_text,
                    input_lang.get(),
                    output_lang.get()
                )

                voice = gTTS(translated_text, lang=output_lang.get())
                voice.save('voice.mp3')
                playsound('voice.mp3')
                os.remove('voice.mp3')

                output_text.insert(tk.END, translated_text + "\n")
                output_text.see(tk.END)
                
            except sr.UnknownValueError:
                output_text.insert(tk.END, "Could not understand!\n")
                output_text.see(tk.END)
            except sr.RequestError:
                output_text.insert(tk.END, "Could not request from Google!\n")
                output_text.see(tk.END)

    win.after(100, update_translation)

def load_user_preferences():
    """Load user preferences from database"""
    preferences = db.get_user_preferences()
    if preferences:
        source_lang, target_lang, theme = preferences
        input_lang.set(source_lang)
        output_lang.set(target_lang)
        # You can add theme handling here if needed

def save_user_preferences():
    """Save current user preferences to database"""
    db.update_user_preferences(
        source_lang=input_lang.get(),
        target_lang=output_lang.get()
    )

# Add these lines after creating the language selection comboboxes
input_lang.bind("<<ComboboxSelected>>", lambda e: save_user_preferences())
output_lang.bind("<<ComboboxSelected>>", lambda e: save_user_preferences())

# Load preferences when the application starts
load_user_preferences()

def run_translator():
    global keep_running
    
    if not keep_running:
        keep_running = True
        # Visual feedback - change button color when active
        run_button.configure(bg="#2E7D32")
        update_translation_thread = threading.Thread(target=update_translation)  # using multi threading for efficient cpu usage
        update_translation_thread.start()

def kill_execution():
    global keep_running
    keep_running = False
    # Reset button color
    run_button.configure(bg="#4CAF50")

def open_about_page():
    about_window = tk.Toplevel()
    about_window.title("About")
    about_window.geometry("500x350")
    about_window.configure(bg="#f0f5ff")
    about_window.iconphoto(False, icon)

    # Add translation history section
    history_frame = tk.Frame(about_window, bg="#f0f5ff", padx=20, pady=10)
    history_frame.pack(fill=tk.BOTH, expand=True)

    history_label = tk.Label(
        history_frame,
        text="Recent Translation History",
        font=("Helvetica", 12, "bold"),
        bg="#f0f5ff",
        fg="#333333"
    )
    history_label.pack(pady=5)

    # Create a text widget for history
    history_text = tk.Text(
        history_frame,
        height=8,
        width=50,
        font=("Georgia", 10),
        bg="#ffffff",
        fg="#333333",
        bd=2,
        relief=tk.GROOVE
    )
    history_text.pack(pady=5, fill=tk.BOTH, expand=True)

    # Load and display translation history
    history = db.get_translation_history(limit=10)
    for entry in history:
        source_text, translated_text, source_lang, target_lang, timestamp = entry
        history_text.insert(tk.END, f"From: {source_text}\n")
        history_text.insert(tk.END, f"To: {translated_text}\n")
        history_text.insert(tk.END, f"Languages: {source_lang} → {target_lang}\n")
        history_text.insert(tk.END, f"Time: {timestamp}\n")
        history_text.insert(tk.END, "-" * 50 + "\n")

    history_text.config(state=tk.DISABLED)  # Make text read-only

    # Add clear history button
    def clear_history():
        db.clear_translation_history()
        history_text.config(state=tk.NORMAL)
        history_text.delete(1.0, tk.END)
        history_text.config(state=tk.DISABLED)

    clear_button = tk.Button(
        history_frame,
        text="Clear History",
        command=clear_history,
        width=15,
        font=button_font,
        bg="#F44336",
        fg="white",
        relief=tk.RAISED
    )
    clear_button.pack(pady=10)

    # Create a "Close" button
    close_button = tk.Button(
        history_frame,
        text="Close",
        command=about_window.destroy,
        width=15,
        font=button_font,
        bg="#3a7ebf",
        fg="white",
        relief=tk.RAISED
    )
    close_button.pack(pady=10)

def open_webpage(url):      # Opens a web page in the user's default web browser.
    import webbrowser
    webbrowser.open(url)

# Create a frame for buttons with a different background
button_frame = tk.Frame(content_frame, bg="#e8f0ff", pady=15, padx=10, bd=2, relief=tk.GROOVE)
button_frame.pack(fill=tk.X, pady=10)

# Container to center the buttons
button_container = tk.Frame(button_frame, bg="#e8f0ff")
button_container.pack(anchor=tk.CENTER, expand=True)

# Create the "Run" button
run_button = tk.Button(
    button_container, 
    text="Start Translation", 
    command=run_translator, 
    width=15, 
    height=2, 
    bg="#4CAF50", 
    fg="white", 
    font=button_font,
    cursor="hand2",
    relief=tk.RAISED
)
run_button.pack(side=tk.LEFT, padx=20)

# Create the "Kill" button
kill_button = tk.Button(
    button_container, 
    text="Stop Translation", 
    command=kill_execution, 
    width=15, 
    height=2, 
    bg="#F44336", 
    fg="white", 
    font=button_font,
    cursor="hand2",
    relief=tk.RAISED
)
kill_button.pack(side=tk.LEFT, padx=20)

# Open about page button
about_button = tk.Button(
    button_container, 
    text="About this project", 
    command=open_about_page, 
    width=15, 
    height=2, 
    font=button_font,
    bg="#3a7ebf",
    fg="white",
    cursor="hand2",
    relief=tk.RAISED
)
about_button.pack(side=tk.LEFT, padx=20)

# Add a status bar at the bottom
status_frame = tk.Frame(win, bg="#e0e0e0", height=25)
status_frame.pack(side=tk.BOTTOM, fill=tk.X)
status_label = tk.Label(status_frame, text="Ready", bg="#e0e0e0", fg="#555555")
status_label.pack(anchor=tk.CENTER)

# Run the Tkinter event loop
if __name__ == "__main__":
    # Check if we should show the login page first
    import sys
    if '--no-login' not in sys.argv:
        # Start the login page in a separate process to avoid circular imports
        import subprocess
        subprocess.Popen([sys.executable, 'modern_login.py'])
        sys.exit(0)  # Exit this process
    else:
        # Run the main application directly
        win.mainloop()