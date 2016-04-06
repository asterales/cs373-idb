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

populate_languages()
populate_countries()

#note: add currencies
#note: account for countries with non-standard characters in names

