import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device1_folder = glob.glob(base_dir + '28*')[0]
device2_folder = glob.glob(base_dir + '28*')[1]
device3_folder = glob.glob(base_dir + '28*')[2]

device_files = [device1_folder + '/w1_slave', device2_folder + '/w1_slave', device3_folder + '/w1_slave']


def read_temp_raw(sensor_num):
    f = open(device_files[sensor_num], 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(sensor_num):
    lines = read_temp_raw(sensor_num)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(sensor_num)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000
        return temp_c

while True:
    print("Sensor 1: " + str(read_temp(0)) + "\tSensor 2: " + str(read_temp(1)) +
          "\tSensor 3: " + str(read_temp(2)))
    time.sleep(0.5)

