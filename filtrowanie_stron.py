import requests

def sprawdzacz_stron(lista):
    dobreStrony = []
    zleStrony = []

    for item in lista:
        r = requests.get(item)
        if r.status_code == 200:
            dobreStrony.append(item)
        else:
            zleStrony.append(item)

    return dobreStrony, zleStrony

strony = ["https://www.wp.pl/", "https://www.youtube.com/", "http://jakasstrona.pl",
          "https://pl-pl.facebook.com/", "http://krucafuks.com/dasdaasd"]

odpowiedz = sprawdzacz_stron(strony)
