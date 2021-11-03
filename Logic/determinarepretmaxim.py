from Domain.aeriene import getClasa, getPret



def determinarepretmaxim(lista):
    """
    Functia determina pretul maxim pentru fiecare clasa
    :param lista: lista
    :return: dictionar ce contine in cele 3 chei maximele
    """
    max_cls = {}
    for avion in lista:
        cls = getClasa(avion)
        pretul = getPret(avion)
        if cls in max_cls:
            if pretul > max_cls[cls]:
                max_cls[cls] = pretul
        else:
            max_cls[cls] = pretul
    return max_cls