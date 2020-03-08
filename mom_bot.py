# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix = '', case_insensitive = True)


bot = ChatBot('Mom')

conv = open('chats.txt', 'r').readlines()

trainer = ListTrainer(bot);

trainer.train(conv)



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
async def make(ctx, ChannelName = 'testing'):
    guild = ctx.guild
    ExistingChannel = discord.utils.get(guild.channels, ChannelName)
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
@client.command(name = 'dmOther')
async def DM(ctx, user: discord.User):
   message = '<AeroMilk is the milk for you> brought to you by an anonymous user'
   await user.send(message)

# Sets your status to I'm home!
#@client.command(name = 'I\'m home')
#async def imHome(ctx):
#   await ctx.send('Testing')
#   await ctx.send('Welcome back, ' + ctx.author.mention)

# Prints everyone's status
#@client.command(name = 'whoshome')
#async def pplHome(ctx):
#   await ctx.send('')


# 3 choices and recipe
#@client.command(name = 'hungry')
#async def Hungry(ctx):

@client.event
async def on_message(message):
        if message.content == "Mom i\'m Hungry":
            await message.channel.send('What do you want for dinner sugar tush? \n'
                                       '1. Spaghetti \n'
                                       '2. Chicken Noodle Soup \n'
                                       '3. Chili \n')

        elif message.content == "Spaghetti" or message.content == "1":
            embed = discord.Embed(
    		title = 'Insta-Pot Spaghetti',
    		description = 'Spaghetti in just 30 mins with instapot \n \n'
             '**Ingredients** \n'
             '• 1/2 lb ground beef, lean (or lean ground turkey) \n'
             '• 1/2 small onion, diced \n'
             '• 2 cloves garlic, pressed or finely minced \n'
             '• 1 cup water \n'
             '• 4 oz spaghetti noodles, broken in thirds \n '
             '• 1 1/2 cups spaghetti sauce (jarred or homemade) \n '
             '• Salt & pepper to taste (will depend on how salty the sauce you use is) \n'
             '• 1/4 cup parmesan cheese, grated \n'
             'Optional: \n'
             '• 1/4 cup mushrooms, sliced \n'
             '• 1/4 cup bell pepper, chopped \n'
             '• 5 basil leaves, chopped \n \n \n'
             '**Instructions** \n'
             'Turn on the Sauté function (Normal/Med heat). When the display reads “Hot” add the meat. Cook, stirring occasionally, until almost done. If using ground turkey you may need to add a little oil first. \n'
             'Add the onion, cook, stirring occasionally, until onion starts to turn translucent. \n'
             'Add garlic, stir. Cancel the Sauté setting. \n'
             'Add the water. \n'
             'Sprinkle on the noodles in a criss cross pattern, varying the placement so not all of them are laying side by side. This is to minimize them sticking together. Use a spoon to gently press them down, but do not stir it. \n'
             'Add spaghetti sauce over noodles, covering them completely. Do Not Stir. \n'
             'Place the lid on the pressure cooker and lock it into place. Set the steam release knob to Sealing. \n'
             'Press the Pressure Cook (Manual) button and then the + or - button to choose 9 minutes (or 7 minutes for firmer al dente). \n'
             'When the cook cycle is finished, let the pot sit and naturally release pressure for 2 minutes (I use a heartier pasta, if you don\'t then do a Quick Release}. Then manually release the remaining pressure by turning the steam release knob to Venting. \n'
             'When the pin in the lid drops, it is safe to open the lid. Open and stir the spaghetti. Separate any noodles that may have stuck together. Taste and adjust salt, if needed. \n'
             'Stir in the Parmesan cheese and serve with any garnish you like.'
             ,
    		colour = discord.Colour.blue()
        )
            embed.set_author(name='Dinner', icon_url='https://i.imgur.com/CKVgFUk.jpg')
            embed.set_image(url='https://i.imgur.com/5QZng5B.jpg')
            embed.set_thumbnail(url='https://i.imgur.com/g6X06Gc.jpg')
            embed.set_footer(text='Love you ♥')
            await message.channel.send(embed=embed)

        elif message.content == "Chicken Noodle Soup" or message.content == "2":
            embed = discord.Embed(
    		title = 'Insta-Pot Chicken Noodle Soup',
    		description = 'Chicken Noodle Soup in just 30 mins with that instapot I gave you last christmas. Ohh remember that time, It was marvelous. Oh dear, You should visit more often, I will whip you up some good ol chicken noodle soup til your tum tum get full. Call me more often as well, I miss you so so much lil pumpkin head. \n \n'
             '**Ingredients** \n'
             '• 2 tbsp butter unsalted \n'
             '• 1 large onion chopped \n'
             '• 2 medium carrots chopped \n'
             '• 2 stalks of celery chopped \n'
             '• 1 tsp salt or to taste \n '
             '• 1 tsp pepper or to taste \n '
             '• 1 tsp thyme dry, 1 tbsp if using fresh \n'
             '• 1 tbsp parsley fresh, chopped \n'
             '• 1 tbsp oregano fresh, chopped, 1 tsp if using dry \n'
             '• 4 cups chicken broth no sodium added \n'
             '• 4 cups water'
             '• 5 oz egg noodles uncooked, (about 2 cups)'
             '• 2 lbs chicken with skin and bones, use at least 1 chicken breast \n \n \n'
             '**Instructions** \n'
             '1) Turn on the Sauté function. \n'
             '2) Add the butter and cook until the butter has melted. Add the onion, carrots and celery and saute for 3 minutes until the onion softens and becomes translucent. \n'
             '3) Season with salt and pepper, add the thyme, parsley, oregano and stir. Pour in the chicken broth. Add the chicken pieces and add another 4 cups of water. \n'
             '4) Close the lid. Set the Instant Pot to the Soup setting and set the timer to 7 minutes \n'
             '5) Once the Instant Pot cycle is complete, wait until the natural release cycle is complete, should take about 10 minutes. Follow the manufacturer\'s guide for quick release, if in a rush. Carefully unlock and remove the lid from the instant pot. \n'
             '6) Remove the chicken pieces from the soup and shred with two forks. \n'
             '7) Add the noodles to the soup and set the Instant Pot to the saute setting again. Cook for another 6 minutes uncovered, or until the noodles are cooked. \n'
             '8) Turn off the Instant Pot, by pressing the cancel button. Add the shredded chicken back to the Instant Pot, taste for seasoning and adjust as necessary. Garnish with additional parsley if preferred. \n'
             ,
    		colour = discord.Colour.blue()
        )
            embed.set_author(name='Dinner', icon_url='https://i.imgur.com/CKVgFUk.jpg')
            embed.set_image(url='https://i.imgur.com/5QZng5B.jpg')
            embed.set_thumbnail(url='https://i.imgur.com/g6X06Gc.jpg')
            embed.set_footer(text='Love you ♥')
            await message.channel.send(embed=embed)
        elif message.content == "Chili" or message.content == "3":
            embed = discord.Embed(
    		title = 'Chili in Pot',
    		description = 'This Chili will just whip you into shape. \n \n'
             '**Ingredients** \n'
             '• 2 lbs Ground Beef \n'
             '• 1/4 cup Green Bell Pepper (Basically half of a Bell Pepper) \n'
             '• 1/4 cup Red Bell Pepper (Not Necessary) \n'
             '• 1 Whole Ass Onion \n'
             '• 2 cloves Garlic \n '
             '• 2 stalks of Celery \n '
             '• 1 1-14.5oz can Diced Tomatoes \n'
             '• 1 cup Beef Broth \n'
             '• 1-6oz Tomato Paste \n'
             '• 1-15oz can Chili Beans \n'
             '• 1-15oz can Kidney Beans \n'
             '• 1 Tbsp Chili Powder \n'
             '• 1 tsp Cumin \n'
             '• 2-1/2 tsps Salt \n'
             '• 2-1/2 tsps Black Pepper \n'
             '• 1/2 tsp Oregano \n'
             'Optional: \n'
             '• 2 pinches of Chili Powder \n'
             '• Smoked Paprika \n \n \n'
             '**Instructions** \n'
             '1) ​In a frying pan season the ground beef with 1-1/2 tsps of salt and 1-1/2 tsp of pepper and brown for 6 minutes. \n'
             '2) After 6 minutes drain off the fat then set ground beef aside for later. \n'
             '3) In a separate pan add the olive oil and saute the onion, celery, red pepper, green pepper and jalapeno pepper for 5 minutes. \n'
             '4) After 5 minutes add the ground beef, diced tomatoes, tomato paste and beef broth. \n'
             '5) Add the garlic, cumin, oregano, chili powder, 1tsp salt, 1tsp pepper and mix well. \n'
             '6) Lastly add the chili beans and kidney beans mix and cover. \n'
             '7) Allow it to cook on low heat for 2 hours stirring ocassionally. After 2 hours remove from heat and serve.  \n'
             ,
    		colour = discord.Colour.blue()
        )
            embed.set_author(name='Dinner', icon_url='https://i.imgur.com/CKVgFUk.jpg')
            embed.set_image(url='https://i.imgur.com/5QZng5B.jpg')
            embed.set_thumbnail(url='https://i.imgur.com/g6X06Gc.jpg')
            embed.set_footer(text='Love you ♥')
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('')


# Allows the user to ask the bot a question, and get advice back.
@client.command(name = 'advice')
async def evil(ctx, arg):
    final_advice = [
        'Burn that ' + arg + ' like when I burned my ex\'s house down!',
        (
            'Rip up that ' + arg + ' like I rip up my taxes!'
        ),
    ]
    test = random.choice(final_advice)
    await ctx.send(test)



@client.command(name = 'talk')
async def smart(ctx, arg):
    bot_input = bot.get_response(arg)
    await ctx.send(bot_input)


client.run(TOKEN)
