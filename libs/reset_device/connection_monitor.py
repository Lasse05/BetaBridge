import time
import sys
import os
import reset_lib

no_conn_counter = 0
consecutive_active_reports = 0
config_hash = reset_lib.config_file_hash()

# If auto_config is set to 0 in /etc/raspiwifi/raspiwifi.conf exit this script
if config_hash['auto_config'] == "0":
    sys.exit()
else:
    # Main connection monitoring loop at 10 second interval
    while True:
        time.sleep(10)

        # If iwconfig report no association with an AP add 10 to the "No
        # Connection Couter"
        if reset_lib.is_wifi_active() == False:
            no_conn_counter += 10
            consecutive_active_reports = 0
        else: 
            sys.exit()
        # If iwconfig report association with an AP add 1 to the
        # consecutive_active_reports counter and 10 to the no_conn_counter
        # If the number of seconds not associated with an AP is greater or
        # equal to the auto_config_delay specified in the /etc/raspiwifi/raspiwifi.conf
        # trigger a reset into AP Host (Configuration) mode.
        if no_conn_counter >= int(config_hash['auto_config_delay']):
            reset_lib.reset_to_host_mode()
