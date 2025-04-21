from DataAccessLayer.AuthorDAL import AuthorDALClass

class AuthorBLLClass:

    def registerAuthorBLL(self,au_id, lastname, firstname, phone, address, city, state, zip, contract):
        AuthorDALObject = AuthorDALClass()
        AuthorDALObject.registerAuthorDAL(au_id, lastname, firstname, phone, address, city, state, zip, contract)
