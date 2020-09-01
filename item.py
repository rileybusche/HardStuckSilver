import json
import pprint
import re
import item_map

pp = pprint.PrettyPrinter(indent=4)

item_file = open('item.json')
item_json = json.load(item_file)['data']

# Gets Basic Info for an Item and returns a dictionary
def get_item_info(item_name : str):
    item_id = item_map.get_item_id_from_name(item_name=item_name)

    item_info = item_json[item_id]

    #Clean up Item Description
    description = []
    tag_map = {
        'br'      : '\n',
        'stats'   : '',
        'stats'   : '',
        'unique'  : '',
        'unique'  : ''
    }

    words = re.findall(r"[\w']+", item_info['description'])
    for word in words:
        if word in tag_map.keys():
            description.append(tag_map[word])
        else:
            description.append(word)

    return_info = {
        'name'        : item_info['name'],
        'description' : ' '.join(description),
        'plaintext'   : item_info['plaintext'],
        'price'       : item_info['gold']['base'],
        'image'       : item_info['image']['full']
    }

    return return_info


if __name__ == "__main__":
    data = get_item_info("Black Cleaver")
    pp.pprint(data)