import json
import requests

def get_json(key):
    j = requests.get(f"{api}{key}")
    return json.loads(j.text)
api="https://api.warframestat.us/pc/"
warframe_lookup=["earthCycle","cetusCycle","vallisCycle","constructionProgress","fissures","sortie"]



data = get_json(warframe_lookup[5])
'''
embed = discord.Embed(
            title=Earth,
            description=desc,
            color=random.choice(color_list)
        )
        # Also set the thumbnail to be the bot's pfp
        embed.set_thumbnail(url=self.bot.user.avatar_url)
'''
print(data)
data["boss"]
data["faction"]
data["eta"]
data["variants"]
description="Boss: "+data["boss"]+"\nFaction: "+data["faction"]+"\nTime Left: "+data["eta"]+"\n\n"
for i in data["variants"]:
    description +="Node: " + i["node"]+ "\nMission Type: " + i["missionType"] + "\nModifier: " + i["modifier"] + "\nModifier Description: " + i["modifierDescription"]  + "\n\n"
print(description)
# print("Fomorian Progress: "+data["fomorianProgress"]+" %\nRazorBack Progress: "+data["razorbackProgress"]+" %")
