#Classes and objects (Student details)
class Box:
    def __init__(self, name, rollNo, dbmsMarks, pythonMarks, cMarks, osMarks, cnMarks):
        self.name = name
        self.rollNo = rollNo
        self.dbmsMarks = dbmsMarks
        self.pythonMarks = pythonMarks
        self.cMarks = cMarks
        self.osMarks = osMarks
        self.cnMarks = cnMarks

student1 = Box(name="Harika", rollNo="5A1", dbmsMarks=78, pythonMarks=67, cMarks=77, osMarks=89, cnMarks=46)
student2 = Box(name="Swapna", rollNo="5A2", dbmsMarks=38, pythonMarks=65, cMarks=97, osMarks=59, cnMarks=41)
student3 = Box(name="Sushma", rollNo="5A3", dbmsMarks=88, pythonMarks=95, cMarks=47, osMarks=89, cnMarks=31)

print(student1.name, student1.rollNo, student1.dbmsMarks, student1.pythonMarks, student1.cMarks, student1.osMarks, student1.cnMarks, end=" ")
print()
print(student2.name, student2.rollNo, student2.dbmsMarks, student2.pythonMarks, student2.cMarks, student2.osMarks, student2.cnMarks, end=" ")
print()
print(student3.name, student3.rollNo, student3.dbmsMarks, student3.pythonMarks, student3.cMarks, student3.osMarks, student3.cnMarks, end=" ")
