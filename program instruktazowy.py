import sqlite3

### Łączenie z bazą danych
conn = sqlite3.connect('baza_instruktazowa.db') #to jest baza zawierajaca KILKA tabel

c = conn.cursor()
###Tworzenie tabeli
c.execute("create table pracownicy(id integer primary key, haslo text)")

### Dodawanie do tabeli
c.execute("insert into pracownicy values('2','test')")

### Wyswietlanie
c.execute('select * from pracownicy')
for row in c:
    print(row)
conn.commit() #potwierdzenie zmian w bazie
print('Dane zaktualizowane...')
conn.close()
