import sqlite3
import os
import linecache

def zmianaHasla(id):
    os.system('cls')
    print('\n ZMIANA HASLA \n')
    zH_id = int(input('Podaj swoje id : '))
    if(zH_id==id):
        if(id<=100):
            c.execute('select haslo_pracownika from pracownicy where id_pracownika="%d"' %id)
            for row in c:
                zH_password=(row)        
            zH_haslo = input('Podaj swoje haslo : ')
            zH_haslo = (zH_haslo,) #zmiana hasla na forme ktora otrzymujemy z bazy danych
            if(zH_haslo==password):
                print('Dane Poprawne')
            else:
                input('Dane Błędne, zmiana hasla nie powiodla sie (nacisnij dowolny kawisz by kontynulowac)')
        if(id>=101):
            c.execute('select haslo_czytelnika from czytelnicy where id_czytelnika="%d"' %id)
            for row in c:
                zH_password=(row)        
            zH_haslo = input('Podaj swoje haslo : ')
            zH_haslo = (zH_haslo,) #zmiana hasla na forme ktora otrzymujemy z bazy danych
            if(zH_haslo==password):
                print('Dane Poprawne')
            else:
                input('Dane Błędne, zmiana hasla nie powiodla sie (nacisnij dowolny kawisz by kontynulowac)')
        else:
            print('Podales inne ID niz te pod ktorym jestes zalogowany, zmiana hasla nie powiodla sie (nacisnij dowolny kawisz by kontynulowac)')
    return

### Łączenie z bazą danych
bd = sqlite3.connect('lib/baza.db')
c = bd.cursor()
uprawnienia = 0 #1-admin 2-bibliotekarz 3-czytelnik
while id != 0:
    while uprawnienia<4:
        os.system('cls')
        print()
        print('************************************************')
        print('*                                              *')
        print('*                 BIBLIOTEKA                   *')
        print('*                                              *')
        print('************************************************')
        print('\n PANEL LOGOWANIA \n')
        id = int(input('Podaj swoje id (0-wyjscie z programu) : '))
        if(id==0):
            break;
        if(id<=100):
            c.execute('select haslo_pracownika from pracownicy where id_pracownika="%d"' %id)
            for row in c:
                password=(row)        
            haslo = input('Podaj swoje haslo : ')
            haslo = (haslo,) #zmiana hasla na forme ktora otrzymujemy z bazy danych
            if(haslo==password):
                print('Dane Poprawne')
                if id==1: uprawnienia=1
                if id>=2: uprawnienia=2
            else:
                print('Dane Błędne')
                break
        if(id>=101):
            c.execute('select haslo_czytelnika from czytelnicy where id_czytelnika="%d"' %id)
            for row in c:
                password=(row)        
            haslo = input('Podaj swoje haslo : ')
            haslo = (haslo,) #zmiana hasla na forme ktora otrzymujemy z bazy danych
            if(haslo==password):
                print('Dane Poprawne')
                uprawnienia=3
            else:
                print('Dane Błędne')
                break
        while(uprawnienia==1):
            os.system('cls')
            print('\n PANEL ADMINISTRATORA \n')
            print('[wkrotce] 1 - Dodaj Czytelnika')
            print('[wkrotce] 2 - Usun Czytelnika')
            print('[wkrotce] 3 - Dodaj Bibliotekarza')
            print('[wkrotce] 4 - Usun Bibliotekarza')
            print('[tworzenie] 5 - Zmiana hasla')
            print('9 - Wylogowanie')
            print('0 - Wylogowanie i wyjscie')
            menu = input('Twoj wybór : ')
            if menu == '5':
                zmianaHasla(id)
            if menu == '9':
                uprawnienie = 0
                haslo = 0
                break
            if menu == '0':
                uprawnienie = 4
                id = 0
                haslo = 0
                break
            if menu!='1' and menu!='2' and menu!='3' and menu!='4' and menu!='5' and menu!='9' and menu!='0': #Obsluga nieznanych funkcji
                input('Nie mamy takiej funkcjonalnosci, nacisnij dowolny przycisk by kontynulowac')
        while(uprawnienia==2):
            os.system('cls')
            print('\n PANEL BIBLIOTEKARZA \n')
            print('9 - Wylogowanie')
            print('0 - Wylogowanie i wyjscie')
            menu = input('Twoj wybór : ')
            if menu == '9':
                uprawnienie = 0
                haslo = 0
                break
            if menu == '0':
                uprawnienie = 4
                id = 0
                haslo = 0
                break
            if menu!='9' and menu!='0': #Obsluga nieznanych funkcji
                input('Nie mamy takiej funkcjonalnosci, nacisnij dowolny przycisk by kontynulowac')
        while(uprawnienia==3):
            os.system('cls')
            print('\n PANEL CZYTELNIKA \n')
            print('9 - Wylogowanie')
            print('0 - Wylogowanie i wyjscie')
            menu = input('Twoj wybór : ')
            if menu == '9':
                uprawnienie = 0
                haslo = 0
                break
            if menu == '0':
                uprawnienie = 4
                id = 0
                haslo = 0
                break
            if menu!='9' and menu!='0': #Obsluga nieznanych funkcji
                input('Nie mamy takiej funkcjonalnosci, nacisnij dowolny przycisk by kontynulowac')
        if uprawnienie == 4:
            break
bd.commit() #potwierdzenie zmian w bazie
bd.close()
