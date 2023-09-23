import sys
import linecache
import colorama
from colorama import Fore
colorama.init(autoreset=True)

print(Fore.LIGHTBLUE_EX + open("logo.txt", "r").read())
i = 1
try:
    debugging = str(sys.argv[2])
    if "debug" in debugging:
        def debug(text):
            print(Fore.RED + "[*]Debug: " + text)
            return
except IndexError:
    def debug(text):
        pass

switch = str(sys.argv[1])
if "add" in str(switch):
    ip = input("Enter ip address: ")
    name = input("Enter name: ")
    ipFile = open('ip.txt', 'w')
    nameFile = open('name.txt', 'w')
    ipFile.writelines(ip)
    nameFile.writelines(name)

elif str(switch) == "check":
    print("#0   Look for corresponding name")
    print("#1   Look for corresponding ip\n")
    look = str(input("User input~\n#"))
    if look == "0":
        name = input("Enter name: ")
        nameFile = open("name.txt", "r")
        lines = len(nameFile.readlines())
        while i < lines+1:
            current_line = linecache.getline(r"name.txt", i)
            debug(f"Iteration {i}, comparing {name} to {current_line}")
            if linecache.getline(r"name.txt", i) == name:
                print(Fore.LIGHTBLUE_EX + "[*]Match found")
                print(linecache.getline(r"ip.txt", i))
                exit()
        print(Fore.LIGHTBLUE_EX + "[*]No matches found")
    elif look == "1":
        ip = input("Enter ip: ")
        ipFile = open("ip.txt", "r")
        lines = len(ipFile.readlines())
        while i < lines+1:
            current_line = linecache.getline(r"ip.txt", i)
            debug(f"Iteration {i}, comparing {ip} to {current_line}")
            if str(ip) in str(linecache.getline(r"ip.txt", i)):
                print(Fore.LIGHTBLUE_EX + "[*]Match found\n")
                print(ip + " --> " + linecache.getline(r"name.txt", i))
                exit()
            i+=1
        print(Fore.LIGHTBLUE_EX + "[*]No matches found")
elif "list" in str(switch):
    print(open("ip.txt", "r").read())
    print("============================")
    print(open("name.txt", "r").read())
