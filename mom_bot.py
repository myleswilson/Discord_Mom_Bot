# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

class Client:
    def event(self, func):
        if func.__name__ == "on_message":
            self.on_message_handle = func
            return func

    def receive_message(self, msg):
        func = getattr(self, "on_message_handle", None)
        if func is not None:
            func(msg)
        else:
            self.process_commands(msg)
client = Client()
bot = commands.Bot(command_prefix='?')

@client.event
class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
    async def on_message(self, message):
    # Whenever a user other than bot says "hi"
        if message.author != self.user:
            if message.content == 'hi':
                await message.channel.send('What the frick did you say to me you lil shoot')

@client.event
async def on_member_join(on_member_join):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')
# Chancla command that sends gif

@bot.command(name='chancla')
async def chancla(ctx):
    chancla_angry = [
        'https://media.giphy.com/media/TH2TwG8loO06Y/giphy.gif',
        (
            'https://media.giphy.com/media/11tGqsN1gN6uc0/giphy.gif'
        ),
    ]

    response = random.choice(chancla_angry)
    await ctx.send(response)
##await message.channel.send('https://media.giphy.com/media/TH2TwG8loO06Y/giphy.gif')
#client = DiscordClient()
bot.run(TOKEN)
