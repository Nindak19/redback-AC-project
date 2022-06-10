#Simple code to generate csv data on setups
# 0.1 Due to me being cheap, make sure you specified the correct track, conditions, race type, car from assetto corsa or content manager and run atleast once!
# 0.2 How assetto corsa should be set....
#   - ideal conditions
#   - ai aggro = 0%
#   - ai skill = 100%
#   - track = optimum
#   - weekend session
#       - 10 opponents
#       - skip practice
#       - quali = 20 minutes
#   - candidates = specific car
#   - presets
#       - autoshift = ON
#       - abs and traction control == OFF
#       - fuel consumption = 0
#       - tyre wear = 0
#       - mechanical damage == OFF
#       - 1x slipstream effect
# 1 Load new setup into specified vehicle location
# 2. type in "acs.exe" to run assetto corsa executable
# 3. Let assetto corsa run until qualifying is over (for now we can say thats 20 minutes) Then terminate using "taskkill /f /im acs.exe"
# 4. Unload setup folder with csv_data into training_data folder, renaming setup to "setup_xxx". A counter should be kept in training data tracking the next setup number
#       e.g if latest is setup_143, counter.txt will contain 144 (next is 144)
#   the vehicle folder should now have no data folder
# 5. Repeat steps 1-4 for number of times i

import sys
import setup
import os
from time import time
import subprocess

#for now, just put the absolute file path below... We will use this to reference the vehicle we modify/update
vehicle = "formula_sae_rb19"
vehiclePath = "C:\\Program Files (x86)\Steam\\steamapps\\common\\assettocorsa\\content\\cars\\" + vehicle
#the repo directory...
currentDirectory = "redback-AC-project" # repo name 

def main(): #assume for now we simply call "python generator.py i", argv[0] = file call, argv[1] is first command line arg if it exist
    # argv[1] = first argument, number of iterations (setups)
    # argv[2] = time of execution in minutes
    checkInputs()
    checkFolderExists(currentDirectory+"/training_data")
    cur_time = time()

    i = 0
    setup.storeData(vehiclePath)        # Currently doesn't do anything
    load()
    subprocess.Popen("acs.exe", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)   # Start Assetto Corsa
    while i < int(sys.argv[1]):
        if (time() - cur_time)/60 > int(sys.argv[2]):
            os.system("taskkill /im acs.exe")       # Kill game when timer is up
            unload(len(os.listdir(currentDirectory+"/training_data")))
            cur_time = time()
            i = i + 1
            if i < int(sys.argv[1]):
                load()
                subprocess.Popen("acs.exe", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    
def load():
    setup.loadData(vehiclePath)
    
def unload(counter):
    setup.unloadData(vehiclePath, currentDirectory+"/training_data", counter)
    setup.copyData(vehiclePath)

def checkInputs():
    if len(sys.argv)-1 != 2:
        print("WARNING: format is incorrect, please include the number of iterations and the execution time")
        exit(-1)
    if not sys.argv[1].isdigit() or not float(sys.argv[1]).is_integer() or float(sys.argv[1]) <= 0:
        print("WARNING: Ensure iterations is a positive whole number")
        exit(-1)
    if not sys.argv[2].isdigit() or not float(sys.argv[2]).is_integer() or float(sys.argv[2]) <= 0:
        print("WARNING: Ensure minutes for execution is a positive whole number")
        exit(-1)
    if not os.path.isdir(vehiclePath+"\data"):
        print("WARNING: Make sure the vehicle has a data folder")
        exit(-1)

def checkFolderExists(path):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as e:
            print("Cannot generate directory path" + path)
        else:
            print("Generated directory" + path)

if __name__ == "__main__":
    main()