from Domain.aeriene import getCheckin, getPret, creeazaRezervare, getAll


def ieftiniri(procentaj, lista):
    if procentaj > 100:
        raise ValueError("Nu se pot face reduceri mai mari de 100% ")
    if procentaj < 0:
        raise ValueError("Procentajul nu trebuie sa fie mai mic decat 0 ")
    lista_noua = []
    for avion in lista:
        if getCheckin(avion) == "Da":
            noulPret = getPret(avion) - (procentaj / 100 * getPret(avion))
            id, nume, clasa, pret, checkin = getAll(avion)
            avionNou = creeazaRezervare(id, nume, clasa, noulPret, checkin)
            lista_noua.append(avionNou)
        else:
            lista_noua.append(avion)
    return lista_noua