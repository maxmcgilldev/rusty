import os 
from dotenv import load_dotenv
from discord import Intents, Client, Message
#from responses import get_response

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)