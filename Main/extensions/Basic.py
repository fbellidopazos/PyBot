from discord.ext import commands
import discord
import random

from scipy.optimize._tstutils import description


class Basic(commands.Cog):
    def ___init___(self,client):
        self.client = client


    @commands.command(name='hello', description="Says hello", brief="Hello",
                      aliases=['hi', 'ping', 'hey'])
    async def hello(self,ctx):
        hellos = ["Hello", "Wazzap!!!", "May the 4th be with You,", "A bit late...", "Goodnight!"]
        await ctx.send(random.choice(hellos) + "{}".format(ctx.message.author.mention))

    @commands.command(name='8ball', description="Answers a yes/no question from the beyond.", brief="Answers from the beyond.",
                      aliases=['eight_ball', 'eightball', '8-ball'])
    async def eight_ball(self,ctx,*,etc):
        possible_responses = ["It is certain.",
                              "It is decidedly so.",
                              "Without a doubt.",
                              "Yes - definitely.",
                              "You may rely on it.",
                              "As I see it, yes.",
                              "Most likely.",
                              "Outlook good.",
                              "Yes.",
                              "Signs point to yes.",
                              "Reply hazy, try again.",
                              "Ask again later.",
                              "Better not tell you now.",
                              "Cannot predict now.",
                              "Concentrate and ask again.",
                              "Don't count on it.",
                              "My reply is no.",
                              "My sources say no.",
                              "Outlook not so good.",
                              "Very doubtful."]
        await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)


    @commands.command(name="join",description="Join available joinable",brief="join <joinable>")
    async def join(self,ctx,arg="list"):
        joinables = ["nsfw", "nitain", "catalyst", "reactor"]
        if(arg.lower() in joinables):
            role = discord.utils.get(ctx.guild.roles, name=str(arg))
            user = ctx.message.author
            await user.add_roles(role)
        elif(arg.lower()=="list"):
            res = ""
            for i in joinables:
                res = res + "\n" + str(i)
            await ctx.send(res)


    @commands.command(name="leave",description="leave joinable",brief="leave <joinable>")
    async def leave(self,ctx,arg="list"):

        joinables = ["nsfw", "nitain", "catalyst", "reactor"]
        if(arg.lower() in joinables):
            user = ctx.message.author
            role = discord.utils.get(ctx.guild.roles, name=str(arg))
            await user.remove_roles(role)
        elif(arg.lower()=="list"):
            res = ""
            for i in joinables:
                res = res + "\n" + str(i)
            await ctx.send(res)


def setup(client):
    client.add_cog(Basic(client))