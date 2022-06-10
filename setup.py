import random
import shutil # use to copy over folder
import os
import itertools
import json
tmp = "\default"
user = os.getlogin()

currentDirectory = "redback-AC-project" # repo name 

setup = {  #dictionary of tuples, where order is [static, minimum_value, maximum_value]
    'suspensions.ini': {
    #parameters broken up by file location
        '[FRONT]': { 
            'TOE_OUT': [0.0015, -0.0015, 0.004], #toe_out_l; length increase of steering link in mm
            'STATIC_CAMBER': [0, -3, 0.5], #camber_F
            'DAMP_BUMP': [2500, 1000, 3500], #damp_slow_bump_F
            'DAMP_FAST_BUMP': [1250, 500, 3500], #damp_fast_bump_F
            'DAMP_REBOUND': [2900, 1500, 4000], #damp_slow_rebound_F
            'DAMP_FAST_REBOUND': [1250, 500, 3500], #damp_fast_rebound_F
            'SPRING_RATE': [38800, 20000, 45000], #wheel_rate_F
            'ROD_LENGTH': [0.012, 0.0, 0.03],  #rod_length_F
            'PACKER_RANGE': [0.08, 0.04, 0.12], #packer_range_F; max sus travel
            'BUMP_STOP_RATE': [90000, 50000, 200000], #bump_stop_F; packer rate
            'TRACK': [1.1, 1, 1.4] #front track
        }, '[HEAVE_FRONT]': {
            'ROD_LENGTH': [0, 0, 0.03],
            'SPRING_RATE': [0, 0, 80000],
            'DAMP_BUMP': [0, 0, 8000],
            'DAMP_FAST_BUMP': [0, 0, 4000],
            'DAMP_REBOUND': [0, 0, 4000],
            'DAMP_FAST_REBOUND': [0,0, 4000]
        }, '[REAR]': {
            'TOE_OUT': [0.0015, -0.0015, 0.004], #toe_out_R; lenght of increase of steering link
            'STATIC_CAMBER': [0, -3, 0.5], #camber_R
            'DAMP_BUMP': [2950, 1000, 4000], #damp_slow_bump_R
            'DAMP_FAST_BUMP': [1350, 500, 3500], #damp_fast_bump_R
            'DAMP_REBOUND': [3400, 1500, 4500], #damp_slow_rebound_R
            'DAMP_FAST_REBOUND': [1350, 500, 3500], #damp_fast_rebound_R
            'SPRING_RATE': [57300, 20000, 65000], #wheel_rate_R
            'ROD_LENGTH': [0.008, 0.0, 0.03], #rod_length_R
            'PACKER_RANGE': [0.08, 0.04, 0.12], #packer_range_R
            'BUMP_STOP_RATE': [90000, 50000, 200000], #bump_stop_R
            'TRACK': [1.1, 1, 1.4] #rear track
        }, '[HEAVE_REAR]': {
            'ROD_LENGTH': [0, 0, 0.03],
            'SPRING_RATE': [0, 0, 80000],
            'DAMP_BUMP': [0, 0, 8000],
            'DAMP_FAST_BUMP': [0, 0, 4000],
            'DAMP_REBOUND': [0, 0, 4000],
            'DAMP_FAST_REBOUND': [0,0, 4000]
        }, '[ARB]': {
            'FRONT': [0, 0, 30000], #arb_F
            'REAR': [0, 0, 30000] #arb_R
        }, '[BASIC]': {
            'WHEELBASE': [1.55, 1.525, 1.9], #wheelbase
            'CG_LOCATION': [0.483, 0.35, 0.6] #center of mass
        } 
    }, 'tyres.ini': {
        #tyres.ini file
        '[FRONT]': {
            'PRESSURE_STATIC': [11, 6, 20] #pressure_F
        }, '[REAR]': {
            'PRESSURE_STATIC': [11, 6, 20] #pressure_R                  
            }
    }, 'drivetrain.ini': {
        #drivetrain.ini
        '[DIFFERENTIAL]': {
            'POWER': [0.25, 0, 1.0],  #differential on power lock
            'COAST': [0.25, 0, 1.0], #differential off power lock
            'PRELOAD': [0, 0, 25] #diff preload
        }
    }, 'brakes.ini': {
        #brakes.ini
        '[DATA]': {
            'FRONT_SHARE': [0.66, 0.5, 0.85], #brake bias
            'MAX_TORQUE': [650, 400, 800] #brake power
        }
    }
}



# def generateSetup():    # Generates a randomised setup (this needs to change so that it takes in setup values from the UI)
#     global setup
#     nSetup = {}
#     for config in setup:
#         nSetup[config] = {}
#         for heading in setup[config]:
#             nSetup[config][heading] = {}
#             for parameter in setup[config][heading]:
#                 min = setup[config][heading][parameter][1]
#                 max = setup[config][heading][parameter][2]
#                 nSetup[config][heading][parameter] = round(random.uniform(min,max),5)   # nSetup[config][heading][parameter] = nSetup[config][heading][parameter][0]
#     return nSetup

def loadData(vehicleFolder):    # Writes the setup into f_setup(vehicleFolder is ...content/cars/formula_sae_rb19)
    jsonFile = open(f"{currentDirectory}\\trial_data.json")
    setup = json.load(jsonFile)
    # setup = generateSetup()     
    referenceFolder = vehicleFolder + tmp   # referenceFolder is the vehicleFolder + tmp (\default) contains the unchanged setup 
    setupFolder = vehicleFolder + "\data"   # setupFolder is a new folder 
    if os.path.exists(setupFolder+"\csv_data"):
        shutil.rmtree(setupFolder+"\csv_data")  # If (...content/cars/formula_sae_rb19/data/csv_data) exists, delete that directory
    for config in setup:                        # Loops through each ini file (suspensions.ini, tyres.ini etc)
        if config == 'race.ini':
            setup_raceini(setup, vehicleFolder)
            continue
        f_data = open(referenceFolder + '\\' + config, 'r')     # Open (with read permissions) directory ...content/cars/formula_sae_rb19/default/(.ini file)
        f_setup = open(setupFolder + '\\' + config, 'w')        # Open (with write permissions) directory ...content/cars/data/formula_sae_rb19/data/(.ini file)
        heading = ''
        newLine = ''
        for line in f_data:                                     # For each line in the default/.ini file
            heading = getHeading(line, heading, setup[config].keys())   # setup[config].keys() is a list of all headings i.e. ([FRONT], [HEAVE_FRONT] etc.)
            if heading != '':                               
                newLine = adjustValue(setup[config][heading], line)     # setup[config][heading] = e.g. entire dictionary of [DIFFERENTIAL] = {'POWER': 0.40738, 'COAST': 0.59882, 'PRELOAD': 24.59209}
                if newLine == '':                                       # If newLine is an empty string, then write the original line back into the .ini file
                    f_setup.write(line)
                else:                                                   # Otherwise write the new parameter into the .ini file
                    f_setup.write(newLine)
            else:
                f_setup.write(line)
        f_data.close()
        f_setup.close()
    return

def unloadData(vehicleFolder, setupFolder, counter):
    if os.path.isdir(setupFolder+"\data_+"+str(counter)):
        print("ERROR: " +setupFolder+"\data_+"+str(counter)+ "already exists in " + setupFolder)
        exit(-1)
    arr = os.listdir(vehicleFolder + "\csv_data")
    print(arr)
    csv_data = vehicleFolder + "/csv_data/" + arr[0]        # arr[0] is 2022-05-26-20-21_losarcos
    setupData = vehicleFolder + "\data_" + str(counter)
    os.rename(vehicleFolder + "\data", setupData)   # Rename ...content/cars/formula_sae_rb19/data -> ...content/cars/formula_sae_rb19/data/1
    shutil.move(csv_data, setupData)                # Move ...content/cars/formula_sae_rb19/csv_data/2022-05-26-20-21_losarcos -> ...content/cars/formula_sae_rb19/data/12
    shutil.move(setupData, setupFolder)             # Moves ...content/cars/formula_sae_rb19/data/12 -> steamapps/common/assettocorsa/generator_test/training_data
    shutil.rmtree(vehicleFolder + "\csv_data")      # Remove directory ...content/cars/formula_sae_rb19/csv_data

def getHeading(line, heading, keys):                # getHeading returns either a heading or key
    for key in keys:
        if key in line:
            return key                              # returns a key if the line that is being compared to is one of the keys in the current ini file (e.g. suspensions.ini), e.g. [FRONT], [HEAVE_FRONT] (this is returned each time a new heading is found)
    return heading                                  # returns heading (such as [FRONT] or '' if it is an empty line) if no matched key is found in the keys list (the same heading is returned repeatedly until a new heading is found))

def adjustValue(heading_dict, line):                # Returns a new line which is either an empty string if the line was not a parameter that needs to be changed or a string containing a parameter with a new value, e.g. DAMP_FAST_REBOUND=2376.03006
    line = line.split('=')[0]                       # If it is a parameter being changed, grabs only the parameter name, e.g. If line being split = 'WHEELBASE=1.54', line = WHEELBASE
    for parameter in heading_dict:
        if parameter == line:
            return parameter + '=' + str(heading_dict[parameter]) + '\n'
    return ''

def storeData(vehicleFolder):
    if not os.path.exists(vehicleFolder+tmp):
        shutil.copytree(vehicleFolder + "\data", vehicleFolder + tmp)
        shutil.copyfile(f"C:\\Users\\{user}\\Documents\\Assetto Corsa\\cfg\\race.ini", vehicleFolder + tmp)
    if os.path.exists(vehicleFolder+"data\csv_data"):
        shutil.rmtree(setupFolder+"data\csv_data")

def copyData(vehicleFolder):
    shutil.copytree(vehicleFolder+tmp, vehicleFolder+"\data")
    os.remove(vehicleFolder+"\\data\\race.ini")

def setup_raceini(setup, vehicleFolder):
    raceSetup = f"C:\\Users\\{user}\\Documents\\Assetto Corsa\\cfg\\race.ini"
    raceDefault = vehicleFolder + tmp + "\\race.ini"
    f_data = open(raceDefault, 'r')
    f_setup = open(raceSetup, 'w')
    heading = ''
    newLine = ''
    for line in f_data:
        heading = getHeading(line, heading, setup['race.ini'].keys())
        if heading != '':
            newLine = adjustValue(setup['race.ini'][heading], line)
            if newLine == '':
                f_setup.write(line)
            else:
                f_setup.write(newLine)
        else:
            f_setup.write(line)
    f_data.close()
    f_setup.close()
    return



