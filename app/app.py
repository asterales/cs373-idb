from flask import Flask, render_template, request, url_for
from collections import namedtuple
app = Flask(__name__)


#Examples data
#Countries
usa = {"name" : "United States of America", "capital" : "Washington D.C.", "latitude" : 38, "longitude" : -97, \
		"region" : "Americas", "subregion" : "Northern America", "area" : 9629091, "population" : 321645000, \
		"languages" : 1, "currencies" : 3, "borders" : 2} 
china = {"name" : "China", "capital" : "Beijing", "latitude" : 35, "longitude" : 105, \
		"region" : "Asia", "subregion" : "Eastern Asia", "area" : 9640011, "population" : 1371590000, \
		"languages" : 1, "currencies" : 1, "borders" : 15}
norway = {"name" : "Norway", "capital" : "Oslo", "latitude" : 62, "longitude" : 10, \
		"region" : "Europe", "subregion" : "Northern Europe", "area" : 323802, "population" : 5176998, \
		"languages" : 3, "currencies" : 1, "borders" : 3} 

#Regions
asia = {"name": "Asia", "area": 32064971, "population": 4339964684, \
		"subregions": 5, "countries": 50, "languages": 37, "currencies": 49}
americas = {"name": "Americas", "area": 42247698, "population": 983832674, \
			"subregions": 4, "countries": 56, "languages": 11, "currencies": 43}
europe = {"name": "Europe", "area": 23138282, "population": 745355450, \
		  "subregions": 4, "countries": 52, "languages": 41, "currencies": 24}

#Languages
norwegian = {"name" : "Norwegian", "iso" : "no", "countries" : 2, "regions" : 1, "subregions": 1}
english = {"name" : "English", "iso" : "en", "countries" : 89, "regions" : 15, "subregions": 18}
chinese = {"name" : "Chinese", "iso" : "zh", "countries" : 5, "regions" : 1, "subregions": 2}

#Currencies
usd = {"code" : "USD", "name" : "US Dollar", "countries" : 19, "regions" : 4, "subregions" : 8}
nok = {"code" : "NOK", "name" : "Norway Kroner", "countries" : 3, "regions": 1, "subregions": 1}
cny = {"code" : "CNY", "name" : "Yuan Renminbi", "countries" : 1, "regions": 1, "subregions": 1}

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/countries")
@app.route("/countries/")
def countries_table():
	attributes = {"name" : "Name", "capital" : "Capital", "latitude" :  "Latitude", "longitude" : "Longitude", "region" : "Region", "population" : "Population", \
				  "languages" : "Languages", "currencies" : "Currencies", "borders" : "Bordering Countries"}
	short_attributes = ["name", "capital", "latitude", "longitude", "region", "population", "languages", "currencies", "borders"]
	countries = [china, norway, usa]
	return render_template('models.html', title = "Countries", attributes = attributes, models = countries, short_name = short_attributes)

@app.route("/regions")
@app.route("/regions/")
def regions_table():
	attributes = {"name":"Name", "area":"Area", "population":"Population", "subregions":"Subregions", "countries":"Countries", "languages":"Languages", "currencies":"Currencies"}
	short_attributes = ["name", "area", "population", "subregions", "countries", "languages", "currencies"]
	regions = [americas, asia, europe]
	return render_template('models.html', title = "Regions", attributes = attributes, models = regions, short_name = short_attributes)

@app.route("/languages")
@app.route("/languages/")
def languages_table():
	attributes = {"name":"Name", "iso":"ISO 639-1 Code", "countries":"Countries", "regions":"Regions", "subregions":"Subregions"}
	short_attributes = ["name", "iso", "countries", "regions", "subregions"]
	languages = [chinese, english, norwegian]
	return render_template('models.html', title = "Languages", attributes = attributes, models = languages, short_name = short_attributes)

@app.route("/currencies")
@app.route("/currencies/")
def currencies_table():
	attributes = {"code":"Currency Code", "name":"Name", "countries":"Countries", "regions":"Regions", "subregions":"Subregions"}
	short_attributes = ["code", "name", "countries", "regions", "subregions"]
	currencies = [cny, nok, usd]
	return render_template('models.html', title = "Currencies", attributes = attributes, models = currencies, short_name = short_attributes)

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/countries/<country>")
def country_page(country):
	attributes = ["Capital", "Latitude", "Longitude", "Region", "Subregion", "Area", "Population", \
				  "Languages", "Currencies", "Bordering Countries"]
	if country == "united-states-of-america":
		languages = get_links_list(["English"])
		currencies = get_links_list(["USD", "USN", "USS"])
		borders = get_links_list(["Canada", "Mexico"])
		return render_template('country.html', country = usa, attributes = attributes, \
								languages = languages, currencies = currencies, borders = borders)
	if country == "china":
		languages = get_links_list(["Chinese"])
		currencies = get_links_list(["CNY"])
		borders = get_links_list(["Afghanistan", "Bhutan", "Hong Kong", "India", "Kazakhstan", \
								  "Kyrgyzstan", "Laos", "Macau", "Mongolia", "Myanmar", "Nepal", \
								  "North Korea", "Pakistan", "Russia", "Tajikistan", "Vietnam"])
		return render_template('country.html', country = china, attributes = attributes, \
								languages = languages, currencies = currencies, borders = borders)
	if country == "norway":
		languages = get_links_list(["Norwegian", "Norwegian Bokmål", "Norwegian Nynorsk"])
		currencies = get_links_list(["NOK"])
		borders = get_links_list(["Finland", "Sweden", "Russia"])
		return render_template('country.html', country = norway, attributes = attributes, \
								languages = languages, currencies = currencies, borders = borders)
	return render_template('nopage.html')

@app.route("/regions/<region>")
def region_page(region):
	attributes = ["Area", "Population", "Subregions", "Countries", "Languages", "Currencies"]
	subregions = []
	countries = []
	languages = []
	currencies = []
	return render_template('nopage.html')

@app.route("/languages/<language>")
def language_page(language):
	attributes = ["ISO 639-1 Code", "Countries", "Regions", "Subregions"]
	countries = []
	regions = []
	subregions = []
	return render_template('nopage.html')

@app.route("/currencies/<currency>")
def currency_page(currency):
	attributes = ["Name", "Countries", "Regions", "Subregions"]
	countries = []
	regions = []
	subregions = []
	return render_template('nopage.html')

Link =namedtuple('Link', ['name', 'link'])
def get_links_list(list):
	return map(lambda x: Link(x, x.replace(" ", "-").lower()), list)

if __name__ == "__main__":
    app.run(debug=True)