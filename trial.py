import json
from datetime import datetime
from operator import itemgetter

# message_author = "jarp01"
# description = "Mr. Robot?"

message_author = "jarp0000000lllllllllllll"
description = "Are you hoomaaoooooooaaaaaaaaan?"



#Initially, challenges.json is just an empty dictionary; so, chal_file = {} as 'challenges.json' = {}
chal_file = json.load(open("challenges.json", "r"))



# what is this about??


#structure of chal_file/challenges.json when not empty:
# { "0": {"id":1, "description":"something" },
#   "1": {"id":2, "description":"something_something" },
#   "2": {"id":3, "description":"something_something_something" }
# }



#in order to append a new challenge/dictionary to the chal_file/challenges.json,
#both the opening and closing braces of the main dictionary i.e. chal_file should be removed
#that is, only inside contents should be present
#
#if the inside elements/dictionaries can be temporarily saved somewhere,
#we can append new element/dictionary to it, and then remove everything in challenges.json
#and if the temporarily saved dictionaries can be wrapped in another dictionary(say main dictionary), 
#then this main dictionary can be directly saved to challenges.json
#
#




#everything is assigned to temporary_ variable--from closing braces/brackets to inside elements
temporary_ = chal_file

#there is no need to do json.load(file.json) as chal_file is already the result of that
#this is also to ensure that all our data remains safe



#this is to assign the "id" to branch/inner dictionary according to the size of the outer dict/list(chal_file)
id = len(temporary_)


dict_branch = {}


#key-value pair is created in empty dictionary dict_branch
dict_branch["id"] = id+1
dict_branch["author"] = message_author #message author passed from bot.py
dict_branch["description"] = description


#now dict_branch becomes: 
#                 dict_branch = { "id": 1, "author": "jarp01", "description": Mr. Robot?" }
#
#  or,    dict_branch =  {
#                           "id": 1,
#                           "author": "jarp01", 
#                           "description": Mr. Robot?"
#                        }



#now time to add this dictionary to previous list/dictionary of dictionaries: temporary_
#but before that let's assume that challenge.json is an empty list,
# so, chal_file and subsequently temporary_  also contain empty list
# i.e. temporary_ = chal_file = []
#thus,
temporary_.append(dict_branch)



#we could as well empty the challenges.json file now 
#so that we can write our new list in temporary_ to that file....so,
open("challenges.json", "w").close()


#now that our challenges.json file is empty, 
#  let's dump our temporary_ list and the dictionary inside it to challenges.json in jsonic way
#for that let's again open our challenges.json
fp = open("challenges.json", "w")

#to ensure that the items are sorted by their id, that is by the value of id:
temporary_.sort(key=itemgetter('id'))

json.dump(temporary_, fp, indent=4)

fp.close()



# append_file = open("challenges.json", "w")
# append_file.write('')
# append_file.close()



response = f"Success: id:{id+1}"

print(response)