#!/usr/bin/env python3

import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#junction tables
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
class Countries(Base): #name, capital, region, population, latlng, Borders, currency, Languages
	__tablename__ = 'Countries'

	id = Column(Integer, primary_key=True)
	name = Column(String(255)) #nullable=False
	capital = Column(String(255)) #nullable=False
	population = Column(Integer)
	lat = Column(Integer)
	lng = Column(Integer)
	region_id = Column(Integer, ForeignKey('Regions.id'))

	#one-to-many relationship 
	region = relationship('Regions')

	#many-to-many relationships
	Languages = relationship("Languages", secondary=country_language, backref='Countries')
	Currencies = relationship("Currencies", secondary=country_currency, backref='Countries')
	Borders = relationship("Borders", secondary=country_border, backref='Countries')

class Languages(Base):
	__tablename__ = 'Languages'

	id = Column(Integer, primary_key=True)
	name = Column(String(255)) #nullable=False

	#many-to-many relationships
	Countries = relationship('Countries', secondary=country_language, backref='Languages')

class Currencies(Base):
	__tablename__ = 'Currencies'

	id = Column(Integer, primary_key=True)
	name = Column(String(255)) #nullable=False

	#many-to-many relationships
	Countries = relationship('Countries', secondary=country_currency, backref='Currencies')

class Borders(Base):
	__tablename__ = 'Borders'

	id = Column(Integer, primary_key=True)
	name = Column(String(255)) #nullable=False

	#many-to-many relationships
	Countries = relationship('Countries', secondary=country_border, backref='Borders')

class Regions(Base): 
	__tablename__ = 'Regions'

	id = Column(Integer, primary_key=True)
	name = Column(String(255)) #nullable=False


###connects to a database that has already been created

###                             user:pass@server/database_name
#engine = create_engine('mysql://root:root@localhost/SWEography')

###creates all tables in database 
#Base.metadata.create_all(engine)