import network
import urequests
import time

ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connection
while not wlan.isconnected():
    time.sleep(1)

# Check Internet connection
try:
    response = urequests.get("https://www.google.com")
    print("The connection has been established.")
    response.close()
except:
    print("The Connection could not be established.")
    raise SystemExit

message = "Type in any message you want!"
discord_url = "YOUR_WEBHOOK_URL"
data = {
    "content": message,
    "username": "PicoBot"
}

ask_user = "1"  # Replace with "2" for repeated messages

if ask_user == "1":
    print(f"The message has been sent: {message}")
    result = urequests.post(discord_url, json=data)
    result.close()
elif ask_user == "2":
    while True:
        result = urequests.post(discord_url, json=data)
        result.close()
        print("Message sent. Waiting...")
        time.sleep(5)
