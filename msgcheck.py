import json
from encrypt import encrypt
from add import add_challenge, add_flag
import joke_api, chutkila, covid19_api

def cmdchecker(msg, message_author): 

#i think it's good to have this input format:
# baje add chal
#<category>
#<title>    
#<decsription>    
# maile copy 
# 
# 

    command = msg.split()[0].lower()        ## command: hello/add/joke/chutkila
    try:
        type = msg.split()[1].lower()           ## type: challenge(or chal)/flag/random/programming
    except IndexError:
        type = 'all'                        
     
    
    msg_new = msg.split('\n')               
                                            
    print(msg_new)
    # for debugging purpose

    category = msg_new[1].strip()       ## category: category for adding chals/ challenge id for flags
    title = msg_new[2].strip()          ## title: title of challenge/ the flag
    description = '\n'.join(msg_new[3:]).strip()    ## description of challenge

    response = ''
   
    try:
        if command == 'hello' or command == 'Hello':
            response = 'hello babu!'


        elif command == 'repeat':
            response = ' '.join(type)  ## type = args[1], see above



        elif command == 'add':
            if type == 'challenge' or type == 'chal':
                response = add_challenge(message_author, category, title, description)



            elif type == 'flag':
                response = add_flag(category, title, message_author)


        elif command == 'submit':
            pass

        elif command == 'publish':  #baje publish <challenge-id> => publish the challenge in #challenges_bot (channel to be renamed)
            # response = chal_function(challenge_id)
            #each and everything this command requires is in chal_function() implementation for search
            #but we need to make this command post challenges in #challenges (to be renamed from #challenges_bot) channel
            pass

        elif command == 'joke':
            response = joke_api.get_joke()


        elif command == 'chutkila':
            response = chutkila.get_chutkila()

        elif command == 'coronavirus' or command == 'corona' or command == 'covid' or command == 'covid19':
            try:
                # return the data for country the users type
                response = covid19_api.covid19_data_country(type)
            
            except:
                # return global data if no additional argument
                response = covid19_api.covid19_data_global()


        elif command == 'clear': #i think we shud make this clear feature to make it easier for us to clear files
            pass


    except:
        return "Oops! Some error occurred!"
    
    return response


def chal_function(command, args, author):
    if command == 'add':
        
        pass


#what about using the same function and method to search as well as publish challenge? because they do/have to do the same work

    if command == 'search' or command == 'publish': #search <chal-id>
        chal_file = json.load(open("challenges.json"))

        chal_id = int(args[0])  

        for each_item_in_list in chal_file:     #each_item_in_list: a dictionary
            for each_value in each_item_in_list.values():
                if each_value == chal_id:
                    author = each_item_in_list["author"]
                    category = each_item_in_list["category"]
                    title = each_item_in_list["title"]
                    description = each_item_in_list["description"]
                    break
                else:
                    continue
        
        chal_file.close()
        response = f"**__author__**: {author}"+"\n"+f"**__category__**: {category}"+"\n"+f"**__title__**: {title}"+"\n"+"**__description__**:"+"\n"+f"{description}"    
        #enclosing a text with double asterisks(** **) makes the text bold and with double underscores(__ __) makes the text underlined

        return response


    if command == 'submit':
        '''here, for 'total' summary '''
        flags = json.load(open("flags.json"))   # here the flag.json file is loaded as a list of doctionaries:: isn't it??
                                            
        chal_id = int(args[0])                  # accepts the challenge id of the challenge from the user
        submitted_flag = encrypt(str(args[1]))      #which algo does encrypt use?    :: look encrypt.py   
            
        response = "Invalid ID"                 # 

        for each_item_in_list in flags:     #each_item_in_list: a dictionary
            for each_value in each_item_in_list:
                if each_value["id"] == chal_id:      # checks every ID to search for the ID of the challenge user wants to submit 
                    if each_value["flag"] == submitted_flag:
                        response = "Right"              
                    else:                               
                        response = "Wrong" 
                        
            
        return response