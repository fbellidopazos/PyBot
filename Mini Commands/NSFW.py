reddit = praw.Reddit(client_id='StI7zL-mxlm2HQ',
                     client_secret='lUkCF66UgqEJgE03JkkAkXWQzKA',
                     user_agent='PyBotNSFW')

@client.command(pass_context = True)
async def nsfw():
    nsfw = reddit.subreddit('RealGirls+LegalTeens+Boobies+TinyTits+redheads+lingerie+stripgirls+FuckingPerfect+HotGirlsNSFW').hot()
    post_to_pick = random.randint(1, 1000)
    for i in range(0, post_to_pick):
        submission = next(x for x in nsfw if not x.stickied)

    await client.say(submission.url)
