import pyodbc

class PublisherDALClass:

    def registerPublisherDAL(self,pub_id,pub_name,city,state,country):
        params = (pub_id, pub_name, city, state, country)
        command_text = 'EXEC	[dbo].[RegisterPublisher] ?,?,?,?,?'
        conncectionString = 'Driver={SQL Server};Server=(local);database=pubs;Trusted_Connection=yes'
        with pyodbc.connect(conncectionString) as sqlconnection:
            cursor = sqlconnection.cursor()
            cursor.execute(command_text, params)
            sqlconnection.commit()
