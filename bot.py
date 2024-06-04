import discord
from discord.ext import tasks

client = discord.Client(intents=discord.Intents.default())
message = "Is it your birthday today, Alyx?"

# channel ID
with open('id.txt', 'r') as file:
    id = file.read().rstrip()

# Static token
with open('id.txt', 'r') as file:
    token = file.read().rstrip()

# Scheduled messages
@tasks.loop(hours=23.0)
async def send_message():
    channel = client.get_channel(id)
    await channel.send(message)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await send_message.start()

client.run(token)
