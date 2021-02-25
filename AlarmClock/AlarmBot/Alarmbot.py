import discord
import time
import datetime
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return



    if message.content.startswith('!remind'):
        x = message.content
        y = x.split()
        while True:
            z = datetime.datetime.now()
            w = z.strftime("%I:%M%p")
            if w == y[-1]:
                output = ''.join(y[1:-1])
                await message.channel.send(output)
                break
            else:
                continue

client.run('__token_here__')
