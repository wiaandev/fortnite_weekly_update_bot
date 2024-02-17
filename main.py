import discord
from discord.ext import commands
import config

# Define your intents
intents = discord.Intents.all()

# Add intents that your bot needs
intents.members = True  # If you need to track member events

# Initialize your Bot instance with the intents
client = commands.Bot(command_prefix="$", intents=intents)

# Creating a client event
@client.event
async def on_ready():
    print("Bot is ready!")
    print("-------------------------------------")
    
@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am a Fornite Weekly Update bot")
    
client.run(config.DISCORD_TOKEN)