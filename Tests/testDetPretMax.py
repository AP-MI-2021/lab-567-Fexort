from Logic.CRUD import adaugaAvion
from Logic.AfisareSumaPretDupaNume import afisaresumapretnume


def testafisaresumapretnume():
    lista = []
    lista = adaugaAvion("1", "pandora", "international", 200, "Nu", lista)
    lista = adaugaAvion("2", "ellen", "international", 100, "Da", lista)
    lista = adaugaAvion("3", "ellen", "national", 500, "Da", lista)
    lista = adaugaAvion("4", "rizoto", "national", 500, "Da", lista)
    suma = afisaresumapretnume(lista)
    assert suma["pandora"] == 600
    assert suma["ellen"] == 200
    assert suma["rizoto"] == 500