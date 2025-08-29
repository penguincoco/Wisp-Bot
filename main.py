import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True #get the intents from the documentation

# ---------- Bot data ----------
funFacts = ["The Wind and the Wisp is made by 28 people!", 
            "The red ribbon represents the red string of fate!"]

# ---------- end bot data ----------

#this sets up the bot
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.event 
async def on_ready():
    print("We are ready to go in {bot.user.name}")

#these are overriding methods
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "yikes" in message.content.lower(): 
        await message.delete()
        await message.channel.send(f"{message.author.mention} lol don't say that bro")

    await bot.process_commands(message) #this is necessary for on_message
    #this allows the bot to continue processing the commands
    #if we are overriding the function, this await bot.process_commands must be called!

@bot.command() #creating a bot command
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)