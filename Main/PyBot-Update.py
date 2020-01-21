from discord.ext import commands
import discord
import json

BOT_PREFIX = (".", "")
client = commands.Bot(command_prefix=BOT_PREFIX, description="Discord Python Rewrite Bot")
with open("config.json", 'r') as f:
    config = json.load(f)

# TODO : https://repl.it/talk/learn/Discordpy-Rewrite-Tutorial-using-commands-extension/10690/25324    HelpSection//Embeds
# TODO : https://hackernoon.com/a-guide-to-building-a-multi-featured-slackbot-with-python-73ea5394acc MusicLyrics//Audio&VideoLink//News


@client.event
async def on_ready():
    client.remove_command("help")
    # activity = discord.Game(name=str(config["MAIN"]["BOT_GAME"]))
    await client.change_presence(activity=discord.Game(name=str(config["MAIN"]["BOT_GAME"])))
    # await client.change_presence(activity=activity)
    print("Logged in as " + client.user.name)
    cogs_loader(client)


# Member Join Action
@client.event
async def on_member_join(member):

    await member.send(str(config["MAIN"]["WELCOME_MSG"]))
    # await member.send("help")
    role = discord.utils.get(member.guild.roles, name=str(config["MAIN"]["ON_JOIN_ROLE"]))
    await member.add_roles(role)


# Member Remove Action
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')
''''
@task.loop(seconds=60)
async def daily_news():
    await get_news()
'''
# Run BOT-TOKEN
def cogs_loader(client):
    cogs=config["MAIN"]["COGS"]
    for i in cogs:
        client.load_extension(i)


client.run(str(config["MAIN"]["TOKEN"]))
