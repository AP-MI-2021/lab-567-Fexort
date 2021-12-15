from Domain.aeriene import getNume, getClasa, toString, getAll, creeazaRezervare


def modificareClasa(numeCitit, lista):


    lista_noua = []
    for avion in lista:
        if getNume(avion) == numeCitit:
            if getClasa(avion) == "economy":
                nouaClasa = "economy plus"
            elif getClasa(avion) == "economy plus":
                nouaClasa = "business"
            else:
                print("avionul " + toString(avion) + ", este deja la cea mai superioara clasa ")
                nouaClasa = getClasa(avion)

            id, nume, clasa, pret, checkin = getAll(avion)
            rezervareClsModificata = creeazaRezervare(id, nume, nouaClasa, pret, checkin)
            lista_noua.append(rezervareClsModificata)
        else:
            lista_noua.append(avion)

    return lista_noua