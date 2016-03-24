from flask import Flask, render_template, request, url_for
from collections import namedtuple
app = Flask(__name__)


#Examples data
#Countries
usa = {"Name" : "United States of America", "Capital" : "Washington D.C.", "Latitude" : 38, "Longitude" : -97, \
		"Region" : "Americas", "Subregion" : "Northern America", "Area" : 9629091, "Population" : 321645000, \
		"Languages" : 1, "Currencies" : 3, "Bordering Countries" : 2} 
china = {"Name" : "China", "Capital" : "Beijing", "Latitude" : 35, "Longitude" : 105, \
		"Region" : "Asia", "Subregion" : "Eastern Asia", "Area" : 9640011, "Population" : 1371590000, \
		"Languages" : 1, "Currencies" : 1, "Bordering Countries" : 15}
norway = {"Name" : "Norway", "Capital" : "Oslo", "Latitude" : 62, "Longitude" : 10, \
		"Region" : "Europe", "Subregion" : "Northern Europe", "Area" : 323802, "Population" : 5176998, \
		"Languages" : 3, "Currencies" : 1, "Bordering Countries" : 3} 

#Regions
asia = {"Name": "Asia", "Area": 32064971, "Population": 4339964684, "Subregions": 5, \
		"Countries": 50, "Languages": 37, "Currencies": 49}
americas = {"Name": "Americas", "Area": 42247698, "Population": 983832674, "Subregions": 4, \
			"Countries": 56, "Languages": 11, "Currencies": 43}
europe = {"Name": "Europe", "Area": 23138282, "Population": 745355450, "Subregions": 4, \
		  "Countries": 52, "Languages": 41, "Currencies": 24}

#Languages
norwegian = {"Name" : "Norwegian", "ISO 639-1 Code" : "no", "Countries" : 2, "Regions" : 1, "Subregions": 1}
english = {"Name" : "English", "ISO 639-1 Code" : "en", "Countries" : 89, "Regions" : 15, "Subregions": 18}
chinese = {"Name" : "Chinese", "ISO 639-1 Code" : "zh", "Countries" : 5, "Regions" : 1, "Subregions": 2}

#Currencies
usd = {"Currency Code" : "USD", "Name" : "US Dollar", "Countries" : 19, "Regions": 4, "Subregions": 8}
nok = {"Currency Code" : "NOK", "Name" : "Norway Kroner", "Countries" : 3, "Regions": 1, "Subregions": 1}
cny = {"Currency Code" : "CNY", "Name" : "Yuan Renminbi", "Countries" : 1, "Regions": 1, "Subregions": 1}

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/countries")
@app.route("/countries/")
def countries_table():
	attributes = ["Name", "Capital", "Latitude", "Longitude", "Region", "Subregion", "Area", "Population", \
				  "Languages", "Currencies", "Bordering Countries"]
	countries = [china, norway, usa]
	return render_template('models.html', title = "Countries", attributes = attributes, models = countries)

@app.route("/regions")
@app.route("/regions/")
def regions_table():
	attributes = ["Name", "Area", "Population", "Subregions", "Countries", "Languages", "Currencies"]
	regions = [americas, asia, europe]
	return render_template('models.html', title = "Regions", attributes = attributes, models = regions)

@app.route("/languages")
@app.route("/languages/")
def languages_table():
	attributes = ["Name", "ISO 639-1 Code", "Countries", "Regions", "Subregions"]
	languages = [chinese, english, norwegian]
	return render_template('models.html', title = "Languages", attributes = attributes, models = languages)

@app.route("/currencies")
@app.route("/currencies/")
def currencies_table():
	attributes = ["Currency Code", "Name", "Countries", "Regions", "Subregions"]
	currencies = [cny, nok, usd]
	return render_template('models.html', title = "Currencies", attributes = attributes, models = currencies)

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