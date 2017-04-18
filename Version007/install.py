import os, sys, time, socket

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

tempdir = os.getcwd()
host    = socket.gethostname()

filetoupdate1 = "TKT007.py"

FTD           = "TKT006.py"

homeset = open("dir.txt", "r")
for line in homeset:
    home = line

homeset.close()
print bcolors.WARNING+"Files To Update: "+str(filetoupdate1)+", Files To Delete: "+str(FTD)
print "Do You Wish To Continue?[Y/n]"
continueme = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> ")
if continueme == str("y" or "Y"):
    os.system("mv TKT007.py "+str(home))
    os.chdir(str(home))
    os.system("rm TKT006.py")
    print bcolors.ENDC+"Update Finished"
    sys.exit(1)

elif continueme == str("n" or "N"):
    sys.exit(1)

else:
    sys.exit(1)
