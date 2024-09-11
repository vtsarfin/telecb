#!/usr/bin/env python3
import os
import configparser
import uvloop
from pyrogram import Client
import argparse
argparser=argparse.ArgumentParser()
argparser.add_argument('--phone',dest='phone_number',type=str,help='Your phone number associated with Telegram account')
config_file = 'config.ini'
def get_api_credentials():
    config = configparser.ConfigParser()
    # Check if the config file exists
    if os.path.exists(config_file):
        config.read(config_file)
        api_id = config['Telegram']['api_id']
        api_hash = config['Telegram']['api_hash']
        phone_number = config['User']['phone_number']
    else:
        # If the config file doesn't exist, prompt the user for input
        print("To use this script, you need to obtain your own Telegram API ID and API Hash.")
        print("Please follow these steps:\n"
              "1. Go to https://my.telegram.org\n"
              "2. Log in with your Telegram account\n"
              "3. Navigate to 'API development tools' and create a new app\n"
              "4. You'll receive your 'api_id' and 'api_hash'")

        # Get user input for API credentials
        api_id = input("Enter your Telegram API ID: ")
        api_hash = input("Enter your Telegram API Hash: ")

        # Save the credentials in the config file
        config['Telegram'] = {
            'api_id': api_id,
            'api_hash': api_hash
        }
        with open(config_file, 'w') as configfile:
            config.write(configfile)

    return int(api_id), api_hash, phone_number

# Get the credentials (either from the file or user input)
api_id, api_hash, phone_number = get_api_credentials()

# Prompt for phone number
if not phone_number: phone_number = input("Enter your phone number (in international format, e.g., +123456789): ")
# Initialize Pyrogram Client
uvloop.install()
app = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number)
dialogs = []
channels =[]
async def main():
    async with app:
        async for dialog in app.get_dialogs():
            # print(dialog.chat.title or dialog.chat.first_name, dialog.chat.type)
             if dialog.chat.type.value == "channel":
                 print (f"{dialog.chat.title}")
                 channels.append(dialog)

app.run(main())

