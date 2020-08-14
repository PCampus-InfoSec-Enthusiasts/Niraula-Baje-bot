import json
from encrypt import encrypt
import joke_api, chutkila, covid19_api
from add_submit import add_challenge, add_flag, submit_flag
from search_publish import search_publish_fn

#input format to expect while adding challenge:
    #baje add chal
    #<category>
    #<title>    
    #<description>

#for flag:
    #baje add flag
    #<challenge-id>
    #<flag>    

#for searching or publishing challenge:
    #baje search <challenge-id>
    #baje publish <challenge-id>        #expecting to publish challenge to #challenges channel 

#for joke/chutkila:                 
    #baje joke
    #baje chutkila   

#for covid19 info:      #there can be multiple replacements for covid19, see its part below
    #baje covid19 <country>
    #baje covid19       [this will return global data, i.e. total data from the world, not from am individual country]


        # args = message.content.split()[1:3]       # args = ['add'/'hello'/'joke', 'chal'/'flag'/'random']
    
        # #so, we can have:
        # # args[0] = 'add'/'hello'/'joke'...
        # # args[1] = 'chal'/'flag'/'random'


        # sub_args = message.content.split('\n')[1:]   #this line avoids add chal .../hello/..etc part|but it is very crucial line esp. for description part(if that part has description in multiple lines)
        #this carries whatever arguments are after what are in args




def cmd_checker(args, sub_args, message_author): 

    command_1 = args[0].lower()        ## command_1 = 'add'/'joke'/'chutkila'/'submit'
    args_3 = args[1].lower()        ## args_3 = 'chal'/'flag'/'random'/country-name(for coronavirus info)/chalenge-id(for flag submission)
    #if there is no arg in args[1] it raises an error
    #this part raising error means the user passed only two commands:
    #baje hello, baje joke, baje chutkila
    #so, we need to do error handling here
    #       if using try-except,
    #commands which can be put in try block:
    #       'baje joke' 'baje chutkila'
    # 
    # commands which can be put in except block have more than 2 arguments
    #again, try block 
    #


    try:
        type = sub_args.split()[0]           ## type: challenge(or chal)/flag/random/programming
    
    except IndexError:
        type = 'all'                        
     
    
    msg_new = sub_args.split('\n')               


    category = msg_new[0].strip()       ## category: category for adding chals/ challenge id for flags
    title = msg_new[1].strip()          ## title: title of challenge/ the flag
    description = '\n'.join(msg_new[3:]).strip()    ## description of challenge

    response = ''
   
    try:

        if command_1 == 'add':
            if type == 'challenge' or type == 'chal':
                response = add_challenge(message_author, category, title, description)



            elif type == 'flag':
                response = add_flag(category, title, message_author)


        elif command_1 == 'submit':
            id = msg_new[0]
            flag = msg_new[1]
            response = submit_flag(id, flag, message_author)
    


        elif command_1 == 'publish':  #baje publish <challenge-id> => publish the challenge in #challenges_bot (channel to be renamed)
            response = search_publish_fn(command_1, args_3)
            


        elif command_1 == 'joke':
            response = joke_api.get_joke()



        elif command_1 == 'chutkila':
            response = chutkila.get_chutkila()

        elif command_1 == 'coronavirus' or command_1 == 'corona' or command_1 == 'covid' or command_1 == 'covid19':
            try:
                # return the data for country the users type
                response = covid19_api.covid19_data_country(args_3)
            
            except:
                # return global data if no additional argument
                response = covid19_api.covid19_data_global()


        elif command_1 == 'clear': #i think we shud make this clear feature to make it easier for us to clear files
            pass


    except:
        return "Oops! Some error occurred!"
    
    return response


#for local testing
#args = 'add chal'
#sub_args = 'reverse \nREVERSIFY \nreverse engg.\nwhy??'
#author = 'jarp01#1910'
#print(cmd_checker(args, sub_args, message_author): )