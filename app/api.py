from flask import Flask, jsonify, abort, request, Blueprint
from models import db, Countries, Languages, Currencies, Borders, Regions, SubRegions
from sqlalchemy import text

sweography_api = Blueprint('sweography_api', __name__, url_prefix='/api/v1')

## ------------------- Country Endpoints ------------------- ##
## create
@sweography_api.route('/country', methods=['POST'])
def createCountry():
    data = request.get_json()
    if not data:
        abort(400)
    country = createCountryModel(data)
    if not country:
        return jsonify({"error":"JSON object did not pass validation"}), 422
    return jsonify_utf8(getCountryModel(country.id)), 201

def createCountryModel(data):
    # check for existing region, create new if necessary
    region = db.session.query(Regions).filter(Regions.name==data["region"]).first()
    if not region:
        region = Regions(name=data["region"])

    # check for existing subregion, create new if necessary
    subregion = db.session.query(SubRegions).filter(SubRegions.name==data["subregion"]).first()
    if not subregion:
        subregion = SubRegions(name=data["subregion"])

    country = Countries(name=data["name"], capital=data["capital"], lat=data["lat"], lng=data["lng"],\
        area=data["area"], population=data["population"], region=region, subregion=subregion)

    # check for existing borders, create new if necessary
    for b in data["borders"]:
        border = db.session.query(Borders).filter(Borders.name==b).first()
        if not border:
            border = Borders(name=b)
        country.Borders.append(border)

    # check for existing languages, create new if necessary
    for l in data["languages"]:
        language = db.session.query(Languages).filter(Languages.iso_code==l).first()
        if not language:
            language = Languages(iso_code=l)
        country.Languages.append(language)

    # check for existing currency, create new if necessary
    for c in data["currencies"]:
        currency = db.session.query(Currencies).filter(Currencies.code==c).first()
        if not currency:
            currency = Currencies(code=c)
        country.Currencies.append(currency)

    db.session.add(country)
    db.session.commit()
    return country

## list
@sweography_api.route('/country', methods=['GET'])
def getCountries():
    params = request.args
    countries = getCountryModels(params)
    return jsonify_utf8({"countries":countries}), 200

def getCountryModels(params):
    query_params = {}
    query = "SELECT c.id, c.name, c.capital, c.population, c.area, c.lat, c.lng, c.region_id, c.subregion_id, r.name AS 'region', s.name AS 'subregion'\
        FROM Countries c\
        JOIN Regions r ON r.id = c.region_id\
        JOIN SubRegions s ON s.id = c.subregion_id"
    if params.get('language_id'):
        query += " JOIN country_language cl ON cl.language_id=:language_id AND cl.country_id=c.id"
        query_params["language_id"] = params.get('language_id')
    if params.get('currency_id'):
        query += " JOIN country_currency cc ON cc.currency_id=:currency_id AND cc.country_id=c.id"
        query_params["currency_id"] = params.get('currency_id')
    query += " WHERE 1"
    if params.get('region_id'):
        query += " AND c.region_id=:region_id"
        query_params["region_id"] = params.get('region_id')
    if params.get('subregion_id'):
        query += " AND c.subregion_id=:subregion_id"
        query_params["subregion_id"] = params.get('subregion_id')

    countries = db.session.execute(text(query), params=query_params).fetchall()
    cols = ["id","name","capital","population","area","lat","lng","region","subregion","region_id","subregion_id"]
    countriesJSON = [{col: str(getattr(r, col)) for col in cols} for r in countries]

    # grab many to many relationships
    for country in countriesJSON:
        country["borders"] = []
        country["languages"] = []
        country["currencies"] = []
        c = db.session.query(Countries).filter(Countries.id==country["id"]).first()

        borders = c.Borders
        for b in borders:
            country["borders"].append(b.toJSON())

        languages = c.Languages
        for l in languages:
            country["languages"].append(l.toJSON())

        currencies = c.Currencies
        for c in currencies:
            country["currencies"].append(c.toJSON())

    return countriesJSON

## get
@sweography_api.route('/country/<int:id>', methods=['GET'])
def getCountry(id):
    country = getCountryModel(id)
    if not country:
        abort(404)
    return jsonify_utf8(country), 200

def getCountryModel(id):
    query = text("SELECT c.id, c.name, c.capital, c.population, c.area, c.lat, c.lng, c.region_id, c.subregion_id, r.name AS 'region', s.name AS 'subregion'\
        FROM Countries c\
        JOIN Regions r ON r.id = c.region_id\
        JOIN SubRegions s ON s.id = c.subregion_id\
        WHERE c.id = :id")
    country = db.session.execute(query, params={"id":id}).fetchone()
    cols = ["id","name","capital","population","area","lat","lng","region","subregion","region_id","subregion_id"]
    countriesJSON = {col: str(getattr(country, col)) for col in cols}

    # grab many to many relationships
    countryModel = db.session.query(Countries).filter(Countries.id==country.id).first()
    countriesJSON["borders"] = []
    borders = countryModel.Borders
    for b in borders:
        border = b.toJSON()
        c = db.session.query(Countries).filter(Countries.name.like("%" + border["name"] + "%")).first()
        border["country_id"] = c.id
        countriesJSON["borders"].append(border)

    countriesJSON["languages"] = []
    languages = countryModel.Languages
    for l in languages:
        countriesJSON["languages"].append(l.toJSON())

    countriesJSON["currencies"] = []
    currencies = countryModel.Currencies
    for c in currencies:
        countriesJSON["currencies"].append(c.toJSON())

    return countriesJSON

## update
@sweography_api.route('/country/<int:id>', methods=['PUT'])
def updateCountry(id):
    data = request.get_json()
    if not data:
        abort(400)
    country = updateCountryModel(id, data)
    if not country:
        abort(404)
    return jsonify_utf8(getCountryModel(id)), 200

def updateCountryModel(id, data):
    country = db.session.query(Countries).get(id)
    if not country:
        return False

    region = db.session.query(Regions).filter(Regions.name==data["region"]).first()
    if not region:
        region = Regions(name=data["region"])

    # check for existing subregion, create new if necessary
    subregion = db.session.query(SubRegions).filter(SubRegions.name==data["subregion"]).first()
    if not subregion:
        subregion = SubRegions(name=data["region"])

    country.name = data["name"]
    country.capital = data["capital"]
    country.lat = data["lat"]
    country.lng = data["lng"]
    country.area = data["area"]
    country.population = data["population"]
    country.region = region
    country.subregion = subregion

    # check for existing borders, create new if necessary
    country.Borders[:] = []
    for b in data["borders"]:
        border = db.session.query(Borders).filter(Borders.name==b).first()
        if not border:
            border = Borders(name=b)
        country.Borders.append(border)

    # check for existing languages, create new if necessary
    country.Languages[:] = []
    for l in data["languages"]:
        language = db.session.query(Languages).filter(Languages.iso_code==l).first()
        if not language:
            language = Languages(iso_code=l)
        country.Languages.append(language)

    # check for existing currency, create new if necessary
    country.Currencies[:] = []
    for c in data["currencies"]:
        currency = db.session.query(Currencies).filter(Currencies.code==c).first()
        if not currency:
            currency = Currencies(code=c)
        country.Currencies.append(currency)

    db.session.add(country)
    db.session.commit()
    return country

## delete
@sweography_api.route('/country/<int:id>', methods=['DELETE'])
def removeCountry(id):
    success = removeCountryModel(id)
    if not success:
        abort(404)
    return (''), 204

def removeCountryModel(id):
    country = getCountryModel(id)
    if not country:
        return False
    db.session.delete(country)
    db.session.commit()
    return True

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
    return jsonify_utf8(getRegionModel(region.id)), 201

def createRegionModel(data):
    region = Regions(name=data["name"])
    db.session.add(region)
    db.session.commit()
    return region

## list
@sweography_api.route('/region', methods=['GET'])
def getRegions():
    regions = getRegionModels()
    return jsonify_utf8({"regions":regions}), 200

def getRegionModels():
    query = text("SELECT r.*, SUM( DISTINCT c.population ) AS  'population', SUM( DISTINCT c.area ) AS  'area', COUNT( DISTINCT c.id ) AS  'countries', \
        COUNT( DISTINCT l.id ) AS  'languages', COUNT( DISTINCT s.id ) AS  'subregions', COUNT( DISTINCT cur.id ) AS 'currencies'\
        FROM Regions r\
        LEFT JOIN Countries c ON c.region_id = r.id\
        LEFT JOIN country_language cl ON cl.country_id = c.id\
        LEFT JOIN Languages l ON l.id = cl.language_id\
        LEFT JOIN SubRegions s ON s.id = c.subregion_id\
        LEFT JOIN country_currency cc ON cc.country_id = c.id\
        LEFT JOIN Currencies cur ON cur.id = cc.currency_id\
        GROUP BY r.id")
    regions = db.session.execute(query).fetchall()
    cols = ["id","name","languages","countries","currencies","area","population","subregions"]
    regionsJSON = [{col: str(getattr(r, col)) for col in cols} for r in regions]
    return regionsJSON

## get
@sweography_api.route('/region/<int:id>', methods=['GET'])
def getRegion(id):
    region = getRegionModel(id)
    if not region:
        abort(404)
    return jsonify_utf8(region), 200

def getRegionModel(id):
    query = text("SELECT r.*, SUM( DISTINCT c.population ) AS  'population', SUM( DISTINCT c.area ) AS  'area', COUNT( DISTINCT c.id ) AS  'countries', \
        COUNT( DISTINCT l.id ) AS  'languages', COUNT( DISTINCT s.id ) AS  'subregions', COUNT( DISTINCT cur.id ) AS 'currencies'\
        FROM Regions r\
        LEFT JOIN Countries c ON c.region_id = r.id\
        LEFT JOIN country_language cl ON cl.country_id = c.id\
        LEFT JOIN Languages l ON l.id = cl.language_id\
        LEFT JOIN SubRegions s ON s.id = c.subregion_id\
        LEFT JOIN country_currency cc ON cc.country_id = c.id\
        LEFT JOIN Currencies cur ON cur.id = cc.currency_id\
        WHERE r.id = :id\
        GROUP BY r.id\
        ")
    region = db.session.execute(query, params={"id":id}).fetchone()
    cols = ["id","name","languages","countries","currencies","area","population","subregions"]
    regionsJSON = {col: str(getattr(region, col)) for col in cols}
    return regionsJSON

## update
@sweography_api.route('/region/<int:id>', methods=['PUT'])
def updateRegion(id):
    data = request.get_json()
    if not data:
        abort(400)
    region = updateRegionModel(id, data)
    if not region:
        abort(404)
    return jsonify_utf8(region), 200

def updateRegionModel(id, data):
    region = db.session.query(Regions).get(id)
    if not region:
        return False
    region.name = data["name"]
    db.session.commit()
    return getRegionModel(id)

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

## ------------------- SubRegion Endpoints ------------------- ##
## create
@sweography_api.route('/subregion', methods=['POST'])
def createSubRegion():
    data = request.get_json()
    if not data:
        abort(400)
    subregion = createSubRegionModel(data)
    if not subregion:
        return jsonify({"error":"JSON object did not pass validation"}), 422
    return jsonify_utf8(getSubRegionModel(subregion.id)), 201

def createSubRegionModel(data):
    subregion = SubRegions(name=data["name"])
    db.session.add(subregion)
    db.session.commit()
    return subregion

## list
@sweography_api.route('/subregion', methods=['GET'])
def getSubRegions():
    subregions = getSubRegionModels()
    return jsonify_utf8({"subregions":subregions}), 200

def getSubRegionModels():
    query = text("SELECT sr.*, COUNT( DISTINCT c.id ) AS  'countries', \
        r.name AS 'region', r.id AS 'region_id', \
        COUNT( DISTINCT l.id ) AS  'languages', COUNT( DISTINCT cur.id ) AS 'currencies'\
        FROM SubRegions sr\
        LEFT JOIN Countries c ON c.subregion_id = sr.id\
        LEFT JOIN country_language cl ON cl.country_id = c.id\
        LEFT JOIN Languages l ON l.id = cl.language_id\
        LEFT JOIN Regions r ON r.id = c.region_id\
        LEFT JOIN country_currency cc ON cc.country_id = c.id\
        LEFT JOIN Currencies cur ON cur.id = cc.currency_id\
        GROUP BY sr.id")

    data = db.session.execute(query).fetchall()
    cols = ["id","name","languages","countries","currencies","region","region_id"]
    subregionsJSON = [{col: str(getattr(d, col)) for col in cols} for d in data]
    return subregionsJSON

## get
@sweography_api.route('/subregion/<int:id>', methods=['GET'])
def getSubRegion(id):
    subregion = getSubRegionModel(id)
    if not subregion:
        abort(404)
    return jsonify_utf8(subregion), 200

def getSubRegionModel(id):
    query = text("SELECT sr.*, COUNT( DISTINCT c.id ) AS  'countries', \
        r.name AS 'region', r.id AS 'region_id', \
        COUNT( DISTINCT l.id ) AS  'languages', COUNT( DISTINCT cur.id ) AS 'currencies'\
        FROM SubRegions sr\
        LEFT JOIN Countries c ON c.subregion_id = sr.id\
        LEFT JOIN country_language cl ON cl.country_id = c.id\
        LEFT JOIN Languages l ON l.id = cl.language_id\
        LEFT JOIN Regions r ON r.id = c.region_id\
        LEFT JOIN country_currency cc ON cc.country_id = c.id\
        LEFT JOIN Currencies cur ON cur.id = cc.currency_id\
        WHERE sr.id=:id\
        GROUP BY sr.id\
        ")

    subregion = db.session.execute(query, params={"id":id}).fetchone()
    cols = ["id","name","languages","countries","currencies","region","region_id"]
    subregionsJSON = {col: str(getattr(subregion, col)) for col in cols}
    return subregionsJSON

## update
@sweography_api.route('/subregion/<int:id>', methods=['PUT'])
def updateSubRegion(id):
    data = request.get_json()
    if not data:
        abort(400)
    subregion = updateSubRegionModel(id, data)
    if not subregion:
        abort(404)
    return jsonify_utf8(subregion), 200

def updateSubRegionModel(id, data):
    subregion = db.session.query(SubRegions).get(id)
    if not subregion:
        return False
    subregion.name = data["name"]
    db.session.commit()
    return getSubRegionModel(subregion.id)

## delete
@sweography_api.route('/subregion/<int:id>', methods=['DELETE'])
def removeSubRegion(id):
    success = removeSubRegionModel(id)
    if not success:
        abort(404)
    return (''), 204

def removeSubRegionModel(id):
    subregion = getSubRegionModel(id)
    if not subregion:
        return False
    db.session.delete(subregion)
    db.session.commit()
    return True

## ------------------- Language Endpoints ------------------- ##
## create
@sweography_api.route('/language', methods=['POST'])
def createLanguage():
    data = request.get_json()
    if not data:
        abort(400)
    language = createLanguageModel(data)
    if not language:
        return jsonify({"error":"JSON object did not pass validation"}), 422
    return jsonify_utf8(getLanguageModel(language.id)), 201

def createLanguageModel(data):
    language = Languages(name=data["name"], iso_code=data["iso_code"])
    db.session.add(language)
    db.session.commit()
    return language

## list
@sweography_api.route('/language', methods=['GET'])
def getLanguages():
    languages = getLanguageModels()
    return jsonify_utf8({"languages":languages}), 200

def getLanguageModels():
    query = text("SELECT l.*, COUNT( DISTINCT c.id ) AS  'countries', \
        COUNT( DISTINCT r.id ) AS  'regions', COUNT( DISTINCT s.id ) AS  'subregions'\
        FROM Languages l\
        LEFT JOIN country_language cl ON cl.language_id = l.id\
        LEFT JOIN Countries c ON cl.country_id = c.id\
        LEFT JOIN Regions r ON r.id = c.region_id\
        LEFT JOIN SubRegions s ON s.id = c.subregion_id\
        GROUP BY l.id\
        ")
    languages = db.session.execute(query).fetchall()
    cols = ["id","name","countries","regions","subregions","iso_code"]
    languagesJSON = [{col: str(getattr(r, col)) for col in cols} for r in languages]
    return languagesJSON

## get
@sweography_api.route('/language/<int:id>', methods=['GET'])
def getLanguage(id):
    language = getLanguageModel(id)
    if not language:
        abort(404)
    return jsonify_utf8(language), 200

def getLanguageModel(id):
    query = text("SELECT l.*, COUNT( DISTINCT c.id ) AS  'countries', \
        COUNT( DISTINCT r.id ) AS  'regions', COUNT( DISTINCT s.id ) AS  'subregions'\
        FROM Languages l\
        LEFT JOIN country_language cl ON cl.language_id = l.id\
        LEFT JOIN Countries c ON cl.country_id = c.id\
        LEFT JOIN Regions r ON r.id = c.region_id\
        LEFT JOIN SubRegions s ON s.id = c.subregion_id\
        WHERE l.id = :id\
        GROUP BY l.id\
        ")
    language = db.session.execute(query, params={"id":id}).fetchone()
    cols = ["id","name","countries","regions","subregions","iso_code"]
    languagesJSON = {col: str(getattr(language, col)) for col in cols}
    return languagesJSON

## update
@sweography_api.route('/language/<int:id>', methods=['PUT'])
def updateLanguage(id):
    data = request.get_json()
    if not data:
        abort(400)
    language = updateLanguageModel(id, data)
    if not language:
        abort(404)
    return jsonify_utf8(language), 200

def updateLanguageModel(id, data):
    language = db.session.query(Languages).get(id)
    if not language:
        return False
    language.name = data["name"]
    language.iso_code = data["iso_code"]
    db.session.commit()
    return getLanguageModel(id)

## delete
@sweography_api.route('/language/<int:id>', methods=['DELETE'])
def removeLanguage(id):
    success = removeLanguageModel(id)
    if not success:
        abort(404)
    return (''), 204

def removeLanguageModel(id):
    language = getLanguageModel(id)
    if not language:
        return False
    db.session.delete(language)
    db.session.commit()
    return True

## ------------------- Currency Endpoints ------------------- ##
## create
@sweography_api.route('/currency', methods=['POST'])
def createCurrency():
    data = request.get_json()
    if not data:
        abort(400)
    currency = createCurrencyModel(data)
    if not currency:
        return jsonify({"error":"JSON object did not pass validation"}), 422
    return jsonify_utf8(getCurrencyModel(currency.id)), 201

def createCurrencyModel(data):
    currency = Currencies(name=data["name"], code=data["code"], unicode=data["unicode"])
    db.session.add(currency)
    db.session.commit()
    return currency

## list
@sweography_api.route('/currency', methods=['GET'])
def getCurrencies():
    currencies = getCurrencyModels()
    return jsonify_utf8({"currencies":currencies}), 200

def getCurrencyModels():
    query = text("SELECT cur.*, COUNT( DISTINCT c.id ) AS  'countries', \
        COUNT( DISTINCT r.id ) AS  'regions', COUNT( DISTINCT s.id ) AS  'subregions'\
        FROM Currencies cur\
        LEFT JOIN country_currency cc ON cc.currency_id = cur.id\
        LEFT JOIN Countries c ON cc.country_id = c.id\
        LEFT JOIN Regions r ON r.id = c.region_id\
        LEFT JOIN SubRegions s ON s.id = c.subregion_id\
        GROUP BY cur.id\
        ")
    currencies = db.session.execute(query).fetchall()
    cols = ["id","name","countries","regions","subregions","code"]
    currenciesJSON = [{col: str(getattr(r, col)) for col in cols} for r in currencies]
    return currenciesJSON

## get
@sweography_api.route('/currency/<int:id>', methods=['GET'])
def getCurrency(id):
    currency = getCurrencyModel(id)
    if not currency:
        abort(404)
    return jsonify_utf8(currency), 200

def getCurrencyModel(id):
    query = text("SELECT cur.*, COUNT( DISTINCT c.id ) AS  'countries', \
        COUNT( DISTINCT r.id ) AS  'regions', COUNT( DISTINCT s.id ) AS  'subregions'\
        FROM Currencies cur\
        LEFT JOIN country_currency cc ON cc.currency_id = cur.id\
        LEFT JOIN Countries c ON cc.country_id = c.id\
        LEFT JOIN Regions r ON r.id = c.region_id\
        LEFT JOIN SubRegions s ON s.id = c.subregion_id\
        WHERE cur.id = :id\
        GROUP BY cur.id\
        ")
    currency = db.session.execute(query, params={"id":id}).fetchone()
    cols = ["id","name","countries","regions","subregions","code"]
    currenciesJSON = {col: str(getattr(currency, col)) for col in cols}
    return currenciesJSON

## update
@sweography_api.route('/currency/<int:id>', methods=['PUT'])
def updateCurrency(id):
    data = request.get_json()
    if not data:
        abort(400)
    currency = updateCurrencyModel(id, data)
    if not currency:
        abort(404)
    return jsonify_utf8(currency), 200

def updateCurrencyModel(id, data):
    currency = db.session.query(Currencies).get(id)
    if not currency:
        return False
    currency.name = data["name"]
    currency.code = data["code"]
    db.session.commit()
    return getCurrencyModel(id)

## delete
@sweography_api.route('/currency/<int:id>', methods=['DELETE'])
def removeCurrency(id):
    success = removeCurrencyModel(id)
    if not success:
        abort(404)
    return (''), 204

def removeCurrencyModel(id):
    currency = getCurrencyModel(id)
    if not currency:
        return False
    db.session.delete(currency)
    db.session.commit()
    return True

def jsonify_utf8(data):
    resp = jsonify(data)
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp