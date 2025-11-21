#Scrivi un programma che legge un numero num e visualizza i primi num termini della successione di Fibonacci.  (Utilizza la formula semplificata: 1, 1, 2, 3, 5, ...)  
#Chiedi un numero all’utente, poi calcola la somma dei numeri pari da 1 a quel numero (incluso)  
#Chiedi un numero all’utente e stampa (massimo 30 numeri) i numeri pari positivi inferiori a quel numero in ordine decrescente
#Albero di Natale: scrivi un programma che legge da tastiera un carattere "c" e un intero "n" e stampa un albero di Natale di altezza "n" usando il carattere "c". Dove c=* ed n=6


#es1:

def fibonacci(number):
    if number == 1:
        return 1
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
    
print(fibonacci(7))

#es2:

def somma_pari(n):
    return (int) (n /2) * ((int) (n / 2) + 1)
    
print(f"somma: {somma_pari(9)}")

num = int(input("nunm: ")) 
somma = 0

for i in range(num + 1):
    if i % 2 == 0:
        somma += i
print(f"somma: {somma}")

#es3
numero = int(input("num: "))

for i in range(30):
    if i % 2 == 0:
        if i < numero:
            print(f"numero: {numero - i}")


#es4
#albero di natale
altezza = int(input("colonne: "))

for i in range(altezza):
    spazi = " " * (altezza - i - 1)
    rami = "*" * (2 * i + 1)
    print(spazi + rami)

for i in range(2):
    spazi = " " * (altezza - 1)
    print(spazi + "|")