import os, re, socket, time, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

home   = os.getcwd()
host   = socket.gethostname()

Banner = bcolors.OKGREEN+"""
##############################################
#.........--....___. .....____...............#
#....... /  \__/   \_ __ /    \ .............#
#...... / /\ \_     _/  \|  __/ .............#
#..... / // \ \|   |     |  | ...............#
#.... / //   \ \___/\___/\__|______ __  __ ..#
#... / ///    \ \  .. |  \/ /| ____\  \/ / ..#
#... \ \      / /  .. |  \  \|  _|_|  \  \ ..#
#.... \ \    / /  ... |__|\__\____/|__|\__\ .#
#..... \ \  / /  ............................#
#...... \ \/ /  .............................#
#....... \  / ...............................#
#.........--.................................#
#--------------------------------------------#
#  o                |                        #
#            .     -O-                     | #
# .                 |        *      .     -0-#
#         *  o     .    '       *      .   | #
#                .         .        |        #
#     *             *              -O-       #
#      ___     .             *      |     ,  #
#   __/   \__           .           o        #
#   \_______/    *                           #
#     / * \   .           *    |  .       *  #
#    /*   *\       . *        -0-    *     , #
#  .   *   .           ,       | .  ,        #
##############################################
          CopyRight @ Jackel | #TopKek
             We Are Always Watching
"""

def Main():
    print Banner
    print bcolors.OKBLUE + "Checking For Updates..."
    print bcolors.HEADER + "Grabbing Current Version..."
    uversion = open("Version.txt", "r")
    for line in uversion:
        userversion = line

    uversion.close()
    print bcolors.OKGREEN + "Current Version Found         : "+bcolors.FAIL+str(userversion)
    os.chdir("Updates")
    print bcolors.OKGREEN + "Updateing Directory File..."
    dirupdate = open("dir.txt", "w")
    dirupdate.write(str(home))
    dirupdate.close()
    print bcolors.OKGREEN + "Home Set To                   : "+bcolors.FAIL+str(home)
    print bcolors.OKGREEN + "Current Directory Set To      : "+bcolors.FAIL+os.getcwd()
    print bcolors.OKGREEN + "Time Set To                   : "+bcolors.FAIL+time.asctime()
    print bcolors.WARNING + "Checking For Current Global... "+bcolors.FAIL
    os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/Version.txt -q")
    cversion = open("Version.txt", "r")
    for line in cversion:
        currentversion = line

    cversion.close()
    print bcolors.OKGREEN + "Current Version Found         : "+bcolors.FAIL+str(currentversion)
    print bcolors.OKGREEN + "Cleaning "+bcolors.FAIL+"Version.txt"
    os.system("rm Version.txt")
    print bcolors.OKGREEN + "Purged Testing Current Version Compared To Current Set."
    if str(userversion) == str(currentversion):
        print bcolors.OKBLUE + "No Possible Updates..."
        sys.exit(1)

    else:
        print bcolors.WARNING + "Checking For Possilbe Updates..."
        print bcolors.WARNING + "Potentially Grabbing Update Dependency File"
        print bcolors.FAIL    + "Do You Wish To Continue?[Y/n]"
        continueme = raw_input(bcolors.FAIL+"["+bcolors.OKBLUE+str(host)+bcolors.FAIL+"]?:>> ")
        if continueme == str("y" or "Y"):
            print bcolors.OKGREEN + "Grabbing File..."
            os.system("wget https://raw.githubusercontent.com/T0PK3K3L1TE/TKTUpdates/master/UpdateDependencies.py -q")
            print bcolors.OKGREEN + "File Grabbed..."
            print bcolors.OKBLUE  + "Running..."
            time.sleep(3)
            os.system("python UpdateDependencies.py")
            print bcolors.FAIL    + "Purging Files..."
            os.system("rm UpdateDependencies.py")
            print bcolors.OKGREEN + "File Purged Returning..."
            sys.exit(1)

        elif continueme == str("n" or "N"):
            print bcolors.OKGREEN + "Returning..."
            sys.exit(1)

        else:
            print bcolors.FAIL + "Operation Failed Due To: "+bcolors.WARNING+"'Invalid Entry'"
            sys.exit(1)

Main()
