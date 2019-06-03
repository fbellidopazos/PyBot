# Prepare https://www.devdungeon.com/content/make-discord-bot-python
# =====================================================
import random
import asyncio
# import aiohttp
# import json
from discord import Game
from discord.ext.commands import Bot
# from discord.ext import commands
import requests
from bs4 import BeautifulSoup
# import datetime
import praw
import discord
import time
# import ast
from User import User
import pickle
'''
COMMANDS
==============================
    -8ball
    -UrbanDictionary (ud <Word>)
    -WolframAlpha(wolfram <Query>)
    -NSFW(nsfw <number> )
    -Clear (clear <number> only ADMIN)
    -join/leave <list/role>
    
    ADMIN ONLY
    =========================
    -backUp 
    -users 
    -addUser
    -removeUser
    -setNick

Functions
==========================
find(name) : User
backUpPickle()
usersToString(): STRING

TODO
===========================
-Giveaways??
-Embeds?? https://www.youtube.com/watch?v=XKQWxAaRgG0&t
'''

BOT_PREFIX = (".", "")
# Get at discordapp.com/developers/applications/me
TOKEN = 'NDgyMTQ3NDM4MTE1Njg0MzYz.D3IkHg.pbRBXPTxphZUY1LwjA_gAp762qg'
role_id = 461171949197066241  # Owner ROLE
client = Bot(command_prefix=BOT_PREFIX)
reddit = praw.Reddit(client_id='StI7zL-mxlm2HQ',
                     client_secret='lUkCF66UgqEJgE03JkkAkXWQzKA',
                     user_agent='PyBotNSFW')
Users = []


def find(name):
    res=-1
    for i in range(len(Users)):
        res+=1
        if(Users[i].name==name):
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
    res=""
    for i in Users:
        res=res+i.toString()
    return(res)


# COMMANDS
# =====================================================
# HELLO´s
@client.command(pass_context=True)
async def hello(context):
    hellos = ["Hello", "Wazzap!!!", "May the 4th be with You,", "A bit late...", "Goodnight!"]
    msg = random.choice(hellos) + "{}".format(context.message.author.mention)
    print(context.message.author.mention)
    await context.send(msg)
# Eight Ball
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
    await context.send(random.choice(possible_responses) + ", " + context.message.author.mention)


# Urban Dictionary
@client.command(name='ud',
                description="Gives the definition of the input word,searched in Urban Dictionary",
                brief="ud <word>")
async def urban(ctx,word):
    source = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))
    soup = BeautifulSoup(source.content, "html.parser")
    msg = soup.find("div", attrs={"class": "meaning"}).text
    await ctx.send(msg)


# Wolfram
@client.command(name='wolfram',
                description="Wolfram Alpha search-NO SPACE IN INPUT",
                brief="wolfram <query>", pass_context=True)
async def wolfram(self,*, ctx):
    url = 'http://api.wolframalpha.com/v1/simple?appid=UQ2PAA-Y2QK6KVRA9&i={}'.format(
        (ctx.replace(" ", "%20")).replace("+", "%2B"))

    await self.send(url)






# NSFW
# TODO Update commands && Role
@client.command(name='nsfw',
                description="Basically PORN",
                brief="command: nsfw",
                pass_context=True)
async def nsfw(ctx, *, ctxnsfw: int):
    # NSFW ROLE ID: 581924915507101701
    server = ctx.message.guild
    author = ctx.message.author
    #role = discord.utils.get(server.roles, id=461179333407539200)
    if(461179333407539200 in author.roles):
        nsfw = reddit.subreddit('').hot()
        post_to_pick = random.randint(1, 15)
        amount = ctxnsfw
        ctx.message.delete(ctx.message)
        while amount != 0:
            for i in range(0, post_to_pick):
                submission = next(x for x in nsfw if not x.stickied)

            await ctx.send(discord.Object(id="461240565980463128"), submission.url)
            amount -= 1
            time.sleep(2)
        await ctx.message.delete(ctx.message)
    else:
        await ctx.send("You must be in nsfw role.\nTry the 'join nsfw' command")
#TODO Update command
@client.command(pass_context=True)
async def nsfwPrivate(ctx, *, ctxnsfw: int):
    # NSFW ROLE ID: 581924915507101701
    server = ctx.message.server
    author = ctx.message.author
    role = discord.utils.get(server.roles, id=461179333407539200)
    nsfw = reddit.subreddit('nsfw+RealGirls+LegalTeens+Boobies+palegirls+redheads+ginger+Hotchickswithtattoos+bodyperfection+PrettyGirls+suicidegirls+goddesses+altgonewild+HighResNSFW+BonerMaterial+nsfw2+SexyFrex+boobs+lingerie+sexygirls+SnowWhites+iWantToFuckHer+SexyButNotPorn+fortyfivefiftyfive+braceface+JustHotWomen+thinspo+stripgirls+Page3Glamour+Playboy+GifsOfRemoval+wet+barelylegalteens+SceneGirls+NSFW_nospam+AlbumBabes+B_Cups+shewantstofuck+Barelylegal+girlsdoingnerdythings+classysexy+Sexy+NSFW_Wallpapers+PantyPeel+UHDnsfw+peachfuzz+UnrealGirls+FuckingPerfect+redhead+TheHottestBabes+slimgirls+primes+skivvies+THEGOLDSTANDARD+SoHotItHurts+nsfw_hd+18_20+18nsfw+Hotness+BareGirls+redlingerie+Perfect_NSFW+OnlyGoodPorn+fyeahsexyteens+AmazingTeens+fuckyeahsexyteens+HotGirls+paleskin+Babes+BetterThanPorn+nsfwnonporn+countrygirls+Playboy_Albums+realperfection+TeaGirls+ThinChicksWithTits+hq_nsfw+Straps+GorgeousGirlsNSFW+DomesticGirls+RealBeauties+Sexyness+StrippingOffShirts+RiaeSuicide+nsfw_bw+nsfw_sexy_girls+BacklitBeauty+SexyGoosebumps+tattooed_redheads+Bangable+TotalBabes+BikiniTeens+Headless+Randomgirls+HotGirlsNSFW+sexynsfw+Adultpics+debs_and_doxies+nsfwonly+nsfwnew').hot()
    post_to_pick = random.randint(1, 15)
    amount = ctxnsfw
    client.delete_message(ctx.message)
    while amount != 0:
        for i in range(0, post_to_pick):
            submission = next(x for x in nsfw if not x.stickied)

        await ctx.send_message(author, submission.url)
        amount -= 1
        time.sleep(2)
    await client.delete_message(ctx.message)
#JOIN
# TODO Update command
@client.command(pass_context=True)
async def join(ctx,command:str):
    joinables=["nsfw","nitain","catalyst","reactor"]
    author = ctx.message.author
    if command=="list":
        res = ""
        for i in joinables:
            res = res + "\n" + str(i)
        await client.say(res)
    elif(command.lower() in joinables):
        await client.add_roles(author, discord.utils.get(author.server.roles, name=command.lower()))
#Leaves
# TODO Update command
@client.command(pass_context=True)
async def leave(ctx,command:str):
    joinables=["nsfw","nitain","catalyst","reactor"]
    author = ctx.message.author
    if command=="list":
        res = ""
        for i in joinables:
            res = res + "\n" + str(i)
        await client.say(res)
    elif(command.lower() in joinables):

       # Users[find(author)].removeRole(command.lower())
        await client.remove_roles(author, discord.utils.get(author.server.roles, name=command.lower()))







# TODO Update command
# Clear messages
@client.command(pass_context=True)
async def clear(ctx, number):
    server = ctx.message.server
    author = ctx.message.author
    role = discord.utils.get(server.roles, id=role_id)
    if role in author.roles:
        number = int(number) + 1  # Converting the amount of messages to delete to an integer
        counter = 0
        async for x in client.logs_from(ctx.message.channel, limit=number):
            if counter < number:
                await client.delete_message(x)
                counter += 1
            await asyncio.sleep(0.2)
    else:
        await client.say("You are not permitted")
# BACKUP
# TODO Update command
@client.command(pass_context=True)
async def backUp(ctx):
    server = ctx.message.server
    author = ctx.message.author
    role = discord.utils.get(server.roles, id=role_id)
    if role in author.roles:
        backUpPickle()
        print(usersToString())
        await client.send_message(author, "LOG:\n========================\n"+usersToString())
        await client.say("BACKED-UP")
    else:
        await client.say("You are not owner")
# BACKUP
# TODO Update command
@client.command(pass_context=True)
async def restore(ctx):
    server = ctx.message.server
    author = ctx.message.author
    role = discord.utils.get(server.roles, id=role_id)
    if role in author.roles:
        loadPickle()
        print(usersToString())
        await client.send_message(author, "LOG:\n========================\n"+usersToString())
        await client.say("BACKED-UP")
    else:
        await client.say("You are not owner")
# TODO Update command
@client.command(pass_context=True)
async def users(ctx):
    server = ctx.message.server
    author = ctx.message.author
    role = discord.utils.get(server.roles, id=role_id)
    if role in author.roles:
        await client.send_message(author, "LOG:\n========================\n"+ usersToString())
    else:
        await client.say("You are not owner")
# TODO Update command
@client.command(pass_context=True)
async def addUser(ctx,name,nick,mainRole):
    server = ctx.message.server
    author = ctx.message.author
    role = discord.utils.get(server.roles, id=role_id)
    if role in author.roles:
        a=User(name,nick,mainRole)
        Users.append(a)
        backUpPickle()

    else:
        await client.say("You are not owner")
# TODO Update command
@client.command(pass_context=True)
async def removeUser(ctx,name):
    server = ctx.message.server
    author = ctx.message.author
    role = discord.utils.get(server.roles, id=role_id)
    if role in author.roles:
        User=Users[find(name)]
        Users.remove(User)
        await client.kick(User.name)
        backUpPickle()
    else:
        await client.say("You are not owner")
# TODO Update command
@client.command(pass_context=True)
async def setNick(ctx,name,nick):
    server = ctx.message.server
    author = ctx.message.author
    role = discord.utils.get(server.roles, id=role_id)
    if role in author.roles:
        User=Users[find(name)]
        User.setNick(nick)
        backUpPickle()
        await client.change_nickname(User.name, nick)
    else:
        await ctx.send("You are not owner")











##Connection INFO
##=====================================================
@client.event
async def on_ready():
    activity = discord.Game(name="with Space-Time")
    await client.change_presence(status=discord.Status.idle, activity=activity)

    print("Logged in as " + client.user.name)

@client.event
async def on_member_join(member):
    a = User(member,member.display_name,"Regular")
    Users.append(a)
    backUpPickle()
    await client.send_message(member, "TEST")
    await client.add_roles(member, discord.utils.get(member.server.roles, name="Regular"))


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for guilds in client.guilds:
            print(guilds.name)
        await asyncio.sleep(1000)


client.loop.create_task(list_servers())
client.run(TOKEN)