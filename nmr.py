import requests
import urllib.parse
import pprint

pp = pprint.PrettyPrinter(indent=4)

def get_nmr(summoner_name : str):
    try:
        summoner_name = urllib.parse.quote(summoner_name)
        url = f'https://na.whatismymmr.com/api/v1/summoner?name={summoner_name}'
        request = requests.get(url)

        text_json = request.json()
        
        if text_json['ranked']['avg'] != None:
            ranked_nmr = str(text_json['ranked']['avg']) + ' ± ' + str(text_json['ranked']['err'])

            summary = text_json['ranked']['summary'].replace('</span>', '\n')

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
        else:
            nrm_info = {
                'ranked_nmr'    : '0',
                'summary'       : 'User has not played enough ranked games recently.'
            }

        return nrm_info

    except Exception as error:
        print(f'Failed in NMR: {error}')

if __name__ == "__main__":
    print(get_nmr('General Sniper'))