import json, random

def get_chutkila():

    append_file = open("send_complete.txt", "a")
    
    read_file = open("send_complete.txt")       #default mode is "r"
    done_list_raw = read_file.read().split(',')    
    done_list = [] 

    for member in done_list_raw:
        if isinstance(member, int):
            done_list.append(member)

        elif isinstance(member, str):
            try:
                done_list.append(int(member))
            except:
                continue

    data = open("chutkila.json")

    joke_dict = json.load(data)

    endpoint = len(joke_dict)   #endpoint according to the size of chutkila.json/number of chutkilas there

    choice = random.randint(0, endpoint-1)

    while choice in done_list:    
        choice = random.randint(0, endpoint)

    joke_response = joke_dict[choice]["title"]+'\n...............................\n\n'+joke_dict[choice]["body"]
    done_list.append(choice)
    append_file.write(str(choice)+', ')

    return joke_response