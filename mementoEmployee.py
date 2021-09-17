class EmployeeMemento(object):
    def __init__(self, pk, name, surname, salary):
        print("Memento:__init__: Creating memento")
        self.__pk = pk
        self.__name = name
        self.__surname = surname
        self.__salary = salary
        
    def getEmployee(self):
        return [self.__pk, self.__name, self.__surname, self.__salary]