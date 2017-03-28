import xlrd

wojewodztwa = {
    1: 'Dolnoslaskie',
    2: 'Dolnoslaskie',
    3: 'Dolnoslaskie',
    4: 'Dolnoslaskie',
    5: 'Kujawsko-Pomorskie',
    6: 'Kujawsko-Pomorskie',
    7: 'Kujawsko-Pomorskie',
    8: 'Lubelskie',
    9: 'Lubelskie',
    10: 'Lubelskie',
    11: 'Lubelskie',
    12: 'Lubelskie',
    13: 'Lubuskie',
    14: 'Lubuskie',
    15: 'Łódzkie',
    16: 'Łódzkie',
    17: 'Łódzkie',
    18: 'Łódzkie',
    19: 'Łódzkie',
    20: 'Małopolskie',
    21: 'Małopolskie',
    22: 'Małopolskie',
    23: 'Małopolskie',
    24: 'Małopolskie',
    25: 'Małopolskie',
    26: 'Małopolskie',
    27: 'Małopolskie',
    29: 'Mazowieckie',
    30: 'Mazowieckie',
    31: 'Mazowieckie',
    32: 'Mazowieckie',
    33: 'Mazowieckie',
    34: 'Mazowieckie',
    35: 'Mazowieckie',
    36: 'Mazowieckie',
    37: 'Opolskie',
    38: 'Opolskie',
    39: 'Podkarpackie',
    40: 'Podkarpackie',
    41: 'Podkarpackie',
    42: 'Podkarpackie',
    43: 'Podlaskie',
    44: 'Podlaskie',
    45: 'Podlaskie',
    46: 'Pomorskie',
    47: 'Pomorskie',
    48: 'Pomorskie',
    49: 'Śląskie',
    50: 'Śląskie',
    51: 'Śląskie',
    52: 'Śląskie',
    53: 'Śląskie',
    54: 'Śląskie',
    55: 'Świętokrzyskie',
    56: 'Świętokrzyskie',
    57: 'Warmińsko-Mazurskie',
    58: 'Warmińsko-Mazurskie',
    59: 'Warmińsko-Mazurskie',
    60: 'Wielkopolskie',
    61: 'Wielkopolskie',
    62: 'Wielkopolskie',
    63: 'Wielkopolskie',
    64: 'Wielkopolskie',
    65: 'Zachodniopomorskie',
    66: 'Zachodniopomorskie',
    67: 'Zachodniopomorskie',
    68: 'Zachodniopomorskie',
}

def wczytaj_kraj():
    print("dd")


def otwotrz_arkusz(numer_okregu):
    numer = str(numer_okregu)
    if numer_okregu < 10:
        numer = "0" + numer

    return xlrd.open_workbook("app/obwody/obw" + numer + ".xls").sheet_by_index(0)


print(otwotrz_arkusz(65).cell(0, 1).value)
