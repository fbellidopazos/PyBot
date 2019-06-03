from discord.ext import commands
from User import User
import discord
import pickle
import os


BOT_PREFIX = (".", "")
client = commands.Bot(command_prefix=BOT_PREFIX, description="Discord Python Rewrite Bot")

Users = []


def find(nick):
    res = -1
    for i in range(len(Users)):
        res += 1
        if (Users[i].nick == nick):
            break
    return res


def backUpPickle():
    f = open("Users.pkl", "wb")
    pickle.dump(Users, f)
    f.close()


def loadPickle():
    f = open("Users.pkl", "rb")
    Users = pickle.load(f)
    f.close()


def usersToString():
    res = ""
    for i in Users:
        res = res + i.toString()
    return (res)


@client.event
async def on_ready():
    activity = discord.Game(name="with Space-Time")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Logged in as " + client.user.name)


# Member Join Action
@client.event
async def on_member_join(ctx,member):
    a = User(member, member.display_name, "Regular")
    # Users.append(a)
    # backUpPickle()
    await ctx.author.send(member, "```prolog\nWelcome to The Quantum Enlightenment." +
                              "\n==========================================\n" +
                              "The following rules you must know:\n" +
                              "RULES\n\nThe following Commands you may use in *BOT_SPAM*:\nCommands\n```")
    '''
    Welcome to The Quantum Enlightenment.
    ==========================================
    The following rules you must know:
    --RULES--
    
    The following Commands you may use in *BOT_SPAM*:
    --COMMANDS--    
    '''
    await ctx.author.add_role(member, discord.utils.get(member.server.roles, name="Regular"))


# Member Remove Action
@client.event
async def on_member_remove(ctx,member):
    Users.remove(find(member.display_name))
    backUpPickle()
    await ctx.author.send(member,"You have left The Quantum Enlightenment.\nMay the Force be with you")


# Run BOT-TOKEN
for filename in os.listdir('./extensions'):
    if filename.endswith('.py'):
        client.load_extension(f'extensions.{filename[:-3]}')

client.run('NDgyMTQ3NDM4MTE1Njg0MzYz.D3IkHg.pbRBXPTxphZUY1LwjA_gAp762qg')
