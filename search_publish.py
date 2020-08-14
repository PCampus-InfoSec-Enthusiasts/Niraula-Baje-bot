import json

def search_publish_fn(command, challenge_id_str):

    chal_id = int(challenge_id_str) 

    def get_data():
        author, added_on, category, title, description = '', '', '', '', ''
        chal_file = json.load(open("challenges.json"))
        
        for each_item_in_list in chal_file:     #each_item_in_list: a dictionary
            for each_value in each_item_in_list.values():
                if each_value == chal_id:
                    author = each_item_in_list["author"]
                    added_on = each_item_in_list["added on"]
                    category = each_item_in_list["category"]
                    title = each_item_in_list["title"]
                    description = each_item_in_list["description"]


                    return f"**__author__**: {author}"+"\n"+f"**__added on__**: {added_on}"+"\n"+f"**__category__**: {category}"+"\n"+f"**__title__**: {title}"+"\n"+"**__description__**:"+"\n"+f"{description}"    
                    #enclosing a text with double asterisks(** **) makes the text bold and with double underscores(__ __) makes the text underlined
                    
                else:
                    continue
                
        else:
            return "No challenge found with that id."


    
    if command == 'search':     #search <chal-id>
        response = get_data()

    elif command == 'publish':  #publish <chal-id>
        response = get_data()
        #this should send the response to a particular challenge id, it is preferably #challenges channel

    
    return response

# d = search_publish_fn('search', '3')
# print(d)