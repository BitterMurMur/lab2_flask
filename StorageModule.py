import pickle

import CompanyModule


class Storage:

    def __init__(self, company):
        self.company = company
        try:
            self.load()
        except:
            self.company.director = CompanyModule.ConcreteEmployee()
            self.company.leadEngineers:list[CompanyModule.ConcreteEmployee]  = []
            self.company.engineers:list[CompanyModule.LeafEmployee] = []

    def save(self):
        pickle.dump((self.company.director, self.company.leadEngineers, self.company.engineers), open("data.dat", "wb"))
        
    def load(self):
        (self.company.director, self.company.leadEngineers, self.company.engineers) = pickle.load(open("data.dat", "rb"))

    def getItems(self):
        company = CompanyModule.Company()
        company.director = self.company.director
        company.leadsEngineers = self.company.leadEngineers
        company.engineers = self.company.engineers
        return company

    def delete(self, id):
        if self.company.director.id == id:
            self.company.director = CompanyModule.ConcreteEmployee()
        if len(self.company.director.childs) > 0:
            for child in self.company.director.childs:
                if child.id == id:
                    self.company.director.removeChild(child)
        if len(self.company.leadEngineers) > 0:
            for emp in self.company.leadEngineers:
                if emp.id == id:
                    self.company.leadEngineers.remove(emp)
                if len(emp.childs) > 0:
                    for child in emp.childs:
                        if child.id == id:
                            emp.removeChild(child)
        if len(self.company.engineers) > 0:
            for emp in self.company.engineers:
                if emp.id == id:
                    self.company.engineers.remove(emp)

    def getItem(self, id):
        if id == '0':
            return CompanyModule.Company()
        if self.company.director.id == id:
             return self.company.director
        if len(self.company.leadEngineers) > 0:
            for emp in self.company.leadEngineers:
                if emp.id == id:
                    return emp
        if len(self.company.engineers) > 0:
            for emp in self.company.engineers:
                if emp.id == id:
                    return emp
        raise Exception("???????????????????? ?? ?????????? Id ???? ????????????????????")

    def add(self, fullName, position):
        if position == "????????????????":
            self.company.director.fullName = fullName
            self.company.director.position = "????????????????"
            if len( self.company.leadEngineers) > 0:
                for emp in  self.company.leadEngineers:
                    self.company.director.addChild(emp)
            if len( self.company.engineers) > 0:
                for emp in  self.company.engineers:
                    self.company.director.addChild(emp)

        elif position == "?????????????? ??????????????":
            leadEngineer = CompanyModule.ConcreteEmployee()
            leadEngineer.fullName = fullName
            leadEngineer.position = "?????????????? ??????????????"
            if len( self.company.engineers) > 0:
                for emp in  self.company.engineers:
                    leadEngineer.addChild(emp)
            self.company.leadEngineers.append(leadEngineer)

        elif position == "??????????????":
            engineer = CompanyModule.LeafEmployee()
            engineer.fullName = fullName
            engineer.position = "??????????????"
            self.company.engineers.append(engineer)
