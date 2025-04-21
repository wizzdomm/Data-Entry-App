from DataAccessLayer.EmployeeDAL import EmployeeDALClass

class EmployeeBLLClass:
    def registerEmployeeBLL(self,emp_id, firstname, minit, lastname, jobid, joblvl, pubid, hiredate):
        employeeDALObject = EmployeeDALClass()
        employeeDALObject.registerEmployeeDAL(emp_id, firstname, minit, lastname, jobid, joblvl, pubid, hiredate)
