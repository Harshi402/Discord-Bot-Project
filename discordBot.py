#import required dependicies
import discord
import requests
import asyncio
import json
from discord.ext import commands
from discord import member
from discord.ext.commands import has_permissions ,MissingPermissions

#import Bot Token
from apikeys import *

#client = commands.Bot(command_prefix= '!')
intents = discord.Intents.all()
intents.members=True

client = commands.Bot(command_prefix='!', intents=intents)
#1st event
@client.event
async def on_ready(): 
    print("The bot is now ready for use!") #not for user to see this is for us to know
    print("---------------------------") #just to make the output look better


@client.command()
async def hello(ctx): #name of the function is hello
    await ctx.send("Hello, I am the OurBot")


# 2nd command
@client.command()
async def bye(ctx): #name of the function is hello
    await ctx.send("Bye, hope to see you soon")


@client.event #detects when a user joins the server and gets a random joke
async def on_member_join(member): 
    url = "https://world-of-jokes1.p.rapidapi.com/v1/jokes/random-joke"

    headers = {
	"X-RapidAPI-Key": "ede18c8c50msh8dc3a00920562f4p1fdab5jsn6fcae69c026e",
	"X-RapidAPI-Host": "world-of-jokes1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)    
    channel=client.get_channel(1168229155905745029)
    print("hello")
    await channel.send("Welcome to the server")
    await channel.send(f'{member} \n Here is a joke for you')
    #await channel.send(response.json()['title'])
    await channel.send(response.json()['body'])#takes up random jokes from rapidapi

@client.event
async def on_member_remove(member):
    channel=client.get_channel(1168229155905745029)
    await channel.send("Goodbyee")

@client.command()
@has_permissions(kick_members=True) #does the user have permission to kick the other user
async def kick(ctx, member:discord.Member, *,reason=None ):
    print("kicked")
    await member.kick(reason=reason)
    await ctx.send(f'{member} has been kicked')


@kick.error #if a error is produced in the above code because the user doesnt have required permission then this coroutine is called
async def kick_error(ctx , error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have the permissions to kick people")
    
#same goes for ban command

@client.command()
@has_permissions(ban_members=True) #does the user have permission to ban the other user
async def ban(ctx, member: discord.Member, *,reason=None ):
    await member.kick(reason=reason)
    await ctx.send(f'User{member} has been banned')

@ban.error #if a error is produced in the above code because the user doesnt have required permission then this coroutine is called
async def ban_error(ctx , error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have the permissions to ban people")



client.run(BOTTOKEN)
