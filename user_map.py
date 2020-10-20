
user_map = {
    'McNuggetMan#5562'  : 'McNuggetMan',
    'LiquidLuck#9488'   : 'XLiquidLuckX',
    'TheDenzel#2847'    : 'The Denzelz',
    'Gaytor#3734'       : 'Gaytor',
    'blueblank#9902'    : 'blueblanks',
    'sirmoose#2516'     : 'adultwipes'
}

def return_summoner(discord_name : str) -> str:
    if discord_name in user_map:
        return user_map[discord_name]
    else:
        return ''