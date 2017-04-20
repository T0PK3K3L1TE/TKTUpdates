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
#~~|...          """+bcolors.OKBLUE+"""3) Version 0.0.9"""+bcolors.OKGREEN+"""          ...|~~#
##\~~\..         """+bcolors.OKBLUE+"""4) Version 0.1.0"""+bcolors+OkGREEN+"""         ../~~/##
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
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version007/install.py -q")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version007/TKT007.py -q")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/UpdateLog.txt -q")
        os.system("python install.py")
        print bcolors.WARNING + "Purging Files..."
        os.system("rm install.py")
        sys.exit(1)

    elif continueme == str("2"):
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version008/TKT008.py -q")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version008/UpdateLog.txt -q")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version008/install.py -q")
        os.system("python install.py")
        print bcolors.WARNING + "Purging Files..."
        os.system("rm install.py")
        sys.exit(1)

    elif continueme == str("3"):
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version009/Oculus.py -q")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version009/TKT009.py -q")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version009/UpdateLog.txt -q")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version009/install.py -q")
        os.system("python install.py")
        print bcolors.WARNING + "Purging Files..."
        os.system("rm install.py")
        sys.exit(1)

    elif continueme == str("4"):
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version010/DefCon.py -q")
        print bcolors.OKGREEN + "New DefCon.py  Downloaded"
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version010/Oculus.py -q")
        print bcolors.WARNING + "New Oculus.py  Downloaded"
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version010/TKT010.py -q")
        print bcolors.OKBLUE +  "UpdateLog.txt  Downloaded"
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version010/Updater.py -q")
        print bcolors.HEADER +  "New Updater.py Downloaded"
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version010/install.py -q")
        print bcolors.WARNING + "Install.py     Dowanloded"
        print bcolors.FAIL    + "Would you like to look at the update log before you install?[y/n]["+bcolors.WARNING+"WARNING:CASE SENSITIVE ( USE LOWER CASE)]"
        installcheck          = raw_input(bcolors.FAIL+"["+bcolors.OKBLUE+str(host)+bcolors.FAIL+"]?:>> ")
        if instalcheck == str("y" or "Y"):
            displaylogset = open("UpdateLog.txt", "r")
            for line in displaylogset:
                displaylog = line

            displaylogset.close
            print bcolors.OKGREEN + str(displaylog)
            print bcolors.FAIL    + "Do You Wish To Continue?"
            secondcheck           = raw_input(bcolors.OKGREEN+"["+bcolors.WARNING+str(host)+bcolors.OKGREEN+"][Y/n]?:>> ")
            if secondcheck == str("y" or "Y"):
                print bcolors.FAIL + "Running Install.py"
                os.system("python install.py")
                print bcolors.OKGREEN + "Purging Files..."
                os.system("rm install.py")
                os.system("mv UpdateLog.txt "+str(home))
                sys.exit(1)

            elif secondcheck == str("n" or "N"):
                print bcolors.FAIL + "Aborting"
                sys.exit(1)

            else:
                print bcolors.FAIL + "Operation Aborted Due To "+bcolors.OKBLUE+"'Invalid Entry'"

    elif continueme == str("abort"):
        print bcolors.WARNING+"Operation Aborted..."
        sys.exit(1)

    else:
        print bcolors.WARNING+"Operation Suspended Due To "+bcolors.FAIL+"'Invalid Entry'"+bcolors.WARNING
        sys.exit(1)

VersionChoiceStart()
