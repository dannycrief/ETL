import zipfile
import io

import requests
import urllib3
import csv
import re

urllib3.disable_warnings()

MAIN_SITE = 'https://api.cepik.gov.pl/'


def parse_marka():
    """
    Wszystkie marki pojazdów występujące w CEPiK
    :return:
    """
    marka_url = f"{MAIN_SITE}slowniki/marka"
    r = requests.get(marka_url, verify=False)
    marka_list = r.json()["data"]['attributes']['dostepne-rekordy-slownika']
    with open('DATA/marka.csv', 'w') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
        writer.writerow(['id_marka', 'liczba-wystapien'])
        for i in marka_list:
            row = [i['klucz-slownika'], i['liczba-wystapien']]
            writer.writerow(row)


def parse_rodzaj_pojazdu():
    """
    Rodzaje pojazdów występujące w CEPiK
    :return:
    """
    rodzaj_pojazdu_url = f"{MAIN_SITE}slowniki/rodzaj-pojazdu"
    r = requests.get(rodzaj_pojazdu_url, verify=False)
    rodzaj_pojazdu_list = r.json()["data"]['attributes']['dostepne-rekordy-slownika']
    with open('DATA/rodzaj-pojazdu.csv', 'w') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
        writer.writerow(['id_rodzaj_pojazdu', 'liczba-wystapien'])
        for i in rodzaj_pojazdu_list:
            row = [i['klucz-slownika'], i['liczba-wystapien']]
            writer.writerow(row)


def parse_wojewodztwa():
    """
    Słownik zawiera listę kodów województw
    :return:
    """
    wojewodztwa_url = f"{MAIN_SITE}slowniki/wojewodztwa"
    r = requests.get(wojewodztwa_url, verify=False)
    wojewodztwa_list = r.json()["data"]['attributes']['dostepne-rekordy-slownika']
    with open('DATA/wojewodztwa.csv', 'w') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
        writer.writerow(['id_wojewodztwa', 'nazwa_wojewodztwa', 'liczba-wystapien'])
        for i in wojewodztwa_list:
            row = [i['klucz-slownika'], i['wartosc-slownika'], i['liczba-wystapien']]
            writer.writerow(row)


def parse_rodzaj_paliwa():
    """
    Rodzaje paliwa pojazdów występujących w CEPiK
    :return:
    """
    rodzaj_paliwa_url = f"{MAIN_SITE}slowniki/rodzaj-paliwa"
    r = requests.get(rodzaj_paliwa_url, verify=False)
    rodzaj_paliwa_list = r.json()["data"]['attributes']['dostepne-rekordy-slownika']
    with open('DATA/rodzaj-paliwa.csv', 'w') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
        writer.writerow(['id_rodzaj_paliwa', 'liczba-wystapien'])
        for i in rodzaj_paliwa_list:
            row = [i['klucz-slownika'], i['liczba-wystapien']]
            writer.writerow(row)


def parse_pochodzenie_pojazdu():
    """
    Pochodzenie pojazdów występujących w CEPiK
    :return:
    """
    pochodzenie_pojazdu_url = f"{MAIN_SITE}slowniki/pochodzenie-pojazdu"
    r = requests.get(pochodzenie_pojazdu_url, verify=False)
    pochodzenie_pojazdu_list = r.json()["data"]['attributes']['dostepne-rekordy-slownika']
    with open('DATA/pochodzenie-pojazdu.csv', 'w') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
        writer.writerow(['id_pochodzenie_pojazdu', 'liczba-wystapien'])
        for i in pochodzenie_pojazdu_list:
            row = [i['klucz-slownika'], i['liczba-wystapien']]
            writer.writerow(row)


def parse_sposob_produkcji():
    """
    Sposoby produkcji pojazdów występujących w CEPiK
    :return:
    """
    sposob_produkcji_url = f"{MAIN_SITE}slowniki/sposob-produkcji"
    r = requests.get(sposob_produkcji_url, verify=False)
    sposob_produkcji_list = r.json()["data"]['attributes']['dostepne-rekordy-slownika']
    with open('DATA/sposob-produkcji.csv', 'w') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
        writer.writerow(['id_pochodzenie_pojazdu', 'liczba-wystapien'])
        for i in sposob_produkcji_list:
            row = [i['klucz-slownika'], i['liczba-wystapien']]
            writer.writerow(row)


def parse_uprawnienia():
    limit = 500
    page = 1
    req = requests.get(f"{MAIN_SITE}prawa-jazdy?limit={limit}&page={page}", verify=False)
    links = int(req.json()["links"]["last"].split('page=')[-1])
    with open('DATA/uprawnienia.csv', 'w') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
        writer.writerow([
            'id_uprawnienia', 'typ', 'kod_uprawnienia', 'data-statystyki', 'wojewodztwo_kod',
            'wojewodztwo_nazwa', 'plec', 'wiek', 'ilosc'
        ])
        for p in range(links + 1):
            req_link = f"{MAIN_SITE}uprawnienia?limit={limit}&page={page + p}"
            print(req_link)
            r = requests.get(req_link, verify=False).json()
            uprawnienia_list = r["data"]
            for i in uprawnienia_list:
                row = [
                    i['id'], i['type'], i['attributes']['kod-uprawnienia'],
                    i['attributes']['data-statystyki'],
                    i['attributes']['wojewodztwo-kod'],
                    i['attributes']['wojewodztwo-nazwa'],
                    i['attributes']['plec'],
                    i['attributes']['wiek'],
                    i['attributes']['ilosc']
                ]
                writer.writerow(row)


def parse_prawa_zajdy():
    limit = 500
    page = 1
    req = requests.get(f"{MAIN_SITE}prawa-jazdy?limit={limit}&page={page}", verify=False)
    links = int(req.json()["links"]["last"].split('page=')[-1])
    with open('DATA/prawa-jazdy.csv', 'w') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
        writer.writerow([
            'id_prawa_jazdy', 'typ', 'data-statystyki', 'wojewodztwo_kod',
            'wojewodztwo_nazwa', 'plec', 'wiek', 'ilosc'
        ])
        for p in range(links + 1):
            req_link = f"{MAIN_SITE}prawa-jazdy?limit={limit}&page={page + p}"
            print(req_link)
            r = requests.get(req_link, verify=False).json()
            uprawnienia_list = r["data"]
            for i in uprawnienia_list:
                row = [
                    i['id'], i['type'],
                    i['attributes']['data-statystyki'],
                    i['attributes']['wojewodztwo-kod'],
                    i['attributes']['wojewodztwo-nazwa'],
                    i['attributes']['plec'],
                    i['attributes']['wiek'],
                    i['attributes']['ilosc']
                ]
                writer.writerow(row)


def parse_pojazdy():
    wojewodztwa = ['02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32', 'XX']
    data_od = '20150501'
    data_do = '20160501'
    limit = 100
    page = 1
    options = 'typ-daty=1&tylko-zarejestrowane=false&pokaz-wszystkie-pola=false'
    with open('DATA/pojazdy.csv', 'a') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n', )
        writer.writerow([
            'id_pojazd', 'typ', 'marka', 'kategoria-pojazdu',
            'typ_pojazdu', 'model', 'wariant', 'rodzaj_pojazdu',
            'pochodzenie_pojazdu', 'rok_produkcji', 'data_pierwszej_rejestracji_w_kraju', 'pojemnosc_skokowa_silnika',
            'masa_wlasna', 'rodzaj_paliwa', 'wojewodztwo_kod'
        ])
        for wojewodztwo in wojewodztwa:
            req = requests.get(
                f"{MAIN_SITE}pojazdy?wojewodztwo={wojewodztwo}&data-od={data_od}&data-do={data_do}&limit={limit}&page={page}&{options}",
                verify=False)
            print(f'TST: {req.json()}')
            if "errors" in req.json():
                print(f"Wystąpił błąd: {req.json()['errors'][0]['error-result']}")
                break
            links = int(re.findall(r"(page=(\d))", req.json()["links"]["last"])[0][1])
            for p in range(links):
                req_link = f'{MAIN_SITE}pojazdy?wojewodztwo={wojewodztwo}&data-od={data_od}&data-do={data_do}&limit={limit}&page={page + p}&{options}'
                print(f"{req_link} and max_links is: {links} and page + p is: {page + p}")
                r = requests.get(req_link, verify=False).json()
                print(f'TST2: {r}')
                if "errors" in r:
                    print(f"Wystąpił błąd: {r['errors'][0]['error-result']}")
                    break
                pojazdy_list = r["data"]
                for i in pojazdy_list:
                    row = [
                        i['id'],
                        i['type'],
                        i['attributes']['marka'],
                        i['attributes']['kategoria-pojazdu'],
                        i['attributes']['typ'],
                        i['attributes']['model'],
                        i['attributes']['wariant'],
                        i['attributes']['rodzaj-pojazdu'],
                        i['attributes']['pochodzenie-pojazdu'],
                        i['attributes']['rok-produkcji'],
                        i['attributes']['data-pierwszej-rejestracji-w-kraju'],
                        i['attributes']['pojemnosc-skokowa-silnika'],
                        i['attributes']['masa-wlasna'],
                        i['attributes']['rodzaj-paliwa'],
                        i['attributes']['wojewodztwo-kod'],
                    ]
                    writer.writerow(row)


def parse_zip_pojazdy():
    link = 'https://api.cepik.gov.pl/pliki?limit=100&page=1'
    req = requests.get(link, verify=False)
    print(f"NOTE: {req}")
    for i in req.json()['data']:
        print(f"NOTE: Downloading {i['attributes']['url-do-pliku']}")
        r = requests.get(i['attributes']['url-do-pliku'], verify=False, stream=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("ZIPs")


if __name__ == "__main__":
    # parse_marka()
    # parse_wojewodztwa()
    # parse_rodzaj_pojazdu()
    # parse_rodzaj_paliwa()
    # parse_pochodzenie_pojazdu()
    # parse_sposob_produkcji()
    # parse_uprawnienia()
    # parse_prawa_zajdy()
    # parse_pojazdy()
    parse_zip_pojazdy()

"""
head -n 50000 pojazdy_02_2022-02-17.csv > 500s/pojazdy_02_2022-04-17.csv
head -n 50000 pojazdy_04_2022-04-17.csv > 500s/pojazdy_04_2022-04-17.csv
head -n 50000 pojazdy_06_2022-04-17.csv > 500s/pojazdy_06_2022-04-17.csv
head -n 50000 pojazdy_08_2022-04-17.csv > 500s/pojazdy_08_2022-04-17.csv
head -n 50000 pojazdy_10_2022-04-17.csv > 500s/pojazdy_10_2022-04-17.csv
head -n 50000 pojazdy_12_2022-04-17.csv > 500s/pojazdy_12_2022-04-17.csv
head -n 50000 pojazdy_14_2022-04-17.csv > 500s/pojazdy_14_2022-04-17.csv
head -n 50000 pojazdy_16_2022-04-17.csv > 500s/pojazdy_16_2022-04-17.csv
head -n 50000 pojazdy_18_2022-04-17.csv > 500s/pojazdy_18_2022-04-17.csv
head -n 50000 pojazdy_20_2022-04-17.csv > 500s/pojazdy_20_2022-04-17.csv
head -n 50000 pojazdy_24_2022-04-17.csv > 500s/pojazdy_24_2022-04-17.csv
head -n 50000 pojazdy_24_2022-04-17.csv > 500s/pojazdy_24_2022-04-17.csv
head -n 50000 pojazdy_26_2022-04-17.csv > 500s/pojazdy_26_2022-04-17.csv
head -n 50000 pojazdy_28_2022-04-17.csv > 500s/pojazdy_28_2022-04-17.csv
head -n 50000 pojazdy_30_2022-04-17.csv > 500s/pojazdy_30_2022-04-17.csv
head -n 50000 pojazdy_32_2022-04-17.csv > 500s/pojazdy_32_2022-04-17.csv
head -n 50000 pojazdy_xx_2022-04-17.csv > 500s/pojazdy_xx_2022-04-17.csv
"""
