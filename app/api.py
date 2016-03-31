from flask import Flask, jsonify, abort, request, Blueprint
from models import db, Countries, Languages, Currencies, Borders, Regions, SubRegions

sweography_api = Blueprint('sweography_api', __name__, url_prefix='/api/v1')

## Country Endpoints
@sweography_api.route('/country', methods=['POST'])
def createCountry():
    data = request.get_json()
    if not data:
        abort(400)
    country = createCountryModel(data)
    if not country:
        return jsonify({"error":"JSON object did not pass validation"}), 422
    return jsonify(country), 201

## data is a json object
## returns false if data object is not complete
def createCountryModel(data):
    # need to figure out validation
    # need to split lat/lng into separate args
    # find region id
    # find subregion id
    # country = {
    #     "name": data["name"],
    #     "population": data["population"],
    #     "capital": data["capital"],
    #     "area": data['area'],
    # }
    country = Countries(
        name=data["name"],
        population=data["population"],
        capital=data["capital"],
        area=data["area"],
        subregion_id=False,
        region_id=False)
    db.session.add(country)
    db.session.commit()
    return country

@sweography_api.route('/country', methods=['GET'])
def getCountries():
    return jsonify({"countries":countries})

@sweography_api.route('/country/<int:id>', methods=['GET'])
def getCountry(id):
    return jsonify({"message": "Getting country " + str(id)})

@sweography_api.route('/country/<int:id>', methods=['PUT'])
def updateCountry(id):
    return jsonify({"message": "Updating country " + str(id)})

@sweography_api.route('/country/<int:id>', methods=['DELETE'])
def removeCountry(id):
    return jsonify({"message": "Removing country " + str(id)})

## Region Endpoints
@sweography_api.route('/region', methods=['POST'])
def createRegion():
    data = request.get_json()
    if not data:
        abort(400)
    region = createRegionModel(data)
    return jsonify({"message":"maybe it works"}), 200
    if not region:
        return jsonify({"error":"JSON object did not pass validation"}), 422
    return jsonify(region), 201

def createRegionModel(data):
    region = Regions(name=data["name"])
    db.session.add(region)
    db.session.commit()
    return region

@sweography_api.route('/region', methods=['GET'])
def getRegions():
    return jsonify({"regions":db.query(Regions)})

@sweography_api.route('/region/<int:id>', methods=['GET'])
def getRegion(id):
    return jsonify({"message": "Getting region " + str(id)})

@sweography_api.route('/region/<int:id>', methods=['PUT'])
def updateRegion(id):
    return jsonify({"message": "Updating region " + str(id)})

@sweography_api.route('/region/<int:id>', methods=['DELETE'])
def removeRegion(id):
    return jsonify({"message": "Removing region " + str(id)})
