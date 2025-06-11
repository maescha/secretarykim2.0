import discord

async def command_ping(message):
  await message.channel.send('pong!')
