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



