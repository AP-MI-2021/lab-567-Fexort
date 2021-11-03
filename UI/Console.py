from Domain.aeriene import toString
from Logic.CRUD import adaugaAvion, stergeavion, ModificaAvion
from Logic.AfisareSumaPretDupaNume import afisaresumapretnume
from Logic.determinarepretmaxim import determinarepretmaxim

def printMenu():
    print("1. adauga avion")
    print("2. sterge avion")
    print("3. modifica avion")
    print("4. afisarea sumelor preturilor dupa nume")
    print("5. afisarea pretului maxim pentru clasa")
    print("a. afiseaza avion")
    print("x. iesire")




def UIadaugaAvion(lista):
    id = input("dati id: ")
    nume = input("dati nume: ")
    clasa = input("dati clasa: ")
    pret = int(input("dati pret: "))
    checkin = bool(input("dati checkin: "))
    return adaugaAvion(id, nume, clasa, pret, checkin, lista)
def UIstergeAvion(lista):
    id = input("dati id de sters: ")
    return stergeavion(id , lista)

def UImodificaAvion(lista):
    id = input("dati id modificiat: ")
    nume = input("dati nume modificat: ")
    clasa = input("dati clasa modificat: ")
    pret = int(input("dati pret modificat: "))
    checkin = bool(input("dati checkin modificat: "))
    return ModificaAvion(id, nume, clasa, pret, checkin, lista)


def showAll(lista):
    for avion in lista:
        print(toString(avion))

def UIafisareSumaPretNume(lista):
    suma = afisaresumapretnume(lista)
    for nume in suma:
        print("{} are suma de {}".format(nume, suma[nume]))
def UIdeterminarePretMax(lista):
    max_cls = determinarepretmaxim(lista)
    for clasa in max_cls:
        print("clasa {} are pretul cel mai mare de: {}".format(clasa,max_cls[clasa]))

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("dati optiunea: ")
        if optiune == "1":
            lista = UIadaugaAvion(lista)
        elif optiune == "2":
            lista = UIstergeAvion(lista)
        elif optiune == "3":
            lista = UImodificaAvion(lista)
        elif optiune == "4":
            lista = UIafisareSumaPretNume(lista)
        elif optiune == "5":
            lista = UIdeterminarePretMax(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("optiune gresita, reincercati: ")