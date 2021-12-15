from Domain.aeriene import getId
from Logic.CRUD import adaugaAvion
from Logic.ieftinire import ieftiniri
from Logic.modificareClasa import modificareClasa


def test_undo_redo_console():

    lista = []
    undo_list = []
    redo_list = []

    rezultat = adaugaAvion("1", "Marcel", "business", 200, "Da", lista)
    undo_list.append(lista)
    lista = rezultat


    # se adauga a 2 a rezervare
    rezultat = adaugaAvion("2", "Marcel2", "business", 2000, "Da", lista)
    undo_list.append(lista)
    lista = rezultat


    rezultat = adaugaAvion("3", "Marcel3", "business", 20, "Da", lista)
    undo_list.append(lista)
    lista = rezultat


    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "3"


    # se face undo + assert
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert undo_list == [[], [['1', 'Marcel', 'business', 200, 'Da']]]


    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undo_list == [[]]


    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert undo_list == []
    assert getId(redo_list[2][0]) == "1"


    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list
    assert len(lista) == 0
    assert undo_list == []
    assert getId(redo_list[2][0]) == "1"


    rezultat = adaugaAvion("1", "Marcel", "business", 200, "Da", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()

    rezultat = adaugaAvion("2", "Marcel3", "business", 2000, "Da", lista)
    undo_list.append(lista)
    lista = rezultat

    rezultat = adaugaAvion("3", "Marcel3", "business", 20, "Da", lista)
    undo_list.append(lista)
    lista = rezultat

    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3


    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3


    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert undo_list == [[], [['1', 'Marcel', 'business', 200, 'Da']]]

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undo_list == [[]]



    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert len(lista) == 2



    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(redo_list) == 0
    assert len(undo_list) == 3
    assert len(lista) == 3

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert undo_list == [[], [['1', 'Marcel', 'business', 200, 'Da']]]

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undo_list == [[]]


    rezultat = adaugaAvion("4", "Marcel4", "economy", 200, "Da", lista)
    undo_list.append(lista)
    lista = rezultat
    redo_list.clear()


    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert len(undo_list) == 2
    assert undo_list == [[], [['1', 'Marcel', 'business', 200, 'Da']]]


    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert len(undo_list) == 1
    assert len(redo_list) == 1



    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert len(undo_list) == 0
    assert len(redo_list) == 2



    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 1

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2
    assert len(redo_list) == 0



    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert len(redo_list) == 0
    assert len(undo_list) == 2



    nume = "Marcel4"
    undo_list.append(lista)
    redo_list.clear()

    lista = modificareClasa(nume, lista)
    assert lista[1][2] == "economy plus"

    redo_list.append(lista)
    lista = undo_list.pop()

    assert len(lista) == 2
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert lista[1][2] == "economy"

    undo_list.append(lista)
    lista = redo_list.pop()
    assert lista[1][2] == "economy plus"

    redo_list.append(lista)
    lista = undo_list.pop()

    assert len(lista) == 2
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert lista[1][2] == "economy"


    procentaj = 100
    undo_list.append(lista)
    redo_list.clear()

    lista = ieftiniri(procentaj, lista)
    assert lista[1][3] == 0

    redo_list.append(lista)
    lista = undo_list.pop()

    assert len(lista) == 2
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert lista[1][3] == 200

    undo_list.append(lista)
    lista = redo_list.pop()
    assert lista[1][3] == 0

    redo_list.append(lista)
    lista = undo_list.pop()

    assert len(lista) == 2
    assert len(redo_list) == 1
    assert len(undo_list) == 2
    assert lista[1][3] == 200