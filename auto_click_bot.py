# © NTM Coporation Pvt.Ltd
import pyautogui
import cv2
import numpy as np
import time

# Disable the PyAutoGUI fail-safe feature
pyautogui.FAILSAFE = False

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
        button_width, button_height = pyautogui.size()  # This is incorrect. Adjust as follows:
        button_width, button_height = 50, 50  # Assume button size, you should replace this with actual button dimensions if known
        pyautogui.click(x + button_width // 2, y + button_height // 2)

# Main loop
button_image = 'ntm.png' # change the image name here
while True:
    click_button(button_image)
    time.sleep(3)  # Wait for the button to change its position
