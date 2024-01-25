class Employee:
    numOfEmployee=0
    def __init__(self,name,family,salary,department):
        self.name=name;
        self.family=family;
        self.salary=salary
        self.department=department
        Employee.numOfEmployee+=1
    def avgSal(self):
        return self.salary/self.numOfEmployee;
        
class FullTime(Employee):
    def __init__(self,name,family,salary,department):
        super().__init__(name,family,salary,department)
        
f=Employee("shivani","female",100,"cse")
e= FullTime("ganesh","male",1000,"h");
print(e.avgSal())
print(f.avgSal())
