import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class mongoConn():

    """ Connect to MongoDB """
    def __init__(self, host, port):
        self.host = host
        self.port = port

        try:
            self.conn = MongoClient(host=self.host , port=self.port)
            print ("Connected Sucessfully")

        except ConnectionFailure as e:
            print ("Could not connect to MonogoDB: %s").format(e)
            sys.exit(1)

    """ Get a database hangle """
    def getDbHandle(self, mongoDb1):
        self.dbh = self.conn[mongoDb1]
        print ("Sucessfully set up a database handle")
        return self.dbh

    """ Get distinct from cursor """
    def selectDistinct(self, collectionName):
        try:
            self.dbh.users.aggregate(
                [ { '$group': { '_id': '$email' } },
                  { '$out' :  "emails1"  }
                 ], allowDiskUse= True )
        except:
            print ("Unable to run aggregator")

        return True

    """ Close Mongo Db connection """
    def closeConn(self):
        self.conn.close()

