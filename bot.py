import discord
import requests

client = discord.Client()
prefix = "!"
    


            

async def id(message):
    await message.channel.send(str(message.author.name) + ": " + str(message.author.id))
async def ping(message):
    await message.channel.send ("pong")
async def prefixChange(message, command, content):
    if content == "" or content == " ":
        await message.channel.send ("That is not a valid prefix.")
    else:
        if len(content) == 1:
            prefix = content
            message.channel.send ("Prefix Changed")
        else:
            await message.channel.send ("That is not a valid prefix.")
async def get_btc_price():
    response = requests.get("https://www.bitstamp.net/api/ticker/")
    data = response.json()
    return data["last"]
    await message.channel.send (data)

   

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(prefix):
        text = message.content[1:]
        command = text.split(" ", 1)[0]
        content = text.split(" ", 1)[1]

        await commandList = {
            "id": id(message),
            "ping": ping(message),
            "prefix": prefixChange(message, command, content),
            "bitcoinPrice": get_btc_price(),
        }


        if command in commandList:
            await commandList[command]

client.run('NzIzMDEwOTAxOTAwMjYzNDU3.XuraXw.5l1bemftEf9J87ddVAr-n62qbD0')

