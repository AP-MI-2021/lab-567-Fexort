from Tests.testAll import runAllTests
from UI.Console import runMenu
from commandlineconsole import commandlineconsole

def main():
    lista = []
    runAllTests()
    undo_list = []
    redo_list = []
    while True:
        option = input("pentru meniu apasati 1, pentru consola apasati 2 ; pentru a inchide apasai x: ")
        if option == "1":
             runMenu(lista,undo_list,redo_list)
        elif option == "2":
            commandlineconsole(lista)
        elif option == "x":
            break
        else:
            print("optiune gresita")
main()