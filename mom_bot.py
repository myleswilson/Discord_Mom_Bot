# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

#client = Client()
bot = commands.Bot(command_prefix='?')

#@client.event
class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
    async def on_message(self, message):
    # Whenever a user other than bot says "hi"
        if message.author != self.user:
            if message.content == 'hi':
                await message.channel.send('What the frick did you say to me you lil shoot')
# Chancla command that sends gif.
# Sends random gif each time.
@bot.command(name='chancla', help='sends chancla gif')
async def chancla(ctx):
    chancla_angry = [
        'https://media.giphy.com/media/TH2TwG8loO06Y/giphy.gif',
        (
            'https://media.giphy.com/media/11tGqsN1gN6uc0/giphy.gif'
        ),
    ]

    response = random.choice(chancla_angry)
    await ctx.send(response)
client = DiscordClient()
bot.run(TOKEN)
