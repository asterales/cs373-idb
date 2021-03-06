#!/usr/bin/env python3

import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

"""
Junction tables to show the relationship between countries and their
respective languages, currencies, and borders
Attributes:
	Foreign keys to the country id and the language, currency, or border id
"""

country_language = Table('country_language', Base.metadata,
	Column('id', Integer, primary_key=True),
	Column('country_id', Integer, ForeignKey('Countries.id')),
	Column('language_id', Integer, ForeignKey('Languages.id'))
)

country_currency = Table('country_currency', Base.metadata,
	Column('id', Integer, primary_key=True),
	Column('country_id', Integer, ForeignKey('Countries.id')),
	Column('currency_id', Integer, ForeignKey('Currencies.id'))
)

country_border = Table('country_border', Base.metadata,
	Column('id', Integer, primary_key=True),
	Column('country_id', Integer, ForeignKey('Countries.id')),
	Column('border_id', Integer, ForeignKey('Borders.id'))
)

#database tables
class Countries(Base):
	"""
	Countries Model: contains information about different countries
	Attributes:
		id - Unique id of a country
		name - Name of the country
		capital - Capital of the country
		lat, lng - Latitude and Longitude of the country
		region_id - Id of the region the country is in
		subregion_id - Id of the subregion the country is in
		area - Area of the country in squared kilometers
		population - Population of country
	"""

	__tablename__ = 'Countries'

	id = Column(Integer, primary_key=True)
	name = Column(String(255)) #nullable=False
	capital = Column(String(255)) #nullable=False
	lat = Column(Integer)
	lng = Column(Integer)
	region_id = Column(Integer, ForeignKey('Regions.id'))
	subregion_id = Column(Integer, ForeignKey('SubRegions.id'))
	area = Column(Integer)
	population = Column(Integer)

	#one-to-many relationship
	region = relationship('Regions')
	subregion = relationship('SubRegions')

	#many-to-many relationships
	Languages = relationship("Languages", secondary=country_language, backref='Countries')
	Currencies = relationship("Currencies", secondary=country_currency, backref='Countries')
	Borders = relationship("Borders", secondary=country_border, backref='Countries')

class Languages(Base):
	"""
	Languages Model: contains all languages used in the countries in the Countires Model
	Attributes:
		id - Unique id of the language
		name - Name of the language
		iso_code - The ISO 639-1 code for the language
	"""

	__tablename__ = 'Languages'

	id = Column(Integer, primary_key=True)
	name = Column(String(255)) #nullable=False
	iso_code = Column(String(255))

	#many-to-many relationships
	Countries = relationship('Countries', secondary=country_language, backref='Languages')

class Currencies(Base):
	"""
	Currencies Model: contains the different currencies used in the countries in the Countries Model
	Attributes:
		id - Unique id of the currency
		name - Name of the currency
		code - The currency code
	"""

	__tablename__ = 'Currencies'

	id = Column(Integer, primary_key=True)
	name = Column(String(255)) #nullable=False
	code = Column(String(255))

	#many-to-many relationships
	Countries = relationship('Countries', secondary=country_currency, backref='Currencies')

class Borders(Base):
	"""
	Borders Model: Contains all country borders that border the countries in the Countries Model
	Attributes:
		id - Unique id of the border
		name - Name of the border
	"""

	__tablename__ = 'Borders'

	id = Column(Integer, primary_key=True)
	name = Column(String(255)) #nullable=False

	#many-to-many relationships
	Countries = relationship('Countries', secondary=country_border, backref='Borders')

class Regions(Base):
	"""
	Regions Model: contains all regions that the countries in the Countries Model are apart of
	Attributes:
		id - Unique id of the region
		name - Name of the region
	"""

	__tablename__ = 'Regions'

	id = Column(Integer, primary_key=True)
	name = Column(String(255)) #nullable=False
	#num_subregions = Column(Integer)

class SubRegions(Base):
	"""
	SubRegions Model: contains all of the subregions of regions that the countries in the Countries Model are apart of
	Attributes:
		id - Unique id of the subregion
		name - Name of the subregion
	"""

	__tablename__ = 'SubRegions'

	id = Column(Integer, primary_key=True)
	name = Column(String(255))
	#parent_region = Column(String(255))

###connects to a database that has already been created

###                             user:pass@server/database_name
#engine = create_engine('mysql://root:root@localhost/SWEography')

###creates all tables in database
#Base.metadata.create_all(engine)