import random

from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
import voteCounter
import asyncio
import config
from CrowdControlWebsiteClicker import clickEffect

APP_ID = config.app_id
APP_SECRET = config.app_secret
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT, AuthScope.CHANNEL_MANAGE_POLLS, AuthScope.CHANNEL_READ_POLLS]
TARGET_CHANNEL = config.channel_name

VOTE_LENGTH = 60
TIME_BETWEEN_VOTES = 60

votedUsers = []


async def on_ready(ready_event: EventData):
    # initialize the twitch instance, this will by default also create a app authentication for you
    await ready_event.chat.join_room(TARGET_CHANNEL)

# Start and stop voting made into a seperate function to allow other programs to start the functions directly.


async def start_voting(twitch):
    voteOptions = voteCounter.createVote()
    pollTitle = "WHATS ABOUT TO HAPPEN TO STRIMMERMAN"
    pollOptions = []
    for option in voteOptions:
        pollOptions.append(voteOptions[option].name[:-4])
    response = await Twitch.create_poll(twitch, "1013090214", pollTitle, pollOptions, VOTE_LENGTH)

    # GET THE ID OF THE POLL JUST CREATED
    print(response.id)
    return response.id

async def stop_voting(twitch, pollId):
    # USE THE ID OF THE POLL TO GET THE RESULT AND MAKE THINGS HAPPEN
    generator = Twitch.get_polls(twitch, "1013090214", pollId)

    winningVoteCount = 0
    currentWinners = []

    # should only be one result but the interable is there because generators
    async for result in generator:
        allChoices = result.choices
        for choice in allChoices:
            if choice.votes == winningVoteCount:
                currentWinners.append(choice.title)
            elif choice.votes > winningVoteCount:
                currentWinners = [choice.title]

    return currentWinners[random.randint(0, len(currentWinners) - 1)]

async def run():
    global votedUsers
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    chat = await Chat(twitch)

    chat.register_event(ChatEvent.READY, on_ready)

    chat.start()

    await asyncio.sleep(5)

    try:
        while True:
            pollId = await start_voting(twitch)
            await asyncio.sleep(VOTE_LENGTH + 3)

            winnerEffect = await stop_voting(twitch, pollId)
            winnerEffect = winnerEffect + ".PNG"
            print(winnerEffect)

            customConf = 0.95

            clickEffect(winnerEffect, "LaptopWebsiteIcons", "Peggle", 1, customConf, "down")
            votedUsers = []

            await asyncio.sleep(TIME_BETWEEN_VOTES)

    finally:
        chat.stop()
        await twitch.close()

# run this example
asyncio.run(run())
