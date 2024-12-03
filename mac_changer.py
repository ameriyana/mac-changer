import subprocess
import time
import itertools
import sys
import threading
import random


mac = ""
print("Wellcome to simple tools mac address changer \n")
time.sleep(2)
print("Please a wait it will check your interface ... \n")
done = False
def loading():
    for i in itertools.cycle(['|', '/', '-', '\\']):
        if done :
            break
        sys.stdout.write('\rloading '+ i)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write('\rDone!    \n')
a = threading.Thread(target=loading)
a.start()
time.sleep(3)
done=True
#Check the network interface
subprocess.call(["ip", "-brief", "link"])
time.sleep(1)
interface = input("Select Your Interface : ")
print(f"your select in interface ,{interface} ")
#create random function
def __random():
        #Create variable to store random MAC Adress with random hexadecimal value
   mac =  ("00:%02x:%02x:%02x:%02x:%02x" %
    ( random.randint(0, 255),
    ( random.randint(0, 255)),
    ( random.randint(0, 255)),
    ( random.randint(0, 255)),
    ( random.randint(0, 255)),
     ))
   print(f"Your New Mac is {mac}")
   print("Please Wait it will be complete ")
   loading() #call loading function
    #call subprocess to execute terminal command
   subprocess.call(["sudo", "ifconfig", interface, "down"])
   subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
   subprocess.call(["sudo", "ifconfig", interface, "up"])
   time.sleep(1)
#create process function

def process():
    while True :
        ifput = input("Are you sure want to change the MAC Adress? y/n : ")
        if ifput == "yes" or ifput == "y" :
            print("Write random MAC or Manual \n")
            print("1. Random")
            print("2. Manual \n")
            ifput= int(input("Chose your : "))
            if ifput == 1 :
                print("print 1")
                __random()
                subprocess.call(["ip", "link", "show", interface ])
                print("\n SUCESS.")
                break
            if ifput == 2:
                   mac = input("Type your mac : ")

                   print(f"Your New Mac is {mac}")
                   print("Please Wait it will be complete ")
                   loading()
                   subprocess.call(["sudo", "ifconfig", interface, "down"])
                   subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
                   subprocess.call(["sudo", "ifconfig", interface, "up"])
                   subprocess.call(["ip","link", "show", interface])
                   break

        elif ifput == "n" or ifput == "no" :
               exit()
        else :
            print("Unexpect, please try again")
process()
