import requests, json, webbrowser
from pprint import pprint


amount = int(input("Ile zdjęć chcesz obejrzeć: "))

params = {
    "count" : amount
}

r = requests.get("http://shibe.online/api/shibes", params)

try:
    content = r.json()
except json.decoder.JSONDecoderError:
    print("Niepoprawny format")
else:
    for picture in content:
        webbrowser.open_new_tab(picture)
