##Prepare https://www.devdungeon.com/content/make-discord-bot-python
##=====================================================
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import datetime
import praw
import discord
import time
import ast



BOT_PREFIX = (".","")
TOKEN = 'NDgyMTQ3NDM4MTE1Njg0MzYz.DmXEww.1daNnGTVdUNZs2-2FVe9lAM1xS4'  # Get at discordapp.com/developers/applications/me
role_id="461171949197066241"#Owner ROLE
client = Bot(command_prefix=BOT_PREFIX)
reddit = praw.Reddit(client_id='StI7zL-mxlm2HQ',
                     client_secret='lUkCF66UgqEJgE03JkkAkXWQzKA',
                     user_agent='PyBotNSFW')

with open('Remembers.txt', 'r') as f:
    Remembers = ast.literal_eval(f.read())
##COMMANDS
##=====================================================


##Eight Ball
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




##Square Number
@client.command(name='square',
                description="Give the square of the input number",
                brief="square <number>")
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

##Urban Dictionary
@client.command(name='ud',
                description="Gives the definition of the input word,searched in Urban Dictionary",
                brief="ud <word>")
async def ud(word):
    source = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))
    soup = BeautifulSoup(source.content, "html.parser")
    msg= soup.find("div",attrs={"class":"meaning"}).text
    await client.say (msg)
##Wolfram
@client.command(name='wolfram',
                description="Wolfram Alpha search-NO SPACE IN INPUT",
                brief="wolfram <query(no spaces)>",pass_context=True)
async def wolfram(self,*,ctx):
    url = 'http://api.wolframalpha.com/v1/simple?appid=UQ2PAA-Y2QK6KVRA9&i={}'.format(ctx.replace(" ", "%20"))

    await client.say (url)
    await client.say (ctx)


#NSFW
@client.command(name='nsfw',
                description="Basically PORN",
                brief="command: nsfw",
                pass_context = True)
async def nsfw(ctx,*,ctxnsfw:int):
    nsfw = reddit.subreddit('nsfw+RealGirls+LegalTeens+Boobies+palegirls+redheads+ginger+Hotchickswithtattoos+bodyperfection+PrettyGirls+suicidegirls+goddesses+altgonewild+HighResNSFW+BonerMaterial+nsfw2+SexyFrex+boobs+lingerie+sexygirls+SnowWhites+iWantToFuckHer+SexyButNotPorn+fortyfivefiftyfive+braceface+JustHotWomen+thinspo+stripgirls+Page3Glamour+Playboy+GifsOfRemoval+wet+barelylegalteens+SceneGirls+NSFW_nospam+AlbumBabes+B_Cups+shewantstofuck+Barelylegal+girlsdoingnerdythings+classysexy+Sexy+NSFW_Wallpapers+PantyPeel+UHDnsfw+peachfuzz+UnrealGirls+FuckingPerfect+redhead+TheHottestBabes+slimgirls+primes+skivvies+THEGOLDSTANDARD+SoHotItHurts+nsfw_hd+18_20+18nsfw+Hotness+BareGirls+redlingerie+Perfect_NSFW+OnlyGoodPorn+fyeahsexyteens+AmazingTeens+fuckyeahsexyteens+HotGirls+paleskin+Babes+BetterThanPorn+nsfwnonporn+countrygirls+Playboy_Albums+realperfection+TeaGirls+ThinChicksWithTits+hq_nsfw+Straps+GorgeousGirlsNSFW+DomesticGirls+RealBeauties+Sexyness+StrippingOffShirts+RiaeSuicide+nsfw_bw+nsfw_sexy_girls+BacklitBeauty+SexyGoosebumps+tattooed_redheads+Bangable+TotalBabes+BikiniTeens+Headless+Randomgirls+HotGirlsNSFW+sexynsfw+Adultpics+debs_and_doxies+nsfwonly+nsfwnew').hot()
    post_to_pick = random.randint(1, 15)

    amount=ctxnsfw

    while amount!=0:
        for i in range(0, post_to_pick):
            submission = next(x for x in nsfw if not x.stickied)

        await client.say (submission.url)
        amount-=1
        time.sleep(2)
    await client.delete_message(ctx.message)


with open('Remembers.txt', 'r') as f:
    Remembers = ast.literal_eval(f.read())
#Remembers
@client.command(pass_context=True)
async def list(context):
    data = Remembers[str(context.message.author.mention)]

    await client.say (data)

#Clear messages
@client.command(pass_context=True)
async def clear(ctx, number):
    server=ctx.message.server
    author=ctx.message.author
    role=discord.utils.get(server.roles,id=role_id)
    if role in author.roles:
        number = int(number)+1 #Converting the amount of messages to delete to an integer
        counter = 0
        async for x in client.logs_from(ctx.message.channel, limit = number):
            if counter < number:
                await client.delete_message(x)
                counter += 1
            await asyncio.sleep(0.2)
    else:
        await client.say("You are not permitted")




##!PingPongs¡
##=====================================================

##Hellos
@client.command(pass_context=True)
async def hello(context):
    hellos = ["Hello","Wazzap!!!", "May the 4th be with You,","A bit late...","Goodnight!"]
    msg = random.choice(hellos) + "{}".format(context.message.author.mention)
    print(context.message.author.mention)

    await client.say (msg)



##Connection INFO
##=====================================================
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with Space-Time"))
    print("Logged in as " + client.user.name)

async def on_member_join(member):
    role=discord.utils.get(member.server.roles,name="Regurlar")
    await client.add_roles(member,role)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(300)






client.loop.create_task(list_servers())
client.run(TOKEN)
