import discord
from discord.ext import commands
import json
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# skit som tydligen behövs
intents = discord.Intents.default()
intents.message_content = True # Behövs tydligen för att kunna läsa meddelanden :shrug:
bot = commands.Bot(command_prefix="!", intents=intents) # sätter bara upp kommandoprefix osv
intents.members = True
# Ladda in svullogrejer så de kan hämtas senare
class SvulloData:
    def __init__(self, path="svullo.json"):
        with open(path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def random_item(self, key):
        arr = self.data.get(key, [])
        if not arr:
            return None
        return random.choice(arr)

    def random_index(self, key):
        arr = self.data.get(key, [])
        if not arr:
            return None
        return random.randint(0, len(arr) - 1)

svullo = SvulloData()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello there!")

# kommandon typ eller något jag vet inte

@bot.command()
async def huh(ctx):
    await ctx.send("Nä nu jävlar! Hovmästaren svarar endast till: !tyst, !rant, !nej, !kaos, !stick")

@bot.command()
async def stick(ctx):
    stickObject = svullo.random_item("insults")
    await ctx.send(stickObject)

@bot.command()
async def kaos(ctx):
    kaosObject = svullo.random_item("kaos")
    await ctx.send(kaosObject)

@bot.command()
async def rant(ctx):
    rantObject = svullo.random_item("hovmastare")
    await ctx.send(rantObject)

@bot.command()
async def nej(ctx):
    rantObject = svullo.random_item("glapord")
    await ctx.send(rantObject)

import random

@bot.command()
async def tyst(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Angne")

    if role is None:
        await ctx.send("MEN VART FAN ÄR ANGNE?!")
        return

    members = []

    async for m in ctx.guild.fetch_members(limit=None):
        if role in m.roles and not m.bot:
            members.append(m)

    if not members:
        await ctx.send("Nä men va fan Angne är ju tom.")
        return

    chosen = random.choice(members)
    #tystObject = svullo.random_item("tyst")

    await ctx.send(
        content=f"{chosen.mention}",
        file=discord.File("svullo-sta.gif")
    )

bot.run(TOKEN)