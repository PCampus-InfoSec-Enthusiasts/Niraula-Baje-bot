#!/usr/bin/python3

import os
import discord, joke_api, chutkila, covid19_api
from dotenv import load_dotenv
from new_msgcheck import cmd_checker
from help_manual import get_help
from search_publish import search_publish_fn

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# create an instance of the class Client from discord.py
client = discord.Client()

# global variable guild
guild = discord.utils.get(client.guilds, name=GUILD)


## NOTE: 'guild' and 'server' refer to the same thing in Discord. 
## Hence, 'connected to a guild' means 'connected to a server'.
## Also, 'client' refers to this bot in particular.


@client.event
async def on_ready():
    '''This function is triggered the first time the bot is online and has successfully connected to a guild.'''
    
    print(f'{client.user} is online.\nHurrrrrrrrray!')
    # print(f'Successfully connected to server {guild.name} -> id:{guild.id}')



@client.event 
async def on_member_join(member):
    '''This function is triggered the first time a member joins the guild. The welcome message is sent via direct message(DM)'''
    
    await member.create_dm()        #there has been an issue with guild.name
    await member.dm_channel.send(
        f"Hello {member.name}, welcome to {guild}. Glad you are here! Type '*baje help*' to see all the commands I can follow.\
             \nTip: If you are a beginner, go to #beginners channel under 'GENERAL' category to get started. \nLet's go!")


@client.event 
async def on_message(message):
    '''Whenever there is a call(message) to the bot using the command below, this function gets triggered
    and the arguments succeeding the command determine what shall be done next.'''

    
    main_cmd = message.content.split()[0]     # main_cmd = 'baje'
    response = ''
    try:
        args = message.content.split()[1:3]       # args = ['add'/'hello'/'joke', 'chal'/'flag'/'random']
    
        #so, we can have:
        # args[1] = 'add'/'hello'/'joke'...
        # args[2] = 'chal'/'flag'/'random'

        try:
            sub_args = message.content.split('\n')[1:]   #this line avoids add chal .../hello/..etc part|but it is very crucial line esp. for description part(if that part has description in multiple lines)
            #this carries whatever arguments are after what are in args
        except:
            
            pass

        if message.author == client.user:
            # if the author of the message(message.author) is the same as the bot(client.user), then nothing happens
            return


        if main_cmd.lower() != 'baaje' and main_cmd.lower() != 'baje':
            # if the beginning command is not either of 'baaje' or 'baje', then nothing happens
            return  


        if args[0].lower() == 'hello':
            response = f"Hello {message.author.name} babu!" 



        elif args[0].lower() == 'help':
            response = f"__Help Commands:__ \n{get_help()}"

        
        elif args[0].lower() == 'joke':
            response = joke_api.get_joke()

        
        elif args[0].lower() == 'chutkila':
            response = chutkila.get_chutkila()

        
        elif args[0].lower() == 'coronavirus' or args[0].lower() == 'corona' or args[0].lower() == 'covid' or args[0].lower() == 'covid19':
            try:
                args[1] = args[1].lower()
                 #  return the data for country the users type
                response = covid19_api.covid19_data_country(args[1])

            except:
                 # return global data if no additional argument
                response = covid19_api.covid19_data_global()

        
        elif args[0].lower() == 'search' or args[0].lower() == 'publish':  #baje publish <challenge-id> / #baje search <challenge-id>
            response = search_publish_fn(args[0].lower(), args[1])



        else:   #if the args[0] doesn't contain 'hello' OR 'help' OR 'joke' OR 'chutkila'
            response = cmd_checker(message.author, args, '\n'.join(sub_args))



        #this except block is used when there is no argument after 'baje', that is, only when there is 'baje' but nothing after that.
    except IndexError:  #more preferable is show help commands, or asking to type command for help.
        response = 'Hajur'
            


    
    await message.channel.send(response)
    
    CHANNEL = client.get_channel(743759173350850561)
    await CHANNEL.send('Rujal, malai dherai nabolau na')
  

# The command below connects and runs the bot using the given token number, which is a way to help the bot(s) communicate with Discord's API for bots.
# The token number is to be obtained from Discord developers portal, made specifically for bots.
client.run(TOKEN) 