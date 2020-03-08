# bot.py
import os
import random
import asyncio
import pickle
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

load_dotenv()


TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix = '', case_insensitive = True)

# Prints when discord bot is connected.
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord! <AeroMilk is the milk for you>')

# Gives the user three choices of food to choose from
@client.command(name = "Mom_I'm_hungry", help = "Mom asks you what you want.")
async def hungry(message):
    await message.channel.send('What do you want for dinner, sugar tush? \n'
                               '• Spaghetti \n'
                               '• Chicken Noodle Soup \n'
                               '• Chili \n', tts = True)

# Spaghetti recipe.
@client.command(name = "Spaghetti", help = "Displays spaghetti recipe.")
async def spaghet(message):
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
    await message.channel.send(embed=embed, tts = True)


# Chicken Noodle Soup recipe.
@client.command(name = "Chicken_Noodle_Soup", help = "Displays chicken noodle soup recipe.")
async def spaghet(message):
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
    embed.set_thumbnail(url='https://i.imgur.com/MtJBiJa.jpg')
    embed.set_footer(text='Love you ♥')
    await message.channel.send(embed=embed, tts = True)

#Chili recipe
@client.command(name = "Chili", help = "Display chili recipe")
async def chili(message):
    embed = discord.Embed(
       title = 'Chili in Pot',
       description = 'This Chili will just whip you into shape. \n \n'
     '**Ingredients** \n'
     '• 2 lbs ground beef \n'
     '• 1/4 cup green bell pepper (Basically half of a Bell Pepper) \n'
     '• 1/4 cup red bell pepper (Not Necessary) \n'
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
    embed.set_thumbnail(url='https://i.imgur.com/LcP0T8P.jpg')
    embed.set_footer(text='Love you ♥')
    await message.channel.send(embed=embed, tts = True)

# Sends a chancla in someone's DM's.
@client.command(name = 'chancla', help = 'Sends the chancla to other people.')
async def DM(ctx, user: discord.User):
   gifs = [
       'https://media.giphy.com/media/TH2TwG8loO06Y/giphy.gif',
       (
           'https://media.giphy.com/media/11tGqsN1gN6uc0/giphy.gif'
       ),
   ]
   gif = random.choice(gifs)
   message = 'A chancla was sent your way by ' + client.user.mention + '\n' + gif
   await user.send(message, tts = True)


# Sends a very, VERY special message.
@client.command(name = 'hi', help = "Sends a very, VERY special message.")
async def hello(ctx):
    await ctx.send('Hey, sugar foot', tts = True)


# Makes a new channel.
'''
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
'''


# Direct messages the user that calls the command.
@client.command(name = 'dm', help = 'Sends propaganda.')
async def dm(ctx):
   await ctx.author.send('<AeroMilk is the milk for you>', tts = True)


# Direct messages the mentioned user.
@client.command(name = 'dmOther', help = 'Sends propaganda to other people.')
async def DM(ctx, user: discord.User):
   message = '<AeroMilk is the milk for you> brought to you by an anonymous user',
   await user.send(message, tts = True)


# Reads a very """"G"""" book in the user's DMs.
@client.command(name = 'book', help = 'Reads a story.')
async def story(ctx, user: discord.User):
    message = 'The cats nestle close to their kittens, \n The lambs have laid down with the sheep. \n You are cozy and warm in your bed, my dear. \n Please go the fuck to sleep. \n The windows are dark in the town, child. \n The whales huddle down in the deep. \n I\'ll read you one very last book if you swear \n You\'ll go the fuck to sleep. \n The eagles who soar through the sky are at rest \n And the creatures who crawl, run and creep. \n I know you\'re not thirsty. That\'s bullshit. Stop lying. \n Lie the fuck down, my darling, and sleep. \n'
    await user.send(message, tts = True)
    message = 'The wind whispers soft through the grass, hon. \n The field mice, they make not a peep. \n It\'s been thirty-eight minutes already. \n Jesus Christ, what the fuck? Go to sleep. \n All the kids from day care are in dreamland. \n The froggie has made his last leap. \n Hell no, you can\'t go to the bathroom. \n You know where you can go? The fuck to sleep. \n The owls fly forth from the treetops. \n Through the air they soar and they sweep. \n The hot, crimson rage fills my heart, love. \n For real: shut the fuck up and sleep. \n The cubs and the lions are snoring (snore) \n'
    await user.send(message, tts = True)
    message = 'Wrapped in a big, snuggly heap. \n How come you can do all this other great shit \n But you can\'t lie the fuck down and sleep? \n The seeds slumber beneath the earth now, \n And the crops that the farmers will reap. \n No more questions, this interview\'s over. \n I\'ve got two words for you, kid: fucking sleep. \n The tiger reclines in the Siberian jungle. \n The sparrow has silenced her cheep. \n Fuck your stuffed bear, I\'m not getting you shit. \n Close your eyes, cut the crap: sleep. \n Flowers doze low in the meadows \n'
    await user.send(message, tts = True)
    message = 'And high on the mountains so steep. \n My life is a failure, I\'m a shitty-ass parent. \n Stop fucking with me please, and sleep. \n The giant pangolins of Madagascar are snoozing \n As I lie here and openly weep. \n Sure, fine, whatever, I\'ll bring you some milk. \n Who the fuck cares? You\'re not gonna sleep. \n This room is all I can remember. \n The furniture crappy and cheap. \n You win! You escape, you run down the hall \n As I nod the fuck off and sleep. \n Bleary and dazed I awaken \n To find your eyes shut, so I keep \n My fingers crossed tight, as I tip-toe away \n And pray that you\'re fucking asleep. \n We\'re finally watching our movie. \n Popcorn\'s in the microwave: "beep!" \n Oh shit, goddamn it, you\'ve got to be kidding. \n Go the fuck back to sleep! \n'
    await user.send(message, tts = True)


# Allows the user to ask the bot a question, and get advice back.
@client.command(name = 'advice', help = 'Gives you advice.')
async def evil(ctx, arg):
    final_advice = [
        'Burn that ' + arg + ' like when I burned my ex\'s house down!',
        (
            'Rip up that ' + arg + ' like I rip up my taxes!'
        ),
    ]
    test = random.choice(final_advice)
    await ctx.send(test, tts = True)


# Allows the user to speak to Mom Bot
@client.command(name = 'talk', help = 'Allows you to talk with Mom.')
async def smart(ctx, arg):
    bot = ChatBot('Mom')

    conv = open('chats.txt', 'r').readlines()
    trainer = ListTrainer(bot);
    trainer.train(conv)


    bot_input = bot.get_response(arg)
    response = bot.get_response(bot_input)
    final_msg = response

    await ctx.channel.send(final_msg, tts = True)

client.run(TOKEN)
