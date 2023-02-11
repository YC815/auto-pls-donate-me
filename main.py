import pyautogui
import time
# say --> x: 0334 y: 0430
time.sleep(5)
while True:
    pyautogui.dragTo(334, 430, duration=0.2, button="left")
    pyautogui.keyDown("shiftleft")
    pyautogui.press("p")
    pyautogui.keyUp("shiftleft")
    pyautogui.typewrite("lease donate")
    pyautogui.press(["enter"])
    pyautogui.press(["space"])
    pyautogui.dragTo(334, 430, duration=0.2, button="left")
    pyautogui.typewrite("/e dance2")
    pyautogui.press(["enter"]) 
    time.sleep(600)