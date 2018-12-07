@client.command(pass_context=True)
async def wolfram(self,ctx):
    url = 'http://api.wolframalpha.com/v1/simple?appid=UQ2PAA-Y2QK6KVRA9&i={}'.format(ctx)

    await client.say (url)
    await client.say (ctx)
