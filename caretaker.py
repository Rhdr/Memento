
class Caretaker(object):
    __employeeMententoDict = dict()
    @staticmethod
    def addEmployeeMemento(lst):
        #print("Caretaker:addMemento: mementoEmployee: " + str(mementoEmployee))
        pk = lst[0]
        memento = lst[1]
        Caretaker.__employeeMententoDict[pk] = memento
    
    @staticmethod
    def getEmployeeMemento(pk):
        print("Caretaker:getMemento: index: " + str(pk))
        return Caretaker.__employeeMententoDict[pk]
    
    @staticmethod
    def toString():
        print(Caretaker.__employeeMententoDict)