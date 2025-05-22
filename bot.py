import discord
import logging
import os
from dotenv import load_dotenv

load_dotenv()
bot_token= os.getenv('DISCORDTOKEN')
# print(bot_token)

## basic logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

## Logging on into server as the bot
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

## intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
# intents.typing = False
# intents.presences = False

client = MyClient(command_prefix='!', intents=intents)
client.run(bot_token, log_handler=handler, log_level=logging.DEBUG) 

# Responding to Messages
# async def on_message(self, message):
#   if message.author == self.user:
#     return

#   if message.content.startswith('$hello'):
#     await message.channel.send('Hello World!')
