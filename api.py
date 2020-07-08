import logging
from flask import Flask

log = logging.getLogger(__name__)
app = Flask(__name__)

log.addHandler(logging.StreamHandler())
logging.basicConfig(level=logging.INFO)


@app.route("/", methods=['GET'])
def welcome():
    log.info("Welcome")
    return "Store garden soil data. Use /updateMoisture"


#TODO change to POST and put data in body
@app.route("/updateMoisture/<data>", methods=['GET'])
def updateMoisture(data):
    log.info("Split raw data %s", data)
    details = data.split()
    updateMoistureDetails(details[0], details[1], details[2])
    return "Updated"


@app.route("/updateMoisture/<potName>/<date>/<moistureIndex>", methods=['GET'])
def updateMoistureDetails(potName, date, moistureIndex):
    log.info("Update moisture %s %s %s", potName, date, moistureIndex)
    return "Updated"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
