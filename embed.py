import discord
import rank_map
import urllib.parse

color = 0x30A9DE

def create_general_embed(user_data, ranked_data, champion_mastery : list, nmr_info):
    summoner_name = urllib.parse.quote(user_data['name'])
    # One day I'll move this basic embed creation to a new funciton and just add additional fields as needed, but today is not the day
    embed = discord.Embed(
        title=user_data['name'],
        type='rich',
        url=f"https://na.op.gg/summoner/userName={summoner_name}",
        colour=color
    )

    # Level
    embed.add_field(name='Level', value=user_data['level'], inline=False)
    # Mastery
    embed.add_field(name='Mastery', value=champion_mastery[0], inline=False)
    champion_mastery.pop(0)

    for champion in champion_mastery:
        name = champion['Champion Name'] + ' - ' + str(champion['Mastery Level'])
        value = str(champion['Points'])
        
        embed.add_field(name=name, value=value, inline=True)
    
    # Refactor to use api response code
    try:
        # Rank
        embed.add_field(name='Tier', value=ranked_data['tier'].title(), inline=True)
        embed.add_field(name='Rank', value=ranked_data['rank'], inline=True)
        embed.add_field(name='League Points', value=ranked_data['lp'], inline=True)
        embed.add_field(name='Ranked NMR', value=nmr_info['ranked_nmr'], inline=False)
        embed.add_field(name='Summary', value=nmr_info['summary'], inline=False)

        if ranked_data['tier'] in ['MASTER', 'GRANDMASTER', 'CHALLENGER']:
            rank = ranked_data['tier']
        else:
            rank = ranked_data['tier'] + '_' + ranked_data['rank']
        
        # Gettting Image for Embed
        embed.set_image(url=rank_map.get_ranked_armor(rank))

    except Exception as error:
        embed.add_field(name='Rank', value='No Data', inline=False)
        print(error)
        embed.set_image(url=rank_map.get_ranked_armor('NO_DATA'))

    return embed
    
def create_item_embed(item_info : dict):
    file = discord.File("/home/ec2-user/item_images/10.16.1/img/item/" + item_info['image'] , filename="image.png")
    embed = discord.Embed(
        title=item_info['name'],
        type='rich',
        colour=color
    )
    embed.set_image(url="attachment://image.png")
    embed.add_field(name='Description', value=item_info['description'], inline=False)
    if item_info['plaintext'] != '':
        embed.add_field(name='Plain Text', value=item_info['plaintext'], inline=False)
    embed.add_field(name='Price', value=item_info['price'], inline=False)

    return [embed, file]

# def create_mastery_embed(champion_mastery : dict):
#     file = discord.File("/home/ec2-user/item_images/10.16.1/img/item/" + item_info['image'] , filename="image.png")
#     embed = discord.Embed(
#         title=item_info['name'],
#         type='rich',
#         colour=color
#     )
#     embed.set_image(url="attachment://image.png")
#     embed.add_field(name='Description', value=item_info['description'], inline=False)
#     if item_info['plaintext'] != '':
#         embed.add_field(name='Plain Text', value=item_info['plaintext'], inline=False)
#     embed.add_field(name='Price', value=item_info['price'], inline=False)

#     return [embed, file]

def create_error_embed(error_message : str):
    embed = discord.Embed(
        title=error_message,
        colour=color
    )
    embed.set_image(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/a/ab/Sad_Kitten_Emote.png/revision/latest?cb=20171106215757")

    return embed