#!/usr/bin/python3

import os
import discord
from dotenv import load_dotenv
from msgcheck import cmdchecker, chal_function

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
    print(f'Successfully connected to server {guild.name} -> id:{guild.id}')

    # uncomment the two lines underneath to also display all the members in the guild(s) the bot has connected to.
    #
    # members = ', '.join([member.name for member in guild.members])
    # print(f'The members in the server are {members}')


@client.event 
async def on_member_join(member):
    '''This function is triggered the first time a member joins the guild. The welcome message is sent via direct message(DM)'''
    
    await member.create_dm()
    await member.dm_channel.send(
        f"Hello {member.name}, welcome to {guild.name}. Glad you are here! Type '*baje help*' to see all the commands I can follow.\
             \nTip: If you are a beginner, go to #beginners channel under 'GENERAL' category to get started. \nLet's go!")


@client.event 
async def on_message(message):
    '''Whenever there is a call(message) to the bot using the command below, this function gets triggered
    and the arguments succeeding the command determine what shall be done next.'''

    # main_cmd = message.content.split()[0]     = 'baje'
    # args = message.content.split()[1:3]       = ['add'/'hello'/'joke', 'chal'/'flag'/'random']
    #args[1] = 'add'/'hello'/'joke'...
    #args[2] = 'chal'/'flag'/'random'
    #
    # response = cmdchecker(args[1], arg[2], '\n'.join(rest_msg_parts), message.author)
    
    beginning_command = message.content.split()[0]
    beginning_args = message.content.split('\n')[0][1:]  #alert!!!

    try:
        rest_msg_parts = message.content.split('\n')[1:]   #this line avoids add chal .../hello/..etc part|but it is very crucial line esp. for description part(if that part has description in multiple lines)
    except IndexError:
        pass

    if message.author == client.user:
        # if the author of the message(message.author) is the same as the bot(client.user), then nothing happens
        return
    
    if beginning_command.lower() != 'baaje' and beginning_command.lower() != 'baje':
        # if the beginning command is not either of 'baaje' or 'baje', then nothing happens
        return  

    if beginning_args[0] == 'hello':
        response = f"Hello {message.author.split('#')[0]} babu!" 

    elif beginning_args[0] == 'repeat':
        response = '\n'.join(rest_msg_parts)
               
    elif beginning_args[0] == 'challenge':
        command = beginning_args[1]
        response = chal_function(command, rest_msg_parts, message.author)


    else:
        response = cmdchecker('\n'.join(rest_msg_parts), message.author) #inside part(split part) shud be ok, it's tested and works good, and does what we want it to do
        # response = chal_function(command, rest_msg_parts, message.author)   
    
    
        await message.channel.send(response)


# The bot cannot magically work in Discord with all the code above, there has to be a way that connnects this particular instance
# of the bot to Discord over the internet. For that reason, we have something called 'token'.

# The command below connects and runs the bot using the given token number, which is a way to help the bot(s) communicate with Discord's API.
# The token number is to be obtained from Discord developers portal, made specifically for bots.
client.run(TOKEN) 