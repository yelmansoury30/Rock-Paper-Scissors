import os
#from dotenv import load_dotenv

import discord
from discord.ext import commands

class Games(command.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx, user_weapon):
        await ctx.send(self.choice.choice)

def setup(bot):
    bot.add_cog(Games(bot))

class RPS:
    Rock = "✊"
    Paper = "✋"
    Scissors = "✂️"

    def choose_weapon(self):
        return (self.Rock, self.Paper, self.Scissors)

    def __init__(self, choice):
        choice = choice.lower()

        if choice == RPS.Rock:
            self.choice = RPS.Rock
        elif choice == RPS.Paper:
            self.choice == RPS.Paper
        elif choice == RPS.Scissors:
            self.choice == RPS.Scissors
        else:
            raise
client.run('DISCORD_TOKEN')



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










