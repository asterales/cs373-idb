from flask import Flask, jsonify, abort, request, Blueprint
from models import db, Countries, Languages, Currencies, Borders, Regions, SubRegions

sweography_api = Blueprint('sweography_api', __name__, url_prefix='/api/v1')

## ------------------- Region Endpoints ------------------- ##
## create
@sweography_api.route('/region', methods=['POST'])
def createRegion():
    data = request.get_json()
    if not data:
        abort(400)
    region = createRegionModel(data)
    if not region:
        return jsonify({"error":"JSON object did not pass validation"}), 422
    region = getRegionModel(region.id)
    return jsonify(region.toJSON()), 201

def createRegionModel(data):
    region = Regions(name=data["name"])
    db.session.add(region)
    db.session.commit()
    return region

## list
@sweography_api.route('/region', methods=['GET'])
def getRegions():
    regions = getRegionModels()
    regionsJSON = [r.toJSON() for r in regions]
    return jsonify({"regions":regionsJSON})

def getRegionModels():
    return db.session.query(Regions).all()

## get
@sweography_api.route('/region/<int:id>', methods=['GET'])
def getRegion(id):
    region = getRegionModel(id)
    if not region:
        abort(404)
    return jsonify(region.toJSON())

def getRegionModel(id):
    region = db.session.query(Regions).get(id)
    return region

## update
@sweography_api.route('/region/<int:id>', methods=['PUT'])
def updateRegion(id):
    data = request.get_json()
    if not data:
        abort(400)
    region = updateRegionModel(id, data)
    if not region:
        abort(404)
    region = getRegionModel(id)
    return jsonify(region.toJSON())

def updateRegionModel(id, data):
    region = getRegionModel(id)
    if not region:
        return False
    db.session.delete(region)
    region = createRegionModel(data)
    region.id = id
    db.session.add(region)
    db.session.commit()
    return region

## delete
@sweography_api.route('/region/<int:id>', methods=['DELETE'])
def removeRegion(id):
    success = removeRegionModel(id)
    if not success:
        abort(404)
    return (''), 204

def removeRegionModel(id):
    region = getRegionModel(id)
    if not region:
        return False
    db.session.delete(region)
    db.session.commit()
    return True
