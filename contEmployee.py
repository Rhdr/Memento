import originatorEmployee
from caretaker import Caretaker


class UiContEmployee(object):
    def __init__(self):
        self.employee = originatorEmployee.Employee()
        #self.caretaker = caretaker.Caretaker()

    def uiBtnSaveEmployee(self, pk, name, surname, salary):
        self.employee.setEmployee(pk, name, surname, salary)
        Caretaker.addEmployeeMemento(self.employee.storeInMemento())

    def printLoadedEmp(self):
        print(self.employee.toString())

    def getEmp(self, index):
        #deserialize
        empMemento = Caretaker.getEmployeeMemento(index)
        self.employee.restoreFromMemento(empMemento)


if __name__ == "__main__":
    cont = UiContEmployee()
    cont.uiBtnSaveEmployee(1, "Sami", "Badsmell", -200)
    cont.uiBtnSaveEmployee(2, "Max", "Maxwell", 200)
    cont.uiBtnSaveEmployee(3, "Oblix", "ix", 1000)
    cont.uiBtnSaveEmployee(4, "Astrix", "ix", 1000)
    cont.printLoadedEmp()
    cont.getEmp(2)
    cont.printLoadedEmp()
    cont.uiBtnSaveEmployee(5, "Diane", "Shiverspoon", 800)
    cont.uiBtnSaveEmployee(6, "Jeny", "Generator", 650)
    cont.getEmp(4)
    cont.printLoadedEmp()
    print()
    Caretaker.toString()
    cont.getEmp(2)
    cont.printLoadedEmp()
    cont.uiBtnSaveEmployee(2, "Max", "Tax", 200)
    cont.getEmp(2)
    cont.printLoadedEmp()
    Caretaker.toString()
    print()
