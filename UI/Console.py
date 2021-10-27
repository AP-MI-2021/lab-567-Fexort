from Domain.aeriene import toString
from Logic.CRUD import adaugaAvion, stergeavion, ModificaAvion


def printMenu():
    print("1. adauga avion")
    print("2. sterge avion")
    print("3. modifica avion")
    print("4. afiseaza avion")
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
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("optiune gresita, reincercati: ")