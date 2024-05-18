from CrowdControlWebsiteClicker import clickEffect
import random
import time
from os import listdir

# The current game variable should match the folder of the game you wish to pull from
currentGame = "Peggle"
chosenEffects = "all"

effectList = [f for f in listdir("LaptopWebsiteIcons\\" + currentGame)]

# Lethal Company "positive" effects
if chosenEffects == "LCPositiveOnly":
    effectList = [
        "charge item battery.PNG",
        "complete quota.PNG",
        "extend deadline by one day.PNG",
        "fast player.PNG",
        "fill quota by 25.PNG",
        "fill quota by 50.PNG",
        "give boom box crewmate.PNG",
        "give boom box player.PNG",
        "give comedy mask crewmate.PNG",
        "give comedy mask player.PNG",
        "give extension ladder crewmate.PNG",
        "give extension ladder player.PNG",
        "give flashlight crewmate.PNG",
        "give flashlight player.PNG",
        "give inhaler crewmate.PNG",
        "give inhaler player.PNG",
        "give jet pack crewmate.PNG",
        "give jet pack player.PNG"
        "give pro flashlight crewmate.PNG",
        "give pro flashlight player.PNG",
        "give radar booster crewmate.PNG",
        "give radar booster player.PNG",
        "give shovel crewmate.PNG",
        "give shovel player.PNG",
        "give stun grenade crewmate.PNG",
        "give stun grenade player.PNG",
        "give stun gun crewmate.PNG",
        "give stun gun player.PNG",
        "give tragedy mask crewmate.PNG",
        "give tragedy mask player.PNG",
        "give walkie talkie crewmate.PNG",
        "give walkie talkie player.PNG",
        "heal crewmate.PNG",
        "heal player.PNG",
        "high jump.PNG",
        "hyper player.PNG",
        "infinite stamina.PNG",
        "invincible.PNG",
        "kill nearby enemies.PNG",
        "restore stamina.PNG",
        "rollback time one hour.PNG",
        "spawn scrap in level.PNG",
        "stock boom box.PNG",
        "stock extension ladder.PNG",
        "stock flashlight.PNG",
        "stock inhaler.PNG",
        "stock jet pack.PNG",
        "stock lockpicker.PNG",
        "stock pro flashlight.PNG",
        "stock radar booster.PNG",
        "stock shovel.PNG",
        "stock stun grenade.PNG",
        "stock stun gun.PNG",
        "stock walkie talkie.PNG",
        "turn breakers on.PNG",
        "ultra jump.PNG",
        "weather clear.PNG"
    ]

DEVICE = "Laptop"

lastEffect = ""

while True:
    customConf = 0.95

    nextEffect = random.randint(0, len(effectList) - 1)
    print(effectList[nextEffect])

    # special exceptions for difficult to detect cases

    if lastEffect < effectList[nextEffect]:
        direction = "down"
    else:
        direction = "up"

    lastEffect = effectList[nextEffect]

    clickEffect(effectList[nextEffect], "LaptopWebsiteIcons", currentGame, 1, customConf, direction)

    time.sleep(30)
