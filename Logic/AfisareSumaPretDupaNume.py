from Domain.aeriene import getNume, getPret


def afisaresumapretnume(lista):
    """
    Functia calculeaza suma preturilor pentru fiecare nume
    :param lista: lista
    :return: dictionar ce contine ca si cheie pentru fiecare nume suma calculata
    """

    suma = {}
    for avion in lista:
        numele = getNume(avion)
        pretul = getPret(avion)
        if numele in suma:
            suma[numele] = suma[numele] + pretul
        else:
            suma[numele] = pretul
    return suma