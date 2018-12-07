@client.command(pass_context = True)
async def command(ctx, number):
    server=ctx.message.server
    author=ctx.message.author
    role=discord.utils.get(server.roles,id=role_id)
    if role in author.roles:
        #Commands Here
    else:
        await client.say("You are not permitted")
