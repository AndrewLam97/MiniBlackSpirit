import settings
import discord
import os

client = discord.Client()

print("Logging in...")
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$test'):
        await message.channel.send('Test Successful')
        print(">Test successful")

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

client.run(settings.DISCORD_TOKEN)
