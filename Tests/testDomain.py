from Domain.aeriene import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckin


def testRezervare():
    avion = creeazaRezervare("1", "pandora", "national", 3000, True)
    assert getId(avion) == "1"
    assert getNume(avion) == "pandora"
    assert getClasa(avion) == "national"
    assert getPret(avion) == 3000
    assert getCheckin(avion) == True

