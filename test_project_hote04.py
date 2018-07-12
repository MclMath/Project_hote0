#Petit test pour voir le bon fonctionnement d'un code simple.
import discord
import asyncio


client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Do you know where you are?'):
        msg = 'Yes. {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('Where are we?'):
        msg2 = 'I am in a dream.'.format(message)
        await client.send_message(message.channel, msg2)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('token')
