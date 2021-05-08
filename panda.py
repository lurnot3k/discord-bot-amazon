import discord
import os
import random
import asyncio
import nest_asyncio
import datetime
from tracker import *
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()

client = discord.Client()

objects_list = []
num_of_objects = -1

hello_message = """
```
\n
I am the Panda bot.\n
Feel free to read my manual by typing !help.\n
\n
```
"""

help_message = """
```
\n
!add followed by the ASIN of a specific product to retrieve the current price and add to price watch! (WAIT 10 SECONDS)\n
!remove followed by the ASIN to remove a specific product from price watch!\n
!clear to clear the list of Amazon products currently on watch!\n
!list to see the list of Amazon products currently on watch!\n
!count to count the number of Amazon products currently on watch!\n
\n
```
"""

@client.event
async def on_ready():
    print(f'{client.user} is now online!')

@client.event
async def on_message(message):
    global num_of_objects
    global objects_list
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel)
    print(f'{username}:{user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'bot-testing':
        if message.content.lower() == '!hello':
            await message.channel.send(f'Hello {username}! {hello_message}')
        elif message.content.startswith(f'!help'):
            await message.channel.send(help_message)
        elif message.content.startswith(f'!add'):
            user_ASIN = user_message.split(' ', 1)[1]
            if user_ASIN[:2] != 'B0':
                await message.channel.send(f'`Invalid ASIN!`')
                return
            for item in objects_list:
                ASIN = item.ASIN
                if ASIN == user_ASIN:
                    await message.channel.send(f'ASIN: {user_ASIN} already in list!')
                    return
            objects_list.append(PandaTracker(user_ASIN))
            num_of_objects += 1
            await objects_list[num_of_objects].get_info()
            await objects_list[num_of_objects].set_desired_price()
            await message.channel.send(f'```ASIN: {objects_list[num_of_objects].ASIN}\n{str(objects_list[num_of_objects].title)}\nCurrent Price: ${objects_list[num_of_objects].price}\nDesired Price: ${objects_list[num_of_objects].desired_price}\n```')
        elif message.content.startswith(f'!list'):
            if len(objects_list) > 0:
                for item in objects_list:
                    await message.channel.send(f'```{item.ASIN}\n{item.title}\n{item.desired_price}\n{item.price}```') 
            else:
                await message.channel.send(f'`List is currently empty!`')
        elif message.content.startswith(f'!remove'):    
            user_ASIN = user_message.split(' ', 1)[1]
            if user_ASIN[:2] != 'B0':
                await message.channel.send(f'`Invalid ASIN!`')
                return
            for item in objects_list:
                ASIN = item.ASIN
                if ASIN == f'{user_ASIN}':
                    objects_list.remove(item)
                    num_of_objects -= 1
                    await message.channel.send(f'`ASIN: {ASIN} has been removed!`')
        elif message.content.startswith(f'!clear'):    
            objects_list.clear()   
            await message.channel.send(f'`List has been cleared!`')
            num_of_objects = -1
        elif message.content.startswith(f'!count'):
            count = len(objects_list)
            await message.channel.send(f'`Count: {count}`')

    
@client.event
async def price_alert():
    global num_of_objects
    global objects_list

    while(True):
        await client.wait_until_ready()
        if num_of_objects >= 0:
            for item in objects_list:
                channel = discord.utils.get(client.guilds[0].channels, name='bot-testing') 
                await item.get_info()
                price = float(item.price)
                desired_price = float(item.desired_price)
                title = item.title
                ASIN = item.ASIN
                if price < desired_price:
                    channel = discord.utils.get(client.guilds[0].channels, name='bot-testing') 
                    current_time = int(datetime.datetime.now().strftime("%I"))
                    await channel.send(f'```PRICE DROP! {title}\nFrom desired price: ${desired_price}\nTo new price: ${price}```')
        await asyncio.sleep(60)

client.loop.create_task(price_alert())


client.run(os.getenv('DISCORD_TOKEN'))

    # if message.channel.name == 'bot-testing':
    #     if message.content.lower() == '!hello':
    #         await message.channel.send(f'Hello {username}! {hello_message}')
    #     elif message.content.startswith(f'!help'):
    #         await message.channel.send(help_message)
    #     elif message.content.startswith(f'!amazon'):
    #         user_ASIN = user_message.split(' ', 1)[1]
    #         if user_ASIN[:2] != 'B0':
    #             await message.channel.send(f'`Invalid ASIN!`')
    #             return
    #         if not user_ASIN in ASIN_list:
    #             ASIN_list.append(user_ASIN)
    #         title, price = await get_info(user_ASIN)
    #         if not title in title_list:
    #             title_list.append(title)
            
    #         await message.channel.send(f'```ASIN: {user_ASIN}\nThe price for: {title} is\n${price}```')
    #     elif message.content.startswith(f'!ASIN'):
    #         for asin, title in zip(ASIN_list, title_list):
    #             await message.channel.send(f'```{asin} {title}```')   
