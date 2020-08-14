import json
from encrypt import encrypt
from add_submit import add_challenge, add_flag, submit_flag
from help_manual import get_help



'''NOTE:
2 args case:
 - baje joke
 - baje chutkila
 - baje covid19         #not including this in 2 args case block, as it is needed with 3 args case

3 args case:
 - baje covid19 <country>
 - baje search <challenge-id>
 - baje publish <challenge-id>

4 args case:
  none

5 args case:
 - baje add flag
   <challenge-id>
   <flag>

6 args case:
- baje add chal
   <category>
   <title>
   <description>

'''

                # args = message.content.split()[1:3]       # args = ['add'/'hello'/'joke', 'chal'/'flag'/'random']

                # #so, we can have:
                # # args[0] = 'add'/'hello'/'joke'...
                # # args[1] = 'chal'/'flag'/'random'


                # sub_args = message.content.split('\n')[1:]   #this line avoids add chal .../hello/..etc part|but it is very crucial line esp. for description part(if that part has description in multiple lines)
                #this carries whatever arguments are after what are in args


#args_2 = 2 arguments case
#args_3 = 3 arguments case
#args_5 = 5 arguments case
#args_6 = 6 arguments case


#ref.::
# args_1 = baje |
# args_2 =        add   | submit    | publish   | search    | covid19 | chutkila | joke
# args_3 =   <category> | <chal-id> | <chal-id> | <chal-id> | <country>
# args_5 =      <title> | <flag>
# args_6 = <description>





def cmd_checker(message_author, args, sub_args): 
    response = ''
    try:
        substitute_args = sub_args
        
    except IndexError:
        substitute_args = 'Unavailable'

#there was problem on the part below: 
    args_2 = args[0].lower()        ## args_2 = 'add'/'submit'
    

    if args_2 == 'add':
        
        try:
            args_3 = args[1].lower()
            if args_3 == 'challenge' or args_3 == 'chal':
                msg_new = substitute_args.split('\n')
                try:
                    category = msg_new[0]
                    title = msg_new[1]
                    description = '\n'.join(msg_new[2:])        ###check this again!!
                    response = add_challenge(message_author, category, title, description)
                                            #problem:function didn't get called!!
                except IndexError:
                    response = 'Error! Please enter ```baje help``` for help commands.'


            elif args_3 == 'flag':
                msg_new = substitute_args.split('\n')
                try:
                    category = msg_new[0]
                    title = msg_new[1]
                    response = add_flag(category, title, message_author)

                except IndexError:
                    
                    pass            #just to suppress warning
                
        except IndexError:
            response = 'Error! Please enter ```baje help``` for help commands.'

    elif args_2 == 'submit':
        if substitute_args == 'Unavailable':
            response = 'Error! Please enter ```baje help``` for help commands.'
            
        else:
            msg_new = substitute_args.split('\n')
            try:
                id = msg_new[0]
                flag = msg_new[1]
                response = submit_flag(id, flag, message_author)

            except IndexError:
                response = 'Error! Please enter ```baje help``` for help commands.'
        
    
        
    ''' 
    #block 1, 2 case
    try: #for two argument case, i.e. for e.g.: 'baje joke'
        args_3 = args[1].lower()        ## args_3 = 'chal'/'flag'/'random'/country-name(for coronavirus info)/chalenge-id(for flag submission)
            
        if args_2 == 'joke':         
            pass
            

        




    except IndexError:
        #block 2, 3 case
        try:    #for three argument case, i.e. for e.g. 'baje covid19 nepal'
            args_3 = sub_args.split('\n')[0]           ## args_3: challenge(or chal)/flag/random/programming

            

    
    msg_new = sub_args.split('\n')               


    category = msg_new[0].strip()       ## category: category for adding chals/ challenge id for flags
    title = msg_new[1].strip()          ## title: title of challenge/ the flag
    description = '\n'.join(msg_new[3:]).strip()    ## description of challenge

    response = ''
   
    try:

        


    



        # elif args_2 == 'clear': #i think we shud make this clear feature to make it easier for us to clear files
        #     pass    ::
    

    except:
        return "Oops! Some error occurred!"
    '''    
    
    return response



# args = 'add chal'
# sub_args = 'reverse_engg. \nPLEASE REVERSE IT \nI don;t know much of reverse engineering\nwhy??'#\ncan u help me?
# message_author = 'jarp01#1910'

# args = 'search'
# sub_args = '1'
# message_author = 'jarp01'
# print(cmd_checker(message_author, args, sub_args))