from flask import Flask, request, Response
import os, sys
import json
from utils import ConnectFauna
import datetime
from http import HTTPStatus

def parseRequestData(data):
    try:
        _data = data.decode('utf-8')
        _json_data = json.loads(_data)
        print("JSON LOADS ", _json_data)
        return _json_data
    except:
        return None


def successResponse(message, status):
    _message = {}
    _message['Result'] = "{rs}".format(rs=message)
    _message['Timestamp'] = "{ts}".format(ts=str(datetime.datetime.now()))
    return Response(json.dumps(_message, indent=4), mimetype='application/json', status=status)

def errResponse(message, status):
    _message = {}
    _message['Error'] = "{msg} at {ts}".format(msg=message, ts=str(datetime.datetime.now()))
    _response = Response(json.dumps(_message, indent=4), mimetype='application/json', status=status)
    return Response(json.dumps(_message, indent=4), mimetype='application/json', status=status)


app = Flask(__name__)

@app.route("/updateMoisture", methods=['POST'])
def createMoisture():
    print("Received: ", request.data)
    _json_data = parseRequestData(request.data)
    if _json_data is None:
        return errResponse("Invalid Json input", HTTPStatus.INTERNAL_SERVER_ERROR)
    db_result = fauna_client.create(_json_data)
    return successResponse(db_result, HTTPStatus.CREATED)


@app.route("/updateMoisture/<int:refId>", methods=['PUT'])
def updateMoisture(refId):
    print("Received: ", request.data)
    # assert refId == request.view_args['refId']
    _json_data = parseRequestData(request.data)
    if _json_data is None:
        return errResponse("Invalid Json input", HTTPStatus.INTERNAL_SERVER_ERROR)
    db_result = fauna_client.update(refId, _json_data)
    return successResponse(db_result, HTTPStatus.OK)


fauna_client = ConnectFauna()

if __name__ == '__main__':
    app.run('localhost', port=8087, debug=True)
