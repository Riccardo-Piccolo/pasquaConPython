import datetime
import sys


def printf(formato, *args):
    sys.stdout.write(formato % args)


print("Calcolo della Pasqua \nInserire un anno tra 1583 e 2499 compresi")
print("------------------------------------------------------")
error = True
year = 0
M = 0
N = 0
while error:
    try:
        year = int(input("Inserisci l'anno: "))
        error = False
        if year < 1583 or year > 2499:
            print("Inserire un anno tra 1583 e 2499")
            error = True
    except ValueError:
        print("Inserire un intero!")
        error = True

a = year % 19
b = year % 4
c = year % 7

if 1583 <= year <= 1699:
    M = 22
    N = 2
elif 1700 <= year <= 1799:
    M = 23
    N = 3
elif 1800 <= year <= 1899:
    M = 23
    N = 4
elif 1900 <= year <= 2099:
    M = 24
    N = 5
elif 2100 <= year <= 2199:
    M = 24
    N = 6
elif 2200 <= year <= 2299:
    M = 25
    N = 0
elif 2300 <= year <= 2399:
    M = 26
    N = 1
elif 2400 <= year <= 2499:
    M = 25
    N = 1

d = (19 * a + M) % 30
e = (2 * b + 4 * c + 6 * d + N) % 7

if (d + e) < 10:
    if year < datetime.date.today().year:
        printf("La Pasqua dell'anno %d e' caduta il giorno %d marzo", year, (d + e + 22))
    else:
        printf("La Pasqua dell'anno %d cadra' il giorno %d marzo", year, (d + e + 22))
else:
    if year < datetime.date.today().year:
        printf("La Pasqua dell'anno %d e' caduta il giorno %d aprile", year, (d + e - 9))
    else:
        printf("La Pasqua dell'anno %d cadra' il giorno %d aprile", year, (d + e - 9))
