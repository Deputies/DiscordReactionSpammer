import requests
from time import sleep
count = 1
Emoji_ID = input("Emoji ID:")
Channel_ID = input("Channel ID:")
Auth_Token = input("Auth Token:")
while True:
    body = {"emoji_id":f"{Emoji_ID}","emoji_name":"Noice","animation_type":0,"animation_id":count}
    headers ={
    "Host":"discord.com",
    "Connection":"keep-alive",
    "Content-Length":f"{int(len(body))}",
    "X-Discord-Locale":"en-US",
    "X-Debug-Options":"bugReporterEnabled",
    "Accept-Language":"en-US,en-AU;q=0.9",
    "Authorization":f"{Auth_Token}",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9007 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
    "Content-Type":"application/json",
    "Accept":"*/*",
    "Origin":"https://discord.com",
    }
    
    url =f"https://discord.com/api/v9/channels/{Channel_ID}/voice-channel-effects"
    r = requests.Session()
    r.length = 99
    count += 1
    r = requests.post(f"{url}", json=body, headers=headers)
    print(r.text)
    if count > 19:
        count = 1
    sleep(0.3)
