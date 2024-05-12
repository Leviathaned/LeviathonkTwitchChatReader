import random

import CrowdControlWebsiteClicker
import time

effectList = ["activate flute", "add arrows", "add bombs", "add rupees", "bee", "blue potion refill", "buff armor",
              "buff magic", "buff sword", "bug net", "cane of byrna", "cucco attack", "deactivate flute", "debuff armor",
              "debuff sword", "fairy", "fairy bottle", "gold bee", "green potion refill", "half magic", "heart", "heart container",
              "heart piece", "ice physics", "infinite arrows", "infinite bombs", "infinite magic", "invert buttons",
              "invert buttons and d-pad", "invert d-pad", "kill player", "large magic", "one hit ko", "quarter magic",
              "red potion refill", "remove arrows", "remove bombs", "remove heart container", "remove rupees",
              "restore health and magic", "silver arrows", "small magic", "swap buttons and d-pad", "upgrade shield",
              "upgrade sword"]

while True:
    customConf = 0.95

    nextEffect = random.randint(0, len(effectList) - 1)
    print(effectList[nextEffect])

    # special exceptions for difficult to detect cases, ALTTP only
    if effectList[nextEffect] == "deactivate flute":
        customConf = 0.7
    elif effectList[nextEffect] == "green potion refill" or "blue potion refill":
        customConf = 0.97

    CrowdControlWebsiteClicker.clickEffect(effectList[nextEffect], 1, customConf)
    # gets rid of the most recently used effect to best test all effects
    effectList.pop(nextEffect)

    time.sleep(2)

    print(str(len(effectList)) + " effects remaining!")

    if len(effectList) == 0:
        print("All effects have been tested!")
        break
