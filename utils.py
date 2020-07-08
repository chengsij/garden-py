from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
import json
import os
import sys
import datetime

class ConnectFauna:
    client = None

    """create connect to Fauna DB"""
    def __init__(self):
        fauna_key = os.environ.get("FAUNA_KEY") or ""
        # print("fauna_key {0}".format(fauna_key))
        if fauna_key == "":
            print ("Cannot find FAUNA_KEY")
            sys.exit()
        self.client = FaunaClient(secret=fauna_key)

    def get_client(self):
        return self.client

    def create(self, json):
        return self.client.query(q.create(q.collection(Constants.COLLECTION_NAME), {"data": json}))

    def update(self, refId, json):
        return self.client.query(q.update(q.ref(q.collection(Constants.COLLECTION_NAME), refId), {"data": json}))

class Moisture:
    potName = None
    description = None
    moistureIndex = None
    updatedTime = None

    def __init__(self, di1, di2, di3, di4):
        self.potName = di1
        self.description = di2
        self.moistureIndex = di3
        self.updatedTime = di4
        if self.updatedTime == None:
            self.updatedTime = 0

    def to_json(self):
        return json.dumps(self.__dict__)

class Constants:
    COLLECTION_NAME="Moisture"

