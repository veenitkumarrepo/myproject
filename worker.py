import database
class worker:
    def __init__(self , name , salary , bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus
        self.total = 0
        self.id = (self.name + str(self.salary) + str(self.bonus) + str(database.num))
        database.num += 1
    def setname(self , name):
        self.name = name
    def setsalary(self , salary):
        self.salary = salary
    def setbonus(self , bonus):
        self.bonus = bonus
    def addtototal(self , cost):
        self.total += cost
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getsalary(self):
        return self.salary
    def getbonus(self):
        return self.bonus
    def gettotal(self):
        return (self.total + self.salary)
    def bonusadder(self , rate):
        bonuscost = ((self.bonus * rate)/100)
        self.addtototal(bonuscost)