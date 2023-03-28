import openai
import json
from datetime import datetime
from telethon import TelegramClient, events
from telethon.tl.types import Message

# Defining a variable with a path to a configuration file
path = "./"
file = open(path + 'config.json', 'r')
config = json.load(file)

# Definition of configurations
openai.api_key = config['openai']
api_id = config['api_id']
api_hash = config['api_hash']

# Creating a TelegramClient Object
client = TelegramClient('session_name', api_id, api_hash)

# Loading the initial messages from a file
with open(path + 'initial_messages.json', 'r') as f:
    messages = json.load(f)

# Message handler
@client.on(events.NewMessage())
async def handler(event):
    user_id = event.sender_id
    if user_id not in [1234567, 7654321]:
        return # Skip if user_id doesn't match
    messages.append({"role": "user", "content": event.text})
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.6,
    )

    await event.reply(response['choices'][0]['message']['content'])
client.start()
client.run_until_disconnected()