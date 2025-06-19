import discord

async def command_poll(message):
  # removes the `poll text in the title
  title_content = message.content[len('poll'):].strip()
  embed = discord.Embed(title=title_content, description='I, Secretary Kim, have voted once in both choices.')
  poll_message = await message.channel.send(embed=embed)
  await poll_message.add_reaction('👍')
  await poll_message.add_reaction('👎')