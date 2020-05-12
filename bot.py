import os
#from dotenv import load_dotenv

import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_ready():
    print('{RockPaperScissorsBot} is awake'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!rps'):
        await message.channel.send('Choose your weapon!')
    if message.content.startswith('✊'):
        await message.channel.send(tool)
    if message.content.startswith('✋'):
        await message.channel.send(tool)
    if message.content.startswith('✂️'):
        await message.channel.send(tool)

client.run(TOKEN)


from random import randint

player = input('rock(r), paper(p), scissors(s)')

if player == 'r':
    print('✊')

elif player == 'p':
    print('✋')

elif player == 's':
    print('✂️')

else:
    print('By the way we are playing Rock Paper Scissors you imbecile!')

tool = randint(1,3)

if tool == 1:
    bot = 'r'
    print('✊')

elif tool == 2:
    bot = 'p'
    print('✋')

elif tool == 3:
    bot = 's'
    print('✂️')

if player == bot:
    print('It looks like a tie folks!')

elif player == 'p' and bot == 'r':
    print('Human Wins!')

elif player == 'r' and bot == 's':
    print('Human Wins!')

elif player == 's' and bot == 'p':
    print('Human Wins!')

elif player == 'r' and bot == 'p':
    print('Bot Wins!')

elif player == 's' and bot == 'r':
    print('Bot Wins!')

elif player == 's' and bot == 's':
    print('Bot Wins!')

else:
    print('Artificial intelligence is not so intelligent after all.')









