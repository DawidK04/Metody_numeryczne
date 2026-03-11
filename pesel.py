from datetime import date

def analizuj_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return "Błąd: PESEL musi składać się z dokładnie 11 cyfr."

    rok_dwie_cyfry = pesel[0:2]
    miesiac_kod = int(pesel[2:4])
    dzien = int(pesel[4:6])
    liczba_kontrolna_podana = int(pesel[10])

    if 81 <= miesiac_kod <= 92:
        rok_poczatek = "18"
        miesiac = miesiac_kod - 80
    elif 1 <= miesiac_kod <= 12:
        rok_poczatek = "19"
        miesiac = miesiac_kod
    elif 21 <= miesiac_kod <= 32:
        rok_poczatek = "20"
        miesiac = miesiac_kod - 20
    elif 41 <= miesiac_kod <= 52:
        rok_poczatek = "21"
        miesiac = miesiac_kod - 40
    elif 61 <= miesiac_kod <= 72:
        rok_poczatek = "22"
        miesiac = miesiac_kod - 60
    else:
        return "Błąd: Nieprawidłowy kod miesiąca."

    pelny_rok = int(f"{rok_poczatek}{rok_dwie_cyfry}")

    try:
        date(pelny_rok, miesiac, dzien)
    except ValueError:
        return f"Błąd: Data {dzien:02d}.{miesiac:02d}.{pelny_rok} jest nieprawidłowa."

    data_urodzenia = f"{dzien:02d}.{miesiac:02d}.{pelny_rok}"

    plec_cyfra = int(pesel[9])
    plec = "Kobieta" if plec_cyfra % 2 == 0 else "Mężczyzna"

    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0
    
    for i in range(10):
        iloczyn = int(pesel[i]) * wagi[i]
        suma += iloczyn % 10

    ostatnia_cyfra_sumy = suma % 10
    wyliczona_kontrolna = (10 - ostatnia_cyfra_sumy) % 10

    print(f"PESEL: {pesel}")
    print(f"Data urodzenia: {data_urodzenia}")
    print(f"Płeć:           {plec}")
    print(f"Suma kontrolna: {wyliczona_kontrolna} " 
          f"({'Poprawna' if liczba_kontrolna_podana == wyliczona_kontrolna else 'BŁĘDNA!'})")

analizuj_pesel("02270803628")
