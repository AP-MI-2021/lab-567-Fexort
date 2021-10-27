def creeazaRezervare(id, nume, clasa, pret, checkin):
    '''
    creeaza o rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: int
    :param checkin: bool
    :return: un dictionar ce contine o rezervare
    '''
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin

    }
def getId(avion):
    return avion["id"]
def getNume(avion):
    return avion["nume"]
def getClasa(avion):
    return avion["clasa"]
def getPret(avion):
    return avion["pret"]
def getCheckin(avion):
    return avion["checkin"]
def toString(avion):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(avion),
        getPret(avion),
        getNume(avion),
        getCheckin(avion),
        getClasa(avion)
    )