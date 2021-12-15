from Domain.aeriene import toString
from Logic.CRUD import adaugaAvion, stergeavion, ModificaAvion
from Logic.AfisareSumaPretDupaNume import afisaresumapretnume
from Logic.determinarepretmaxim import determinarepretmaxim
from Logic.ieftinire import ieftiniri
from Logic.modificareClasa import modificareClasa

def printMenu():
    print("1. adauga avion")
    print("2. sterge avion")
    print("3. modifica avion")
    print("4. afisarea sumelor preturilor dupa nume")
    print("5. afisarea pretului maxim pentru clasa")
    print("6. ieftinirea tuturor rezervarilor dupa un procentaj")
    print("7. modificarea clasei")
    print("u. undo")
    print("r. redo")
    print("a. afiseaza avion")
    print("x. iesire")




def UIadaugaAvion(lista, undo_list, redo_list):
    id = input("dati id: ")
    nume = input("dati nume: ")
    clasa = input("dati clasa: ")
    pret = int(input("dati pret: "))
    checkin = bool(input("dati checkin: "))
    undo_list.append(lista)
    redo_list.clear()
    return adaugaAvion(id, nume, clasa, pret, checkin, lista)
def UIstergeAvion(lista, undo_list, redo_list):
    id = input("dati id de sters: ")
    undo_list.append(lista)
    redo_list.clear()
    return stergeavion(id , lista)

def UImodificaAvion(lista, undo_list, redo_list):
    id = input("dati id modificiat: ")
    nume = input("dati nume modificat: ")
    clasa = input("dati clasa modificat: ")
    pret = int(input("dati pret modificat: "))
    checkin = bool(input("dati checkin modificat: "))
    undo_list.append(lista)
    redo_list.clear()
    return ModificaAvion(id, nume, clasa, pret, checkin, lista)


def showAll(lista):
    for avion in lista:
        print(toString(avion))

def UIafisareSumaPretNume(lista):
    suma = afisaresumapretnume(lista)
    for nume in suma:
        print("{} are suma de {}".format(nume, suma[nume]))

def UIdeterminarepretmaxim(lista):
    maxim_cls = determinarepretmaxim(lista)
    for clasa in maxim_cls:
        print("Clasa {} are pretul cel mai mare de : {}".format(clasa,maxim_cls[clasa]))
    return None
def UIieftinire(lista, undo_list, redo_list):
    try:
        procentaj = float(input("Cu cat la suta vreti sa se reduca pretul rezervarilor cu checkin? "))
        rezultat = ieftiniri(procentaj, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def UImodificareClasa(lista, undo_list, redo_list):


    nume_citit = input("Care este numele persoanei careia trebuie modificata superior clasa?")
    rezultat = modificareClasa(nume_citit, lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat

def runMenu(lista,undo_list,redo_list):
    while True:
        printMenu()
        optiune = input("dati optiunea: ")
        if optiune == "1":
            lista = UIadaugaAvion(lista,undo_list,redo_list)
        elif optiune == "2":
            lista = UIstergeAvion(lista,undo_list,redo_list)
        elif optiune == "3":
            lista = UImodificaAvion(lista,undo_list,redo_list)
        elif optiune == "4":
            lista = UIafisareSumaPretNume(lista)
        elif optiune == "5":
            lista = UIdeterminarepretmaxim(lista)
        elif optiune == "6":
            lista = UIieftinire(lista,undo_list,redo_list)
        elif optiune == "7":
            lista = UImodificareClasa(lista,undo_list,redo_list)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo ")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo ")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("optiune gresita, reincercati: ")