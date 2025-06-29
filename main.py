import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class RustBot(commands.Bot):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)
    
    async def on_ready(self):
        print(f'Rust bot online as {self.user}!')

bot = RustBot()

@bot.command()
async def serverstatus(ctx, *, server_ip):
    await ctx.send(f"Checking {server_ip}...")

bot.run(TOKEN)