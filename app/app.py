from flask import Flask, render_template, request, url_for
from flask_googlemaps import GoogleMaps
from collections import namedtuple
import api
import os
from cgi import escape

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
GoogleMaps(app)
app.register_blueprint(api.sweography_api)

panel_styles = {"countries" : "panel-primary", "regions" : "panel-danger", "subregions" : "panel-info", \
				"languages" : "panel-success", "currencies" : "panel-warning", "media" : "panel-default"}

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/countries")
@app.route("/countries/")
def countries_table():
	attributes = {"name" : "Name", "capital" : "Capital", "lat" :  "Latitude", "lng" : "Longitude", "region" : "Region", "subregion" : "Subregion",\
				  "area":"Area", "population" : "Population", "languages" : "Languages", "currencies" : "Currencies", "borders" : "Bordering Countries"}
	short_attributes = ["name", "capital", "lat", "lng", "region", "subregion", "area", "population", "languages", "currencies", "borders"]
	countries = api.getCountryModels({})
	for c in countries:
		c["currencies"] = len(c["currencies"])
		c["languages"] = len(c["languages"])
		c["borders"] = len(c["borders"])

	return render_template('models.html', model_type = "Countries", attributes = attributes, models = countries, short_name = short_attributes, style = panel_styles["countries"])

@app.route("/regions")
@app.route("/regions/")
def regions_table():
	attributes = {"name":"Name", "area":"Area", "population":"Population", "subregions":"Subregions", "countries":"Countries", \
				  "languages":"Languages", "currencies":"Currencies"}
	short_attributes = ["name", "area", "population", "subregions", "countries", "languages", "currencies"]
	regions = api.getRegionModels({})
	return render_template('models.html', model_type = "Regions", attributes = attributes, models = regions, short_name = short_attributes, style = panel_styles["regions"])

@app.route("/subregions")
@app.route("/subregions/")
def subregions_table():
	attributes = {"name" : "Name", "region" : "Region", "countries" : "Countries", "languages" : "Languages", "currencies" : "Currencies"}
	short_attributes = ["name", "region", "countries", "languages", "currencies"]
	subregions = api.getSubRegionModels({})
	return render_template('models.html', model_type = "Subregions", attributes = attributes, models = subregions, short_name = short_attributes, style = panel_styles["subregions"])

@app.route("/languages")
@app.route("/languages/")
def languages_table():
	attributes = {"name":"Name", "iso_code":"ISO 639-1 Code", "countries":"Countries", "regions":"Regions", "subregions":"Subregions"}
	short_attributes = ["name", "iso_code", "countries", "regions", "subregions"]
	languages = api.getLanguageModels({})
	return render_template('models.html', model_type = "Languages", attributes = attributes, models = languages, short_name = short_attributes, style = panel_styles["languages"])

@app.route("/currencies")
@app.route("/currencies/")
def currencies_table():
	attributes = {"code":"Currency Code", "name":"Name", "countries":"Countries", "regions":"Regions", "subregions":"Subregions"}
	short_attributes = ["code", "name", "countries", "regions", "subregions"]
	currencies = api.getCurrencyModels({})
	return render_template('models.html', model_type = "Currencies", attributes = attributes, models = currencies, short_name = short_attributes, style = panel_styles["currencies"])

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/about/tests")
def run_tests():
	os.system("python3 tests.py > tests.tmp 2>&1")
	result = ""
	with open('tests.tmp', 'r') as output:
		for line in output:
			result += line
	os.system("rm tests.tmp")
	result = "<br />".join(result.split("\n"))
	return result

# Individual Pages
@app.route("/countries/<country>")
def country_page(country):
	country = api.getCountryModel(country)
	if(country):
		return render_template('country.html', country = country, languages = country["languages"], currencies = country["currencies"], borders = country["borders"], panel_styles = panel_styles)
	return render_template('nopage.html', model_title = "Country", model = "country", redirect = "countries")

@app.route("/regions/<region>")
def region_page(region):
	region_id = region
	region = api.getRegionModel(region_id)
	if(region):
		subregions = api.getSubRegionModels({"region_id":region_id})
		countries = api.getCountryModels({"region_id":region_id})
		languages = api.getLanguageModels({"region_id":region_id})
		currencies = api.getCurrencyModels({"region_id":region_id})
		
		return render_template('region.html', region = region, subregions=subregions, countries=countries, languages=languages, \
								currencies = currencies, panel_styles = panel_styles, map_data = get_map_data(countries))

	return render_template('nopage.html', model_title = "Region", model = "region", redirect = "regions")

@app.route("/subregions/<subregion>")
def subregion_page(subregion):
	subregion_id = subregion
	subregion = api.getSubRegionModel(subregion_id)
	if subregion:
		countries = api.getCountryModels({"subregion_id":subregion_id})
		languages = api.getLanguageModels({"subregion_id":subregion_id})
		currencies = api.getCurrencyModels({"subregion_id":subregion_id})
	
		return render_template('subregion.html', subregion = subregion, countries=countries, languages=languages, currencies=currencies,\
								panel_styles = panel_styles, map_data = get_map_data(countries))

	return render_template('nopage.html', model_title = "Subregion", model = "subregion", redirect = "subregions")

@app.route("/languages/<language>")
def language_page(language):
	language_id = language
	language = api.getLanguageModel(language_id)
	if(language):
		regions = api.getRegionModels({"language_id":language_id})
		subregions = api.getSubRegionModels({"language_id":language_id})
		countries = api.getCountryModels({"language_id":language_id})

		return render_template('language.html', language = language, countries = countries, regions = regions, subregions = subregions, panel_styles = panel_styles, \
								map_data = get_map_data(countries))

	return render_template('nopage.html', model_title = "Language", model = "language", redirect = "languages")

@app.route("/currencies/<currency>")
def currency_page(currency):
	currency_id = currency
	currency = api.getCurrencyModel(currency_id)
	if(currency):
		regions = api.getRegionModels({"currency_id":currency_id})
		subregions = api.getSubRegionModels({"currency_id":currency_id})
		countries = api.getCountryModels({"currency_id":currency_id})

		return render_template('currency.html', currency = currency, countries = countries, regions = regions, subregions = subregions, panel_styles = panel_styles, \
								map_data = get_map_data(countries))

	return render_template('nopage.html', model_title = "Currency", model = "currency", redirect = "currencies")

# helper functions to process examples
Link = namedtuple('Link', ['name', 'link'])
def get_links_list(list):
	return map(lambda s: Link(s, get_link(s)), list)

def get_link(s):
	return s.replace(" ", "-").lower()
app.jinja_env.globals.update(get_link=get_link)

# helper functions for calculating map position
from math import radians, degrees, hypot, cos, sin, atan2, fsum

def cartesian_coord(latlng):
	lat = radians(latlng[0])
	lng = radians(latlng[1])
	x = cos(lat) * cos(lng)
	y = cos(lat) * sin(lng)
	z = sin(lat)
	return (x, y, z)

def map_center(coords):
	if not coords:
		return (0, 0)
	cartesians = list(map(cartesian_coord, coords))
	xavg = fsum((t[0] for t in cartesians))/ len(coords)
	yavg = fsum((t[1] for t in cartesians)) / len(coords)
	zavg = fsum((t[2] for t in cartesians)) / len(coords)

	lng = degrees(atan2(yavg, xavg))
	lat = degrees(atan2(zavg, hypot(xavg, yavg)))
	return (lat, lng)

def get_map_data(countries):
	coords = []
	for c in countries:
		if c["lat"] != "" and c["lng"] != "":
			latlng = (float(c["lat"]),float(c["lng"]))
			coords.append(latlng)

	center = map_center(coords)
	map_data = {}
	map_data["lat"] = center[0]
	map_data["lng"] = center[1]
	map_data["coords"] = coords
	return map_data

import populate_db

if __name__ == "__main__":
    app.run(debug=True)
