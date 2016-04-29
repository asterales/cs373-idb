#!/usr/bin/env python3

import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database, drop_database


SQLALCHEMY_DATABASE_URI = \
    '{engine}://{username}:{password}@{hostname}/{database}'.format(
        engine='mysql+pymysql',
        username=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        hostname=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## our models will extend base model
class Base(object):
    def toJSON(self):
        json_exclude = getattr(self, '__json_exclude__', set())
        return {key: value for key, value in self.__dict__.items()
                # Do not serialize 'private' attributes
                # (SQLAlchemy-internal attributes are among those, too)
                if not key.startswith('_')
                and key not in json_exclude}

Base = declarative_base(cls=Base)

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
	lat = Column(Float)
	lng = Column(Float)
	region_id = Column(Integer, ForeignKey('Regions.id'))
	subregion_id = Column(Integer, ForeignKey('SubRegions.id'))
	area = Column(Integer)
	population = Column(Integer)

	#one-to-many relationship
	region = relationship('Regions', backref="RegionsCountries")
	subregion = relationship('SubRegions', backref="SubRegionsCountries")

	#many-to-many relationships
	Languages = relationship("Languages", secondary=country_language, backref='LanguagesCountries')
	Currencies = relationship("Currencies", secondary=country_currency, backref='CurrenciesCountries')
	Borders = relationship("Borders", secondary=country_border, backref='BordersCountries')

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
	Countries = relationship('Countries', secondary=country_language, backref='Languages_')

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
    unicode = Column(String(255))

    #many-to-many relationships
    Countries = relationship('Countries', secondary=country_currency, backref='Currencies_')

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
	Countries = relationship('Countries', secondary=country_border, backref='Borders_')

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
def create_sweography_db():

    engine = create_engine(SQLALCHEMY_DATABASE_URI)

    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)

    ##creates all tables in database
    Base.metadata.create_all(engine)

# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/countries'

# use this for local host only
if "TRAVIS" in os.environ:
	app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/myapp_test'
	create_sweography_db();

