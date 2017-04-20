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

filestoreplace1 = "Assets/Oculus.py"
filestoreplace2 = "Assets/DefCon.py"
filestoreplace3 = "TKT009.py"
filestoreplace4 = "Updater.py"

tmpdir     = os.getcwd()
homedirset = open("dir.txt", "r")
time       = time.asctime()
host       = socket.gethostname()
for line in homedirset:
    home = line

homedirset.close()

def Install():
    print bcolors.OKBLUE + "Checking For Positive Directory's..."
    assetpath = os.path.exists(str(home)+"/Assets")
    if assetpath == True:
        print bcolors.OKGREEN+"Assets File Positive..."
        print bcolors.WARNING+"Checking For Needed Files For Replace..."
        defconpath = os.path.isfile(str(home)+"/Assets/DefCon.py")
        oculuspath = os.path.isfile(str(home)+"/Assets/Oculus.py")
        tkt009path = os.path.isfile(str(home)+"/TKT009.py")
        updatepath = os.path.isfile(str(home)+"/Updater.py")
        print bcolors.OKGREEN+"DefCon Status  : "+bcolors.FAIL+str(defconpath)+bcolors.OKGREEN
        print bcolors.OKGREEN+"Oculus Status  : "+bcolors.FAIL+str(oculuspath)+bcolors.OKGREEN
        print bcolors.OKGREEN+"TKT009 Status  : "+bcolors.FAIL+str(tkt009path)+bcolors.OKGREEN
        print bcolors.OKGREEN+"Updater Status : "+bcolors.FAIL+str(updatepath)+bcolors.OKGREEN
        print "Begining Install..."
        os.system("rm "+str(home)+"/Assets/DefCon.py")
        os.system("rm "+str(home)+"/Assets/Oculus.py")
        os.system("rm "+str(home)+"/Updater.py")
        os.system("rm "+str(home)+"/TKT009.py")
        os.system("mv DefCon.py "+str(home)+"/Assets")
        os.system("mv Oculus.py "+str(home)+"/Assets")
        os.system("mv TKT010.py "+str(home)+"/")
        os.system("mv Updater.py "+str(home)+"/")
        print bcolors.OKGREEN + "All Files Purged..."
        print "All Files Moved..."
        print bcolors.WARNING + "Update Finished"
        sys.exit(1)


print bcolors.OKGREEN    + "Temp Dir Set To: "+bcolors.FAIL+str(tmpdir)
print bcolors.OKGREEN    + "Home Dir Set To: "+bcolors.FAIL+str(home)
print bcolors.OKGREEN    + "TIme Set To    : "+bcolors.FAIL+str(time)
print bcolors.OKGREEN    + "Host Set To    : "+bcolors.FAIL+str(host)
print bcolors.OKGREEN    + "Files To Delete >> "
print bcolors.OKGREEN    + "File 1         : "+bcolors.FAIL+str(filestoreplace1)
print bcolors.OKGREEN    + "File 2         : "+bcolors.FAIL+str(filestoreplace2)
print bcolors.OKGREEN    + "File 3         : "+bcolors.FAIL+str(filestoreplace3)
print bcolors.OKGREEN    + "File 4         : "+bcolors.FAIL+str(filestoreplace4)
print bcolors.WARNING    + "Do you wish to continue? [Y/n]"
continueme = raw_input(bcolors.OKBLUE+"["+bcolors.BOLD+str(host)+bcolors.OKBLUE+"]?:>> ")
if continueme == str("y" or "Y"):
    Install()

elif continueme == str("n" or "N"):
    sys.exit(1)

else:
    sys.exit(1)
