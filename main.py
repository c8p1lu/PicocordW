import network
import urequests
import random
import time

ssid = 'NAME OF NETWORK'
password = 'PASSWORD'



wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

if urequests.get("https://www.google.com"): #Checks for internet
    print("The connection has been established.")
else:
    print("The Connection could not be established.")
    #end of function
message = ["Type in any message you want!"]

discord_url = "WEBHOOK"
data = {
    "content" : message,
    "username" : "Name of webhook"
    }

ask_user = input("Do you want the message to be sent once or multiple times (1 = once, 2 = multiple : ")
if ask_user == "1":
    print(f"The message has been sent: {message}")
    result = urequests.post(discord_url, json = data)
elif ask_user == "2":
    while True:
        result = urequests.post(discord_url, json = data)
