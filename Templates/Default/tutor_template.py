import os, time, socket, sys

#Modules Above Globally Used
#Tutorial By Jackel
#Globally Used Class

#Call Colors By '+bcolors.'color''+
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Banner To Display
Banner = bcolors.HEADER+"""
Banner
"""

# Global Used Functions Main_Commands And Running
# will can be used to keep a simple command structure
# looping commands will allow for simple user iteration

# Set host

host = socket.gethostname()
# Directories /Assets and /Updates will have a home dir
# this is shown as 'dir.txt' you can call this with simple
# file IO

# dirset = open("dir.txt", "r")
# for line in dirset:
#     home = line
#
# filenameset.close()

def Running():
    # Make a global input command
    # adding colors will spice up the screen
    # 'bcolors.FAIL' will set the text to red
    #
    # colors need to be called in incements as such
    # begining color till string end
    # in this case i used bcolors.OKGREEN+"[""]"
    # This will set all characters after to have green text
    # after my disired string character ended i seperate the string
    # to add variables you can use the following
    # +str()+ - string
    # +int()+ - initger
    #
    # with this i seperate the string
    # bcolors.OKGREEN+"[]" - green text
    # bcolors.OKGREEN+["+bcolors.FAIL"] - '[ ' -green text
    # everything after the +bcolors.FAIL will be red
    # soon after we call out host string and print it to the Screen
    # after we call the green again to allow the 'str(host)' to be red
    #      green                          red          green
    # bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>>"
    #                  green              red                    green
    inputcommand = raw_input(bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]")
    # Here you would set up your command structure
    # this is also where you can set up possible user input
    # as you can see we are seeing if the user inputs a '1'
    # if they do it will run the command function()
    # if our 'exit' command we are running code from that line
    # we also created a 'invalid entry' command under our else function
    # if inputcommand == str("1"):
    #     fuction()
    #
    # elif inputcommand == str("2"):
    #     function2()
    #
    # elif inputcommand == str("exit"):
    #     sys.exit(1)
    #
    # else:
    #     print bcolors.WARNING+"Invalid Entry..."
    #     os.system("clear")
    #     Running()
    sys.exit(1)

def Main_Commands():
    # Print Banner To Screen
    print Banner

    # Here you could put any extra commands needed to
    # run before startup
    # you can call modules from 'os' to allow to check file existence
    # this can look like the following
    # filevariable = os.path.exists("file")
    # if filevariable == True:
    #     commands
    #
    # elif filevariable == False:
    #     commands
    #
    # else:
    #     print bcolors.FAIL+"Operation Failed..."
    #     sys.exit(1)
    #
    # Send To Running
    Running()

#Call Main Function At Startup
Main_Commands()
