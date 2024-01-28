import requests

chat_id = "6755634224"
urlp = "https://t.me/eTsfine"
url = f"https://api.telegram.org/6986030644:AAEOtcKtaw_z2WPPPv2mN_8emzC5j3W1RyU/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
