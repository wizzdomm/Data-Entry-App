from DataAccessLayer.TitleDAL import TitleDALClass

class TitleBLLClass:
    def registerTitleBLL(self,title_id, title, type, pub_id, price, advance, royalty, ytd_sales, notes, pub_date):
        titleDALObject = TitleDALClass()
        titleDALObject.registerTitleDAL(title_id, title, type, pub_id, price, advance, royalty, ytd_sales, notes, pub_date)

