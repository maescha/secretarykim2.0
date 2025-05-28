import discord
import logging
import os
from dotenv import load_dotenv

import requests
import json

load_dotenv()
bot_token= os.getenv('DISCORDTOKEN')
# print(bot_token)

## basic logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

## getting memes from memeapi // meme-api.com/gimme
def get_meme():
  response = requests.get('https://meme-api.com/gimme/wholesomememes')
  json_data = json.loads(response.text)
  return json_data['url']

## getting people names from tv api
def get_people_print_multiple(who):
    response = requests.get(f'https://api.tvmaze.com/search/people{who}')
    json_data = json.loads(response.text)

    if not json_data:
        return 'no names found in database matching what was inputted into the chat'

    results_names = []
    for item_dict in json_data[:5]:
        if 'person' in item_dict and 'name' in item_dict['person']:
            results_names.append(item_dict['person']['name'])

    if results_names:
        return ', '.join(results_names) # Returns a string of names separated by commas
    else:
        return 'no suitable names found in the first 5 items'

## Logging on into server as the bot
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  # Responding to Messages
  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('`hello'):
      await message.channel.send('# Hello World :earth_americas:')
      await message.channel.send(f'-# **and hello {message.author.display_name}!** :wave:')

    if message.content.startswith('`meme'):
      await message.channel.send(get_meme())

    if message.content.startswith('`ping'):
      await message.channel.send('pong!')

    if message.content.startswith('`poll'):
      # removes the `poll text in the title
      title_content = message.content[len('`poll'):].strip()

      embed = discord.Embed(title=title_content, description='I, Secretary Kim, have voted once in both choices.')
      poll_message = await message.channel.send(embed=embed)
      await poll_message.add_reaction('👍')
      await poll_message.add_reaction('👎')

    if message.content.startswith('`ppl'):
      search_text = '?q=' + message.content[len('`ppl'):].strip()
      await message.channel.send(get_people_print_multiple(search_text))

## intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.polls = True

client = MyClient(intents=intents)
client.run(bot_token, log_handler=handler, log_level=logging.DEBUG)

