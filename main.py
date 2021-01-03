import settings
import discord
import os

import input_parser
import sanitizer
from bdo_embed import *

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
        await message.channel.send("$next displays the upcoming boss. \n$showme boss_name displays all upcoming instances of the specified boss.")
    
    if message.content == '$schedule':
        await message.channel.send(input_parser.parse(message.content))

    if message.content == '$test':
        await message.channel.send(input_parser.parse(message.content))

    if message.content.startswith('$showme'):
        await message.channel.send(input_parser.parse_showme(message.content))

    if message.content.startswith('$enhance'):
        await message.channel.send(input_parser.parse_enhancement_sim(message.content))

    if message.content.startswith('$tpoop'):
        embed = BDOembed(message, "Black Spirit", "Hiya, I'm gonna be in you forever!", 0, ["Height", "Color", "Favorite food"], ["2'5\"", "Black", "Equipment"], "./assets/BlackSpiritChibi.jpg")
        await embed.sendMessage()

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

client.run(settings.DISCORD_TOKEN)
