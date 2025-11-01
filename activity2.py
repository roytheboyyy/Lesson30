class per:
    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum
    def display(self):
        print(self.name)
        print(self.idnum)
class emp(per):
    def __init__(self,name,idnum,salary,post):
        self.salary = salary
        self.post = post
        per.__init__(self,name,idnum)

a = emp("rahul", 886012, 200000, "Intern")
a.display()
