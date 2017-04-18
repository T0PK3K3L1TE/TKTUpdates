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

def Main():
    print Banner
    input_me = raw_input(bcolors.OKBLUE+"["+bcolors.FAIL+str(host)+bcolors.OKBLUE+"]?:>> ")
    # Add Commands Below
    if input_me == str("exit"):
        print bcolors.WARNING+"Exiting..."
        sys.exit(1)

    else:
        print bcolors.FAIL+"Operation Failed Due To "+bcolors.HEADER+"'Invalid Entry'"
        Main()

Main()
