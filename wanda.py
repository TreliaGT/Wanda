import os
import random
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get

intents = discord.Intents.default()
intents.presences = True
intents.members = True

#https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='*' , intents=intents)

@bot.command(name='test2' , help='Admin : tests arg the bot', category="Admin")
@commands.has_role('Admin')
async def test2(ctx , *, arg):
    await ctx.send(arg)

@bot.command(name='joke' , help='tells a joke' , category="Fun")
async def test(ctx):
    URL = "https://official-joke-api.appspot.com/random_joke"
    r = requests.get(url = URL)
    data = r.json()
    await ctx.send(data["setup"] + ' : ' + data["punchline"])


@bot.command(name='ticket' , help="sends a message to user *ticket 'name' 'Message'" , category="Ticket System")
async def ticket(ctx, Name, Message):
    user = get(bot.get_all_members(), display_name=Name)
    if user:
        await user.send(Message)
    else:
        await ctx.send("Can't find user")

bot.run(TOKEN)