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

        if message .content.lower().startswith('happy'):
            await message.channel.send('Aye sir!')
       
        elif message .content.lower().startswith("let's") or message .content.lower().startswith("lets"):
            await message.channel.send('Aye sir!)
       
        elif 'haha' in message.content.lower():# or 'HAHA' in message.content or 'haha' in message.content:
            await message.channel.send("THAT's FUNNY!😂️")     

        elif 'sad' in message.content.lower():
            await message.channel.send('Dont be sad, be Happy!')

        elif message.content.lower().startswith('oop') or ' oop' in message.content.lower():
            await message.channel.send('Sksksksk (>o<)')

        elif 'ówò'  in message.content.lower():
            await message.channel.send('UwU')   
        
        elif 'yeet'  in message.content.lower():
            await message.channel.send('YEET')
        
        elif 'goog'  in message.content.lower():
            await message.channel.send('goog jog')
        
        elif "i'm new"  in message.content.lower() or "i am new"  in message.content.lower():
            await message.channel.send('Hello and welcome to the SERVER :)')

       
           
     
if __name__ == '__main__':
    client = MyClient()
    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Game(name="Catch The Fish 🐟️"))
        print('Bot Is Ready')
        
    client.run(BOT_TOKEN)  

