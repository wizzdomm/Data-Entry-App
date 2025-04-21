from DataAccessLayer.PublisherDAL import PublisherDALClass

class PublisherBLLClass:
    def registerPublisher(self,pub_id,pub_name,city,state,country):
        publisherDALObject = PublisherDALClass()
        publisherDALObject.registerPublisherDAL(pub_id,pub_name,city,state,country)