#!/usr/bin/env python3

from io			import StringIO
from unittest 	import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import db, Base, Countries, Languages, Currencies, Borders, Regions, SubRegions

class ModelsTest(TestCase) :

	# ---------------
    # Countries Test
    # ---------------

    def test_countries_blank(self):
        country = Countries()

        db.session.add(country)
        db.session.commit()

        c = db.session.query(Countries).filter_by(name=None).first()

        self.assertEqual(c.name, None)
        self.assertEqual(c.capital, None)
        self.assertEqual(c.population, None)
        self.assertEqual(c.lat, None)
        self.assertEqual(c.lng, None)

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

    	c = db.session.query(Countries).filter_by(name='United States of America').first()

    	self.assertEqual(c.name, 'United States of America')
    	self.assertEqual(c.capital, 'Austin')
    	self.assertEqual(c.lat, 38)
    	self.assertEqual(c.lng, -97)
    	self.assertEqual(c.area, 9629091)
    	self.assertEqual(c.population, 321645000)

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

    	c = db.session.query(Countries).filter_by(name='Afghanistan').first()

    	self.assertEqual(c.name, 'Afghanistan')
    	self.assertEqual(c.capital, 'Kabul')
    	self.assertEqual(c.lat, 33)
    	self.assertEqual(c.lng, 65)
    	self.assertEqual(c.area, 652230)
    	self.assertEqual(c.population, 26023100)

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

    	c = db.session.query(Countries).filter_by(name='Albania').first()

    	self.assertEqual(c.name, 'Albania')
    	self.assertEqual(c.capital, 'Tirana')
    	self.assertEqual(c.lat, 41)
    	self.assertEqual(c.lng, 20)
    	self.assertEqual(c.area, 28748)
    	self.assertEqual(c.population, 2893005)


    # ---------------
    # Languages Test
    # ---------------

    def test_languages_blank(self):

    	language = Languages()	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).filter_by(name=None).first()

    	self.assertEqual(l.name, None)
    	self.assertEqual(l.iso_code, None)

    def test_languages_1(self):

    	language = Languages(
    		name='English',
    		iso_code='en'
    	)	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).filter_by(name='English').first()

    	self.assertEqual(l.name, 'English')
    	self.assertEqual(l.iso_code, 'en')

    def test_languages_2(self):

    	language = Languages(
    		name='Chinese',
    		iso_code='zh'
    	)	

    	db.session.add(language)
    	db.session.commit()

    	l = db.session.query(Languages).filter_by(name='Chinese').first()

    	self.assertEqual(l.name, 'Chinese')
    	self.assertEqual(l.iso_code, 'zh')


    # ---------------
    # Currencies Test
    # ---------------

    def test_currencies_blank(self):

    	currency = Currencies()

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).filter_by(name=None).first()

    	self.assertEqual(c.name, None)
    	self.assertEqual(c.code, None)

    def test_currencies_1(self):

    	currency = Currencies(
    		name='US Dollar',
    		code='USD'
    	)

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).filter_by(name='US Dollar').first()
    	
    	self.assertEqual(c.name, 'US Dollar')
    	self.assertEqual(c.code, 'USD')

    def test_currencies_2(self):

    	currency = Currencies(
    		name='Yuan Renminbi',
    		code='CNY'
    	)

    	db.session.add(currency)
    	db.session.commit()

    	c = db.session.query(Currencies).filter_by(name='Yuan Renminbi').first()

    	self.assertEqual(c.name, 'Yuan Renminbi')
    	self.assertEqual(c.code, 'CNY')


    # ---------------
    # Borders Test
    # ---------------

    def test_borders_blank(self):

    	border = Borders()

    	db.session.add(border)
    	db.session.commit()

    	b = db.session.query(Borders).filter_by(name=None).first()

    	self.assertEqual(b.name, None)

    def test_borders_1(self):

    	border = Borders(
    		name='CAN'
    	)

    	db.session.add(border)
    	db.session.commit()

    	b = db.session.query(Borders).filter_by(name='CAN').first()

    	self.assertEqual(b.name, 'CAN')

    def test_borders_2(self):

    	border = Borders(
    		name='MEX'
    	)

    	db.session.add(border)
    	db.session.commit()

    	b = db.session.query(Borders).filter_by(name='MEX').first()

    	self.assertEqual(b.name, 'MEX')


    # ---------------
    # Regions Test
    # --------------

    def test_regions_blank(self):

    	region = Regions()

    	db.session.add(region)
    	db.session.commit()

    	r = db.session.query(Regions).filter_by(name=None).first()

    	self.assertEqual(r.name, None)

    def test_regions_1(self):

    	region = Regions(
    		name='Americas'
    	)

    	db.session.add(region)
    	db.session.commit()

    	r = db.session.query(Regions).filter_by(name='Americas').first()

    	self.assertEqual(r.name, 'Americas')

    def test_regions_2(self):

    	region = Regions(
    		name='Europe'
    	)

    	db.session.add(region)
    	db.session.commit()

    	r = db.session.query(Regions).filter_by(name='Europe').first()

    	self.assertEqual(r.name, 'Europe')


    # ---------------
    # SubRegions Test
    # --------------

    def test_subregions_blank(self):
    	subregion = SubRegions()

    	db.session.add(subregion)
    	db.session.commit()

    	sr = db.session.query(SubRegions).filter_by(name=None).first()

    	self.assertEqual(sr.name, None)

    def test_subregions_1(self):
    	subregion = SubRegions(
    		name='Southern Europe'
    	)

    	db.session.add(subregion)
    	db.session.commit()

    	sr = db.session.query(SubRegions).filter_by(name='Southern Europe').first()

    	self.assertEqual(sr.name, 'Southern Europe')    	

    def test_subregions_2(self):
    	subregion = SubRegions(
    		name='Northern Africa'
    	)

    	db.session.add(subregion)
    	db.session.commit()

    	sr = db.session.query(SubRegions).filter_by(name='Northern Africa').first()

    	self.assertEqual(sr.name, 'Northern Africa')

if __name__ == "__main__" :
	main()
