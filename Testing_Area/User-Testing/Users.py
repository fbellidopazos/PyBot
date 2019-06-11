from discord.ext import commands
import discord
import sqlite3
class database():
    def __init__(self):
        self.db = sqlite3.connect("Users.db")
    def add_user(self,name,nick,role="Regular"):
        self.db.execute(f"INSERT INTO Users VALUES ('{name}','{nick}','{role}')")
class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.manageUsers = database()

        # Member Join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Adds member to
        print(member)
        print (member.display_name)
        name=str(member)
        nick=str(member.display_name)
        role="Regular"

        await member.send("```\nWelcome to The Quantum Enlightenment." +
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
        # await member.send("help")
        role = discord.utils.get(member.guild.roles, name="Regular")
        await member.add_roles(role)
        self.manageUsers.add_user(name, role)

        # Member Remove
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        self.manageUsers.remove_user(member.display_name)
        print(f'{member} has left the server')

    @commands.command(name="Users")
    async def all_users(self, ctx):
        res = self.manageUsers.to_string()
        await ctx.send(res)


def setup(bot):
    bot.add_cog(User(bot))