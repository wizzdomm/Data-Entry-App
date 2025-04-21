import pyodbc


class AuthorDALClass:

    def registerAuthorDAL(self,au_id, lastname, firstname, phone, address, city, state, zip, contract):
        params = (au_id, lastname, firstname, phone, address, city, state, zip, contract)
        command_text = 'EXEC	[dbo].[RegisterAuthor] ?,?,?,?,?,?,?,?,?'
        conncectionString = 'Driver={SQL Server};Server=(local);database=pubs;Trusted_Connection=yes'
        with pyodbc.connect(conncectionString) as sqlconnection:
            cursor = sqlconnection.cursor()
            cursor.execute(command_text, params)
            sqlconnection.commit()