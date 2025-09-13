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
    "love": [
        "https://tenor.com/view/zaunvi-caitvitwt-gif-1251875630135871970"
    ],
    "hate": [
        "https://tenor.com/view/zaunvi-caitvitwt-gif-12615945993949253836"
    ],
    "felicia": [
        "https://tenor.com/view/zaunvi-caitvitwt-gif-8411954659816570775"
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