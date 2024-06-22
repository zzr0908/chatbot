import asyncio, os
from wechaty import Wechaty


class MyBot(Wechaty):
    async def on_message(self, msg):
        from_contact = msg.talker()
        text = msg.text()
        room = msg.room()
        if text == 'ding':
            conversation = from_contact if room is None else room
            await conversation.ready()
            await conversation.say('dong')


os.environ['TOKEN'] = "b750b55b-e5d7-4528-910e-40c97b70fe94"
bot = MyBot()
