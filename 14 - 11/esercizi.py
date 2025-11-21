#es1
#costo del biglietto 
#Auto: fino a 1000, 20 €
#Auto: fino a 2000, 30 €
#oltre 40€

#camion fino a 2000, 40€
#camion fino a 3000, 50€
#oltre 100€

veicolo = int(input("Tipo di veicolo (1 auto 2 camion)"))

if veicolo != 1 or veicolo != 2:
    print("Valore non valido, inserire di nuovo")
    veicolo = int(input("Tipo di veicolo (1 auto 2 camion)"))

if veicolo == 1:
    celindrata = int(input("Celindrata: "))

    if celindrata <= 1000:
        biglietto = 20
    elif celindrata <= 2000:
        biglietto = 30
    elif celindrata > 2000:
        biglietto = 40

if veicolo == 2:
    celindrata = int(input("Celindrata: "))

    if celindrata <= 2000:
        biglietto = 40
    elif celindrata <= 3000:
        biglietto = 40
    elif celindrata > 2000:
        biglietto = 1000

print(f"Il tuo biglietto costa {biglietto}")