from flask import Flask, render_template, request, url_for
from collections import namedtuple

# Get examples data from outside file
from examples import usa, china, norway, \
					 americas, asia, europe, \
					 chinese, english, norwegian, \
					 cny, nok, usd, \
					 east_asia, north_amer, north_euro

app = Flask(__name__)

panel_styles = {"countries" : "panel-primary", "regions" : "panel-danger", "subregions" : "panel-info", \
				"languages" : "panel-success", "currencies" : "panel-warning"}

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/countries")
@app.route("/countries/")
def countries_table():
	attributes = {"name" : "Name", "capital" : "Capital", "latitude" :  "Latitude", "longitude" : "Longitude", "region" : "Region", "subregion" : "Subregion",\
				  "area":"Area", "population" : "Population", "languages" : "Languages", "currencies" : "Currencies", "borders" : "Bordering Countries"}
	short_attributes = ["name", "capital", "latitude", "longitude", "region", "subregion", "area", "population", "languages", "currencies", "borders"]
	countries = [china, norway, usa]
	return render_template('models.html', model_type = "Countries", attributes = attributes, models = countries, short_name = short_attributes, style = panel_styles["countries"])

@app.route("/regions")
@app.route("/regions/")
def regions_table():
	attributes = {"name":"Name", "area":"Area", "population":"Population", "subregions":"Subregions", "countries":"Countries", \
				  "languages":"Languages", "currencies":"Currencies"}
	short_attributes = ["name", "area", "population", "subregions", "countries", "languages", "currencies"]
	regions = [americas, asia, europe]
	return render_template('models.html', model_type = "Regions", attributes = attributes, models = regions, short_name = short_attributes, style = panel_styles["regions"])

@app.route("/subregions")
@app.route("/subregions/")
def subregions_table():
	attributes = {"name" : "Name", "region" : "Region", "countries" : "Countries", "languages" : "Languages", "currencies" : "Currencies"}
	short_attributes = ["name", "region", "countries", "languages", "currencies"]
	subregions = [east_asia, north_amer, north_euro]
	return render_template('models.html', model_type = "Subregions", attributes = attributes, models = subregions, short_name = short_attributes, style = panel_styles["subregions"])

@app.route("/languages")
@app.route("/languages/")
def languages_table():
	attributes = {"name":"Name", "iso":"ISO 639-1 Code", "countries":"Countries", "regions":"Regions", "subregions":"Subregions"}
	short_attributes = ["name", "iso", "countries", "regions", "subregions"]
	languages = [chinese, english, norwegian]
	return render_template('models.html', model_type = "Languages", attributes = attributes, models = languages, short_name = short_attributes, style = panel_styles["languages"])

@app.route("/currencies")
@app.route("/currencies/")
def currencies_table():
	attributes = {"code":"Currency Code", "name":"Name", "countries":"Countries", "regions":"Regions", "subregions":"Subregions"}
	short_attributes = ["code", "name", "countries", "regions", "subregions"]
	currencies = [cny, nok, usd]
	return render_template('models.html', model_type = "Currencies", attributes = attributes, models = currencies, short_name = short_attributes, style = panel_styles["currencies"])

@app.route("/about")
def about():
	return render_template('about.html')

# Individual Pages
@app.route("/countries/<country>")
def country_page(country):
	if country == "united-states-of-america":
		languages = get_links_list(usa["languages_list"])
		currencies = get_links_list(usa["currencies_list"])
		borders = get_links_list(usa["borders_list"])
		return render_template('country.html', country = usa, languages = languages, currencies = currencies, borders = borders, panel_styles = panel_styles)
	if country == "china":
		languages = get_links_list(china["languages_list"])
		currencies = get_links_list(china["currencies_list"])
		borders = get_links_list(china["borders_list"])
		return render_template('country.html', country = china, languages = languages, currencies = currencies, borders = borders, panel_styles = panel_styles)
	if country == "norway":
		languages = get_links_list(norway["languages_list"])
		currencies = get_links_list(norway["currencies_list"])
		borders = get_links_list(norway["borders_list"])
		return render_template('country.html', country = norway, languages = languages, currencies = currencies, borders = borders, panel_styles = panel_styles)
	return render_template('nopage.html', model_title = "Country", model = "country", redirect = "countries")

@app.route("/regions/<region>")
def region_page(region):
	if region == "americas":
		subregions = get_links_list(americas["subregions_list"])
		countries = get_links_list(americas["countries_list"])
		languages = get_links_list(americas["languages_list"])
		currencies = get_links_list(americas["currencies_list"])
		return render_template('region.html', region = americas, countries = countries, subregions = subregions, \
								languages = languages, currencies = currencies, panel_styles = panel_styles)

	if region == "asia":
		subregions = get_links_list(asia["subregions_list"])
		countries = get_links_list(asia["countries_list"])
		languages = get_links_list(asia["languages_list"])
		currencies = get_links_list(asia["currencies_list"])
		return render_template('region.html', region = asia, countries = countries, subregions = subregions, \
								languages = languages, currencies = currencies, panel_styles = panel_styles)
	if region == "europe":
		subregions = get_links_list(europe["subregions_list"])
		countries = get_links_list(europe["countries_list"])
		languages = get_links_list(europe["languages_list"])
		currencies = get_links_list(europe["currencies_list"])
		return render_template('region.html', region = europe, countries = countries, subregions = subregions, \
								languages = languages, currencies = currencies, panel_styles = panel_styles)

	return render_template('nopage.html', model_title = "Region", model = "region", redirect = "regions")

@app.route("/subregions/<subregion>")
def subregion_page(subregion):
	if subregion == "eastern-asia":
		countries = get_links_list(east_asia["countries_list"])
		languages = get_links_list(east_asia["languages_list"])
		currencies = get_links_list(east_asia["currencies_list"])
		return render_template('subregion.html', subregion = east_asia, countries = countries, languages = languages, currencies = currencies, panel_styles = panel_styles)
	if subregion == "northern-america":
		countries = get_links_list(north_amer["countries_list"])
		languages = get_links_list(north_amer["languages_list"])
		currencies = get_links_list(north_amer["currencies_list"])
		return render_template('subregion.html', subregion = north_amer, countries = countries, languages = languages, currencies = currencies, panel_styles = panel_styles)
	if subregion == "northern-europe":
		countries = get_links_list(north_euro["countries_list"])
		languages = get_links_list(north_euro["languages_list"])
		currencies = get_links_list(north_euro["currencies_list"])
		return render_template('subregion.html', subregion = north_euro, countries = countries, languages = languages, currencies = currencies, panel_styles = panel_styles)

	return render_template('nopage.html', model_title = "Subregion", model = "subregion", redirect = "subregions")

@app.route("/languages/<language>")
def language_page(language):
	if language == "chinese":
		countries = get_links_list(chinese["countries_list"])
		regions = get_links_list(chinese["regions_list"])
		subregions = get_links_list(chinese["subregions_list"])
		return render_template('language.html', language = chinese, countries = countries, regions = regions, subregions = subregions, panel_styles = panel_styles)
	
	if language == "english":
		countries = get_links_list(english["countries_list"])
		regions = get_links_list(english["regions_list"])
		subregions = get_links_list(english["subregions_list"])
		return render_template('language.html', language = english, countries = countries, regions = regions, subregions = subregions, panel_styles = panel_styles)
	
	if language == "norwegian":
		countries = get_links_list(norwegian["countries_list"])
		regions = get_links_list(norwegian["regions_list"])
		subregions = get_links_list(norwegian["subregions_list"])
		return render_template('language.html', language = norwegian, countries = countries, regions = regions, subregions = subregions, panel_styles = panel_styles)

	return render_template('nopage.html', model_title = "Language", model = "language", redirect = "languages")

@app.route("/currencies/<currency>")
def currency_page(currency):
	if currency == "cny":
		countries = get_links_list(cny["countries_list"])
		regions = get_links_list(cny["regions_list"])
		subregions = get_links_list(cny["subregions_list"])
		return render_template('currency.html', currency = cny, countries = countries, regions = regions, subregions = subregions, panel_styles = panel_styles)
	
	if currency == "nok":
		countries = get_links_list(nok["countries_list"])
		regions = get_links_list(nok["regions_list"])
		subregions = get_links_list(nok["subregions_list"])
		return render_template('currency.html', currency = nok, countries = countries, regions = regions, subregions = subregions, panel_styles = panel_styles)
	
	if currency == "usd":
		countries = get_links_list(usd["countries_list"])
		regions = get_links_list(usd["regions_list"])
		subregions = get_links_list(usd["subregions_list"])
		return render_template('currency.html', currency = usd, countries = countries, regions = regions, subregions = subregions, panel_styles = panel_styles)

	return render_template('nopage.html', model_title = "Currency", model = "currency", redirect = "currencies")

Link = namedtuple('Link', ['name', 'link'])
def get_links_list(list):
	return map(lambda s: Link(s, get_link(s)), list)

def get_link(s):
	return s.replace(" ", "-").lower()
app.jinja_env.globals.update(get_link=get_link)


if __name__ == "__main__":
    app.run(debug=True)