# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord! <AeroMilk is the milk for you>')

# Sends random chancla gif each time.
@client.command(name = 'chancla')
async def chancla(ctx):
    chancla_angry = [
        'https://media.giphy.com/media/TH2TwG8loO06Y/giphy.gif',
        (
            'https://media.giphy.com/media/11tGqsN1gN6uc0/giphy.gif'
        ),
    ]

    response = random.choice(chancla_angry)
    await ctx.send(response)


# Sends a very, VERY special message.
@client.command(name = 'hi')
async def hello(ctx):
    await ctx.send('What the frick did you say to me you lil shoot!')


# Makes a new channel.
@client.command(name = 'channel')
async def make(ctx, ChannelName = 'THE H O U S E'):
    guild = ctx.guild
    ExistingChannel = discord.utils.get(guild.channels, name = ChannelName)
    if not ExistingChannel:
        print(f'{ChannelName} has been created.')
        await guild.create_text_channel(ChannelName)
    if ExistingChannel:
        await ctx.send('Can you not')


@client.command(name = 'dm')
async def dm(ctx):
   await ctx.author.send('<AeroMilk is the milk for you>')


@client.command(name = 'DM')
async def DM(ctx, user: discord.User, *, message=None):
   #message = '<AeroMilk is the milk for you> brought to you by an anonymous user'
   await ctx.user.send_message('<AeroMilk is the milk for you> brought to you by an anonymous user')


@client.command(pass_context=True)
async def clear(ctx, amount=100):
	channel = ctx.message.channel
	messages = []
	async for message in client.logs_from(channel, limit=int(amount)):
		messages.append(message)
	await client.delete_messages(messages)


@client.command()
async def hungry():
	embed = discord.Embed(
		title = 'Title',
		description = 'This is a description. ',
		colour = discord.Colour.blue()
		)

	embed.set_footer(text='This is a footer.')
	await client.say(embed=embed)


#@client.command(name = 'advice')
#async def say(ctx):

client.run(TOKEN)
