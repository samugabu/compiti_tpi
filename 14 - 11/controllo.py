tipo = int(input("Che ruolo hai (1 amministratore, 2 utente): "))
pass_amm = "admin123"
pass_ut = "user123"

while tipo != 1 or tipo != 2:
    print("Errore, si prega di reinserire")
    tipo = int(input("Che ruolo hai (1 amministratore, 2 utente): "))


if tipo == 1:
    p = str(input("password amminstratore: "))

    if p != pass_amm:
        print("Accesso amministratore consentito")
    else:
        print("Accesso amministratore negato")

if tipo == 2:
    p1 = str(input("password utente: "))

    if p1 == pass_ut:
        print("Accesso utente consentito")
    else:
        print("Accesso utente negato")