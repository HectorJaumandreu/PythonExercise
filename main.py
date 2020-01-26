#
# CLASS Employe: Defines the employee properties
#
class Employee:
  def __init__(self, name, ID_num, department, Job_title):
        self.name = name
        self.ID_num = ID_num
        self.department = department
        self.Job_title = Job_title
  def printEmployee(self):
    print ("ID_num: ",  self.ID_num, " Name:" , self.name, " Department: " , self.department,  " Job Title ", self.Job_title)

class EmployeeDictionary:
  def __init__(self, fileName):
    self.dic = {}
    self.fileName = fileName
    try: EmployeeFile = open(fileName, "r")
    except:
        return
    for line in EmployeeFile.readlines():
        EmpData = line.split(",")
        employee = Employee(EmpData[0], EmpData[1], EmpData[2], EmpData[3].strip())

        self.dic[employee.ID_num] = employee
    EmployeeFile.close()

  def closeDictionary(self):
    EmployeeFile = open(self.fileName, "w")
    for ID_num in self.dic:
      employee = self.dic[ID_num]
      EmployeeFile.write(employee.name + "," + employee.ID_num + "," + employee.department + "," + employee.Job_title+ "\n")
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

class MenuOptions:
  def __init__(self):
    self.end = False
    self.employee_dictionary = EmployeeDictionary("Socialnauta.txt")
    self.options = {"D":lambda :self.optionDeleteEmployee(), "I" : lambda : self.optionInsertEmployee(), "E": lambda : self.optionEditEmployee(), "Q" : lambda : self.optionEndSession(), "P" : lambda : self.optionPrintEmployee()}
    while  not self.end:
      self.SelectOption()
  def SelectOption(self):
    option = input("Please Select an option: (I)nsert, (D)elete, (E)dit, (P)rint Employee, (Q)uit: ").upper()
    ExecuteOption = self.options[option]
    ExecuteOption()

  def optionDeleteEmployee(self):
    ID_num = input("Please Insert the Id of the customer to be deleted: ")
    self.employee_dictionary.deleteEmployee(ID_num)
  def optionInsertEmployee(self):
    ID_num = input("Please Insert the Id of the customer to be created:")
    employeeName = input("Please Insert the name of the employee: ")
    jobRole = input("Please insert the Job Role: ")
    department = input("Please insert the department: ")
    employee = Employee(employeeName, ID_num, department, jobRole)
    self.employee_dictionary.addEmployee(employee)

  def optionEditEmployee(self):
    ID_num = input("Please Insert the Id of the customer to be Edited: ")
    self.optionPrintEmployee(ID_num)
    print("Leave empty if you don't want to change the value: ")
    employeeName = input("Please Insert the new name of the employee: ")
    jobRole = input("Please insert the new Job Role: ")
    department = input("Please insert the new department: ")
    self.employee_dictionary.editEmployee(ID_num, employeeName, department, jobRole)
    self.optionPrintEmployee(ID_num)

  def optionPrintEmployee(self, ID_num=""):
    if ID_num=="":
      ID_num = input("ID of the employee to print: ")
    employee = self.employee_dictionary.searchEmployee(ID_num)
    employee.printEmployee()


  def optionEndSession(self):
    save = input("Do you want to save the changes in the file Y/N: ")
    if save == "Y":
      self.employee_dictionary.closeDictionary()
    print("Bye")
    self.end=True


    
    


menu = MenuOptions()
#empleado = Employee("Bigotes", "5", "Infrastructure", "Rocket Scientist")

#diccionario = EmployeeDictionary("Socialnauta.txt")
#diccionario.addEmployee(empleado)


#diccionario.editEmployee("5", "", "Rocketing")
#empleado = diccionario.searchEmployee("5")
#empleado.printEmployee()
#diccionario.deleteEmployee("5")
#diccionario.deleteEmployee("5")
#diccionario.closeDictionary()




        
        
