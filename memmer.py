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
        "https://media.tenor.com/2W6tUygBb1gAAAAC/gunge-male.gif"
    ],
    "slime": [
        "https://media.tenor.com/fwUh3G_4g3cAAAAC/slime-sliming.gif"
    ],
    "congrat": [
        "https://media.tenor.com/VOUzW9uvebkAAAAC/dantdm-cbbc.gif"
    ],
    "more": [
        "https://media.tenor.com/wshzHt1SerQAAAAC/elmo-slime-slime.gif"
    ],
    "yikes": [
        "https://media.tenor.com/xmlrr-H-yGYAAAAC/yikes.gif"
    ],
    "no way": [
        "https://media.tenor.com/we9F9lBaHKMAAAAC/whaaa-what.gif"
    ],
    "love you": [
        "https://media.tenor.com/GnQIL9rSPWkAAAAC/castanholas.gif"
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