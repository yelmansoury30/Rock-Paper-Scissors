import os
# from dotenv import load_dotenv

import discord
from discord.ext import commands

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    box = discord.Embed(title="Help", description="a help box")
    box.add_field(name="Field_1", value="Hi")
    box.add_field(name="Field_2", value="Bye")
    #await ctx.send(f"Hello {ctx.author.display_name}")
    await ctx.send(embed=box)

bot.run(TOKEN)


