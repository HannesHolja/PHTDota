#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     To manage the GUI and data flow. In the MVC-model
#              this is the controller
#
# Author:      Hannes Holja
#
# Created:     05.02.2014
# Copyright:   (c) Hannes Holja 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from pelaajat import *
from pickler import *

def add_player():
    pass
def manage_playerdata():
    pass
def delete_player():
    pass
def searchforplayer():
    pass
def savedata():
    saveplayers(listofplayers)
def loaddata():
    listofplayers = load()
    return listofplayers

def main():
    print("Hello World!")
    listofplayers = load()
    print(listofplayers)
main()
