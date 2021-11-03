from Tests.testCRUD import testAdaugaAvion, testStergeAvion
from Tests.testDomain import testRezervare
def runAllTests():
    testRezervare()
    testAdaugaAvion()
    testStergeAvion()