#!/usr/bin/env python3

from io			import StringIO
from unittest 	import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Countries, Languages, Currencies, Borders, Regions

class ModelsTest(TestCase) :

	# ---------------
    # Countries Test
    # ---------------

    def test_countries_blank(self):
    	
    	country = Countries(
    		id=1
    	)

    	db.session.add(country)
    	db.session.commit()

    	c = db.session.query(Country).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == None
    	assert c.capital == None
    	assert c.population == None
    	assert c.lat == None
    	assert c.lng == None
    	assert c.region_id == None

    def test_countries_1(self):

    	country = Countries(
    		id=1,
    		name='United States of America',
    		capital='Austin',
    		population=321645000,
    		lat=38,
    		lng=-97,
    		region_id=1
    	)

    	db.session.add(country)
    	db.session.commit()

    	c = db.session.query(Country).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == 'United States of America'
    	assert c.capital == 'Austin'
    	assert c.population == 321645000
    	assert c.lat == 38
    	assert c.lng == -97
    	assert c.region_id == 1

    def test_countries_2(self) :

    	country = Countries(
    		id=1,
    		name='Afghanistan',
    		capital='Kabul',
    		population=26023100,
    		lat=33,
    		lng=65,
    		region_id=2
    	)

    	db.session.add(country)
    	db.session.commit()

    	c = db.session.query(Country).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == 'Afghanistan'
    	assert c.capital == 'Kabul'
    	assert c.population == 26023100
    	assert c.lat == 33
    	assert c.lng == 65
    	assert c.region_id == 2

    def test_countries_3(self):

    	country = Countries(
    		id=1,
    		name='Albania',
    		capital='Tirana',
    		population=2893005,
    		lat=41,
    		lng=20,
    		region_id=3
    	)

    	db.session.add(country)
    	db.session.commit()

    	c = db.session.query(Countries).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == 'Albania'
    	assert c.capital == 'Tirana'
    	assert c.population == 2893005
    	assert c.lat == 41
    	assert c.lng == 20
    	assert c.region_id == 3


    # ---------------
    # Languages Test
    # ---------------

    def test_languages_blank(self):

    	language = Languages(
    		id=1
    	)	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).filter_by(id=1).first()

    	assert l.id == 1
    	assert l.name == None

    def test_languages_1(self):

    	language = Languages(
    		id=1,
    		name='en'
    	)	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).filter_by(id=1).first()

    	assert l.id == 1
    	assert l.name == 'en'

    def test_languages_2(self):

    	language = Languages(
    		id=1,
    		name='ps'
    	)	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).filter_by(id=1).first()

    	assert l.id == 1
    	assert l.name == 'ps'


    # ---------------
    # Currencies Test
    # ---------------

    def test_currencies_blank(self):

    	currency = Currencies(
    		id=1
    	)

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == None

    def test_currencies_1(self):

    	currency = Currencies(
    		id=1,
    		name='USD'
    	)

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == 'USD'

    def test_currencies_2(self):

    	currency = Currencies(
    		id=1,
    		name='USN'
    	)

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == 'USN'


    # ---------------
    # Borders Test
    # ---------------

    def test_borders_blank(self):

    	border = Borders(
    		id=1
    	)

    	db.session.add(border)
    	db.session.commit()

    	b = db.session.query(Borders).filter_by(id=1).first()

    	assert b.id == 1
    	assert b.name == None

    def test_borders_1(self):

    	border = Borders(
    		id=1,
    		name='CAN'
    	)

    	db.session.add(border)
    	db.session.commit()

    	b = db.session.query(Borders).filter_by(id=1).first()

    	assert b.id == 1
    	assert b.name == 'CAN'

    def test_borders_2(self):

    	border = Borders(
    		id=1,
    		name='MEX'
    	)

    	db.session.add(border)
    	db.session.commit()

    	b = db.session.query(Borders).filter_by(id=1).first()

    	assert b.id == 1
    	assert b.name == 'MEX'


    # ---------------
    # Regions Test
    # --------------

    def test_regions_blank(self):

    	region = Regions(
    		id=1
    	)

    	db.session.add(region)
    	db.session.commit()

    	r = db.session.query(Regions).filter_by(id=1).first()

    	assert r.id == 1
    	assert r.name == None

    def test_regions_1(self):

    	region = Regions(
    		id=1,
    		name='Americas'
    	)

    	db.session.add(region)
    	db.session.commit()

    	r = db.session.query(Regions).filter_by(id=1).first()

    	assert r.id == 1
    	assert r.name == 'Americas'

	def test_regions_2(self):

    	region = Regions(
    		id=1,
    		name='Europe'
    	)

    	db.session.add(region)
    	db.session.commit()

    	r = db.session.query(Regions).filter_by(id=1).first()

    	assert r.id == 1
    	assert r.name == 'Europe'


if __name__ == "__main__" :
	main()