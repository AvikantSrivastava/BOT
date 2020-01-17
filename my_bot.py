import discord
import asyncio
from discord.ext.commands import Bot
from discord import Game

from discord.ext import commands



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
   

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('happy') or message.content.startswith('Happy') or message.content.startswith('HAPPY'):
            await message.channel.send('Aye sir!'.format(message))
       
        elif message.content.startswith("Let's") or message.content.startswith("let's"):
            await message.channel.send('Aye sir!'.format(message))
       
        elif 'Haha' in message.content or 'HAHA' in message.content or 'haha' in message.content:
            await message.channel.send("LOL 😂️".format(message))     

        elif 'sad'  in message.content or 'Sad'  in message.content or 'SAD'  in message.content:
            await message.channel.send('Dont be sad, be Happy!'.format(message))

        elif 'Oop'  in message.content or 'oop'  in message.content or 'OOP'  in message.content:
            await message.channel.send('Sksksksk'.format(message))

        elif 'ÓwÒ'  in message.content or 'ówò'  in message.content in message.content:
            await message.channel.send('UwU'.format(message))   
        
        elif 'yeet'  in message.content or 'Yeet'  in message.content or 'YEET'  in message.content:
            await message.channel.send('YEET'.format(message))
        
        elif 'goog'  in message.content or 'Goog'  in message.content or 'GOOG'  in message.content:
            await message.channel.send('goog jog'.format(message))
        
        elif "I'm new"  in message.content or "i'm new"  in message.content or 'i am new'  in message.content:
            await message.channel.send('Hello and welcome to Chill Corner! :)'.format(message))

           
       


client = MyClient()
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Catch The Fish 🐟️"))

    #print('Bot Is Ready')

client.run(TOKEN_HERE)   
