import pyautogui
import time
import random
#pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.
pyautogui.FAILSAFE = False
screenWidth, screenHeight = pyautogui.size()
print(pyautogui.size())
prevMouseX, prevMouseY = pyautogui.position()
while True:
    # Starting from 10 to aviod a moving corner failure reported by pyautogui
    for x in range(10,screenWidth):
        for y in range(10,screenHeight):
            # Check the position of the previous Mouse with the current Mouse
            # If not the same then it means user are moving, pause the auto move 
            curMouseX, curMouseY = pyautogui.position()
            print(curMouseX, curMouseY, prevMouseX, prevMouseY, x, y)
            if prevMouseX == curMouseX and prevMouseY == curMouseY:
                print("The User is not using mouse")
                #pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInOutQuad)
                #prevMouseX, prevMouseY = x, y
                # Set to random because 
                ranX, ranY = random.randint(10,screenWidth), random.randint(1,screenHeight)
                pyautogui.moveTo(ranX, ranY, duration=1, tween=pyautogui.easeInOutQuad)
                # Set the pre Mouse position to where it's now moved to
                prevMouseX, prevMouseY = ranX, ranY 
            else:
                print("The User is using mouse")
                prevMouseX, prevMouseY = curMouseX, curMouseY
            time.sleep(60)
