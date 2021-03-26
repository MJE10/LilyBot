import pickle
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

print('starting script')

from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound
from discord import Intents
import discord

intents = Intents.default()
bot = Bot(command_prefix='$', intents=intents)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send('hi')


@bot.command(name='hello')
async def fetchServerInfo(context):
    await context.send('hi')


@bot.command(name='ping')
async def fetchServerInfo(context):
    await context.send('pong')


print('starting bot')
bot.run(TOKEN)
print('bad')
# while 1:
