from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    ## example of rendering a template and passing in data
    country = {"name": "USA", "population":999999, "capitol":"Washington, DC"}
    return render_template("index.html", country = country)

@app.route("/countries")
def countries_table():
	attributes = ["Name", "Latitude", "Longitude", "Region", "Population", "Languages", "Currencies", "Bordering Countries"]
	usa = {"Name" : "United States of America", "Latitude" : 38, "Longitude" : -97, \
			"Region" : "Americas", "Population" : 321645000, \
			"Languages" : 1, "Currencies" : 3, "Bordering Countries" : 2} 
	china = {"Name" : "China", "Latitude" : 35, "Longitude" : 105, \
			"Region" : "Asia", "Population" : 1371590000, \
			"Languages" : 1, "Currencies" : 1, "Bordering Countries" : 15}
	norway = {"Name" : "Norway", "Latitude" : 62, "Longitude" : 10, \
			"Region" : "Europe", "Population" : 5176998, \
			"Languages" : 3, "Currencies" : 1, "Bordering Countries" : 3} 
	countries = [china, norway, usa]
	return render_template('models.html', title = "Countries", attributes = attributes, models = countries)

@app.route("/regions")
def regions_table():
	attributes = ["Name", "Area", "Population", "Subregions", "Countries", "Languages", "Currencies"]
	regions = []
	return render_template('models.html', title = "Regions", attributes = attributes, models = regions)

@app.route("/languages")
def languages_table():
	attributes = ["Name", "ISO 639-1 Code", "Countries", "Regions", "Subregions"]
	norwegian = {"Name" : "Norwegian", "ISO 639-1 Code" : "no", "Countries" : 2, "Regions" : 1, "Subregions": 1}
	afrikaans = {"Name" : "Afrikaans", "ISO 639-1 Code" : "af", "Countries" : 2, "Regions" : 1, "Subregions": 1}
	chinese = {"Name" : "Chinese", "ISO 639-1 Code" : "zh", "Countries" : 5, "Regions" : 1, "Subregions": 2}
	languages = [afrikaans, chinese, norwegian]
	return render_template('models.html', title = "Languages", attributes = attributes, models = languages)

@app.route("/currencies")
def currencies_table():
	attributes = ["Currency Code", "Name", "Countries", "Regions", "Subregions"]
	usd = {"Currency Code" : "USD", "Name" : "US Dollar", "Countries" : 19, "Regions": 4, "Subregions": 8}
	nok = {"Currency Code" : "NOK", "Name" : "Norway Kroner", "Countries" : 3, "Regions": 1, "Subregions": 1}
	cny = {"Currency Code" : "CNY", "Name" : "Yuan Renminbi", "Countries" : 1, "Regions": 1, "Subregions": 1}
	currencies = [cny, nok, usd]
	return render_template('models.html', title = "Currencies", attributes = attributes, models = currencies)

if __name__ == "__main__":
    app.run(debug=True)