import requests
import champion_map
import urllib.parse
# import pprint

# pp = pprint.PrettyPrinter(indent=4)

def get_summoner(summoner_name : str, api_key : str):
    summoner_name = urllib.parse.quote(summoner_name)
    print(summoner_name)
    request = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}')
    data = request.json()

    user_data = {
        'account_id'    : data['accountId'],
        'summoner_id'   : data['id'],
        'puuid'         : data['puuid'],
        'name'          : data['name'],
        'level'         : data['summonerLevel']
    }

    # print("******User Data******")
    # pp.pprint(data)
    # print(user_data)

    return user_data

def get_ranked(summoner_id : str, api_key : str):
    request = requests.get(f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}')
    data = request.json()

    ranked_data = {}

    for rank in data:
        if rank['queueType'] == 'RANKED_SOLO_5x5':
            ranked_data['tier'] = rank['tier']
            ranked_data['rank'] = rank['rank']
            ranked_data['lp']   = rank['leaguePoints']
    
    # print("******Ranked Data******")
    # pp.pprint(data)
    # print(ranked_data)

    return ranked_data

def get_mastery(summoner_id : str, api_key : str):
    request = requests.get(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}?api_key={api_key}')
    data = request.json()
    top_three = data[0:3]

    mastery = []

    mastery_score = requests.get(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{summoner_id}?api_key={api_key}').json()
    mastery.append(str(mastery_score))

    for champion in top_three:
        champ_dict = {
            'Champion Name' : champion_map.get_champion_name(champion['championId']),
            'Points'        : champion['championPoints'],
            'Mastery Level' : champion['championLevel']
        }
        mastery.append(champ_dict)
    
    return mastery