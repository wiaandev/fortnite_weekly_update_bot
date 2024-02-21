import discord
from discord.ext import commands
import config
import requests

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
    
@client.command()
async def jou_ma(ctx):
    await ctx.send("hello oom")
    
@client.event
async def on_member_join(member):
    channel = client.get_channel(1040667357045063805)
    await channel.send(f"Look who joined guys, it's @{member}. Another fucking faggot. I hope you are ready for some foooortniiite")
    
@client.event
async def on_member_remove(member):
    channel = client.get_channel(1040667357045063805)
    await channel.send("https://tenor.com/view/fortnite-emote-waving-good-bye-sig-fortnite-gif-12033393698545252797")
    await channel.send(f"Goodbye {member}. See you on the flipside")
    
@client.command()
async def get_stats(ctx, username):
    url = f"https://fortnite-api.com/v2/stats/br/v2?name={username}&accountType=epic&timeWindow=season&image=keyboardMouse"

    headers = {
        "Authorization": f"{config.FORTNITE_API_KEY}" 
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        # print(data)  # Print the data within the try block
        
        banner = data['data']['image']
        
        print(banner)

    except requests.exceptions.HTTPError as err:
        await ctx.send(f"An error occurred while fetching stats for {username}. Make sure the username is valid")
    except Exception as err:
        await ctx.send(f"Oops! Something went wrong: {err}")
        
    await ctx.send(banner)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("https://tenor.com/view/jonesy-fortnite-fortnite-jonesy-fortnite-john-jones-john-jones-gif-27246597")
        await ctx.send("**This command does not exist**, jou **DOM** etter!")
    else:
        raise error 
    
client.run(config.DISCORD_TOKEN)
