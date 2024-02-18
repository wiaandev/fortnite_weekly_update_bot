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
    await ctx.send("https://tenor.com/view/fortnite-wave-hi-hello-gif-13632843")
    
@client.event
async def on_member_join(member):
    channel = client.get_channel(1040667357045063805)
    await channel.send(f"Look who joined guys, it's @{member}. Another fucking faggot. I hope you are ready for some foooortniiite")
    
@client.event
async def on_member_remove(member):
    channel = client.get_channel(1040667357045063805)
    await channel.send("https://tenor.com/view/fortnite-emote-waving-good-bye-sig-fortnite-gif-12033393698545252797")
    await channel.send(f"Goodbye {member}. See you on the flipside")
    
client.run(config.DISCORD_TOKEN)
