from Logic.CRUD import adaugaAvion
from Logic.determinarepretmaxim import determinarepretmaxim


def test_determinare_pret_maxim_clasa():
    lista = []
    lista = adaugaAvion("1", "pandora", "international", 300, "Nu", lista)
    lista = adaugaAvion("2", "Adrian", "international", 100, "Da", lista)
    lista = adaugaAvion("3", "Marcel", "national", 550, "Da", lista)
    lista = adaugaAvion("4", "Dorel", "lucru", 200, "Da", lista)
    maxim_cls = determinarepretmaxim(lista)
    assert maxim_cls["national"] == 550
    assert maxim_cls["international"] == 300
    assert maxim_cls["lucru"] == 200