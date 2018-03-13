#!/usr/bin/python3


#import main mongo connect class
from joiningSegments.mongoConnect import mongoConn

config = {
    "host" : "127.0.0.1",
    "port" : 27017,
    "db" : "testing"
}

print (config["db"])

if __name__ == "__main__":
    """make new monogo conn"""
    dbConn = mongoConn(config["host"], config["port"])
    dbConn.getDbHandle(config["db"])
    dbConn.selectDistinct("users")
