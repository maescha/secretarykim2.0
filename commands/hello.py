import discord

async def command_hello(message):
    await message.channel.send('# Hello World :earth_americas:')
    await message.channel.send(f'-# **and hello {message.author.display_name}!** :wave:')


