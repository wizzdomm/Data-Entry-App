import pyodbc
class EmployeeDALClass:


    def registerEmployeeDAL(self,emp_id, firstname, minit, lastname, jobid, joblvl, pubid, hiredate):
        params = (emp_id, firstname, minit, lastname, jobid, joblvl, pubid, hiredate)
        commandText = 'EXEC	[dbo].[RegisterEMP] ?,?,?,?,?,?,?,?'
        conncectionString = 'Driver={SQL Server};Server=(local);database=pubs;Trusted_Connection=yes'
        with pyodbc.connect(conncectionString) as sqlconnection:
            cursor = sqlconnection.cursor()
            cursor.execute(commandText, params)
            sqlconnection.commit()
