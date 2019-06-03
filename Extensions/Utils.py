from discord.ext import commands
from discord.utils import *
import discord
from bs4 import BeautifulSoup
import requests
import praw
import time
import random

reddit = praw.Reddit(client_id='StI7zL-mxlm2HQ',
                             client_secret='lUkCF66UgqEJgE03JkkAkXWQzKA',
                             user_agent='PyBotNSFW')

class Utils(commands.Cog):
    def ___init___(self,client):
        self.client = client

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
                    brief="command: nsfw")
    @commands.has_role("nsfw")
    async def nsfw(self,ctx,amount=1):
        nsfw = reddit.subreddit('nsfw+RealGirls+LegalTeens+Boobies+palegirls+redheads+ginger+Hotchickswithtattoos+bodyperfection+PrettyGirls+suicidegirls+goddesses+altgonewild+HighResNSFW+BonerMaterial+nsfw2+SexyFrex+boobs+lingerie+sexygirls+SnowWhites+iWantToFuckHer+SexyButNotPorn+fortyfivefiftyfive+braceface+JustHotWomen+thinspo+stripgirls+Page3Glamour+Playboy+GifsOfRemoval+wet+barelylegalteens+SceneGirls+NSFW_nospam+AlbumBabes+B_Cups+shewantstofuck+Barelylegal+girlsdoingnerdythings+classysexy+Sexy+NSFW_Wallpapers+PantyPeel+UHDnsfw+peachfuzz+UnrealGirls+FuckingPerfect+redhead+TheHottestBabes+slimgirls+primes+skivvies+THEGOLDSTANDARD+SoHotItHurts+nsfw_hd+18_20+18nsfw+Hotness+BareGirls+redlingerie+Perfect_NSFW+OnlyGoodPorn+fyeahsexyteens+AmazingTeens+fuckyeahsexyteens+HotGirls+paleskin+Babes+BetterThanPorn+nsfwnonporn+countrygirls+Playboy_Albums+realperfection+TeaGirls+ThinChicksWithTits+hq_nsfw+Straps+GorgeousGirlsNSFW+DomesticGirls+RealBeauties+Sexyness+StrippingOffShirts+RiaeSuicide+nsfw_bw+nsfw_sexy_girls+BacklitBeauty+SexyGoosebumps+tattooed_redheads+Bangable+TotalBabes+BikiniTeens+Headless+Randomgirls+HotGirlsNSFW+sexynsfw+Adultpics+debs_and_doxies+nsfwonly+nsfwnew').hot()
        post_to_pick = random.randint(1, 30)
        channel=ctx.bot.get_channel(461240565980463128)
        await ctx.channel.purge(limit=1)
        while amount != 0:
            for i in range(0, post_to_pick):
                submission = next(x for x in nsfw if not x.stickied)
            await channel.send(submission.url)
            amount -= 1
            # time.sleep(2)
        # await ctx.message.delete(ctx.message)


def setup(client):
    client.add_cog(Utils(client))
