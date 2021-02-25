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
        print(y)
        while True:
            z = datetime.datetime.now()
            w = z.strftime("%I:%M%p")
            print(w) # just for debugging purposes
            if w == y[-1]:
                output = ''.join(y[1:-1])
                print(output)
                await message.channel.send(output)
                break
            else:
                continue


client.run('__token_here___')

