from Domain.aeriene import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaAvion, getById, stergeavion


def testAdaugaAvion():
    lista = []
    lista = adaugaAvion("1", "pandora", "national", 3000, True, lista)
    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "pandora"
    assert getClasa(getById("1", lista)) == "national"
    assert getPret(getById("1", lista)) == 3000
    assert getCheckin(getById("1", lista)) == True

def testStergeAvion():
    lista = []
    lista = adaugaAvion("1", "pandora", "national", 3000, True, lista)
    lista = adaugaAvion("2", "terminator", "national", 3000, True, lista)

    lista = stergeavion("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None