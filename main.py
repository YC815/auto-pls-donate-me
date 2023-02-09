import pyautogui
import keyboard as k # pip install keyboard
import time
# say --> x: 0334 y: 0430 or 71 318
time.sleep(3)
while True:
    pyautogui.typewrite("/")
    pyautogui.keyDown("shiftleft")
    pyautogui.press("p")
    pyautogui.keyUp("shiftleft")
    pyautogui.typewrite("lease donate")
    k.press_and_release("enter")
    time.sleep(8)
    pyautogui.typewrite("/donate me to make me happy")
    k.press_and_release("enter")
    time.sleep(8)
    pyautogui.typewrite("/plsssssssss")
    k.press_and_release("enter")
    time.sleep(8)

