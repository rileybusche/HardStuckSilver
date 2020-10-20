import discord
from discord.ext import commands
from discord.utils import get
import riot_api, nmr, embed

def get_info(summoner_name : str, api_key : str):
    try:
        user_data = riot_api.get_summoner(summoner_name=summoner_name, api_key=api_key)
        ranked_data = riot_api.get_ranked(summoner_id=user_data['summoner_id'], api_key=api_key)
        champion_mastery = riot_api.get_mastery(summoner_id=user_data['summoner_id'], api_key=api_key)
        nmr_info = nmr.get_nmr(summoner_name)

        return embed.create_general_embed(user_data, ranked_data, champion_mastery, nmr_info)

    except Exception as error:
        print(error)
        return embed.create_error_embed(f"No Data for {summoner_name}")