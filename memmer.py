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
        "https://tenor.com/bRMz0.gif"
    ],
    "slime": [
        "https://tenor.com/bESpJ.gif"
    ],
    "congrat": [
        "https://tenor.com/brBMj.gif"
    ],
    "more": [
        "https://tenor.com/bXDDI.gif"
    ],
    "yikes": [
        "https://tenor.com/rciVwrEUYEk.gif"
    ],
    "no way": [
        "https://tenor.com/qOtmsKE03Nv.gif"
    ]
}

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online and ready!")
    await bot.change_presence(activity=discord.Game(name="for: love, hate, felicia"))

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    msg = message.content.lower()
    for trigger, gifs in meme_database.items():
        if trigger in msg:
            await message.channel.send(random.choice(gifs))
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