import json, pytz
from encrypt import encrypt
from operator import itemgetter
from datetime import datetime


NPT = pytz.timezone('Asia/Kathmandu')

def add_challenge(author, category, title, description):
    '''This function is for adding challenges to challenges.json file along with a few attributes.'''

    global NPT
    chal_file = json.load(open("challenges.json", "r"))
    _temp = chal_file
    
    id = len(_temp)

    dict_branch = {}

    dict_branch["id"] = id+1
    dict_branch["author"] = author #message author passed from bot.py
    dict_branch["added on"] = str(datetime.now(NPT).replace(microsecond=0))
    dict_branch["category"] = category
    dict_branch["title"] = title
    dict_branch["description"] = description

    _temp.append(dict_branch)

    #to ensure that the items are sorted by their id, that is, by the value of id:
    _temp.sort(key=itemgetter('id'))

    #this is not needed as the line below also opens the file in write mode, thus, clearing all the contents of the file
    open("challenges.json", "w").close()

    fp = open("challenges.json", "w")

    json.dump(_temp, fp, indent=4)

    fp.close()


    return f"Wohoo! Challenge successfully added as: id: {id+1}"



def add_flag(challenge_id, flag, flag_author):
    '''This function is for adding flags to flags.json file along with a few attributes.'''

    global NPT

    # since the challenge_id parameter will be a string(str), it has to be type-casted into integer(int) first
    chal_id_int = int(challenge_id)

    chal_file = json.load(open("challenges.json", "r"))
    #to get the author name for specific challenge id

    chal_author = ''

    for each_item_in_list in chal_file:     #each_item_in_list means a dictionary
        for value in each_item_in_list.values():
            if value == chal_id_int:
                chal_author = each_item_in_list["author"]
                break
            else:
                continue

    if flag_author == chal_author:

        flag_file = json.load(open("flags.json", "r"))

        _temp = flag_file

        dict_branch = {}

        dict_branch["id"] = chal_id_int
        dict_branch["author"] = flag_author #message author passed from bot.py
        dict_branch["added on"] = str(datetime.now(NPT).replace(microsecond=0))
        dict_branch["flag"] = encrypt(flag)     #changed here


        _temp.append(dict_branch)
        
        #to ensure that the items are sorted by their id, that is, by the value of id:
        _temp.sort(key=itemgetter('id'))

        #this is not needed as the line below also opens the file in write mode, thus, clearing all the contents of the file
        open("flags.json", "w").close()

        fp = open("flags.json", "w")

        json.dump(_temp, fp, indent=4)

        fp.close()

        return f'Flag successfully added for challenge id: {chal_id_int}'

    else:
        return "Sorry, you aren't the challenge author, so you can't add the flag."