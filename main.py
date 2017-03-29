
def przetworz_arkusz(numer_okregu):
    arkusz = otwotrz_arkusz(numer_okregu)

    for i in range(8, 24):
        print(arkusz.cell(0, i).value)

    return 42


def konwertuj_nazwe(napis):
    ltrPL = "ŻÓŁĆĘŚĄŹŃżółćęśąźń "
    ltrnoPL = "ZOLCESAZNzolcesazn-"

    trantab = str.maketrans(ltrPL, ltrnoPL)

    napis = napis.translate(trantab)
    napis = napis.lower()

    return napis


napis = 'Gąska BaRdzo Piękna'

print(konwertuj_nazwe(napis))

url_list = [{'target': 'http://10.58.48.103:5000/', 'clicks': '1'},
            {'target': 'http://slash.org', 'clicks': '4'},
            {'target': 'http://10.58.48.58:5000/', 'clicks': '1'},
            {'target': 'http://de.com/a', 'clicks': '0'}]

print(type(url_list[1]))

# wczytaj_kraj()
