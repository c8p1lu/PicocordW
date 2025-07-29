# 📡 Pico W Discord Webhook Bot

A simple MicroPython script for the Raspberry Pi Pico W that connects to Wi-Fi and sends messages to a Discord channel using a webhook.

---

## 📋 Overview

This project demonstrates how to:

- Connect a Raspberry Pi Pico W to a Wi-Fi network.
- Check for internet access.
- Post messages to a Discord webhook.
- Optionally loop the message send with a delay.

---

## ✅ What's Working

- **Wi-Fi Connection**: Uses `network.WLAN` to connect to a Wi-Fi network.
- **Internet Check**: Makes an HTTP GET request to Google to verify internet access.
- **Webhook Message Send**: Successfully sends a message to Discord via a webhook using `urequests.post()`.
- **Optional Looping**: Supports single or repeated message sending.
- **Memory Management**: `.close()` used after HTTP requests to free up memory.

---

## ⚠️ What's Not Ideal

- ❌ `input()` is used in the original version, which **doesn't work** outside of the REPL (interactive console).
- ❌ The original message was a **list**, which is not accepted by Discord (`"content"` must be a string). 
- ❌ No rate-limiting protection — repeated messages sent too fast may **trigger Discord's rate limit**. - Future Update
- ❌ Wi-Fi credentials and webhook URL are **hardcoded**, which is insecure for production use.

---

## 🔧 Recommended Improvements

- Use a **config file** or `secrets.py` to store credentials securely.
- Add **physical button input** or **timer-based triggers** instead of hardcoding or relying on REPL.
- Implement **rate limiting** and **error logging**.
- Consider wrapping the loop in a try/except block to avoid crashing on failed webhook requests.

---

## 🚀 Getting Started

### 📦 Requirements

- Raspberry Pi Pico W
- MicroPython firmware (latest version)
- urequests library

### 🔧 Setup

1. Flash MicroPython onto your Pico W.
2. Upload the script (`main.py`) using Thonny or another IDE.
3. Replace the following values in the script:
   ```python
   ssid = 'YOUR_WIFI_SSID'
   password = 'YOUR_WIFI_PASSWORD'
   discord_url = 'YOUR_DISCORD_WEBHOOK_URL'
