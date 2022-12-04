#   Project Name: SDev Discord Bot Base
#   Date: 10/1/2022
#   Updated: 10/1/2022
#   Created By: Spencer Lynch
#   Contact: Contact@SpencerLynch.us
#
#   Licensed under the MIT License


import discord
import botcommands
import requests

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:  # If the message is from the bot, then don't reply.
        return

    else:  # If it is not from the bot, we pass it to the Bot Commands.
        await message.channel.send(botcommands.bot_commands(message))


client.run('Your Token')
