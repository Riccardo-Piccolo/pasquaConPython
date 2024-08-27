# Calcolo della data di Pasqua

Questo script Python calcola la data della Pasqua per un anno specifico compreso tra il 1583 e il 2499. 
Lo script utilizza il metodo di calcolo del concilio di Nicea, che determina la Pasqua come la prima domenica dopo il primo plenilunio dopo l'equinozio di primavera.

## Requisiti

- Python 3.x

## Utilizzo

1. Eseguire lo script Python.
2. Inserire un anno compreso tra il 1583 e il 2499 quando richiesto.
3. Lo script restituirà la data della Pasqua per l'anno inserito.

## Esempio di esecuzione

$ python calcolo_pasqua.py

Calcolo della pasqua

Inserire un anno tra 1583 e 2499 compresi

Inserisci l'anno: 2024

La Pasqua dell'anno 2024 cadrà il giorno 31 marzo

## Descrizione del codice

Lo script esegue i seguenti passaggi:

1. **Input dell'utente**: Viene richiesto all'utente di inserire un anno. Il programma continua a richiedere un anno fino a quando l'utente non fornisce un valore valido (compreso tra 1583 e 2499).
2. **Calcolo dei parametri**: Vengono calcolati i valori necessari per determinare la data della Pasqua:
- `a`, `b`, `c`: Resti delle divisioni dell'anno per 19, 4 e 7 rispettivamente.
- `M`, `N`: Costanti dipendenti dall'intervallo dell'anno inserito.
- `d`, `e`: Variabili intermedie utilizzate per calcolare il giorno della Pasqua.
3. **Determinazione della data della Pasqua**: Se la somma di `d + e` è minore di 10, la Pasqua cadde in marzo, altrimenti cade in aprile.
4. **Output**: Lo script stampa la data della Pasqua per l'anno specificato, indicando se è una data futura o passata rispetto alla data corrente.

## Note

- Il calcolo segue il metodo gregoriano e potrebbe non essere accurato per alcune religioni che seguono altri calendari liturgici.
- Questo script è inteso solo per scopi educativi e dimostrativi.
- Sono possibili future espansioni agli anni precedenti al 1583 o successivi al 2499.


## Autore

Script creato da Riccardo Piccolo.
