from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
import voteCounter
import asyncio
import config

APP_ID = config.app_id
APP_SECRET = config.app_secret
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = config.channel_name

async def on_ready(ready_event: EventData):
    # initialize the twitch instance, this will by default also create a app authentication for you
    await ready_event.chat.join_room(TARGET_CHANNEL)

async def on_message(msg:ChatMessage):
    print(f'in {msg.room.name}, {msg.user.name} said: {msg.text}')
    if msg.text == '1' or '2':


# this will be called whenever the !reply command is issued
async def test_command(cmd: ChatCommand):
    if len(cmd.parameter) == 0:
        await cmd.reply('you did not tell me what to reply with')
    else:
        await cmd.reply(f'{cmd.user.name}: {cmd.parameter}')

async def run():
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    chat = await Chat(twitch)

    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)

    chat.register_command('reply', test_command)

    chat.start()

    try:
        input('Press ENTER to stop!\n')
    finally:
        chat.stop()
        await twitch.close()

# run this example
asyncio.run(run())
