##Prepare https://www.devdungeon.com/content/make-discord-bot-python
##=====================================================
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
import requests
from bs4 import BeautifulSoup
import datetime


BOT_PREFIX = (".",",")
TOKEN = 'NDgyMTQ3NDM4MTE1Njg0MzYz.DmXEww.1daNnGTVdUNZs2-2FVe9lAM1xS4'  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

##COMMANDS
##=====================================================
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


        
    
        
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

    




@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

@client.command()
async def ud(word):
    source = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))
    soup = BeautifulSoup(source.content, "html.parser")
    msg= soup.find("div",attrs={"class":"meaning"}).text
    await client.say (msg)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        hellos = ["Hello","Wazzap!!!", "May the 4th be with You,","A bit late...","Goodnight!"]
        msg = random.choice(hellos) + "{0.author.mention}".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('.220'):
        msg= "228"
        await client.send_message(message.channel, msg)
    if message.content.startswith('.228'):
        msg= "220"
        await client.send_message(message.channel, msg)
    if message.content.startswith('.time'):
        msg= datetime.datetime.now()
        await client.send_message(message.channel, msg)

##Connection INFO
##=====================================================
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with Space-Time"))
    print("Logged in as " + client.user.name)
    
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
