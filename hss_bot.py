import requests
import pprint
import discord
from discord.ext import commands
from discord.utils import get
import json
import riot_api, champion_map, embed, item, item_map

pp = pprint.PrettyPrinter(indent=4)

with open('./creds/creds.json') as file:
    creds = json.load(file)

client = discord.Client()

bot = commands.Bot(command_prefix='!')

token = creds['bot_token']
api_key = creds['RG-API']

bot_owner = 'LiquidLuck#9488'


@client.event
async def on_message(message):
    
    channel = message.channel
    author = str(message.author)
    msg = message.content.strip().lower()
 
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if msg.startswith('!league'):
        msg_tokens = msg.split()
        summoner_name = msg_tokens[1]
        
        try:
            user_data = riot_api.get_summoner(summoner_name=summoner_name, api_key=api_key)
            ranked_data = riot_api.get_ranked(summoner_id=user_data['summoner_id'], api_key=api_key)
            champion_mastery = riot_api.get_mastery(summoner_id=user_data['summoner_id'], api_key=api_key)

            embedVar = embed.create_general_embed(user_data, ranked_data, champion_mastery)

            await channel.send(embed=embedVar)
        except:
            await channel.send(embed=embed.create_error_embed(f"Do Data for {summoner_name}"))

    if msg.startswith('!item'):
        msg_tokens = message.content.split()
        item_name = " "
        item_name = item_name.join(msg_tokens[1:])

        if item_map.is_item(item_name):

            item_info = item.get_item_info(item_name=item_name)

            return_val = embed.create_item_embed(item_info)

            await channel.send(file=return_val[1], embed=return_val[0])
        else:
            await channel.send(embed=embed.create_error_embed(f"Could not find data for item: {item_name}"))
        
    # Quit Bot
    if msg == 'bot_close' and author == bot_owner:
        await client.close()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Malding'))


client.run(token)