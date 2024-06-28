import pyautogui
import cv2
import numpy as np
import time
import threading
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# Disable the PyAutoGUI fail-safe feature
pyautogui.FAILSAFE = False

# Global variable to control the running state of the bot
running = False

def find_button(image_path):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(image_path)
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_loc if max_val > 0.8 else None  # Adjust threshold as needed

def click_button(image_path):
    position = find_button(image_path)
    if position:
        x, y = position
        button_width, button_height = 50, 50  # Assume button size, replace with actual dimensions if known
        pyautogui.click(x + button_width // 2, y + button_height // 2)

def start_clicking():
    global running
    running = True
    button_image = 'ntm3.png' # change the image name here
    while running:
        click_button(button_image)
        time.sleep(3)  # Wait for the button to change its position

def stop_clicking():
    global running
    running = False

def start_thread():
    clicking_thread = threading.Thread(target=start_clicking)
    clicking_thread.start()

# Create the UI
root = ThemedTk(theme="arc")
root.title("Auto Clicker Bot")

# Configure the grid layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

title_label = ttk.Label(frame, text="Auto Clicker Bot", font=("Helvetica", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

start_button = ttk.Button(frame, text="Start", command=start_thread, style="Accent.TButton")
start_button.grid(row=1, column=0, padx=10, pady=10)

stop_button = ttk.Button(frame, text="Stop", command=stop_clicking, style="Accent.TButton")
stop_button.grid(row=1, column=1, padx=10, pady=10)

# Apply styles
style = ttk.Style()
style.configure("Accent.TButton", font=("Helvetica", 14), padding=10)

# Run the application
root.mainloop()
