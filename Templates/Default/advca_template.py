import os, time, socket, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

Banner = """

banner

"""

host = socket.gethostname()
home = os.getcwd()

def Running():
    main_command = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> ")
    if main_command == str("exit"):
        print bcolors.OKBLUE+"Exiting..."
        sys.exit(1)

    # Add commands here with elif main_command == str("input variable"):

    else:
        print bcolors.FAIL+"Operation Failed Due To "+bcolors.WARNING+"'Invalid Commands'"
        Running()

def Main_Commands():
    print banner
    Running()

Main_Commands()
