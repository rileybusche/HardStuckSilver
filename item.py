import json
import pprint
import re
import item_map

pp = pprint.PrettyPrinter(indent=4)

item_file = open('./json/item.json')
item_json = json.load(item_file)['data']

# Gets Basic Info for an Item and returns a dictionary
def get_item_info(item_name : str):
    item_id = item_map.get_item_id_from_name(item_name=item_name)

    item_info = item_json[item_id]

    pp.pprint(item_info)

    #Clean up Item Description
    description = item_info['description']

    tag_list = ['<br>', '<groupLimit>', '<unique>']
    for tag in tag_list:
        description = description.replace(tag, '\n')

    groomed_description = ' '

    keep_letter = True
    for letter in description:
        if letter in ['<', '>']:
            keep_letter = not keep_letter
            continue
        if keep_letter:
            groomed_description += letter
            

    return_info = {
        'name'        : item_info['name'],
        'description' : groomed_description,
        'plaintext'   : item_info['plaintext'],
        'price'       : item_info['gold']['total'],
        'image'       : item_info['image']['full']
    }

    return return_info


if __name__ == "__main__":
    data = get_item_info("Black Cleaver")
    pp.pprint(data)