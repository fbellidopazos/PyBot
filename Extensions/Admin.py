from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'```prolog\nERROR:\n {type(e).__name__} - {e}```')
        else:
            await ctx.send('```prolog\nSUCCESS```')

    @commands.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'```prolog\nERROR:\n {type(e).__name__} - {e}```')
        else:
            await ctx.send('```prolog\nSUCCESS```')

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('```prolog\nSUCCESS```')

    @commands.command(name='clear',
                      description="clears messages(ADMIN ONLY)",
                      brief="clear <Integer>")
    @commands.has_role("Staff")
    async def clear(self, ctx, amount=1):
        limit=amount
        if(amount<=0):
            limit=0
        await ctx.channel.purge(limit=limit + 1)

def setup(bot):
    bot.add_cog(Admin(bot))