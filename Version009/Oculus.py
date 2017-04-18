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

Help = bcolors.OKBLUE+ """
#################################################
####~~-------------------------------------~~####
###~~~ """+bcolors.HEADER+"""             Commands"""+bcolors.OKBLUE+"""               ~~~###
##~~~~ """+bcolors.OKGREEN+"""1) Check For Possible New Assets"""+bcolors.OKBLUE+"""    ~~~~##
##~~~~ """+bcolors.OKGREEN+"""2) Copy Template And Move"""+bcolors.OKBLUE+"""           ~~~~##
##~~~~ """+bcolors.OKGREEN+"""3) Compatability Check """+bcolors.OKBLUE+"""             ~~~~##
###~~~ """+bcolors.OKGREEN+"""                ~&~"""+bcolors.OKBLUE+"""                 ~~~###
####~~-------------------------------------~~####
#################################################
         Use """+bcolors.FAIL+"""'abort'"""+bcolors.OKBLUE+""" to escape all actions
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
        os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/AssetDependencies.py")
        os.system("python AssetDependencies.py")
        os.system("rm AssetDependencies.py")
        Command_Hub()

    elif commandhub == str("2"):
        print bcolors.HEADER+"Listing Possible Files..."
        os.system("ls")
        print bcolors.OKBLUE+"Please Enter The Directory: "
        copyfilecheck = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> ")
        print bcolors.OKGREEN+"Checking If Path Exists..."
        entetedfilecheck = os.path.exists(str(home)+"/"+str(copyfilecheck))
        if enteredfilecheck == True:
            os.chdir(str(home)+"/"+str(enteredfilecheck))
            print bcolors.ENDC+"Listing Templates..."
            os.system("ls")
            print bcolors.HEADER+"Please Enter Disired File: "
            templateinput = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> ")
            template_set = os.getcwd()+"/"+str(templateinput)
            print bcolors.OKBLUE+"Please Enter A Target Directory: "
            targetdir = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> ")
            print bcolors.WARNING+("Checking Path...")
            targetdirchk == os.path.exists(str(targetdir))
            if targetdirchk == True:
                print bcolors.OKGREN+"Positive Directory Entered..."
                print "Moving..."
                os.system("cp "+str(template_set)+" "+str(targetdir))
                print bcolors.HEADER+"Operation Successfull..."
                Command_Hub()

            elif targetdirchk == False:
                print bcolors.FAIL+"Operation Failed Due To "+bcolors.WARNING+"'Invalid Target Directory':"+bcolors.ENDC+str(targetdir)
                Command_Hub()

            else:
                print bcolors.FAIL+"Operation Failed..."
                Command_Hub()

        elif entetedfilecheck == False:
            print bcolors.FAIL+"Operation Failed Due To "+bcolors.WARNING+"Invalid Entry"
            Command_Hub()

        else:
            print bcolors.FAIL+"Operation Failed..."
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
