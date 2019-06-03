from discord.ext import commands
import discord
import random

class Basic(commands.Cog):
    def ___init___(self,client):
        self.client = client
    @commands.command(name='hello', description="Says hello", brief="Hello",
                      aliases=['hi', 'ping', 'hey'])
    async def hello(self,ctx):
        hellos = ["Hello", "Wazzap!!!", "May the 4th be with You,", "A bit late...", "Goodnight!"]
        await ctx.send(random.choice(hellos) + "{}".format(ctx.message.author.mention))

    @commands.command(name='8ball', description="Answers a yes/no question.", brief="Answers from the beyond.",
                      aliases=['eight_ball', 'eightball', '8-ball'])
    async def eight_ball(self,ctx):
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
def setup(client):
    client.add_cog(Basic(client))