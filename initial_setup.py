import os
import sys
import setup_lib


if os.getuid():
    sys.exit('You need root access to install!')


os.system('clear')
print()
print()
print("###################################")
print("##### RaspiWiFi Intial Setup  #####")
print("###################################")
print()
print()
entered_ssid = "BetaScanner"
print()
wpa_enabled_choice = "N"
print()
wpa_entered_key = ""
print()
auto_config_choice = "y"
print()
auto_config_delay = ""
print()
server_port_choice = "8080"
print()
ssl_enabled_choice = "N"
os.system('clear')
print()
print()
install_ans = 'y'

if(install_ans.lower() == 'y'):
	setup_lib.install_prereqs()
	setup_lib.copy_configs(wpa_enabled_choice)
	setup_lib.update_main_config_file(entered_ssid, auto_config_choice, auto_config_delay, ssl_enabled_choice, server_port_choice, wpa_enabled_choice, wpa_entered_key)
else:
	print()
	print()
	print("===================================================")
	print("---------------------------------------------------")
	print()
	print("RaspiWiFi installation cancelled. Nothing changed...")
	print()
	print("---------------------------------------------------")
	print("===================================================")
	print()
	print()
	sys.exit()

os.system('clear')
print()
print()
print("#####################################")
print("##### RaspiWiFi Setup Complete  #####")
print("#####################################")
print()
print()
print("Initial setup is complete. A reboot is required to start in WiFi configuration mode...")
reboot_ans = 'y'

if reboot_ans.lower() == 'y':
	os.system('reboot')
