import pyautogui
import time
# say --> x: 0334 y: 0430
time.sleep(5)
pyautogui.moveTo(334, 430, duration = 1.5) 

while True:
    pyautogui.dragTo(334, 430, duration=0.2, button="left")
    pyautogui.keyDown("shiftleft")
    pyautogui.press("p")
    pyautogui.keyUp("shiftleft")
    pyautogui.typewrite("lease donate")
    pyautogui.press(["enter"])
    time.sleep(8)
    pyautogui.dragTo(334, 430, duration=0.2, button="left")
    pyautogui.press("d")
    pyautogui.press("o") 
    pyautogui.press("n")
    pyautogui.press("a")
    pyautogui.press("t")
    pyautogui.press("e")
    pyautogui.press("space")
    pyautogui.press("m")
    pyautogui.press("e")
    pyautogui.press("space")
    pyautogui.press("m")
    pyautogui.press("a")
    pyautogui.press("k")
    pyautogui.press("e")
    pyautogui.press("space")
    pyautogui.press("m")
    pyautogui.press("e")
    pyautogui.press("space")
    pyautogui.press("h")
    pyautogui.press("a")
    pyautogui.press("p")
    pyautogui.press("p")
    pyautogui.press("y")
    pyautogui.press(["enter"])
    time.sleep(8)
    pyautogui.dragTo(334, 430, duration=0.2, button="left")
    pyautogui.press("p")
    pyautogui.press("l")
    pyautogui.press("s")
    pyautogui.press("s")
    pyautogui.press("s")
    pyautogui.press("s")
    pyautogui.press("s")
    pyautogui.press("s")
    pyautogui.press("s")
    pyautogui.press("s")
    pyautogui.press(["enter"])
    time.sleep(8)
