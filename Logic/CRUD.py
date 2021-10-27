from Domain.aeriene import creeazaRezervare, getId


def adaugaAvion(id, nume, clasa, pret, checkin, lista):
    '''
    adauga un avion in lista
    :param id: string
    :param nume: string
    :param clasa: string 
    :param pret: int
    :param checkin: bool
    :param lista: lista de avioane
    :return: elem vechi si elem noi intr-o lista
    '''
    avion = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [avion]

def getById(id, lista):
    for avion in lista:
        if getId(avion) == id:
            return avion
    return None
def stergeavion(id, lista):
    return [avion for avion in lista if getId(avion) != id]

def ModificaAvion(id, nume, clasa, pret, checkin, lista):
    listaNoua = []
    for avion in lista:
        if getId(avion) == id:
            avionNou = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(avionNou)
        else:
            listaNoua.append(avion)
    return listaNoua
