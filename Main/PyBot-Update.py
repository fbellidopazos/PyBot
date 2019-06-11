from discord.ext import commands
import discord
import os



BOT_PREFIX = (".", "")
client = commands.Bot(command_prefix=BOT_PREFIX, description="Discord Python Rewrite Bot")



# TODO : https://repl.it/talk/learn/Discordpy-Rewrite-Tutorial-using-commands-extension/10690/25324    HelpSection//Embeds
# TODO : https://hackernoon.com/a-guide-to-building-a-multi-featured-slackbot-with-python-73ea5394acc MusicLyrics//Audio&VideoLink//News
@client.event
async def on_ready():
    client.remove_command("help")
    activity = discord.Game(name="with Space-Time")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Logged in as " + client.user.name)
    cogs_loader(client)


# Member Join Action
@client.event
async def on_member_join(member):

    await member.send( "```\nWelcome to The Quantum Enlightenment." +
                              "\n==========================================\n" +
                              "The following rules you must know:\n" +
                              "RULES\n\nThe following Commands you may use in *BOT_SPAM*:\nCommands\n```")
    # await member.send("help")
    role = discord.utils.get(member.guild.roles, name="Regular")
    await member.add_roles(role)


# Member Remove Action
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


# Run BOT-TOKEN
def cogs_loader(client):
    for filename in os.listdir('./extensions'):
        if filename.endswith('.py'):
            client.load_extension(f'extensions.{filename[:-3]}')

client.run('NDgyMTQ3NDM4MTE1Njg0MzYz.D3IkHg.pbRBXPTxphZUY1LwjA_gAp762qg')
