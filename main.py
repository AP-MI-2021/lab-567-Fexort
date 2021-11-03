from Tests.testAll import runAllTests
from UI.Console import runMenu
from commandlineconsole import commandlineconsole

def main():
    lista = []
    runAllTests()
    while True:
        option = input("pentru meniu apasati 1, pentru consola apasati 2; pentru a inchide apasai x: ")
        if option == "1":
             runMenu([])
        elif option == "2":
            commandlineconsole(lista)
        elif option == "x":
            break
        else:
            print("optiune gresita")
main()