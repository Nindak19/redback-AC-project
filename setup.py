import random
import shutil # use to copy over folder
import os
import itertools


#we need a folder location so we can read in and then export new Data folders, assume this is our folder location for now

#generate setup and load into...
data = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\assettocorsa\\content\\cars\\formula_sae_rb19\\data'

counter = 0

tmp = "\original"

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
            'FRONT': [0, 0, 150000], #arb_F
            'REAR': [0, 0, 150000] #arb_R
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

def generateSetup():
    global setup
    nSetup = {}
    for config in setup:
        nSetup[config] = {}
        for heading in setup[config]:
            nSetup[config][heading] = {}
            for parameter in setup[config][heading]:
                min = setup[config][heading][parameter][1]
                max = setup[config][heading][parameter][2]
                nSetup[config][heading][parameter] = round(random.uniform(min,max),5)
                value = nSetup[config][heading][parameter]
    return nSetup

def loadData(vehicleF):
    setup = generateSetup()
    refFol = vehicleF + tmp
    setupFol = vehicleF + "\data"
    shutil.copytree(refFol, setupFol, symlinks = True)
    if os.path.exists(setupFol+"\csv_data"):
        shutil.rmtree(setupFol+"\csv_data")

    for config in setup:
        f_data = open(refFol + '\\' + config, 'r')
        f_setup = open(setupFol + '\\' + config, 'w')
        heading = ''
        newLine = ''
        for line in f_data:
            heading = getHeading(line, heading, setup[config].keys())
            if heading != '':
                newLine = adjustValue(setup[config][heading], line)
                if newLine == '':
                    f_setup.write(line)
                else:
                    f_setup.write(newLine)
            else:
                f_setup.write(line)
        f_data.close()
        f_setup.close()
    return

def unloadData(vehicleFol, setupFol, counter):
    setupData = vehicleFol + "\data_" + str(counter)
    os.rename(vehicleFol + "\data", setupData)
    shutil.move(setupData, setupFol)

def getHeading(line, heading, keys):
    for key in keys:
        if key in line:
            return key
    return heading

def adjustValue(heading_dict, line):
    line = line.split('=')[0]
    for parameter in heading_dict:
        if parameter == line:
            return parameter + '=' + str(heading_dict[parameter]) + '\n'
    return ''

def hideData(vehicleFol):
    if not os.path.exists(vehicleFol+tmp):
        os.rename(vehicleFol + "\data", vehicleFol + tmp)