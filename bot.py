import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot_token= os.getenv('DISCORDTOKEN')
# print(bot_token)

## Logging on into server as the bot

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(bot_token) 

