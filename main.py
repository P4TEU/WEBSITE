import discord
from discord.ext import commands
import os

# Preia variabilele din environment
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")  # optional, pentru comenzi owner-only
PREFIX = os.getenv("PREFIX", "!")  # optional, pentru comenzi text dacă vrei

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectat ca {bot.user}")
    # sincronizare slash commands
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands sincronizate: {len(synced)}")
    except Exception as e:
        print(f"Eroare sincronizare slash commands: {e}")

# Încarcă toate cogs din folderul cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Cog încărcată: {filename}")
        except Exception as e:
            print(f"Eroare la încărcarea cog-ului {filename}: {e}")

# Porneste botul
if TOKEN is None:
    print("❌ Nu a fost găsit tokenul! Setează DISCORD_TOKEN în Pella.")
else:
    bot.run(TOKEN)
