#######################################
# Operation Steal BeatSavers Database #
#######################################
#      Created by: Thijnmens          #
#         Version: 1.1.2              #
#######################################

import webbrowser, time, sys, os, json, psutil

print('---------------')
print('Running version 1.1.2')
print('Created by Thijnmens, pls don\'t DDoS BeatSaver with this script thank you very much')
print('---------------')
print('Checking dependencies, please wait')

if 'psutil' not in sys.modules:
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
scrap = str(input('Do you want to use the scraper? [Y/N] : '))
if(scrap == 'Y' or scrap == 'y'):
    count = 0
    delay = int(input('Input the delay in seconds between each download [Default: 5] : '))
    rever = 'N'
    maxra = 0
    progress = {}
    progress[''] = []
    data = str(json.loads(open('beatSaverScrappedData.json', encoding='utf8').read()))
    datas = data.split(', ')
    done = str(json.loads(open('Progress.json', encoding='utf8').read()))
    maxim = len(datas)
    while(count < maxim):
        if(datas[count].startswith('\'key') == True or datas[count].startswith('\"key') == True):
            key = datas[count].split('\'')
            if(str(key[3] in done) == 'False'):
                url = 'beatsaver://' + key[3]
                print(f'Starting download of song with {datas[count]}')
                webbrowser.open(url)
                progress[''].append({f'key': str(key[3])})
                with open('Progress.json', 'w') as outfile:
                    json.dump(progress, outfile)
                time.sleep(delay)
            else:
                print(f'{key[3]} is already downloaded, skipping')
                progress[''].append({f'key': str(key[3])})
                with open('Progress.json', 'w') as outfile:
                    json.dump(progress, outfile)
        count = count + 1
        
        
else:
    count = int(input('Input the last reported count value here [Default: 0] : '))
    delay = int(input('Input the delay in seconds between each download [Default: 5] : '))
    maxim = int(input('Input the maximum amount of songs to download [Default: 72644] : '))
    rever = str(input('Do you want it to run backwards? [Y/N] : '))
    maxra = float(input('What is the maximum amount of ram that can be used by the system? [0~100, decimals allowed] : '))
    url = 'beatsaver://'
    if(rever == 'N' or rever == 'n'):
        while(count < maxim):
            pro = psutil.Process(os.getpid())
            ram = pro.memory_percent()
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
    
    if(rever == 'Y' or rever == 'y'):
        while(maxim > count):
            pro = psutil.Process(os.getpid())
            ram = pro.memory_percent()
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
