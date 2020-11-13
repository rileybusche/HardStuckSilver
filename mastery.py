import discord
from discord.ext import commands
from discord.utils import get
import riot_api, embed

def get_mastery(summoner_name : str, api_key : str, count : int):
    user_data = riot_api.get_summoner(summoner_name=summoner_name, api_key=api_key)
    champion_mastery = riot_api.get_mastery(summoner_id=user_data['summoner_id'], api_key=api_key, count=count)
    
