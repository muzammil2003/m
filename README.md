# Real-Time Voice Translator

A Python application that translates voice from one language to another in real-time.

## Features

- Real-time voice translation
- Multiple language support
- Translation history
- User preferences saving
- Beautiful GUI interface

## Setup Instructions

1. Install Python 3.8 or higher
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python main.py
   ```

## Usage

1. Select input and output languages from the dropdown menus
2. Click "Start Translation" to begin
3. Speak into your microphone
4. The translation will appear in the output text box
5. Click "Stop Translation" to end

## Requirements

- Python 3.8+
- Microphone
- Internet connection (for translation services)

## Note

Make sure you have a working microphone connected to your system before running the application.

<div align="center">
<h1> LinguaSync: Real-Time Voice Translator </h1> <a href="#"><img alt="language" src="https://user-images.githubusercontent.com/132539454/278971782-9453805e-e2e6-4d99-b1de-cf8fcd3e7105.svg"></a>
</div>

Real-Time Voice Translator is a machine learning project that aims to provide a seamless and natural experience of cross-lingual communication. It uses deep neural networks to translate voice from one language to another in real time while preserving the tone and emotion of the speaker. It is a desktop application that supports Windows, Linux, and Mac operating systems.

The application is easy to use: simply select the languages you want to translate between and start speaking. The application will listen to your voice and provide instant translations in real-time. You can also use the application to translate conversations between two or more people.


### Dependencies
    <=Python3.11, gTTS, pyaudio, playsound==1.2.2, deep-translator, SpeechRecognition, google-transliteration-api, cx-Freeze
    
    Optional: Pillow - for enhanced image processing in the login page
    Note: If Pillow is not installed, the application will use built-in tkinter image handling or stub modules


### Getting started

1. Clone this project and create virtualenv (recommended) and activate virtualenv.
    ```
    # Create virtualenv
    python -m venv env
 
    # Linux/MacOS
    source env/bin/activate
    
    # Windows
    env\Scripts\activate
    ```
    
2. Install require dependencies.
    ```
    pip install --upgrade wheel
    
    pip install -r requirements.txt
    ```

3. Run code and speech (have fun).
    ```
    python run.py  # Starts with login page
    # OR
    python main.py --no-login  # Skip login page
    ```

### Program Flow:
<a href="#"><img src="https://github.com/SamirPaulb/real-time-voice-translator/assets/77569653/73dd62d6-798d-4129-aff3-16d6d932a817" alt="Block Diagram of Voice Translator"></a>


### Install Windows/Linux/Mac Application <a href="https://github.com/SamirPaulb/real-time-voice-translator/releases/latest"><img src="https://user-images.githubusercontent.com/132539454/278971282-8d676023-a03a-463c-8e55-3f0afe6e3e58.svg" alt="DOWNLOAD"></a>

I am using <a href="https://github.com/marcelotduarte/cx_Freeze/tree/main">cx_Freeze</a> to build executable file of this app. The build settings can be changed by modifying the <a href="https://github.com/SamirPaulb/real-time-voice-translator/blob/main/setup.py">setup.py</a> file.

##### Build installer containing all the files:
- Windows: ```python setup.py bdist_msi```
- Linux: ```python setup.py bdist_rpm```
- Mac: ```python setup.py bdist_mac```


### GUI 

#### Login Page
The application now features a modern login page with a clean and minimal design:
- Centered login form with rounded corners and subtle shadow
- Fields for username/email and password
- 'Login' button with hover effect
- 'Forgot password?' link
- Responsive layout for different screen sizes

#### Main Application
<a href="#"><img src="https://github.com/SamirPaulb/real-time-voice-translator/assets/77569653/f96a4115-a88f-4096-9a00-954b8527d872" alt="App GUI"></a>

