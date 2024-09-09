#!/usr/bin/env python3
import os
import configparser
from pyrogram import Client

# Define the path to the config file
config_file = 'config.ini'

# Function to read or prompt for API credentials
def get_api_credentials():
    config = configparser.ConfigParser()

    # Check if the config file exists
    if os.path.exists(config_file):
        config.read(config_file)
        api_id = config['Telegram']['api_id']
        api_hash = config['Telegram']['api_hash']
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

    return int(api_id), api_hash

# Get the credentials (either from the file or user input)
api_id, api_hash = get_api_credentials()

# Prompt for phone number
phone_number = input("Enter your phone number (in international format, e.g., +123456789): ")
# Initialize Pyrogram Client
app = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number)

# Main function to retrieve the list of subscribed channels
# async def list_channels():
#     with app:
#         print("Successfully logged in.")
#         
#         # Fetch the list of dialogs (channels, groups, etc.)
#         dialogs = app.get_dialogs()
#
#         # Filter only the channels from the dialogs
#         channels = [dialog.chat for dialog in dialogs if dialog.chat.type == "channel"]
#
#         # Print the subscribed channels
#         print("\nSubscribed channels:")
#         for channel in channels:
#             print(f"Channel: {channel.title}, ID: {channel.id}")
#
# # Run the function to list subscribed channels
# app.run(list_channels())
async def main():
    async with app:
        async for dialog in app.get_dialogs():
            print(dialog.chat.title or dialog.chat.first_name)


app.run(main())

