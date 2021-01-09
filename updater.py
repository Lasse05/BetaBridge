from git import Repo
import os
import paho.mqtt.client as mqtt
import json
import wget
import hashlib

with open('/home/pi/data.json') as json_file:
    data = json.load(json_file)
name = data['id']
ip = data['ip']
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("update" + name)
    statusupdate("online")
def statusupdate(status):
    client.publish("status" + name, status)

def on_message(client, userdata, msg):
    print(msg)
    if msg.topic == "update" + name:
        payload = str(msg.payload)
        statusupdate("update")
        os.system('sudo rm /home/pi/RaspiWiFi/update.sh')
        print(payload)
        wget.download(payload,'/home/pi/RaspiWiFi/update.sh')
        os.system('sudo chmod 777 /home/pi/RaspiWiFi/update.sh')
        os.system('sh /home/pi/RaspiWiFi/update.sh')
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print "Unexpected MQTT disconnection. Will auto-reconnect"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect


client.username_pw_set(name,encrypt_string(name))
   
client.connect(ip, 1883)
client.loop_forever()
def main():
    while True:
        time.sleep(1)
if __name__ == '__main__':
    main()
