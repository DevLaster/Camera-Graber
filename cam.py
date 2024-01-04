from pystyle import *
import os
from colorama import *
import time
import requests
import re
from tqdm import tqdm
import random

os.system('clear' if os.name == 'posix' else 'cls')

intro = """
 ▄▀▄▄▄▄    ▄▀▀█▄     ▄▄▄▄▄▄▄▄▄▄▄   ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄      ▄▀▀▄▀▀▀▄
█ █    ▌  ▐ ▄▀ ▀▄             █    █   █   ▐  ▄▀   ▐     █   █   █   Lasterfor3ver
▐ █         █▄▄▄█     ▄▄▄▄▄▄▄▄     ▐  █     █▄▄▄▄▄       ▐  █▀▀█▀
 █        ▄▀   █      █              █      █    ▌        ▄▀    █ 
 ▄▀▄▄▄▄▀  █   ▄▀      █            ▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄        █     █
█     ▐  ▐   ▐       ▄▄▄▄▄▄▄▄      ▄▄▄▄▄▄▀  █    ▐        ▐     ▐ 
▐                        
                

"""

Anime.Fade(Center.Center(intro), Colors.purple_to_blue, Colorate.Vertical, interval=0.035, enter=True)

print(f"""{Fore.LIGHTBLUE_EX}

 ▄▀▄▄▄▄    ▄▀▀█▄     ▄▄▄▄▄▄▄▄▄▄▄   ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄      ▄▀▀▄▀▀▀▄
█ █    ▌  ▐ ▄▀ ▀▄             █    █   █   ▐  ▄▀   ▐     █   █   █   
▐ █         █▄▄▄█     ▄▄▄▄▄▄▄▄     ▐  █     █▄▄▄▄▄       ▐  █▀▀█▀
 █        ▄▀   █      █              █      █    ▌        ▄▀    █ 
 ▄▀▄▄▄▄▀  █   ▄▀      █            ▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄        █     █
█     ▐  ▐   ▐       ▄▄▄▄▄▄▄▄      ▄▄▄▄▄▄▀  █    ▐        ▐     ▐ 
▐                        
         

""")

time.sleep(1)

countries = ["US","IR"]

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

name = input(f"Enter your name: ")
name_entered = True  

while True:
    if name_entered:
        Write.Print(f"Welcome, {name}!", Colors.purple_to_blue)
        print("\n")
        name_entered = False  

    Write.Print("1 Start Grabing Ips ( Ips Will Save In Text)", Colors.purple_to_blue)
    print("\n")
    Write.Print("2.Exit The Tool", Colors.purple_to_blue)
    print("\n")
    num = int(input("OPTIONS : "))

    if num == 1:
        try:
            country = countries[0]
            res = requests.get(f"http://www.insecam.org/en/bycountry/{country}", headers=headers)
            last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

            ip_list = []

            with tqdm(total=int(last_page), desc="Loading") as pbar:
                for page in range(int(last_page)):
                    res = requests.get(
                        f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
                        headers=headers
                    )
                    find_ip = re.findall(r"http://\d+\.\d+\.\d+\.\d+:\d+", res.text)
                    ip_list.extend(find_ip)
                    pbar.update(1)

            with open("ips.txt", "w") as file:
                file.write("\n".join(ip_list))

            print("\nIP addresses saved to 'ips.txt'")
            time.sleep(3)
            exit()
        except Exception as e:
            print("Error While Searching IPs! Please Try Again", e)
        finally:
            print("\033[1;37m")
    elif num == 2:
        break

if num == 2:
    exit()
