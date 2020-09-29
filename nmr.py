import requests
import urllib.parse
import pprint

pp = pprint.PrettyPrinter(indent=4)

def get_mmr(summoner_name : str):
    summoner_name = urllib.parse.quote(summoner_name)
    url = f'https://na.whatismymmr.com/api/v1/summoner?name={summoner_name}'
    request = requests.get(url)

    text_json = request.json()

    pp.pprint(text_json)

    ranked_nmr = str(text_json['ranked']['avg']) + ' ± ' + str(text_json['ranked']['err'])
    summary = text_json['ranked']['summary']

    groomed_summary = ' '

    keep_letter = True
    for letter in summary:
        if letter in ['<', '>']:
            keep_letter = not keep_letter
            continue
        if keep_letter:
            groomed_summary += letter

    nrm_info = {
        'ranked_nmr'    : ranked_nmr,
        'summary'       : groomed_summary
    }

    return nrm_info
