import pyshorteners
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import praw
import random
from time import sleep
import pafy

reddit = praw.Reddit(client_id='StI7zL-mxlm2HQ',
                             client_secret='lUkCF66UgqEJgE03JkkAkXWQzKA',
                             user_agent='PyBotNSFW')

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
        url = 'http://api.wolframalpha.com/v1/simple?appid=UQ2PAA-Y2QK6KVRA9&i={}'.format(
            (query.replace(" ", "%20")).replace("+", "%2B"))
        await ctx.send(url)

    @commands.command(name='nsfw',
                    description="Basically PORN",
                    brief="nsfw <amount>(optional)")
    @commands.has_role("nsfw")
    async def nsfw(self,ctx,amount=1):
        nsfw = reddit.subreddit('nsfw+RealGirls+LegalTeens+Boobies+palegirls+redheads+ginger+Hotchickswithtattoos+bodyperfection+PrettyGirls+suicidegirls+goddesses+altgonewild+HighResNSFW+BonerMaterial+nsfw2+SexyFrex+boobs+lingerie+sexygirls+SnowWhites+iWantToFuckHer+SexyButNotPorn+fortyfivefiftyfive+braceface+JustHotWomen+thinspo+stripgirls+Page3Glamour+Playboy+GifsOfRemoval+wet+barelylegalteens+SceneGirls+NSFW_nospam+AlbumBabes+B_Cups+shewantstofuck+Barelylegal+girlsdoingnerdythings+classysexy+Sexy+NSFW_Wallpapers+PantyPeel+UHDnsfw+peachfuzz+UnrealGirls+FuckingPerfect+redhead+TheHottestBabes+slimgirls+primes+skivvies+THEGOLDSTANDARD+SoHotItHurts+nsfw_hd+18_20+18nsfw+Hotness+BareGirls+redlingerie+Perfect_NSFW+OnlyGoodPorn+fyeahsexyteens+AmazingTeens+fuckyeahsexyteens+HotGirls+paleskin+Babes+BetterThanPorn+nsfwnonporn+countrygirls+Playboy_Albums+realperfection+TeaGirls+ThinChicksWithTits+hq_nsfw+Straps+GorgeousGirlsNSFW+DomesticGirls+RealBeauties+Sexyness+StrippingOffShirts+RiaeSuicide+nsfw_bw+nsfw_sexy_girls+BacklitBeauty+SexyGoosebumps+tattooed_redheads+Bangable+TotalBabes+BikiniTeens+Headless+Randomgirls+HotGirlsNSFW+sexynsfw+Adultpics+debs_and_doxies+nsfwonly+nsfwnew').hot()
        post_to_pick = random.randint(1, 30)
        channel=ctx.bot.get_channel(461240565980463128)
        await ctx.channel.purge(limit=1)
        while amount > 0:
            for i in range(0, post_to_pick):
                submission = next(x for x in nsfw if not x.stickied)
            await channel.send(submission.url)
            sleep(2)
            amount -= 1
    
    @commands.command(name="news",description="You will be updated about current affairs and breaking news daily",brief="Get the daily news")
    async def get_news(self,ctx):

        s = pyshorteners.Shortener()
        sources =["techcrunch","mashable","the-next-web","the-verge","techradar","engadget","wired"]

        channel = ctx.bot.get_channel(585892474896252947)

        for i in range(len(sources)):
            get_news = ''
            news = requests.get(f"https://newsapi.org/v2/top-headlines?sources={sources[i]}&apiKey=062f6f4c9afb4d15b5d34fe36f89c969")
            data = news.json()
            title = data["articles"][0]["title"]
            description = data["articles"][0]["description"]
            link = data["articles"][0]["url"]
            flink = s.short(link)
            # flink = flink["url"]
            get_news += "*" + title + " :* _" + description + "_ \n" + flink + "\n\n"
            await channel.send(get_news)

    @commands.command(name="SongLink",description="Returns the youtube link to given Song Name",aliases=["song","songlink","linksong"])
    async def song_link(self,ctx,*,song_name):

        s = pyshorteners.Shortener()

        song_name = song_name + " song"

        url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + song_name +"&key=" + "AIzaSyAVcy7mHQ983VrWmmRIbMf6In2bj08dSOg" + "&maxResults=1&type=video"
        page = requests.get(url)
        data = page.json()
        sear = data["items"][0]["id"]["videoId"]
        title = data["items"][0]["snippet"]["title"]

        myaud = pafy.new(sear)
        genlink = myaud.audiostreams[2].url
        vlink = "https://www.youtube.com/watch?v=" + sear


        vlink = s.short(vlink)
        await ctx.send(title+"\n"+vlink)



def setup(client):
    client.add_cog(Utils(client))
