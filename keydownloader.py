#######################################
# Operation Steal BeatSavers Database #
#######################################

import webbrowser
import time
import sys

count = int(input('Input the last reported count value here [Default: 0] : '))
delay = int(input('Input the delay in seconds between each download [Default: 5] : '))
maxim = int(input('Input the maximum amount of songs to download [Default: 72644] : '))
url = 'beatsaver://'

while(count < maxim):
    count = count + 1
    key = hex(count)[2:]
    time.sleep(delay)
    url = 'beatsaver://' + key
    print('Starting Download of: ', key)
    print('url: ', url)
    print('count', count)
    print('---------------')
    webbrowser.open(url)

if(count == maxim):
    print('ALL SONGS HAVE BEEN DOWNLOADED!')
    print('The program will exit in 60 seconds')
    time.sleep(60)
    sys.exit()
