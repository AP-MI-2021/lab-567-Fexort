from Tests.testCRUD import testAdaugaAvion, testStergePrajitura
from Tests.testDomain import testRezervare
def runAllTests():
    testRezervare()
    testAdaugaAvion()
    testStergePrajitura()