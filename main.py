import discord
from discord.ext import commands
import requests 
import json 

# bot initialization
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)

@client.event
async def on_ready():
    print("The bot is now ready.")
    print("----------------------")

# to call a certain action from user
@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am a discord bot")

@client.command()
async def goodbye(ctx):
    await ctx.send("GoodBye, See you next time")

@client.event
async def on_member_join(member):
    url = "https://jokes-by-api-ninjas.p.rapidapi.com/v1/jokes"

    headers = {
	"X-RapidAPI-Key": "ede18c8c50msh8dc3a00920562f4p1fdab5jsn6fcae69c026e",
	"X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    await channel.send(response.text)
    channel = client.get_channel(1169685112905007247)
    await channel.send("Welcome to OurBot")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1169685112905007247)
    await channel.send("GoodBye, Hope you had fun")

client.run('MTE2ODE0NzYzNDU0NDk3MTkxNw.GQbb4K.fDujTB1Adl-4zHaa80vO6WPV50iFPRE_Wq_D1s')
# link bot to web app -> tell the code what application to link to
