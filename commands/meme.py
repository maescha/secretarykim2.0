import discord
import requests
import json

## getting memes from memeapi
def __get_meme():
  response = requests.get('https://meme-api.com/gimme/wholesomememes')
  json_data = json.loads(response.text)
  return json_data['url']

async def command_meme(message):
  await message.channel.send(__get_meme())