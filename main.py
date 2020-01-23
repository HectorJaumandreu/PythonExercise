class Employee:
    def __init__(self, name, ID_num, department, Job_title):
        self.name = name
        self.ID_num = ID_num
        self.department = department
        self.Job_title = Job_title
  def printEmployee(self)
    print (self.name, self.ID_num, self.department, self.Job_title)

    class EmployeeDictionary:
      def __init__(self, fileName)
        self.dic = {}
        self.fileName = fileName
        try: EmployeeFile = open(FileName, "r")
        except:
          print("no encontrado")
          return

        for line in EmployeeFile
          EmpData = line.split(",")
          employee = Employee(EmpData[0], EmpData[1], EmpData[2], EmpData[3])

          self.dic[employee.ID_num] = employee

      def closeDictionary(self)
        EmployeeFile = open(self.fileName, "w")
        for ID_num in self.dic:
          employee = self.dic[ID_num]
          EmployeeFile.write(employee.name + "," + employee.ID_num + "," + employee.department + "," + employee.Job_title)
          


        
        
