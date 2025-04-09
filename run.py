#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Voice Translator Application Launcher

This script serves as the entry point for the Voice Translator application.
It starts with the login page and then launches the main application after successful login.
"""

import sys
import subprocess

# Start the application with the login page
if __name__ == "__main__":
    # Launch the modern login page
    subprocess.Popen([sys.executable, 'modern_login.py'])