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
async def make(ctx, ChannelName = "reee"):
    guild = ctx.guild
    ExistingChannel = discord.utils.get(guild.channels, name = ChannelName)
    if not ExistingChannel:
        print(f'{ChannelName} has been created.')
        await guild.create_text_channel(ChannelName)
    else:
        await ctx.send('Can you not')
        await ctx.send('https://media.giphy.com/media/jPA6KI2Mdbj5viVW4d/giphy.gif')

# Direct messages the user that calls the command.
@client.command(name = 'dm')
async def dm(ctx):
   await ctx.author.send('<AeroMilk is the milk for you>')

# Direct messages the mentioned user.
@client.command(name = 'DM')
async def DM(ctx, user: discord.User):
   message = '<AeroMilk is the milk for you> brought to you by an anonymous user'
   await user.send(message)


# 3 choices and recipe
@client.command()
async def embedt(ctx):

    embed = discord.Embed(
		title = 'Spahetti',
		description = 'Spaghetti in just 30 mins with instapot \n \n Ingredient = "1/2 lb Ground Beef, lean (or lean ground turkey)',
		colour = discord.Colour.blue()
    )
    embed.set_author(name='Dinner', icon_url='https://i.imgur.com/CKVgFUk.jpg')
    embed.set_image(url='https://i.imgur.com/GFvVWpD.jpg')
    embed.set_thumbnail(url='https://i.imgur.com/zm7BXHj.png')
    embed.add_field(name='Test Field', value='this is test', inline=False)
    embed.set_footer(text='This is a footer')

    await ctx.send(embed=embed)


# Allows the user to ask the bot a question, and get advice back.
@client.command(name = 'advice')
async def smart(ctx, arg):
    final_advice = [
        'Burn that ' + arg + ' like when I burned my ex\'s house down!',
        (
            'Rip up that ' + arg + ' like I rip up my taxes!'
        ),
    ]
    test = random.choice(final_advice)
    await ctx.send(test)

client.run(TOKEN)
