from Domain.aeriene import getPret
from Logic.CRUD import adaugaAvion
from Logic.ieftinire import ieftiniri


def testIeftiniri():
    lista = []
    lista = adaugaAvion("1", "Marcel", "economy plus", 200, "Nu", lista)
    lista = adaugaAvion("2", "Mihai", "economy plus", 100, "Da", lista)
    lista = ieftiniri(10, lista)
    assert getPret(lista[1]) == 90.0
    lista = ieftiniri(10, lista)
    assert getPret(lista[1]) == 81.0
    assert getPret(lista[0]) == 200