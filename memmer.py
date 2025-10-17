import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Your meme database
meme_database = {
    "slimer": [
        "https://media1.tenor.com/m/2W6tUygBb1gAAAAd/gunge-male.gif"
    ],
    "slime": [
        "https://media1.tenor.com/m/fwUh3G_4g3cAAAAd/slime-sliming.gif"
    ],
    "congrat": [
        "https://media1.tenor.com/m/VOUzW9uvebkAAAAd/dantdm-cbbc.gif"
    ],
    "more": [
        "https://media1.tenor.com/m/wshzHt1SerQAAAAd/elmo-slime-slime.gif"
    ],
    "yikes": [
        "https://media1.tenor.com/m/xmlrr-H-yGYAAAAd/yikes.gif"
    ],
    "no way": [
        "https://media1.tenor.com/m/we9F9lBaHKMAAAAd/whaaa-what.gif"
    ],
    "love you": [
        "https://media1.tenor.com/m/GnQIL9rSPWkAAAAC/castanholas.gif"
    ]
}

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    msg = message.content.lower()
    for trigger, gifs in meme_database.items():
        if trigger in msg:
            gif_url = random.choice(gifs)
            
            # Create embed with GIF
            embed = discord.Embed(color=0x00ff00)
            embed.set_image(url=gif_url)
            
            await message.channel.send(embed=embed)
            break

@bot.command()
async def test(ctx):
    await ctx.send("✅ Bot is working properly!")

# Get token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    print("Error: BOT_TOKEN not found in environment variables!")
else:
    bot.run(BOT_TOKEN)