import json
import requests
from discord.ext import commands
import discord

# https://docs.warframestat.us/#tag/worldstate/paths/~1pc/get

class Warframe(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.api="https://api.warframesstat.us/pc/"
        self.warframe_lookup=["earthCycle","cetusCycle","vallisCycle","constructionProgress","fissures","sortie","events"]

    def get_json(self,key):
        j = requests.get(f"{self.api}{key}",timeout=5)
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
        elif(key.lower()=="vallis"):
            data = self.get_json(self.warframe_lookup[2])
            title = "Vallis Cycle"
            description = f"Current State: "+data["state"]+"\nTime left: "+data["shortString"]
        elif (key.lower() == "razorback" or key.lower()=="fomorian"):
            data = self.get_json(self.warframe_lookup[3])
            title = "RazorBack/Fomorian Progress"
            description = "Fomorian Progress: "+data["fomorianProgress"]+" %\nRazorBack Progress: "+data["razorbackProgress"]+" %"
        elif(key.lower()=="fissures"):
            data=self.get_json(self.warframe_lookup[4])
            description = ""
            title = "Fissures"
            for i in data:
                description += "Node: " + i["node"] + "\nMission Type: " + i["missionType"] + "\nEnemy: " + i["enemy"]+"\nRelic Type: " + i["tier"] + "\nTime Left: " + i["eta"] + "\n\n"
        elif(key.lower()=="sortie"):
            data=self.get_json(self.warframe_lookup[5])
            description = "Boss: " + data["boss"] + "\nFaction: " + data["faction"] + "\nTime Left: " + data[
                "eta"] + "\n\n"
            for i in data["variants"]:
                description += "Node: " + i["node"] + "\nMission Type: " + i["missionType"] + "\nModifier: " + i[
                    "modifier"] + "\nModifier Description: " + i["modifierDescription"] + "\n\n"
        elif(key.lower()=="events"):
            data=self.get_json(self.warframe_lookup[6])
            description=""
            for i in range(len(data)):
                description+=data[i]["asString"]


        await ctx.send(embed=self.generate_embed(ctx,title,description,img_url),content=None)


def setup(bot):
    bot.add_cog(Warframe(bot))
