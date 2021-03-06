import pyshorteners
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import praw
import pafy
import json

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


with open("config.json", 'r') as f:
    config = json.load(f)
# https://scrolller.com/nsfw-subreddits
reddit = praw.Reddit(client_id=str(config["UTILS"]["REDDIT_PRAW"]["CLIENT_ID"]),
                     client_secret=str(config["UTILS"]["REDDIT_PRAW"]["CLIENT_SECRET"]),
                     user_agent=str(config["UTILS"]["REDDIT_PRAW"]["USER_AGENT"]))
already_done = []
subreddit = reddit.subreddit(str(config["UTILS"]["NSFW"]["SUBREDDIT"]))

class Utils(commands.Cog):
    def ___init___(self, bot):

        self.client = bot


    @commands.command(name='ud',
                description="Gives the definition of the input word,searched in Urban Dictionary",
                brief="ud <word>")
    async def urban(self,ctx, word):
        source = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word))
        soup = BeautifulSoup(source.content, "html.parser")
        msg = soup.find("div",attrs={"class":"meaning"}).text
        await ctx.send(str(msg))

    @commands.command(name='wolfram',
                      description="Wolfram Alpha search",
                      brief="wolfram <query>")
    async def wolfram(self,ctx, *,query):
        url = "http://api.wolframalpha.com/v1/simple?appid="+config["UTILS"]["WOLFRAM_APPID"]+"&i={}".format(
            (query.replace(" ", "%20")).replace("+", "%2B"))
        await ctx.send(url)

    @commands.command(name='nsfw',
                    description="Basically PORN",
                    brief="nsfw <amount>(optional)",
                    aliases=["porn"]
                      )
    @commands.has_role(str(config["UTILS"]["NSFW"]["ROLE"]))
    async def nsfw(self,ctx,amount=1):
        channel=ctx.bot.get_channel(config["UTILS"]["NSFW"]["CHANNEL"])
        await ctx.channel.purge(limit=1)
        while True:
            i = amount
            for submission in subreddit.hot():
                if submission.id not in already_done:
                    url = submission.url
                    await channel.send(url)
                    already_done.append(submission.id)
                    i -= 1
                    if (len(already_done) >= config["UTILS"]["NSFW"]["RST_LIMIT"]):
                        del already_done[:]

                if (i <= 0):

                    break
            break
    
    @commands.command(name="news",
                      description="You will be updated about current affairs and breaking news daily",
                      brief="Get the daily news" ,
                      aliases=["techlinked","daily"])
    async def get_news(self,ctx):

        s = pyshorteners.Shortener()
        sources = config["UTILS"]["NEWS"]["SOURCES"]

        channel = ctx.bot.get_channel(config["UTILS"]["NEWS"]["CHANNEL"])
        res = ""
        for i in (sources):
            get_news = ''
            news = requests.get(f"https://newsapi.org/v2/top-headlines?sources={i}&apiKey={config['UTILS']['NEWS']['API']}")
            data = news.json()
            title = data["articles"][0]["title"]
            description = data["articles"][0]["description"]
            link = data["articles"][0]["url"]
            flink = s.short(link)
            get_news += "*" + title + " :* _" + description + "_ \n" + flink + "\n\n"
            await channel.send(get_news)

    @commands.command(name="SongLink",description="Returns the youtube link to given Song Name",aliases=["song","songlinked","linksong"])
    async def song_link(self,ctx,*,song_name):

        s = pyshorteners.Shortener()

        song_name = song_name + " song"

        url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + song_name +"&key=" + config["UTILS"]["SONGLINK"]["API"] + "&maxResults=1&type=video"
        page = requests.get(url)
        data = page.json()
        sear = data["items"][0]["id"]["videoId"]
        title = data["items"][0]["snippet"]["title"]

        myaud = pafy.new(sear)
        genlink = myaud.audiostreams[2].url
        vlink = "https://www.youtube.com/watch?v=" + sear


        vlink = s.short(vlink)
        await ctx.send(title+"\n"+vlink)

    @commands.command(name="tldrl",description="Summarises the text in a given link",aliases=[])
    async def tldrl(self,ctx,url : str):
        LANGUAGE = "english"
        SENTENCES_COUNT = 5
        res = ""
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        # or for plain text files
        # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            res += f"\n{sentence}"
        await ctx.send(res)

    @commands.command(name="tldrt", description="Summarises the text in a given bunch of text", aliases=[])
    async def tldrt(self,ctx,text):
        create_doc(text)
        LANGUAGE = "english"
        SENTENCES_COUNT = 5
        res = ""
        parser = PlaintextParser.from_file("tldr.txt", Tokenizer(LANGUAGE))
            # or for plain text files
            # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            res += f"\n{sentence}"
        await ctx.send( res)


def create_doc(text:str):
    f= open("tldr.txt","w+")
    f.write(text)
    f.close

def setup(client):
    client.add_cog(Utils(client))
