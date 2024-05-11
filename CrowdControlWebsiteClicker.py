import pyautogui

# TODO: separate icons by games to make the list of images more organized

def clickEffect(effectName, effectQuantity):
    pyautogui.PAUSE = 1.0

    focusLocation = pyautogui.locateOnScreen("WebsiteIcons\\ccicon.png")
    pyautogui.moveTo(focusLocation)
    currentPos = pyautogui.position()
    pyautogui.moveTo(currentPos.x + 300, None)
    pyautogui.click()
    pyautogui.moveTo(None, currentPos.y + 300)

    #the amount of times the program will attempt to find the image before quitting
    #it will scroll down for the first half of attempts, then scroll down for the second half
    attemptLimit = 10

    finalString = "WebsiteIcons\\ALTTP\\" + effectName + ".png"
    print(finalString)

    attemptCount = 0

    while True:
        try:
            effectLocation = pyautogui.locateOnScreen(finalString, confidence=0.9)
            break
        except pyautogui.ImageNotFoundException:
            print("couldn't find image, scrolling")
            if attemptCount < attemptLimit / 2:
                pyautogui.scroll(-300)
            else:
                pyautogui.scroll(300)

        attemptCount += 1
        print("Currently on attempt #" + str(attemptCount))

        if attemptCount > attemptLimit:
            print("Sorry, the CC bot had an issue finding which effect to activate.")
            return

    pyautogui.click(effectLocation)

    orderLocation = pyautogui.locateOnScreen("WebsiteIcons\\Order Button.PNG", confidence=0.9)
    while effectQuantity > 0:
        pyautogui.click(orderLocation)
        effectQuantity -= 1

    # Close the effect window back up to not confuse the bot the next time
    currentPos = pyautogui.position()
    pyautogui.moveTo(None, currentPos.y - 80)
    pyautogui.click()

    pyautogui.moveTo(0, 0)


clickEffect("invert d-pad", 1)
