import settings
import discord
import os
import sched
import asyncio
import time

import input_parser
import sanitizer

client = discord.Client()

 = 

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
    
    if message.content == '$test':
        await message.channel.send(input_parser.parse(message.content))

    if message.content.startswith('$showme'):
        await message.channel.send(input_parser.parse_showme(message.content))

    if message.content.startswith('$enhance'):
        await message.channel.send(input_parser.parse_enhancement_sim(message.content))

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

async def my_background_task():
    await client.wait_until_ready()
    
    # failstacking channel
    channel_id = 761151710097571862

    channel = client.get_channel(channel_id)

    while not client.is_closed():
        
        await channel.send('Deez Nuts')
        await asyncio.sleep(5)

    # while not client.is_closed():
    #     counter += 1
    #     s = sched.scheduler(time.perf_counter, asyncio.sleep)
    #     args = (channel.send(counter), )
    #     s.enter(5, 1, client.loop.create_task, args)
    #     s.run()
    #     await 

client.loop.create_task(my_background_task())
client.run(settings.DISCORD_TOKEN)
