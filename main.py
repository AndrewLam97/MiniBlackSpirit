import settings
import discord
import os

import input_parser
import sanitizer

client = discord.Client()

print("Logging in...")
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$next':
        await message.channel.send(input_parser.parse(message.content))

    if message.content == '$help':
        await message.channel.send("$next displays the upcoming boss \n$showme _________ displays all upcoming instances of the specified boss")
    
    if message.content == '$test':
        await message.channel.send(input_parser.parse(message.content))

    if message.content.startswith('$showme'):
        await message.channel.send(input_parser.parse_showme(message.content))

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

client.run(settings.DISCORD_TOKEN)
