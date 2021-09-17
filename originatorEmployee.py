import mementoEmployee

#originator
class Employee(object):
    def __init__(self):
        self.__pk = 0
        self.__name = ""
        self.__surname = ""
        self.__salary = 0
        
    def setEmployee(self,  pk, name, surname, salary):   
        self.__pk = pk
        self.__name = name
        self.__surname = surname
        self.__salary = salary
        
    def toString(self):
        return "Employee:toString: %d, %s, %s, %d" % (self.__pk, self.__name, self.__surname, self.__salary)

    def storeInMemento(self):
        mempMemento = mementoEmployee.EmployeeMemento(self.__pk, self.__name, self.__surname, self.__salary)
        return [self.__pk, mempMemento]

    def restoreFromMemento(self, employeeMementoCls):
        type(employeeMementoCls)
        restoreLst = employeeMementoCls.getEmployee()
        self.setEmployee(restoreLst[0], restoreLst[1], restoreLst[2], restoreLst[3])
        #print("Employee:restoreFromMemento")
        