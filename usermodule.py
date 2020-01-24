class Employee:
  def __init__(self, name, ID_num, department, Job_title):
        self.name = name
        self.ID_num = ID_num
        self.department = department
        self.Job_title = Job_title
  def printEmployee(self):
    print (self.name, self.ID_num, self.department, self.Job_title)

class EmployeeDictionary:
  def __init__(self, fileName):
    self.dic = {}
    self.fileName = fileName
    try: EmployeeFile = open(fileName, "r")
    except:
        return
    for line in EmployeeFile:
        EmpData = line.split(",")
        employee = Employee(EmpData[0], EmpData[1], EmpData[2], EmpData[3])

        self.dic[employee.ID_num] = employee
    EmployeeFile.close()

  def closeDictionary(self):
    EmployeeFile = open(self.fileName, "w")
    for ID_num in self.dic:
      employee = self.dic[ID_num]
      EmployeeFile.write(employee.name + "," + employee.ID_num + "," + employee.department + "," + employee.Job_title)
    EmployeeFile.close()

  def addEmployee(self, employee):
    self.dic[employee.ID_num] = employee

  def searchEmployee(self, ID_num):
    return self.dic[ID_num]
  
  def editEmployee(self, ID_num, name="", department="", Job_title=""):
    employee = self.dic[ID_num]
    if name != "":
      employee.name = name
    if department != "":
      employee.department = department
    if Job_title != "":
      employee.Job_title = Job_title

  def deleteEmployee(self, ID_num):
    try: del self.dic[ID_num]
    except: raise Exception("Non existing employee")

empleado = Employee("Bigotes", "5", "Infrastructure", "Rocket Scientist")

diccionario = EmployeeDictionary("Socialnauta.txt")
diccionario.addEmployee(empleado)


diccionario.editEmployee("5", "", "Rocketing")
empleado = diccionario.searchEmployee("5")
empleado.printEmployee()
diccionario.deleteEmployee("5")
diccionario.deleteEmployee("5")
diccionario.closeDictionary()




        
        
