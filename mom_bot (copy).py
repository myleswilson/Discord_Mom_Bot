# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('Njg1ODk2OTYyODg0ODk0ODA2.XmPfuA.MqBr5LHeDo85vHGqdXxjs9p4iBE')

#client = discord.Client()

#@client.event
class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
    async def on_message(self, message):
    # Whenever a user other than bot says "hi"
        if message.author != self.user:
            if message.content == 'hi':
                await message.channel.send('What the frick did you say to me you lil shoot')

client = DiscordClient()
client.run(TOKEN)
