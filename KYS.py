#
# # python3
# >>> import sys
# >>> sys.path
# [ create a file named same as the module and put modules in this path ]
#
# OR
#
# just have the module in the same directory as the calling program
#
#C:\Users\jakeo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\KYS
#
#
# apt install sox libsox-fmt-all :: for 'play any.mp3' command (CLI mp3 play)

#
#pronounced "kiss", this moduleis made by deusxmachina 2021. 
#

import speech_recognition as sr # pip3 install SpeechRecognition
from gtts import gTTS # pip3 install gTTS :: google Text To Speech api
import os
import sys

def get_platform(): # determine which OS python is running on
    platforms = {
    	'linux' : 'Linux',
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

def ALPHA_listen():
	return 0
def ALPHA_speak(): # referred to as KYS.ALPHA_speak()
	return 0
def ALPHA_read(text): # referred to as KYS.ALPHA_read()
	save_FILE = './response.mp3'

	response = gTTS(text=text,lang='en',slow=False) # pass text and language to function
	response.save(save_FILE) # pass filename and directory to save response in

	# play audio, determine platform/OS first.
	platform = get_platform()
	if platform == 'win32' or platform == 'Windows': # Win10
		os.system('start'+save_FILE) 
	if platform == 'darwin' or platform == 'OS X': # Mac
		os.system('mpg123 '+save_FILE) 
	if platform == 'linux1' or platform == 'Linux' or platform == 'linux2':
		os.system('sudo chown deusxmachina '+save_FILE+') # Linux :: play -q response.mp3 (quiet mode)
		os.system("xdotool key alt+space")
		os.system(WID=`xdotool search --onlyvisible "@deus" | head -1`)
		os.system('xdotool windowactivate --sync $WID')
		os.system("xdotool type --clearmodifiers 'play response.mp3'")
		
		'''
		xdotool search --onlyvisible "@deus" | tail -1 # searching for "@deus" because that is the title name. head -1 will return active window.

		'''
		# sudo -u deusxmachina terminator -e "whoami && ping 1.1.1.1 -c 10 && play response.mp3"