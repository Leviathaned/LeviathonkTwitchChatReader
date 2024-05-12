from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
import voteCounter
import asyncio
import config
import socketServer

APP_ID = config.app_id
APP_SECRET = config.app_secret
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = config.channel_name

votedUsers = []
currentlyVoting = False

async def on_ready(ready_event: EventData):
    # initialize the twitch instance, this will by default also create a app authentication for you
    await ready_event.chat.join_room(TARGET_CHANNEL)
    # start up socket server
    socketServer.start()

async def on_message(msg:ChatMessage):
    if (msg.text == '1' or '2') and currentlyVoting and not any(x == msg.user.id for x in votedUsers):
        voteCounter.takeVote(msg.text)
        votedUsers.append(msg.user.id)

# Start and stop voting made into a seperate function to allow other programs to start the functions directly.

#
async def start_voting(chat):
    global currentlyVoting
    voteOptions = voteCounter.createVote()
    preparedMessage = "Vote has begun! Type the number of the option you'd like to vote for:\n"
    counter = 1
    for option in voteOptions:
        preparedMessage += str(counter) + ") " + voteOptions[option].name + "\n"
        counter += 1
    await chat.send_message(TARGET_CHANNEL, preparedMessage)
    currentlyVoting = True

async def stop_voting(chat):
    global currentlyVoting
    winner, voteCount = voteCounter.finalizeVote()
    preparedMessage = f"The vote has ended! The winner is {winner} with {voteCount} votes!"
    await chat.send_message(TARGET_CHANNEL, preparedMessage)
    currentlyVoting = False

async def run():
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    chat = await Chat(twitch)

    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)

    chat.start()

    try:
        while True:
            inputSelection = input('Enter 1 to create a vote, 2 to stop the vote, and 3 to shut down the program.\n')

            if inputSelection == '1':
                await start_voting(chat)

            if inputSelection == '2':
                await stop_voting(chat)

            if inputSelection == '3':
                break
    finally:
        chat.stop()
        await twitch.close()

# run this example
asyncio.run(run())
