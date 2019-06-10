import json
import requests
from discord.ext import commands
import discord

# https://docs.warframestat.us/#tag/worldstate/paths/~1pc/get

class Warframe(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.api="https://api.warframestat.us/pc/"
        self.warframe_lookup=["earthCycle","cetusCycle","vallisCycle","constructionProgress","fissures","sortie"]

    def get_json(self,key):
        j = requests.get(f"{self.api}{key}")
        return json.loads(j.text)
    def generate_embed(self,ctx,title,description,img_url):
        embed = discord.Embed(
            title=title,
            description=description,
        )
        # Also set the thumbnail to be the bot's pfp
        embed.set_thumbnail(url=img_url)

        # Also set the embed author to the command user
        embed.set_author(
            name=ctx.message.author.name,
            icon_url=ctx.message.author.avatar_url
        )
        return embed
    @commands.command(name="warframe",description="Returns information about warframe")
    async def Warframe(self,ctx,*,key="list"):
        title=""
        description=""
        img_url=self.bot.user.avatar_url
        if(key=="list"):
            title="warframe <command>"

            for i in ["earth","cetus","vallis","razorback/fomorian","fissures","sortie"]:
                description+=i+"\n"

        elif(key.lower()=="earth"):
            data = self.get_json(self.warframe_lookup[0])
            title="Earth Cycle"
            description=f"Current Cycle: "+data["state"]+"\nTime left: "+data["timeLeft"]

        elif(key.lower()=="cetus"):
            data = self.get_json(self.warframe_lookup[1])
            title = "Cetus Cycle"
            description = f"Current Cycle: "+data["state"]+"\nTime left: "+data["shortString"]



        await ctx.send(embed=self.generate_embed(ctx,title,description,img_url),content=None)


def setup(bot):
    bot.add_cog(Warframe(bot))