#using psutil to create a script that launches the robloxfpsunlocker upon launch of RobloxPlayer:

import psutil
import subprocess
import time
import sys
#change path
path_fps_unlocker = r'C:\Users\xakak\Downloads\rbxfpsunlocker-x64-hotfix1\rbxfpsunlocker.exe'

while True:
    processes = psutil.process_iter()
    for process in processes:
        if process.name() == 'RobloxPlayerBeta.exe':
            subprocess.Popen(path_fps_unlocker)
            sys.exit()
    time.sleep(1)