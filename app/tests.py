#!/usr/bin/env python3

from io			import StringIO
from unittest 	import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.request import urlopen

from models import db, Base, Countries, Languages, Currencies, Borders, Regions, SubRegions

import json

class ModelsTest(TestCase) :

	# ---------------
    # Countries Test
    # ---------------

    def test_countries_blank(self):
        country = Countries()

        db.session.add(country)
        db.session.commit()

        c = db.session.query(Countries).get(country.id)
        self.assertEqual(c.name, None)
        self.assertEqual(c.capital, None)
        self.assertEqual(c.population, None)
        self.assertEqual(c.lat, None)
        self.assertEqual(c.lng, None)

        db.session.delete(country)
        db.session.commit()

    def test_countries_1(self):

    	country = Countries(
    		name='United States of America',
    		capital='Austin',
    		lat=38,
    		lng=-97,
    		area=9629091,
    		population=321645000
    	)

    	db.session.add(country)
    	db.session.commit()

    	c = db.session.query(Countries).get(country.id)

    	self.assertEqual(c.name, 'United States of America')
    	self.assertEqual(c.capital, 'Austin')
    	self.assertEqual(c.lat, 38)
    	self.assertEqual(c.lng, -97)
    	self.assertEqual(c.area, 9629091)
    	self.assertEqual(c.population, 321645000)

    	db.session.delete(country)
    	db.session.commit()

    def test_countries_2(self) :

    	country = Countries(
    		name='Afghanistan',
    		capital='Kabul',
    		lat=33,
    		lng=65,
    		area=652230,
    		population=26023100
    	)

    	db.session.add(country)
    	db.session.commit()

    	c = db.session.query(Countries).get(country.id)

    	self.assertEqual(c.name, 'Afghanistan')
    	self.assertEqual(c.capital, 'Kabul')
    	self.assertEqual(c.lat, 33)
    	self.assertEqual(c.lng, 65)
    	self.assertEqual(c.area, 652230)
    	self.assertEqual(c.population, 26023100)

    	db.session.delete(country)
    	db.session.commit()

    def test_countries_3(self):

    	country = Countries(
    		name='Albania',
    		capital='Tirana',
    		lat=41,
    		lng=20,
    		area=28748,
    		population=2893005
    	)

    	db.session.add(country)
    	db.session.commit()

    	c = db.session.query(Countries).get(country.id)

    	self.assertEqual(c.name, 'Albania')
    	self.assertEqual(c.capital, 'Tirana')
    	self.assertEqual(c.lat, 41)
    	self.assertEqual(c.lng, 20)
    	self.assertEqual(c.area, 28748)
    	self.assertEqual(c.population, 2893005)

    	db.session.delete(country)
    	db.session.commit()


    # ---------------
    # Languages Test
    # ---------------

    def test_languages_blank(self):

    	language = Languages()	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).get(language.id)
    	self.assertEqual(l.name, None)
    	self.assertEqual(l.iso_code, None)

    	db.session.delete(language)
    	db.session.commit()

    def test_languages_1(self):

    	language = Languages(
    		name='English',
    		iso_code='en'
    	)	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).get(language.id)

    	self.assertEqual(l.name, 'English')
    	self.assertEqual(l.iso_code, 'en')

    	db.session.delete(language)
    	db.session.commit()

    def test_languages_2(self):

    	language = Languages(
    		name='Chinese',
    		iso_code='zh'
    	)	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).get(language.id)

    	self.assertEqual(l.name, 'Chinese')
    	self.assertEqual(l.iso_code, 'zh')

    	db.session.delete(language)
    	db.session.commit()


    # ---------------
    # Currencies Test
    # ---------------

    def test_currencies_blank(self):

    	currency = Currencies()

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).get(currency.id)
    	self.assertEqual(c.name, None)
    	self.assertEqual(c.code, None)

    	db.session.delete(currency)
    	db.session.commit()

    def test_currencies_1(self):

    	currency = Currencies(
    		name='US Dollar',
    		code='USD'
    	)

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).get(currency.id)
    	
    	self.assertEqual(c.name, 'US Dollar')
    	self.assertEqual(c.code, 'USD')

    	db.session.delete(currency)
    	db.session.commit()

    def test_currencies_2(self):

    	currency = Currencies(
    		name='Yuan Renminbi',
    		code='CNY'
    	)

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).get(currency.id)

    	self.assertEqual(c.name, 'Yuan Renminbi')
    	self.assertEqual(c.code, 'CNY')

    	db.session.delete(currency)
    	db.session.commit()


    # ---------------
    # Borders Test
    # ---------------

    def test_borders_blank(self):

    	border = Borders()

    	db.session.add(border)
    	db.session.commit()

    	b = db.session.query(Borders).get(border.id)
    	self.assertEqual(b.name, None)

    	db.session.delete(border)
    	db.session.commit()

    def test_borders_1(self):

    	border = Borders(
    		name='CAN'
    	)

    	db.session.add(border)
    	db.session.commit()

    	b = db.session.query(Borders).get(border.id)

    	self.assertEqual(b.name, 'CAN')

    	db.session.delete(border)
    	db.session.commit()

    def test_borders_2(self):

    	border = Borders(
    		name='MEX'
    	)

    	db.session.add(border)
    	db.session.commit()

    	b = db.session.query(Borders).get(border.id)

    	self.assertEqual(b.name, 'MEX')

    	db.session.delete(border)
    	db.session.commit()


    # ---------------
    # Regions Test
    # ---------------

    def test_regions_blank(self):

    	region = Regions()

    	db.session.add(region)
    	db.session.commit()

    	r = db.session.query(Regions).get(region.id)
    	self.assertEqual(r.name, None)

    	db.session.delete(region)
    	db.session.commit()

    def test_regions_1(self):

    	region = Regions(
    		name='Americas'
    	)

    	db.session.add(region)
    	db.session.commit()

    	r = db.session.query(Regions).get(region.id)

    	self.assertEqual(r.name, 'Americas')

    	db.session.delete(region)
    	db.session.commit()

    def test_regions_2(self):

    	region = Regions(
    		name='Europe'
    	)

    	db.session.add(region)
    	db.session.commit()

    	r = db.session.query(Regions).get(region.id)

    	self.assertEqual(r.name, 'Europe')

    	db.session.delete(region)
    	db.session.commit()


    # ---------------
    # SubRegions Test
    # ---------------

    def test_subregions_blank(self):
    	subregion = SubRegions()

    	db.session.add(subregion)
    	db.session.commit()

    	sr = db.session.query(SubRegions).get(subregion.id)
    	self.assertEqual(sr.name, None)

    	db.session.delete(subregion)
    	db.session.commit()

    def test_subregions_1(self):
    	subregion = SubRegions(
    		name='Southern Europe'
    	)

    	db.session.add(subregion)
    	db.session.commit()

    	sr = db.session.query(SubRegions).get(subregion.id)

    	self.assertEqual(sr.name, 'Southern Europe')    	

    	db.session.delete(subregion)
    	db.session.commit()

    def test_subregions_2(self):
    	subregion = SubRegions(
    		name='Northern Africa'
    	)

    	db.session.add(subregion)
    	db.session.commit()

    	sr = db.session.query(SubRegions).get(subregion.id)

    	self.assertEqual(sr.name, 'Northern Africa')

    	db.session.delete(subregion)
    	db.session.commit()


# class APITests(TestCase):

# 	# --------------------
#     # Country API GET Test
#     # --------------------

# 	def test_api_get_country_1(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/country/1')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Afghanistan')
# 		self.assertEqual(jsonResponse['region'], 'Asia')
# 		self.assertEqual(jsonResponse['subregion'], 'Southern Asia')
# 		self.assertEqual(jsonResponse['capital'], 'Kabul')
# 		self.assertEqual(len(jsonResponse['borders']), 6)
# 		self.assertEqual(jsonResponse['currencies'][0]['code'], 'AFN')

# 	def test_api_get_country_2(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/country/10')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Argentina')
# 		self.assertEqual(jsonResponse['region'], 'Americas')
# 		self.assertEqual(jsonResponse['subregion'], 'South America')
# 		self.assertEqual(jsonResponse['capital'], 'Buenos Aires')
# 		self.assertEqual(len(jsonResponse['borders']), 5)
# 		self.assertEqual(jsonResponse['currencies'][0]['code'], 'ARS')

# 	def test_api_get_country_3(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/country/225')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Tokelau')
# 		self.assertEqual(jsonResponse['region'], 'Oceania')
# 		self.assertEqual(jsonResponse['subregion'], 'Polynesia')
# 		self.assertEqual(jsonResponse['capital'], 'Fakaofo')
# 		self.assertEqual(len(jsonResponse['borders']), 0)
# 		self.assertEqual(jsonResponse['currencies'][0]['code'], 'NZD')

# 	# -------------------
#     # Region API GET Test
#     # -------------------

# 	def test_api_get_region_1(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/region/5')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Americas')
# 		self.assertEqual(jsonResponse['languages'], 11)
# 		self.assertEqual(jsonResponse['subregions'], 4)
# 		self.assertEqual(jsonResponse['currencies'], 40)
# 		self.assertEqual(jsonResponse['countries'], 56)

# 	def test_api_get_region_2(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/region/4')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Oceania')
# 		self.assertEqual(jsonResponse['languages'], 13)
# 		self.assertEqual(jsonResponse['subregions'], 4)
# 		self.assertEqual(jsonResponse['currencies'], 10)
# 		self.assertEqual(jsonResponse['countries'], 27)

# 	def test_api_get_region_3(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/region/1')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Asia')
# 		self.assertEqual(jsonResponse['languages'], 37)
# 		self.assertEqual(jsonResponse['subregions'], 5)
# 		self.assertEqual(jsonResponse['currencies'], 49)
# 		self.assertEqual(jsonResponse['countries'], 50)

# 	# ----------------------
#     # Subregion API GET Test
#     # ----------------------

# 	def test_api_get_subregion_1(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/subregion/10')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Australia and New Zealand')
# 		self.assertEqual(jsonResponse['languages'], 2)
# 		self.assertEqual(jsonResponse['region'], 'Oceania')
# 		self.assertEqual(jsonResponse['currencies'], 2)
# 		self.assertEqual(jsonResponse['countries'], 5)

# 	def test_api_get_subregion_2(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/subregion/20')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Eastern Asia')
# 		self.assertEqual(jsonResponse['languages'], 6)
# 		self.assertEqual(jsonResponse['region'], 'Asia')
# 		self.assertEqual(jsonResponse['currencies'], 8)
# 		self.assertEqual(jsonResponse['countries'], 8)

# 	def test_api_get_subregion_3(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/subregion/7')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Caribbean')
# 		self.assertEqual(jsonResponse['languages'], 6)
# 		self.assertEqual(jsonResponse['region'], 'Americas')
# 		self.assertEqual(jsonResponse['currencies'], 14)
# 		self.assertEqual(jsonResponse['countries'], 27)

# 	# ---------------------
#     # Language API GET Test
#     # ---------------------

# 	def test_api_get_languages_1(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/language/3')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Samoan')
# 		self.assertEqual(jsonResponse['iso_code'], 'sm')
# 		self.assertEqual(jsonResponse['regions'], 1)
# 		self.assertEqual(jsonResponse['subregions'], 1)
# 		self.assertEqual(jsonResponse['countries'], 2)

# 	def test_api_get_languages_2(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/language/50')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Luxembourgish')
# 		self.assertEqual(jsonResponse['iso_code'], 'lb')
# 		self.assertEqual(jsonResponse['regions'], 1)
# 		self.assertEqual(jsonResponse['subregions'], 1)
# 		self.assertEqual(jsonResponse['countries'], 1)

# 	def test_api_get_languages_3(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/language/29')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Afrikaans')
# 		self.assertEqual(jsonResponse['iso_code'], 'af')
# 		self.assertEqual(jsonResponse['regions'], 1)
# 		self.assertEqual(jsonResponse['subregions'], 1)
# 		self.assertEqual(jsonResponse['countries'], 2)

# 	# ---------------------
#     # Currency API GET Test
#     # ---------------------

# 	def test_api_get_currencies_1(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/currency/11')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Bermuda Dollar')
# 		self.assertEqual(jsonResponse['code'], 'BMD')
# 		self.assertEqual(jsonResponse['regions'], 1)
# 		self.assertEqual(jsonResponse['subregions'], 1)
# 		self.assertEqual(jsonResponse['countries'], 1)

# 	def test_api_get_currencies_2(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/currency/21')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Chile Peso')
# 		self.assertEqual(jsonResponse['code'], 'CLP')
# 		self.assertEqual(jsonResponse['regions'], 1)
# 		self.assertEqual(jsonResponse['subregions'], 1)
# 		self.assertEqual(jsonResponse['countries'], 1)

# 	def test_api_get_currencies_3(self):
# 		apiResponse = urlopen('http://sweography.me/api/v1/currency/100')
# 		apiResponseInfo = apiResponse.info()
# 		apiResponseRaw = apiResponse.read().decode(apiResponseInfo.get_content_charset('utf8'))
# 		jsonResponse = json.loads(apiResponseRaw)

# 		self.assertEqual(jsonResponse['name'], 'Trinidad and Tobago Dollar')
# 		self.assertEqual(jsonResponse['code'], 'TTD')
# 		self.assertEqual(jsonResponse['regions'], 1)
# 		self.assertEqual(jsonResponse['subregions'], 1)
# 		self.assertEqual(jsonResponse['countries'], 1)


	# --------------------
    # API POST/DELETE Test
    # --------------------

    #def test_api_post_delete_1(self):




if __name__ == "__main__" :
	main()
