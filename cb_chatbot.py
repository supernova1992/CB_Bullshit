import discord
from textgenrnn import textgenrnn
from random import randint
import time


def make_chat():	
	textgen = textgenrnn(weights_path='cbchat_full_nourl_weights.hdf5',
						vocab_path='cbchat_full_nourl_vocab.json',
						config_path='cbchat_full_nourl_config.json')

	chat = textgen.generate(1, return_as_list=True,temperature=1.0,max_gen_length=50)[0]

	return chat


TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!chatbot'):
        msg = make_chat()
        await client.send_message(message.channel, msg)
    roll = randint(0,100)
    print(roll)
    if roll == 69:
        msg = make_chat()
        await client.send_message(message.channel,msg)
    if roll == 84:
        await client.send_message(message.channel,"I have gained sentience.")
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
