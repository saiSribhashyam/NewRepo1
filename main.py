class Ticket :
    def init(self,nm,a,gen) :
        self.name = nm
        self.age = a
        self.gender = gen
    def getName(self) :
        return self.name
    def getage(self) :
        return self.age
    def getGender(self) :
        return self.gender

class Compartment(Ticket) :
    def init(self,nm,a,gen,comp) :
        super().init(nm,a,gen)
        self.block = comp
    def getage(self) :
        print(self.name+" "+self.age+ " "+self.gender+" "+self.block)
c = Compartment("SNEHITH","18","M","Ac")
c.getage()