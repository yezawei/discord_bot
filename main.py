import os
import random
import discord
from discord.ext import commands
from secrettoken import *
import requests
import json


intents = discord.Intents.all()
intents.message_content = True
intents.members = True
intents.typing = True
intents.presences = True

client = discord.Client(intents=intents)  

client = commands.Bot(command_prefix = '!',intents=intents)



@client.event
async def on_ready():
    print("The bot is now ready for use")
    print("..............")

@client.command()
async def hello(ctx):
    await ctx.send("Hello! I am the bot! ")

@client.command()
async def byebye(ctx):
    await ctx.send("Bye! I hope you have a great day fellow human!")

@client.event
async def on_member_join(member):
    url = "https://joke3.p.rapidapi.com/v1/joke"

    payload = {
	"content": "A joke here",
	"nsfw": "false"
    }
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": JOKEAPI, 
	"X-RapidAPI-Host": "joke3.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    channel = client.get_channel(1086451935558766666)
    await channel.send("Welc0me, to the server fell0w hUman! ")
    await channel.send(json.loads(response.text)['content'])

@client.event
async def on_member_remove(member):
    jokeurl = "https://joke3.p.rapidapi.com/v1/joke"

    payload = {
	"content": "A joke here",
	"nsfw": "false"
    }
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": JOKEAPI,
	"X-RapidAPI-Host": "joke3.p.rapidapi.com"
    }

    response = requests.request("POST", jokeurl, json=payload, headers=headers)
    channel = client.get_channel(1086451935558766666)
    await channel.send("Loser left the channel... bye.. i guess?")
    await channel.send(json.loads(response.text)['content'])

    
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command.")


@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in a voice channel")

client.run(BOTTOKEN)

