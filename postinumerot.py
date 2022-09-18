# Kopioi aikaisempi ratkaisusi tänne. Lisää tarvittaessa myös muut ratkaisusi tiedostot.

import json
from time import strftime
from typing import Optional

def postinum(name: str) -> str:
    with open ("postcode_map_light.json") as data:
        x = data.read()
        postinumerot = json.loads(x)

        lista = []

        for avain, arvo in postinumerot.items():
            if name.replace(" ", "").lower() == "smartpost" and arvo.replace(" ", "").lower() == name.replace(" ", "").lower():
                lista.append(avain)
            elif arvo.lower() == name.lower():
                lista.append(avain)


        tulos = ", ".join(sorted(lista))
        if len(lista) > 0:
            return (f"Postinumerot: {tulos}")
        else:
            return None


if __name__ == '__main__':
    haku = input("Kirjoita postitoimipaikka: ")
    code = postinum(haku)

    if code:
        print(code)
    else:
        print("Tuntematon postitoimipaikka")