# python è un linguaggio di programmazione di alto livello 
# (verso l'utente) per rendere la scrittura di programmi più intuitiva.

#esercizi di inizio
import calendar
import math

def meggiorenne(eta):
    if eta >= 18:
        print("maggiorenne")
    else:
        print("minorenne")


n = int(input("N: "))

for i in range(10):
    print(i*3)

if n > 0:
    print("Numero positivo")
else:
    print("Numero negativo")

eta = int(input("Età: "))
meggiorenne(eta)

nome = "pippo"
punti = 19

print(f"Il giocatore {nome} ha ottenuto: {punti} punti")

mese = 10
yy = 2020
print(calendar.month(yy, mese))

num = int(input("Numero da radicare: "))
print(math.sqrt(16))

print(math.pow(2, 5))

conta = 1
while conta == 10:
    print("hello: ", conta)
    conta += 1