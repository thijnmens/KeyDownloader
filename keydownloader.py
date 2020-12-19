#######################################
# Operation Steal BeatSavers Database #
#######################################
#      Created by: Thijnmens          #
#         Version: 1.1.2              #
#######################################

import webbrowser
import time
import sys
import os
import psutil

print('---------------')
print('Running version 1.1.2')
print('Created by Thijnmens, pls don\' DDoS BeatSaver with this script thank you very much')
print('---------------')
print('Checking dependencies, please wait')

modul = 'psutil'
if modul not in sys.modules:
    print('---------------')
    print('!!!YOU DO NOT HAVE PSUTIL INSTALLED!!!')
    print('PLEASE INSTALL PSUTIL BY RUNNING THE FOLLOWING COMMAND')
    print('vvvvvv')
    print('pip install psutil')
    print('^^^^^^')
    print('WITHOUT THIS THE PROGRAM WILL CRASH')
    print('---------------')
else:
    print('All dependecies are validated')

count = int(input('Input the last reported count value here [Default: 0] : '))
delay = int(input('Input the delay in seconds between each download [Default: 5] : '))
maxim = int(input('Input the maximum amount of songs to download [Default: 72644] : '))
rever = str(input('Do you want it to run backwards? [Y/N] : '))
maxra = float(input('What is the maximum amount of ram that can be used by the system? [0~100, decimals allowed] : '))
url = 'beatsaver://'

if(rever == 'N'):
    while(count < maxim):
        pro = psutil.Process(os.getpid())
        ram = pro.memory_percent() * 10
        if(ram > maxra):
            print('Ram usage is too high, waiting 30 seconds')
            print('Memory Usage: ', ram,'%')
            print('Memory Left: ', maxra - ram,'%')
            print('---------------')
            time.sleep(30)
        else:
            count = count + 1
            key = hex(count)[2:]
            time.sleep(delay)
            url = 'beatsaver://' + key
            print('Starting Download of: ', key)
            print('url: ', url)
            print('count', count)
            print('Memory Usage: ', ram,'%')
            print('Memory Left: ', maxra - ram,'%')
            print('---------------')
            webbrowser.open(url)
            
if(rever == 'Y'):
    while(maxim > count):
        pro = psutil.Process(os.getpid())
        ram = pro.memory_percent() * 10
        if(ram > maxra):
            print('Ram usage is too high, waiting 30 seconds')
            print('Memory Usage: ', ram,'%')
            print('Memory Left: ', maxra - ram,'%')
            print('---------------')
            time.sleep(30)
        else:
            maxim = maxim - 1
            key = hex(maxim)[2:]
            time.sleep(delay)
            url = 'beatsaver://' + key
            print('Starting Download of: ', key)
            print('url: ', url)
            print('count: ', maxim)
            print('Memory Usage: ', ram,'%')
            print('Memory Left: ', maxra - ram,'%')
            print('---------------')
            webbrowser.open(url)

if(count == maxim):
    print('ALL SONGS HAVE BEEN DOWNLOADED!')
    print('The program will exit in 60 seconds')
    time.sleep(60)
    sys.exit()
