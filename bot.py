import discord
import logging
import os
from dotenv import load_dotenv

from commands.hello import command_hello
from commands.ping import command_ping
from commands.meme import command_meme
from commands.ppl import command_ppl
from commands.poll import command_poll

load_dotenv()
bot_token= os.getenv('DISCORDTOKEN')
# print(bot_token)

## basic logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

def is_command(message, command):
  return message.content.startswith(f"`{command}")

## Logging on into server as the bot
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  # Responding to Messages
  async def on_message(self, message):
    if message.author == self.user:
      return

    if is_command(message, 'hello'):
      await command_hello(message)
    elif is_command(message, 'meme'):
      await command_meme(message)
    elif is_command(message, 'ping'):
      await command_ping(message)
    elif is_command(message, 'poll'):
      await command_poll(message)
    elif is_command(message, 'ppl'):
      await command_ppl(message)


## intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.polls = True

client = MyClient(intents=intents)
client.run(bot_token, log_handler=handler, log_level=logging.DEBUG)

