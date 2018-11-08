import discord
from discord.ext import commands

import os
from random import choice
import time

prefix = "!"
bot = commands.Bot(command_prefix=prefix, description="G'day mate, it's JimmyD")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("with the API"))
    print("Logged in as")
    print(bot.user.name)
    
@bot.command()
async def hello(ctx):
    '''
    Says g'day
    '''
    author = ctx.message.author.mention
    await ctx.send(f":wave: G'day, {author}")

@bot.command()
async def ping(ctx):
    '''
    An accurate way to measure ping
    '''
    await ctx.send("PONG!")

@bot.command()
async def mock(ctx, a):
    '''
    Mocks the given text
    '''
    msg = ctx.message.content[5:].lower()
    returnMsg = ""

    for char in msg:
        returnMsg += choice((char.upper, char.lower))()

    await ctx.send(returnMsg)

@bot.command()
async def test(ctx, a:int):
    channel = ctx.message.channel
    history = await channel.history(limit=10).flatten()

    count = 0
    for message in history:
        sendmsg = f"{count}: {message.content}"
        print(sendmsg)
        count += 1

@bot.command(hidden=True)
async def commit(ctx):
    build = os.environ.get("SOURCE_VERSION")

    await ctx.send(f"Current commit: ```{build}```")    

bot.run(os.environ.get("DISCORD_KEY"))