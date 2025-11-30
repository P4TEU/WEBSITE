import discord
from discord.ext import commands
import json
import os

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    await bot.tree.sync()
    print("Slash commands synced.")

# Load cogs dynamically
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded cog: {filename}")

bot.run(config["token"])
