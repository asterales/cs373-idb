#!/usr/bin/env python3

import json, requests
from lang_codes import lang_codes

api_url = "https://restcountries.eu/rest/v1/all"
countries_list = []
languages_list = []

def parse_country_codes():
	resp = requests.get(api_url)
	d = {}
	for country in resp.json():
		d[country["alpha3Code"]] = country["name"]
	return d

def parse_countries():
	country_codes = parse_country_codes()
	attr = ["name", "capital", "area", "population", "languages", "currencies"]
	nullable_attr = ["region", "subregion"]
	resp = requests.get(api_url)
	for country in resp.json():
		d = {a : country[a] for a in attr}
		for na in nullable_attr:
			d[na] = country[na] if country[na] else "Unassigned"
		if country["latlng"]:
			d["lat"] = country["latlng"][0]
			d["lng"] = country["latlng"][1]
		else:
			d["lat"] = d["lng"] = None
		d["borders"] = [ country_codes[code] for code in country["borders"] if code in country_codes ]
		countries_list.append(d)

def parse_languages():
	if not countries_list:
		parse_countries()
	lang_code_set = set()
	for country in countries_list:
		lang_code_set.update(country["languages"])
	for code in lang_code_set:
		languages_list.append({"name" : lang_codes[code], "iso_code" : code})

def write_json(filename, list_data):
	w = open(filename, "w")
	w.write(json.dumps(list_data, ensure_ascii=False, indent=4))
	w.close()

if __name__ == "__main__":
	parse_countries()
	write_json("countries.json", countries_list)
	
	parse_languages()
	write_json("languages.json", languages_list)




