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
    		lat=38,
    		lng=-97,
    		region_id=1,
    		subregion_id=4,
    		area=9629091,
    		population=321645000
    	)

    	db.session.add(country)
    	db.session.commit()

    	c = db.session.query(Country).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == 'United States of America'
    	assert c.capital == 'Austin'
    	assert c.lat == 38
    	assert c.lng == -97
    	assert c.region_id == 1
    	assert c.subregion_id == 4
    	assert c.area == 9629091 
    	assert c.population == 321645000

    def test_countries_2(self) :

    	country = Countries(
    		id=1,
    		name='Afghanistan',
    		capital='Kabul',
    		lat=33,
    		lng=65,
    		region_id=2,
    		subregion_id=3,
    		area=652230,
    		population=26023100
    	)

    	db.session.add(country)
    	db.session.commit()

    	c = db.session.query(Country).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == 'Afghanistan'
    	assert c.capital == 'Kabul'
    	assert c.lat == 33
    	assert c.lng == 65
    	assert c.region_id == 2
    	assert c.subregion_id == 3
    	assert c.area == 652230
    	assert c.population == 26023100

    def test_countries_3(self):

    	country = Countries(
    		id=1,
    		name='Albania',
    		capital='Tirana',
    		lat=41,
    		lng=20,
    		region_id=3,
    		subregion_id=6,
    		area=28748,
    		population=2893005
    	)

    	db.session.add(country)
    	db.session.commit()

    	c = db.session.query(Countries).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == 'Albania'
    	assert c.capital == 'Tirana'
    	assert c.lat == 41
    	assert c.lng == 20
    	assert c.region_id == 3
    	assert c.subregion_id == 6
    	assert c.area == 28748
    	assert c.population == 2893005


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
    	assert l.iso_code == None

    def test_languages_1(self):

    	language = Languages(
    		id=1,
    		name='English',
    		iso_code='en'
    	)	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).filter_by(id=1).first()

    	assert l.id == 1
    	assert l.name == 'English'
    	assert l.iso_code == 'en'

    def test_languages_2(self):

    	language = Languages(
    		id=1,
    		name='Chinese',
    		iso_code='zh'
    	)	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).filter_by(id=1).first()

    	assert l.id == 1
    	assert l.name == 'Chinese'
    	assert l.iso_code == 'zh'


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
    	assert c.code == None

    def test_currencies_1(self):

    	currency = Currencies(
    		id=1,
    		name='US Dollar',
    		code='USD'
    	)

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == 'US Dollar'
    	assert c.code == 'USD'

    def test_currencies_2(self):

    	currency = Currencies(
    		id=1,
    		name='Yuan Renminbi',
    		code='CNY'
    	)

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).filter_by(id=1).first()

    	assert c.id == 1
    	assert c.name == 'Yuan Renminbi'
    	assert c.code == 'CNY'


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


    # ---------------
    # SubRegions Test
    # --------------

    def test_subregions_blank(self):
    	subregion = SubRegions(
    		id=1
    	)

    	db.session.add(subregion)
    	db.session.commit()

    	r = db.session.query(SubRegions).filter_by(id=1).first()

    	assert r.id == 1
    	assert r.name == None

    def test_subregions_1(self):
    	subregion = SubRegions(
    		id=2,
    		name='Southern Europe'
    	)

    	db.session.add(subregion)
    	db.session.commit()

    	r = db.session.query(SubRegions).filter_by(id=2).first()

    	assert r.id == 2
    	assert r.name == 'Southern Europe'

    def test_subregions_2(self):
    	subregion = SubRegions(
    		id=1,
    		name='Northern Africa'
    	)

    	db.session.add(subregion)
    	db.session.commit()

    	r = db.session.query(SubRegions).filter_by(id=1).first()

    	assert r.id == 1
    	assert r.name == 'Southern Africa'

if __name__ == "__main__" :
	main()
