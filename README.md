# PyBot

<h2>Discord Bot In Python</h2>



Contents
====================================
* Commands.txt -> Doc With Help section
* PyBot-DrawIO diagram -> DrawIO Diagram with structure of program (XML and PNG)
* requirements.txt -> Python installs
* Actual program:
  * extensions folder -> Cogs
    * Admin
    * Basic
    * embeds
    * Error_Handler
    * Music
    * Utils
    * Warframe
  * PyBot - Update -> Main Program
  * Config.json -> Configuration file
## Installation
* Clone Repository(Actual Program files)
* Edit config.json
```
{
  "MAIN": {
    "TOKEN":"<Insert DISCORD Bot TOKEN>",
    "COGS" : ["extensions.Admin","extensions.Basic","extensions.embeds","extensions.Error_Handler","extensions.Music","extensions.Utils","extensions.Warframe"],
    "WELCOME_MSG" : "```\nWelcome to The Quantum Enlightenment.\n==========================================\nThe following rules you must know:\nRULES\n\nThe following Commands you may use in *BOT_SPAM*:\nCommands\n```",
    "ON_JOIN_ROLE" : "<Write Role>",
    "BOT_GAME" : "with Space-Time"
    },
  "ADMIN": {
    "CLEAR_ROLE" : "Staff"
    },
  "BASIC": {
    "JOINABLES": ["nsfw", "nitain", "catalyst", "reactor"]
    },
  "EMBEDS": {

    },
  "ERROR_HANDLER": {

    },
    "MUSIC": {
      "MUSIC_COMMANDS_CHANNEL": <Music_Bot_Spam Channel (ID)>
    },
  "UTILS": {
    "REDDIT_PRAW": {
      "CLIENT_ID" : "<Reddit ID>",
      "CLIENT_SECRET" : "<Reddit Secret>",
      "USER_AGENT" : "<Reddit Agent>"
    },
    "WOLFRAM_APPID" : "",
    "NSFW" :{
      "ROLE" : "nsfw",
      "CHANNEL" : <NSFW Channel ID(int)>,
      "RST_LIMIT" : 200,
      "SUBREDDIT" :  "<Selec6 your NSFW subrredits>"
    },
    "NEWS" : {
        "SOURCES" : ["techcrunch","ign","the-next-web","the-verge","techradar","engadget","wired"],
      "CHANNEL" : 585892474896252947,
      "API" : "<https://newsapi.org/  GET YOUR API>"
    },
    "SONGLINK" : {
      "API" : "<GET GOOGLE YT API>"
    }
  },
  "WARFRAME": {

  }
}
```

* Launch PyBot-Update.py
## Commands
```
Admin
load - Loads cog(OWNER ONLY)
unload - Unloads cog(OWNER ONLY)
reload - Reloads cog(OWNER ONLY)
help - The help command!
clear - Clears messages(ADMIN ONLY)
​
​
Basic
hello - Says hello
8ball - Answers a yes/no question from the beyond.
join - Join available joinable
leave - leave joinable
​
​
Embed
embed - The embed command
​
​
CommandErrorHandler
repeat - Repeat a given command(Owner Only)
​
​
Music
connect - Connect to a given voice channel/channel you are in
play - Play´s song given by link
pause - Pause current player
resume - Resume current player
skip - Skips current song
queue - Give the current playlist
now_playing - Current music
volume - Chanegs music volume
stop - Deletes current player
​
​
Utils
ud - Gives the definition of the input word,searched in Urban Dictionary
wolfram - Wolfram Alpha search
news - You will be updated about current affairs and breaking news daily
SongLink - Returns the youtube link to given Song Name
​
​
Warframe
warframe - Returns information about warframe
```
##
