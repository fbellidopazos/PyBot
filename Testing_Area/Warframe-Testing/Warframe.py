import json
import requests

def get_json(key):
    j = requests.get(f"{api}{key}")
    return json.loads(j.text)
api="https://api.warframestat.us/pc/"
warframe_lookup=["earthCycle","cetusCycle","vallisCycle","constructionProgress","fissures","sortie"]



data = get_json(warframe_lookup[1])
'''
embed = discord.Embed(
            title=Earth,
            description=desc,
            color=random.choice(color_list)
        )
        # Also set the thumbnail to be the bot's pfp
        embed.set_thumbnail(url=self.bot.user.avatar_url)
'''
print(f"Current Cycle: "+data["state"]+"\nTime left: "+data["shortString"])