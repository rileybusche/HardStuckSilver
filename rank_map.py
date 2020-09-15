
def get_ranked_armor(rank):
    rank_map = {
        'NO_RANK'         : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/3/38/Season_2019_-_Unranked.png/revision/latest?cb=20190908074432',

        'IRON_I'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/0/03/Season_2019_-_Iron_1.png/revision/latest?cb=20181229234926',
        'IRON_II'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/5/5f/Season_2019_-_Iron_2.png/revision/latest?cb=20181229234927',
        'IRON_III'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/9/95/Season_2019_-_Iron_3.png/revision/latest?cb=20181229234927',
        'IRON_IV'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/7/70/Season_2019_-_Iron_4.png/revision/latest?cb=20181229234928',

        'BRONZE_I'        : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/f/f4/Season_2019_-_Bronze_1.png/revision/latest?cb=20181229234910',
        'BRONZE_II'        : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/a/ac/Season_2019_-_Bronze_2.png/revision/latest?cb=20181229234911',
        'BRONZE_III'        : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/8/81/Season_2019_-_Bronze_3.png/revision/latest?cb=20181229234912',
        'BRONZE_IV'        : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/5/5a/Season_2019_-_Bronze_4.png/revision/latest?cb=20181229234913',

        'SILVER_I'        : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/7/70/Season_2019_-_Silver_1.png/revision/latest?cb=20181229234936',
        'SILVER_II'        : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/5/56/Season_2019_-_Silver_2.png/revision/latest?cb=20181229234936',
        'SILVER_III'        : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/1/19/Season_2019_-_Silver_3.png/revision/latest?cb=20181229234937',
        'SILVER_IV'        : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/5/52/Season_2019_-_Silver_4.png/revision/latest?cb=20181229234938',

        'GOLD_I'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/9/96/Season_2019_-_Gold_1.png/revision/latest?cb=20181229234920',
        'GOLD_II'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/8/8a/Season_2019_-_Gold_2.png/revision/latest?cb=20181229234921',
        'GOLD_III'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/a/a6/Season_2019_-_Gold_3.png/revision/latest?cb=20181229234921',
        'GOLD_IV'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/c/cc/Season_2019_-_Gold_4.png/revision/latest?cb=20181229234922',

        'PLATINUM_I'      : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/7/74/Season_2019_-_Platinum_1.png/revision/latest?cb=20181229234932',
        'PLATINUM_II'      : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/a/a3/Season_2019_-_Platinum_2.png/revision/latest?cb=20181229234933',
        'PLATINUM_III'      : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/2/2b/Season_2019_-_Platinum_3.png/revision/latest?cb=20181229234934',
        'PLATINUM_IV'      : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/a/ac/Season_2019_-_Platinum_4.png/revision/latest?cb=20181229234934',
        
        'DIAMOND_I'       : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/9/91/Season_2019_-_Diamond_1.png/revision/latest?cb=20181229234917',
        'DIAMOND_II'       : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/7/70/Season_2019_-_Diamond_2.png/revision/latest?cb=20181229234918',
        'DIAMOND_III'       : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/d/dc/Season_2019_-_Diamond_3.png/revision/latest?cb=20181229234918',
        'DIAMOND_IV'       : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/e/ec/Season_2019_-_Diamond_4.png/revision/latest?cb=20181229234919',

        'MASTER'          : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/1/11/Season_2019_-_Master_1.png/revision/latest?cb=20181229234929',

        'GRANDMASTER'     : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/7/76/Season_2019_-_Grandmaster_1.png/revision/latest?cb=20181229234923',

        'CHALLENGER'      : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/5/5f/Season_2019_-_Challenger_1.png/revision/latest?cb=20181229234913'
        # 'CHALLENGER'      : 'https://vignette.wikia.nocookie.net/leagueoflegends/images/e/ec/Season_2019_-_Diamond_4.png/revision/latest?cb=20181229234919'
    }

    print(rank_map[rank])
    return rank_map[rank]