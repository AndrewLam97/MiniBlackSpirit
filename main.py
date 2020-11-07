import settings
import discord
import os
import sched
import asyncio
import time
from discord.ext.tasks import loop

import input_parser
import sanitizer
import boss_timer

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

    if message.content == '$test1':
        await message.channel.send(input_parser.parse(message.content))

    if message.content.startswith('$showme'):
        await message.channel.send(input_parser.parse_showme(message.content))

    if message.content.startswith('$enhance'):
        await message.channel.send(input_parser.parse_enhancement_sim(message.content))

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

@loop(seconds=1)
async def poll_boss_time():
    remaining_time = await boss_timer.till_next_boss_async()

    # Gracefully stops current tasks that aren't supposed to be running at certain time intervals
    if remaining_time[1] == 0 and remaining_time[2] < 15 and alert_hour.is_running():
        alert_hour.stop()
    elif remaining_time[1] == 0 and remaining_time[2] < 2  and alert_min.is_running():
        alert_min.stop()
    elif remaining_time[1] == 0 and remaining_time[2] < 1 and alert_sec.is_running():
        alert_sec.stop()

    # Run boss timer alerts
    if (remaining_time[1] == 1 and remaining_time[2] == 0) or (remaining_time[1] == 0 and remaining_time[2] >= 30) and not alert_hour.is_running():
        if alert_sec.is_running():
            alert_sec.cancel()  # forcefully stop if it has not been stopped yet
        alert_hour.start()      # runs at most two times, between 60 and 30 minutes remaining
    elif remaining_time[1] == 0 and remaining_time[2] <= 15 and remaining_time[2] > 1 and not alert_min.is_running():
        if alert_hour.is_running():
            alert_hour.cancel()
        alert_min.start()       # runs at most three times, between 15 and 2 minutes remaining
    elif remaining_time[1] == 0 and remaining_time[2] == 1 and not alert_sec.is_running():
        if alert_min.is_running():
            alert_min.cancel()
        alert_sec.start()  # runs once on last minute, but needs to be on a separate function with count=1 to prevent spamming (poll_boss_time() runs every second)

@poll_boss_time.before_loop
async def before_poll_boss_time():
    print('Waiting until client is ready before running boss timer scheduler...')
    await client.wait_until_ready()

@loop(minutes=30, count=2)
async def alert_hour():
    get_boss_time = await boss_timer.till_next_boss_async()
    channel = client.get_channel(761151710097571862)
    if get_boss_time[1] == 1 and get_boss_time[2] == 0:
        await channel.send(str(get_boss_time[0]) + ' in 1 hour.')
    else:
        await channel.send(str(get_boss_time[0]) + ' in ' + str(get_boss_time[2]) + ' minutes.')

@loop(minutes=5, count=2)
async def alert_min():
    get_boss_time = await boss_timer.till_next_boss_async()
    channel = client.get_channel(761151710097571862)
    await channel.send(str(get_boss_time[0]) + ' in ' + str(get_boss_time[2]) + ' minutes.')

@loop(seconds=1, count=1)
async def alert_sec():
    get_boss_time = await boss_timer.till_next_boss_async()
    channel = client.get_channel(761151710097571862)
    await channel.send(str(get_boss_time[0]) + ' in less than a minute.')

poll_boss_time.start()
client.run(settings.DISCORD_TOKEN)
