#
# CLASS Employe: Defines the employee properties
#
class Employee:
  #----------------------------------------------------
  # __init__ Instantiation methdo for Class Employee
  # Creates and initializes the properties of the employee
  #----------------------------------------------------
  def __init__(self, name, ID_num, department, Job_title):
        self.name = name
        self.ID_num = ID_num
        self.department = department
        self.Job_title = Job_title
  #-----------------------------------------------------
  # printEmployee
  # Prints in a friendly way the properties of the employee
  #-----------------------------------------------------
  def printEmployee(self):
    print ("ID_num: ",  self.ID_num, " Name:" , self.name, " Department: " , self.department,  " Job Title ", self.Job_title)
#
# Creates a dictionary of Employee objects
# Allows to Insert, Delete, update and save the dictionary to file.
#
class EmployeeDictionary:
  #-----------------------------------------------------
  # __init__ instantiation method of EmployeeDictionary Class.
  # Reads the employees from a file if it exists.
  #-----------------------------------------------------
  def __init__(self, fileName):
    self.dic = {}#creates a dictionary
    self.fileName = fileName
    try: EmployeeFile = open(fileName, "r")#opens a text file 
    except:
        return#if not found it returns 
    for line in EmployeeFile.readlines():#read the lines in the text file 
        EmpData = line.split(",")#Creates array with the different properties
        employee = Employee(EmpData[0], EmpData[1], EmpData[2], EmpData[3].strip())#creates an object

        self.dic[employee.ID_num] = employee#inserts object to the dictionary
    EmployeeFile.close()#closes the text file
  #-----------------------------------------------------
  # closeDictionary 
  # Stores the contents of the dictionary to a file.
  #-----------------------------------------------------
  def closeDictionary(self):
    EmployeeFile = open(self.fileName, "w")#creates or opens file 
    for ID_num in self.dic:#goes through the dictionary aving data into the file
      employee = self.dic[ID_num]
      EmployeeFile.write(employee.name + "," + employee.ID_num + "," + employee.department + "," + employee.Job_title+ "\n")
    EmployeeFile.close()
  #-----------------------------------------------------
  # addEmployee 
  # Inserts a new Employee object into the dictionary using as index the ID_num of the employee.
  #-----------------------------------------------------
  def addEmployee(self, employee):
    self.dic[employee.ID_num] = employee
  #-----------------------------------------------------
  # searchEmployee 
  # Returns the Employee ojbect that is indexed with the ID_num. The index and the ID_num of the employee are the same. 
  #-----------------------------------------------------
  def searchEmployee(self, ID_num):
    return self.dic[ID_num]
  #-----------------------------------------------------
  # editEmployee 
  # Searches an employee by ID_num and modifies the fields that are different to "".
  # The ID_num can't be changed.
  #-----------------------------------------------------
  def editEmployee(self, ID_num, name="", department="", Job_title=""):#parameters except ID_num are optional
    employee = self.dic[ID_num]
    if name != "":#if parameter is entered it is edited with the data entered 
      employee.name = name
    if department != "":
      employee.department = department
    if Job_title != "":
      employee.Job_title = Job_title
  #-----------------------------------------------------
  # delteEmployee 
  # Deletes an employee by its ID_num.
  #-----------------------------------------------------
  def deleteEmployee(self, ID_num):
    try: del self.dic[ID_num]#finds employee with the number entered and deletes it 
    except: raise Exception("Non existing employee")#if not found program raises an error
  #-------------------------------------------
  # MenuOptions: Class that manages the interactive session with the user.
  # Gets input to Create, Modify or delete Employees in an Employee Dictionary that is instantiated on it.
  #-----------------------------------------------
class MenuOptions:
  #-------------------------------------------------
  # __Init__ Instantiation method for MenuOptions class.
  # Instantiates an Employee Dictionary reading the contents from a File and creates a Dictionary with the menu options.
  #-------------------------------------------------
  def __init__(self):
    self.end = False
    self.employee_dictionary = EmployeeDictionary("Socialnauta.txt")
    self.options = {"D":lambda :self.optionDeleteEmployee(), "I" : lambda : self.optionInsertEmployee(), "E": lambda : self.optionEditEmployee(), "Q" : lambda : self.optionEndSession(), "P" : lambda : self.optionPrintEmployee()} #creates a dictionary with all different options, including the corresponding functions. "lambda" creates an anonymous function which can be stored in a variable
    while  not self.end:#loops until end = True      
      self.SelectOption()
  #-------------------------------------------
  # Select Option: Reads the input of the user and executes the option.
  #-----------------------------------------------
  def SelectOption(self):
    option = input("Please Select an option: (I)nsert, (D)elete, (E)dit, (P)rint Employee, (Q)uit: ").upper()
    ExecuteOption = self.options[option] #Selects the function to execute from the menu class and introduces it in the ExecuteOption variable.
    ExecuteOption() #Executes the lambda stored in the variable.
  #-------------------------------------------
  # option Delete Employee: Ask for an employee ID and deletes de employee from the dictionary.
  #-----------------------------------------------
  def optionDeleteEmployee(self):
    ID_num = input("Please Insert the Id of the customer to be deleted: ") 
    self.employee_dictionary.deleteEmployee(ID_num) #Deletes the selected employee from the menu.
  #-----------------------------------------------------
  # optionInsertEmployee: Creates a new employee from user interaction and inserts it into the dictionary
  #-----------------------------------------------------
  def optionInsertEmployee(self):
    ID_num = input("Please Insert the Id of the customer to be created:")
    employeeName = input("Please Insert the name of the employee: ")
    jobRole = input("Please insert the Job Role: ")
    department = input("Please insert the department: ")
    employee = Employee(employeeName, ID_num, department, jobRole) #Creates an employee object with the data from the user
    self.employee_dictionary.addEmployee(employee) #Stores the employee in the dictionary.
  
  #-----------------------------------------------------
  # optionEditEmployee: Edits an existing employee from user interaction
  #-----------------------------------------------------
  def optionEditEmployee(self):
    ID_num = input("Please Insert the Id of the customer to be Edited: ")
    self.optionPrintEmployee(ID_num)
    print("Leave empty if you don't want to change the value: ")
    employeeName = input("Please Insert the new name of the employee: ")
    jobRole = input("Please insert the new Job Role: ")
    department = input("Please insert the new department: ")
    self.employee_dictionary.editEmployee(ID_num, employeeName, department, jobRole) #Changes the values entered by the user.
    self.optionPrintEmployee(ID_num)
  #-----------------------------------------------------
  # optionPrintEmployee: Prints an existing employee from user interaction or taking the ID_num as a parameter.
  #-----------------------------------------------------
  def optionPrintEmployee(self, ID_num=""):
    if ID_num=="":
      ID_num = input("ID of the employee to print: ")
    employee = self.employee_dictionary.searchEmployee(ID_num)
    employee.printEmployee()
  #-----------------------------------------------------
  # optionEndSession: Ask if the object has to be saved in file and ends the interactive session with the user.
  #-----------------------------------------------------
  def optionEndSession(self):
    save = input("Do you want to save the changes in the file Y/N: ")
    if save == "Y":
      self.employee_dictionary.closeDictionary()
    print("Bye")
    self.end=True


    
    


menu = MenuOptions()





        
        
