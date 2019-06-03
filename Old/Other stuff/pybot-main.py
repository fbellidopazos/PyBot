##Prepare https://www.devdungeon.com/content/make-discord-bot-python
##=====================================================

import discord
import random
import requests
from discord.ext.commands import Bot
from bs4 import BeautifulSoup

BOT_PREFIX = (".")
TOKEN = 'NDgyMTQ3NDM4MTE1Njg0MzYz.DmAr9g.Zd5yY4LnLJLDoLuW6qMNf8JX420'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itselfaw
    if message.author == client.user:
        return
    

##COMMANDS
##=====================================================
    if message.content.startswith('hello'):
        hellos = ["Hello","Wazzap!!!", "May the 4th be with You,","A bit late...","Goodnight!"]
        msg = random.choice(hellos) + "{0.author.mention}".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('.220'):
        msg= "228  <3"
        await client.send_message(message.channel, msg)
    if message.content.startswith('.228'):
        msg= "220  <3"
        await client.send_message(message.channel, msg)


@client.event
async def urban(word):
    print(word)
    source = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))
    soup = BeautifulSoup(source.content, "html.parser")
    msg= soup.find("div",attrs={"class":"meaning"}).text
    await client.say (msg)
##Connection INFO
##=====================================================
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run(TOKEN)
