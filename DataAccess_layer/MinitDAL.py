from Model.MinitModel import MinitModelClass
import pyodbc

class MinitDALClass:
    def __init__(self):
        pass
    def Minit(self,minitModelObjet:MinitModelClass):
        pass
    def getallMinnitList(self):
        commandText = 'select minit from dbo.employee'
        conncectionString = 'Driver={SQL Server};Server=(local);database=pubs;Trusted_Connection=yes'
        with pyodbc.connect(conncectionString) as sqlconnection:
            cursor = sqlconnection.cursor()
            cursor.execute(commandText,)
            rows = cursor.fetchall()
        minitList = []
        for row in rows:
            minitModelObject = MinitModelClass(row[0])
            minitList.append(minitModelObject)

        return minitList
    
