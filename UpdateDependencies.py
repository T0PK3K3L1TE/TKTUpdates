import os, socket, time, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

Banner = bcolors.OKGREEN+"""
##################################################
###."""+bcolors.FAIL+"""_/ \_   ____ /    \  \/  /  ____/|  \/  /."""+bcolors.OKGREEN+"""###
##."""+bcolors.FAIL+"""|_  __| / __ \|  __/     /|  |__  |     /."""+bcolors.OKGREEN+"""  ##
##."""+bcolors.FAIL+"""|  |  | /  \ |  | |  \  \|   __/ |  \  \."""+bcolors.OKGREEN+"""   ##
##."""+bcolors.FAIL+"""|  |__| \__/ |  | |  |\  \   |___|  |\  \."""+bcolors.OKGREEN+"""  ##
###."""+bcolors.FAIL+"""\____/\____/\__/ |__| \__\_____/|__| \__\."""+bcolors.OKGREEN+"""###
##################################################
"""

versions = """
##################################################
###/~~/...       """+bcolors.OKBLUE+"""1) Version 0.0.7"""+bcolors.OKGREEN+"""       ...\~~\###
##/~~/..         """+bcolors.OKBLUE+"""2) Version 0.0.8"""+bcolors.OKGREEN+"""         ..\~~\##
#~~|...          """+bcolors.FAIL+"""3) No Other Update"""+bcolors.OKGREEN+"""          ...|~~#
##\~~\..         """+bcolors.FAIL+"""4) No Other Update"""+bcolors.OKGREEN+"""         ../~~/##
###\~~\...       """+bcolors.FAIL+"""5) No Other Update"""+bcolors.OKGREEN+"""       .../~~/###
##################################################
"""+bcolors.FAIL+""" Type """+bcolors.ENDC+"""'abort'"""+bcolors.FAIL+""" To Exit Script"""+bcolors.OKGREEN+"""
"""

host = socket.gethostname()

def VersionChoiceStart():
    print Banner
    print versions
    VersionChoice()

def VersionChoice():
    continueme = raw_input(bcolors.OKBLUE+"["+bcolors.FAIL+str(host)+bcolors.OKBLUE+"]?:>> ")
    if continueme == str("1"):
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version007/install.py")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version007/TKT007.py")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/UpdateLog.txt")
        os.system("python install.py")
        sys.exit(1)

    elif continueme == str("2"):
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version008/TKT008.py")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version008/UpdateLog.txt")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version008/install.py")
        os.system("python install.py")
        sys.exit(1)

    elif continueme == str("abort"):
        print bcolors.WARNING+"Operation Aborted..."
        sys.exit(1)

    else:
        print bcolors.WARNING+"Operation Suspended Due To "+bcolors.FAIL+"'Invalid Entry'"+bcolors.WARNING
        sys.exit(1)

VersionChoiceStart()
