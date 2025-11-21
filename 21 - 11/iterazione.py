#Iterazione definita e indefinita
#liste

a = ["a, b, c, d"]

for i in a:
    print(f"alfabeto: {i}")


#liste temp di una settimana

temp = [22, 10, 20, 21, 3]
conta = 0

for i in temp:
    conta += i

media = conta/len(temp)

print(f"temperature media: {media}")


#range:
#forma minima range(stop): numeri da 0 a stop esculoso
#forma avanzata range(start, stop): da start a stop escluso
#forma complessa range(start, stop, step): per contare all'indietro, ed è un passo tra start e stop

for i in range(3, 8):
    ca += 1

for i in range(len(temp)):
    c += 1
