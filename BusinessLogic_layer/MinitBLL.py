from Model.MinitModel import MinitModelClass
from DataAccessLayer.MinitDAL import MinitDALClass
class MinitBLLClass:
    def __init__(self):
        pass
    def getallMinnitList(self):
         minitDALObject = MinitDALClass()
         return minitDALObject.getallMinnitList()

