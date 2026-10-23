class Patient:
    name = str
    bill = float
    def __init__ (self, name):
        self.__name = name
    def set_bill(self, bill):
            self.bill = bill
    
            self.bill = bill
    def get_bill(self):
        return self.bill
    
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
         return self.__name
class Senior(Patient):
    def calcbill():
        calcbill = bill
    def set_calcbill(self, calcbill):
        calcbill = self.bill*0.8
        self.calcbill = calcbill
    
    def get_calcbill(self):
        return self.calcbill
        
class Philhealth(Patient):
    def calcbill():
        calcbill = bill
    def set_calcbill(self, calcbill):
        calcbill = self.bill*0.85
        self.calcbill = calcbill
    
    def get_calcbill(self):
        return self.calcbill
        
patient1 = Patient("Staurakios")
patient1.set_bill(2000)
patient1.set_name("John Rane")
print(patient1.get_name(), "\n- Bill amount: ", patient1.get_bill(), "php")

senior1 = Senior("Johmm")
senior1.set_bill(2000)
senior1.set_calcbill(2000)
senior1.set_name("Gertrude Tolouse")
print(senior1.get_name(), "\n- Original bill amount: ", senior1.get_bill(), "php", "\n- Discounted bill amount: ", senior1.get_calcbill(), "php")

philhealth1 = Philhealth("Jart")
philhealth1.set_bill(2000)
philhealth1.set_calcbill(2000)
philhealth1.set_name("Beth Yvat")
print(philhealth1.get_name(), "\n- Original bill amount: ", philhealth1.get_bill(), "php", "\n- Discounted bill amount: ", philhealth1.get_calcbill(), "php")
