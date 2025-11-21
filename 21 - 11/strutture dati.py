#1: SLICING deòòa tupla: prende tutti gli elementi da 1 i poi
# strutture dati sono:
#sequenze:
#   liste: 
    #   mutabile
    #   ordinata
    #   sintassi []
#   tuple: 
    #   ordinata
    #   immutabili
    #   sintassi ()
    #   può contenere tipi dfiversi

#mappatura:
#   dizionari

#insiemi: set

#tuple:
coordinate = (41.90, 12.49)

lat = coordinate[0]
long = coordinate[1]

print(f"Le coordiinate di bs: {lat}, {long}")

#lista:
num = [1, 4, 2, 6, 6, 9, 3, 0]

# num.sort()
num.sort(reverse = True)
num.append(10)
print(num)