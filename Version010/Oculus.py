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

Banner = bcolors.HEADER + """
#################################################
##### ------------------------------------- #####
####  """+bcolors.FAIL+"""____  ____         _             ___   """+bcolors.HEADER+"""####
###  """+bcolors.FAIL+"""/ __ \/  __/   __  / |   _   __  / __/_  """+bcolors.HEADER+"""###
### """+bcolors.FAIL+"""| |__| | |_| \_/  \_| |__| \_/  \_\ __  | """+bcolors.HEADER+"""###
#### """+bcolors.FAIL+"""\____/\___/\___/\_/|____/\___/\_/\____/ """+bcolors.HEADER+"""####
##### ------------------------------------- #####
#################################################

"""

Help = bcolors.HEADER + """
#################################################
####~"""+bcolors.OKGREEN+"""0"""+bcolors.OKBLUE+""" ----------------------------------- """+bcolors.OKGREEN+"""1"""+bcolors.HEADER+"""~####
###~"""+bcolors.OKGREEN+"""01"""+bcolors.OKBLUE+"""|      """+bcolors.FAIL+"""T         """+bcolors.ENDC+"""HELP          """+bcolors.FAIL+"""K"""+bcolors.OKBLUE+"""    |"""+bcolors.OKGREEN+"""10"""+bcolors.HEADER+"""~###
##~"""+bcolors.OKGREEN+"""000"""+bcolors.OKBLUE+"""| --------------------------------- |"""+bcolors.OKGREEN+"""110"""+bcolors.HEADER+"""~##
#~"""+bcolors.OKGREEN+"""1111"""+bcolors.OKBLUE+"""| """+bcolors.WARNING+"""1) Get More Assets"""+bcolors.OKBLUE+"""                |"""+bcolors.OKGREEN+"""0111"""+bcolors.HEADER+"""~#
#~"""+bcolors.OKGREEN+"""0000"""+bcolors.OKBLUE+"""| """+bcolors.WARNING+"""2) See Installed Template"""+bcolors.OKBLUE+"""         |"""+bcolors.OKGREEN+"""0100"""+bcolors.HEADER+"""~#
##~"""+bcolors.OKGREEN+"""101"""+bcolors.OKBLUE+"""| """+bcolors.WARNING+"""3) Run Installed Assets"""+bcolors.OKBLUE+"""           |"""+bcolors.OKGREEN+"""101"""+bcolors.HEADER+"""~##
###~"""+bcolors.OKGREEN+"""01"""+bcolors.OKBLUE+"""|___________________________________|"""+bcolors.OKGREEN+"""10~"""+bcolors.HEADER+"""###
####~"""+bcolors.OKGREEN+"""011010110111001101101101011001000000101"""+bcolors.HEADER+"""~####
#################################################
### """+bcolors.FAIL+"""Extra Commands \                 """+bcolors.HEADER+"""           #
##------------------                            #
#   """+bcolors.WARNING+"""clear                 """+bcolors.OKBLUE+"""Clear screen"""+bcolors.HEADER+"""          #
#   """+bcolors.WARNING+"""exit                  """+bcolors.OKBLUE+"""Exits The Program"""+bcolors.HEADER+"""     #
#   """+bcolors.WARNING+"""host                  """+bcolors.OKBLUE+"""Prints Host Name"""+bcolors.HEADER+"""      #
#   """+bcolors.WARNING+"""dir                   """+bcolors.OKBLUE+"""Prints Current Dir"""+bcolors.HEADER+"""    #
##--------------------------------              #
### """+bcolors.FAIL+"""Use 'abort' To End All Actions \  """+bcolors.HEADER+"""           #
#################################################
"""


host = socket.gethostname()
home = os.getcwd()

def Command_Hub():
    os.chdir(str(home))
    print bcolors.HEADER+"Use 'help' To Display Help Screen"
    commandhub = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> ")
    if commandhub == str("help"):
        print Help
        Command_Hub()

    elif commandhub == str("1"):
        print bcolors.OKGREEN+"Checking..."
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/AssetDependencies.py -q")
        os.system("python AssetDependencies.py")
        os.system("rm AssetDependencies.py")
        Command_Hub()

    elif commandhub == str("2"):
        os.getcwd()
        os.chdir("Oculus/Templates")
        print bcolors.OKGREEN + "Listing Templats"
        os.system("ls")
        Command_Hub()

    elif commandhub == str("exit"):
        sys.exit(1)

    elif commandhub == str("host"):
        os.system("clear")
        print bcolors.FAIL + "Current Host: "+bcolors.OKBLUE+str(host)
        Command_Hub()

    elif commandhub == str("dir"):
        os.system("clear")
        print bcolors.FAIL + "Current Directory: "+bcolors.OKBLUE+os.getcwd()
        Command_Hub()

    else:
        os.system("clear")
        print Help
        print bcolors.FAIL + "Operation Failed Due To: "+bcolors.WARNING+"'Invalid Entry'"
        Command_Hub()

def Main_Commands():
    print bcolors.ENDC+"Loading Default Templates..."
    defaultassets = os.path.exists("Templates/Default")
    if defaultassets == True:
        print bcolors.OKBLUE + "Found Default Directory..."
        Command_Hub()

    elif defaultassets == False:
        print bcolors.OKBLUE+"Could Not Find Files Installing..."
        os.mkdir("Templates")
        os.chdir("Templates")
        os.mkdir("Default")
        os.chdir("Default")
        print bcolors.HEADER+"Created 'Template/Default'"
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Templates/Default/basic_template.py")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Templates/Default/advca_template.py")
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Templates/Default/tutor_template.py")
        sys.exit(1)

def Running():
    print Banner
    oculusexists = os.path.exists("Oculus")
    if oculusexists == True:
        os.chdir("Oculus")
        Main_Commands()

    elif oculusexists == False:
        os.mkdir("Oculus")
        sys.exit(1)

    else:
        print bcolors.WARNING+"Operation Failed..."
        sys.exit(1)

Running()
