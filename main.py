from pwd_generator import Generator
from pwd_manager import Commands
import sys


go = Generator()
co = Commands()
title = """                                   
 _ ____      ____| |_ __ ___  _ __   __ _ _ __ 
| '_ \ \ /\ / / _` | '_ ` _ \| '_ \ / _` | '__|
| |_) \ V  V / (_| | | | | | | | | | (_| | |   
| .__/ \_/\_/ \__,_|_| |_| |_|_| |_|\__, |_|   
|_|                                 |___/   """

"""COMMANDS:
        . n
            - websitename
        . u
            - websitename
        . r
            - websitename
        . v
        . help
        . exit
"""
print(title)
def get_command():
    command = input("Enter a command: ")
    return command
command = get_command()

# The following is the most innefficient way to loop, but it is 3:00 AM and I am tired
if command == "help":
    print(""". n: Makes a new query\n. u: Updates a password\n. v: View a query\n. r: Remove a query\n. va: View all queries\n. exit: exits your code ^^\n. help: it is obvious...""")
    get_command()
elif command == "exit":
    sys.exit()
elif command == "n":
    wbname = input("Enter the site name: ")
    pwd = go.generate_pwd()
    co.new_query(wbname, pwd)
    get_command()
elif command == "u":
    wbname = input("Enter the site name: ")
    co.update_query(wbname)
    get_command()
elif command == "v":
    co.view_all()
    get_command()
elif command == "r":
    wbname = input("Enter the site name: ")
    co.remove_query(wbname)
    get_command()