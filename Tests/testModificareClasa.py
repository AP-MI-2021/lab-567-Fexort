from Domain.aeriene import getClasa
from Logic.CRUD import adaugaAvion
from Logic.modificareClasa import modificareClasa


def testModificareClasa():
    lista = []
    lista = adaugaAvion("1", "Marian", "economy plus", 200, "Nu", lista)
    lista = adaugaAvion("2", "Mihai", "economy plus", 100, "Da", lista)
    lista = modificareClasa("Mihai", lista)
    assert getClasa(lista[0]) == "business"
    assert getClasa(lista[1]) == "economy plus"
    lista = modificareClasa("Marian", lista)
    assert getClasa(lista[1]) == "business"