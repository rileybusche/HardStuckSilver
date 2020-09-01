import discord

color = 0x30A9DE

rank_map = {
    'NO_RANK'       : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/3/38/Season_2019_-_Unranked.png/revision/latest?cb=20190908074432',
    'IRON'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/0/03/Season_2019_-_Iron_1.png/revision/latest?cb=20181229234926',
    'SILVER'        : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/7/70/Season_2019_-_Silver_1.png/revision/latest?cb=20181229234936',
    'GOLD'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/9/96/Season_2019_-_Gold_1.png/revision/latest?cb=20181229234920',
    'PLATINUM'      : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/7/74/Season_2019_-_Platinum_1.png/revision/latest?cb=20181229234932',
    'DIAMOND'       : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/9/91/Season_2019_-_Diamond_1.png/revision/latest?cb=20181229234917',
    'MASTER'        : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/1/11/Season_2019_-_Master_1.png/revision/latest?cb=20181229234929',
    'GRANDMASTER'   : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/7/76/Season_2019_-_Grandmaster_1.png/revision/latest?cb=20181229234923',
    'CHALLENGER'    : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/5/5f/Season_2019_-_Challenger_1.png/revision/latest?cb=20181229234913'
}

def create_general_embed(user_data, ranked_data, champion_mastery : list):
    # One day I'll move this basic embed creation to a new funciton and just add additional fields as needed, but today is not the day
    embed = discord.Embed(
        title=user_data['name'],
        type='rich',
        colour=color
    )

    # Mastery
    embed.add_field(name='Mastery', value=champion_mastery[0], inline=False)
    champion_mastery.pop(0)

    for champion in champion_mastery:
        name = champion['Champion Name'] + ' - ' + str(champion['Mastery Level'])
        value = str(champion['Points'])
        
        embed.add_field(name=name, value=value, inline=True)
    try:
        # Rank
        value = ranked_data['tier'] + ' - ' + ranked_data['rank'] + ' - ' + str(ranked_data['lp'])
        embed.add_field(name='Rank', value=value, inline=False)

        embed.set_image(url=rank_map[ranked_data['tier']])
    except:
        embed.add_field(name='Rank', value='No Data', inline=False)

        embed.set_image(url=rank_map['NO_RANK'])
    return embed
    
def create_item_embed(item_info : dict):
    file = discord.File("D:\\Downloads\\dragontail-10.16.1\\10.16.1\\img\\item\\" + item_info['image'] , filename="image.png")
    embed = discord.Embed(
        title=item_info['name'],
        type='rich',
        colour=color
    )
    embed.set_image(url="attachment://image.png")
    embed.add_field(name='Description', value=item_info['description'], inline=False)
    embed.add_field(name='Plain Text', value=item_info['plaintext'], inline=False)
    embed.add_field(name='Price', value=item_info['price'], inline=False)

    return [embed, file]

def create_error_embed(error_message : str):
    embed = discord.Embed(
        title=error_message,
        colour=color
    )
    embed.set_image(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/a/ab/Sad_Kitten_Emote.png/revision/latest?cb=20171106215757")

    return embed