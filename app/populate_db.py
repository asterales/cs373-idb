#!/usr/bin/env python3

import json, api

def populate_languages():
	languages = json.load(open("data/languages.json"))
	for lang in languages:
		api.createLanguageModel(lang)

def populate_countries():
	countries = json.load(open("data/countries.json"))
	for country in countries:
		api.createCountryModel(country)

def populate_currencies():
	currencies = json.load(open("data/currency_data.json"))
	for data in currencies:
		currency = {}
		currency["name"] = data["currency_name"]
		currency["code"] = data["code"]
		currency["unicode"] = data["unicode"]
		api.createCurrencyModel(currency)

populate_languages()
populate_currencies()
populate_countries()


