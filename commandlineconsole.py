from Logic.CRUD import adaugaAvion, stergeavion, ModificaAvion
from UI.Console import showAll


def commandlineconsole(lista):
    while True:
        try:
            print("pentru ajutor tastati h")
            comand = input("Dati comanda: ")
            if comand == "h":
                print("Pentru a adauga o noua rezervare scrieti comanda add urmata de datele pe care doriti sa le introduceti, separate prin virgula")
                print("Pentru a modifica, scrieti update, apoi virgula si id-ul avionului, urmat de noile date")
                print("Pentru a sterge scrieti delete,apoi virgula si id-ul rezerarii ce urmeaza sa se stearga")
                print("Pentru a afisa toate datele scrieti showall")
                print("Puteti scrie mai multe comenzi separandu-le prin ;")
                print("Exemple: add,1,pandora,national,200,Da")
                print("add,2,elice,international,250,Nu")
                print("showall;")
                print("delete,2;showall")
                print("update,1,pandora,international,100,Nu")
                print("stop pentru inchide")
            elif comand == "stop":
                break
            else:
                executacomenzi = comand.split(";")
                for i in range(len(executacomenzi)):
                    comandadiferita = executacomenzi[i].split(",")
                    if comandadiferita[0] == "add":
                        if len(comandadiferita) != 6:
                            raise ValueError("trebuie sa introduceti 5 date")
                        id = comandadiferita[1]
                        nume = comandadiferita[2]
                        clasa = comandadiferita[3]
                        pret = float(comandadiferita[4])
                        checkin = comandadiferita[5]
                        lista = adaugaAvion(id, nume, clasa, pret, checkin, lista)
                    elif comandadiferita[0] == "delete":
                        id = comandadiferita[1]
                        lista = stergeavion(id, lista)
                        print("Au fost sterse date ")
                    elif comandadiferita[0] == "update":
                        if len(comandadiferita) != 6:
                            raise ValueError("Trebuie sa introduceti exact 5 date!")
                        id = comandadiferita[1]
                        nume = comandadiferita[2]
                        clasa = comandadiferita[3]
                        pret = float(comandadiferita[4])
                        checkin = comandadiferita[5]
                        lista = ModificaAvion(id, nume, clasa, pret, checkin, lista)
                        print("au fost modificate date")
                    elif comandadiferita[0] == "showall":
                        showAll(lista)
                    else:
                        print("comanda gresita ")
        except ValueError as err:
            print("Eroare: {}".format(err))