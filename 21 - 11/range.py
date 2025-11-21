#range:
#forma minima range(stop): numeri da 0 a stop esculoso
#forma avanzata range(start, stop): da start a stop escluso
#forma complessa range(start, stop, step): per contare all'indietro, ed è un passo tra start e stop
#genera numeri da 0 a 4

#forma 1
for i in range(5):
    print(f"num: {i}")

#forma 2
for i in range(5, 10):
    print(f"num: {i}")

#forma 3
for i in range(1, 10, 2):
    print(f"num: {i}")