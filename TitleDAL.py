import pyodbc

class TitleDALClass:
    def registerTitleDAL(self,title_id, title, type, pub_id, price, advance, royalty, ytd_sales, notes, pub_date):
        params = (title_id, title, type, pub_id, price, advance, royalty, ytd_sales, notes, pub_date)
        command_text = 'EXEC   [dbo].[Registertitle] ?,?,?,?,?,?,?,?,?,?'
        conncectionString = 'Driver={SQL Server};Server=(local);database=pubs;Trusted_Connection=yes'
        with pyodbc.connect(conncectionString) as sqlconnection:
            curosor = sqlconnection.cursor()
            curosor.execute(command_text,params)
            sqlconnection.commit()

