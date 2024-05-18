import pyautogui

def clickEffect(effectName, directory, gamename, effectQuantity, customConfidence, direction):

    # Fill deactivatedEffects with the names of the images that have been banned to help the bot flow smoothly!
    deactivatedEffects = ["ohko.PNG"]
    if deactivatedEffects.__contains__(effectName):
        print("That effect has been deactivated!")
        return

    pyautogui.PAUSE = 0.6

    focusLocation = pyautogui.locateOnScreen("LaptopWebsiteIcons\\ccicon.PNG")
    pyautogui.moveTo(focusLocation)
    currentPos = pyautogui.position()
    pyautogui.moveTo(currentPos.x - 45, None)
    pyautogui.click()
    pyautogui.moveTo(None, currentPos.y + 300)

    # the amount of times the program will attempt to find the image before quitting
    # it will scroll down for the first half of attempts, then scroll down for the second half
    attemptLimit = 40

    finalString = directory + "\\" + gamename + "\\" + effectName

    attemptCount = 0
    modifier = 1

    if direction == "down":
        modifier = 1
    else:
        modifier = -1

    while True:
        try:
            effectLocation = pyautogui.locateOnScreen(finalString, confidence=customConfidence)
            break
        except pyautogui.ImageNotFoundException:
            if attemptCount < attemptLimit / 2:
                pyautogui.scroll(-400 * modifier)
            else:
                pyautogui.scroll(400 * modifier)

        attemptCount += 1

        if attemptCount > attemptLimit:
            print("Sorry, the CC bot had an issue finding which effect to activate.")
            return

    pyautogui.click(effectLocation)

    #make sure that the order button isn't cut off at the bottom
    try:
        orderLocation = pyautogui.locateOnScreen(directory + "\\Order Button.PNG", confidence=0.9)
    except pyautogui.ImageNotFoundException:
        pyautogui.scroll(-200)
        orderLocation = pyautogui.locateOnScreen(directory + "\\Order Button.PNG", confidence=0.9)

    while effectQuantity > 0:
        pyautogui.click(orderLocation)
        effectQuantity -= 1

    # Close the effect window back up to not confuse the bot the next time
    currentPos = pyautogui.position()
    pyautogui.moveTo(None, currentPos.y - 80)
    pyautogui.click()

    pyautogui.moveTo(1, 1)
