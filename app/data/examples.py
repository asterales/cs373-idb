#Examples data
#countries
usa = {	"name" : "United States of America", "capital" : "Washington D.C.", "latitude" : 38, "longitude" : -97, \
		"region" : "Americas", "subregion" : "Northern America", "area" : 9629091, "population" : 321645000, \
		"languages" : 1, "currencies" : 3, "borders" : 2, \
		"languages_list" : ["English"], "currencies_list" : ["USD", "USN", "USS"], "borders_list" : ["Canada", "Mexico"]}

china = {"name" : "China", "capital" : "Beijing", "latitude" : 35, "longitude" : 105, \
		"region" : "Asia", "subregion" : "Eastern Asia", "area" : 9640011, "population" : 1371590000, \
		"languages" : 1, "currencies" : 1, "borders" : 15, \
		"languages_list" : ["Chinese"], "currencies_list" : ["CNY"], \
		"borders_list" : ["Afghanistan", "Bhutan", "Hong Kong", "India", "Kazakhstan", "Kyrgyzstan", "Laos", \
			"Macau", "Mongolia", "Myanmar", "Nepal", "North Korea", "Pakistan", "Russia", "Tajikistan", "Vietnam"]}

norway = {"name" : "Norway", "capital" : "Oslo", "latitude" : 62, "longitude" : 10, \
		"region" : "Europe", "subregion" : "Northern Europe", "area" : 323802, "population" : 5176998, \
		"languages" : 3, "currencies" : 1, "borders" : 3, \
		"languages_list" : ["Norwegian", "Norwegian Bokmal", "Norwegian Nynorsk"], "currencies_list" : ["NOK"], \
		"borders_list" : ["Finland", "Sweden", "Russia"]}


#regions
americas = {"name": "Americas", "area": 42247698, "population": 983832674, "subregions": 4, \
			"countries": 56, "languages": 11, "currencies": 43, \
			"subregions_list" : ['Caribbean', 'Central America', 'Northern America', 'South America'], \
			"countries_list" : ['Anguilla', 'Antigua and Barbuda', 'Argentina', 'Aruba', 'Barbados', 'Belize', \
				'Bermuda', 'Bolivia', 'Bonaire', 'Brazil', 'British Virgin Islands', 'Canada', 'Cayman Islands', \
				'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Curacao', 'Dominica', 'Dominican Republic', 'Ecuador', \
				'El Salvador', 'Falkland Islands', 'French Guiana', 'Greenland', 'Grenada', 'Guadeloupe', 'Guatemala', \
				'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Martinique', 'Mexico', 'Montserrat', 'Nicaragua', 'Panama', \
				'Paraguay', 'Peru', 'Puerto Rico', 'Saint Barthelemy', 'Saint Kitts and Nevis', 'Saint Lucia', \
				'Saint Martin', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Sint Maarten', \
				'South Georgia', 'Suriname', 'The Bahamas', 'Trinidad and Tobago', 'Turks and Caicos Islands', \
				'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Venezuela'], \
			"languages_list" : ['Aymara', 'Dutch', 'English', 'French', 'Guarani', 'Haitian', 'Kalaallisut', 'Panjabi', \
				'Portuguese', 'Quechua', 'Spanish'], \
			"currencies_list" : ['ANG', 'ARS', 'AWG', 'BBD', 'BMD', 'BOB', 'BOV', 'BRL', 'BSD', 'BZD', 'CAD', 'CLF', 'CLP', \
				'COP', 'CRC', 'CUC', 'CUP', 'DKK', 'DOP', 'EUR', 'FKP', 'GBP', 'GTQ', 'GYD', 'HNL', 'HTG', 'JMD', 'KYD', \
				'MXN', 'NIO', 'PAB', 'PEN', 'PYG', 'SRD', 'SVC', 'TTD', 'USD', 'USN', 'USS', 'UYI', 'UYU', 'VEF', 'XCD']}

asia = {"name": "Asia", "area": 32064971, "population": 4339964684, "subregions": 5, "countries": 50, \
		"languages": 37, "currencies": 49, \
		"subregions_list" : ['Central Asia', 'Eastern Asia', 'South-Eastern Asia', 'Southern Asia', 'Western Asia'], \
		"countries_list" : ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', \
			'China', 'East Timor', 'Georgia', 'Hong Kong', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', \
			'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Macau', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', \
			'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', \
			'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Turkey', 'Turkmenistan', \
			'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'], \
		"languages_list" : ['Arabic', 'Armenian', 'Azerbaijani', 'Bengali', 'Burmese', 'Central Khmer', 'Chinese', 'Divehi', \
			'Dzongkha', 'English', 'French', 'Georgian', 'Hebrew', 'Hindi', 'Indonesian', 'Japanese', 'Kazakh', 'Kirghiz', \
			'Korean', 'Kurdish', 'Lao', 'Malay', 'Mongolian', 'Nepali', 'Persian', 'Portuguese', 'Pushto', 'Russian', 'Sinhala', \
			'Tajik', 'Tamil', 'Thai', 'Turkish', 'Turkmen', 'Urdu', 'Uzbek', 'Vietnamese'], \
		"currencies_list" : ['AED', 'AFN', 'AMD', 'AZN', 'BDT', 'BHD', 'BND', 'BTN', 'CNY', 'GEL', 'HKD', 'IDR', 'ILS', 'INR', 'IQD', \
			'IRR', 'JOD', 'JPY', 'KGS', 'KHR', 'KPW', 'KRW', 'KWD', 'KZT', 'LAK', 'LBP', 'LKR', 'MMK', 'MNT', 'MOP', 'MVR', 'MYR', \
			'NPR', 'OMR', 'PHP', 'PKR', 'QAR', 'SAR', 'SGD', 'SYP', 'THB', 'TJS', 'TMT', 'TRY', 'TWD', 'USD', 'UZS', 'VND', 'YER']}

europe = {"name": "Europe", "area": 23138282, "population": 745355450, "subregions": 4, \
		  "countries": 52, "languages": 41, "currencies": 24, \
		  "subregions_list" : ['Eastern Europe', 'Northern Europe', 'Southern Europe', 'Western Europe'], \
		  "countries_list" : ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', \
		  	'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Faroe Islands', 'Finland', 'France', 'Germany', 'Gibraltar', \
		  	'Greece', 'Guernsey', 'Hungary', 'Iceland', 'Isle of Man', 'Italy', 'Jersey', 'Latvia', 'Liechtenstein', 'Lithuania', \
		  	'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', \
		  	'Republic of Ireland', 'Republic of Kosovo', 'Republic of Macedonia', 'Romania', 'Russia', 'San Marino', 'Serbia', \
		  	'Slovakia', 'Slovenia', 'Spain', 'Svalbard and Jan Mayen', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', \
		  	'Aland Islands'], \
		  "languages_list" : ['Albanian', 'Armenian', 'Belarusian', 'Bokmal, Norwegian', 'Bosnian', 'Bulgarian', 'Catalan', 'Croatian', \
		  	'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Faroese', 'Finnish', 'French', 'German', 'Greek, Modern (1453-)', \
		  	'Hungarian', 'Icelandic', 'Irish', 'Italian', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Maltese', 'Manx', \
		  	'Norwegian', 'Norwegian Nynorsk', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', \
		  	'Swedish', 'Turkish', 'Ukrainian'], \
		  "currencies_list" : ['ALL', 'BAM', 'BGN', 'BYR', 'CHE', 'CHF', 'CHW', 'CZK', 'DKK', 'EUR', 'GBP', 'GIP', 'HRK', 'HUF', 'ISK', 'MDL', \
		  	'MKD', 'NOK', 'PLN', 'RON', 'RSD', 'RUB', 'SEK', 'UAH']}


#subregions
east_asia = {"name" : "Eastern Asia", "region" : "Asia", "countries" : 8, "languages" : 6, "currencies" : 8, \
			 "countries_list" : ['China', 'Hong Kong', 'Japan', 'Macau', 'Mongolia', 'North Korea', 'South Korea', 'Taiwan'], \
			 "languages_list" : ['Chinese', 'English', 'Japanese', 'Korean', 'Mongolian', 'Portuguese'], \
			 "currencies_list" : ['CNY', 'HKD', 'JPY', 'KPW', 'KRW', 'MNT', 'MOP', 'TWD']}

north_amer = {"name" : "Northern America", "region" : "Americas", "countries" : 6, "languages" : 3, "currencies" : 7, \
			  "countries_list" : ['Bermuda', 'Canada', 'Greenland', 'Saint Pierre and Miquelon', 'United States', 'United States Minor Outlying Islands'], \
			 "languages_list" : ['English', 'French', 'Kalaallisut'], "currencies_list" : ['BMD', 'CAD', 'DKK', 'EUR', 'USD', 'USN', 'USS']}

north_euro = {"name" : "Northern Europe", "region" : "Europe", "countries" : 16, "languages" : 15, "currencies" : 6, \
			  "countries_list" : ['Denmark', 'Estonia', 'Faroe Islands', 'Finland', 'Guernsey', 'Iceland', 'Isle of Man', 'Jersey', 'Latvia', \
			  		'Lithuania', 'Norway', 'Republic of Ireland', 'Svalbard and Jan Mayen', 'Sweden', 'United Kingdom', 'Aland Islands'], \
			  "languages_list" : ['Bokmal, Norwegian', 'Danish', 'English', 'Estonian', 'Faroese', 'Finnish', 'French', 'Icelandic', 'Irish', \
			  		'Latvian', 'Lithuanian', 'Manx', 'Norwegian', 'Norwegian Nynorsk', 'Swedish'], \
			  "currencies_list" : ['DKK', 'EUR', 'GBP', 'ISK', 'NOK', 'SEK']}


#languages
chinese = {"name" : "Chinese", "iso_code" : "zh", "countries" : 5, "regions" : 1, "subregions": 2, \
			"subregions_list" : ['Eastern Asia', 'South-Eastern Asia'], \
			"countries_list" : ['China', 'Hong Kong', 'Macau', 'Singapore', 'Taiwan'], "regions_list" : ['Asia'], \
			"coords" : [(23.5, 121.0), (22.16666666, 113.55), (35.0, 105.0), (22.25, 114.16666666), (1.36666666, 103.8)]}

english = {"name" : "English", "iso_code" : "en", "countries" : 89, "regions" : 15, "subregions": 18, \
		   "subregions_list" : ['Australia and New Zealand', 'Caribbean', 'Central America', 'Eastern Africa', \
		   		'Eastern Asia', 'Melanesia', 'Micronesia', 'Middle Africa', 'Northern Africa', 'Northern America', \
		   		'Northern Europe', 'Polynesia', 'South America', 'South-Eastern Asia', 'Southern Africa', 'Southern Asia', \
		   		'Southern Europe', 'Western Africa'], \
		   	"countries_list" : ['American Samoa', 'Anguilla', 'Antigua and Barbuda', 'Australia', 'Barbados', 'Belize', 'Bermuda', \
		   		'Botswana', 'British Indian Ocean Territory', 'British Virgin Islands', 'Cameroon', 'Canada', 'Cayman Islands', \
		   		'Christmas Island', 'Cocos (Keeling) Islands', 'Cook Islands', 'Curacao', 'Dominica', 'Eritrea', 'Falkland Islands', \
		   		'Federated States of Micronesia', 'Fiji', 'Ghana', 'Gibraltar', 'Grenada', 'Guam', 'Guernsey', 'Guyana', \
		   		'Heard Island and McDonald Islands', 'Hong Kong', 'India', 'Isle of Man', 'Jamaica', 'Jersey', 'Kenya', 'Kiribati', \
		   		'Lesotho', 'Liberia', 'Malawi', 'Malta', 'Marshall Islands', 'Mauritius', 'Montserrat', 'Namibia', 'Nauru', \
		   		'New Zealand', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Pakistan', 'Palau', 'Papua New Guinea', \
		   		'Philippines', 'Pitcairn Islands', 'Puerto Rico', 'Republic of Ireland', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', \
		   		'Saint Lucia', 'Saint Martin', 'Saint Vincent and the Grenadines', 'Samoa', 'Seychelles', 'Sierra Leone', 'Singapore', \
		   		'Sint Maarten', 'Solomon Islands', 'South Africa', 'South Georgia', 'South Sudan', 'Sudan', 'Swaziland', 'Tanzania', \
		   		'The Bahamas', 'The Gambia', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', \
		   		'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Vanuatu', 'Zambia', 'Zimbabwe'],\
		   	"regions_list" : ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania'], \
		   	"coords" : [(-29.0, 24.0), (21.75, -71.58333333), (-19.03333333, -169.86666666), (15.41666666, -61.33333333), (13.46666666, -16.56666666), \
		   		(-10.5, 105.66666666), (10.0, 8.0), (9.0, 168.0), (15.0, 30.0), (8.5, -11.5), (13.46666666, 144.78333333), (-12.5, 96.83333333), \
		   		(-22.0, 24.0), (-54.5, -37.0), (18.431383, -64.62305), (16.75, -62.2), (6.91666666, 158.25), (-0.53333333, 166.91666666), (-18.0, 175.0), \
		   		(-20.0, -175.0), (-2.0, 30.0), (15.2, 145.75), (17.25, -88.75), (13.25, -61.2), (-51.75, -59.0), (17.33333333, -62.75), (1.0, 38.0), (-29.5, 28.5), \
		   		(20.0, 77.0), (-27.0, 133.0), (19.5, -80.5), (36.13333333, -5.35), (30.0, 70.0), (7.5, 134.5), (-4.58333333, 55.66666666), (-6.0, 35.0), (53.0, -8.0), \
		   		(35.83333333, 14.58333333), (54.0, -2.0), (18.25, -63.16666666), (18.08333333, -63.95), (18.033333, -63.05), (-53.1, 72.51666666), (-9.0, -172.0), \
		   		(18.25, -77.5), (18.25, -66.5), (38.0, -97.0), (-13.5, 34.0), (1.36666666, 103.8), (-29.03333333, 167.95), (-14.33333333, -170.0), \
		   		(13.16666666, -59.53333333), (-25.06666666, -130.1), (15.0, 39.0), (1.0, 32.0), (-26.5, 31.5), (-20.0, 30.0), (12.116667, -68.933333), \
		   		(-6.0, 147.0), (49.46666666, -2.58333333), (49.25, -2.16666666), (13.0, 122.0), (7.0, 30.0), (-13.58333333, -172.33333333), (12.11666666, -61.66666666), \
		   		(-20.28333333, 57.55), (-15.95, -5.7), (-16.0, 167.0), (32.33333333, -64.75), (-8.0, 178.0), (1.41666666, 173.0), (11.0, -61.0), (8.0, -2.0), (-41.0, 174.0), \
		   		(-21.23333333, -159.76666666), (24.25, -76.0), (13.88333333, -60.96666666), (-15.0, 30.0), (17.05, -61.8), (60.0, -95.0), (22.25, 114.16666666), \
		   		(-6.0, 71.5), (6.0, 12.0), (5.0, -59.0), (-22.0, 17.0), (6.5, -9.5), (54.25, -4.5), (-8.0, 159.0)]}

norwegian = {"name" : "Norwegian", "iso_code" : "no", "countries" : 2, "regions" : 1, "subregions": 1, \
			 "subregions_list" : ['Northern Europe'], "countries_list" : ['Norway', 'Svalbard and Jan Mayen'], "regions_list" : ['Europe'], 
			 "coords" : [(78.0, 20.0), (62.0, 10.0)]}


#currencies
cny = {"code" : "CNY", "name" : "Yuan Renminbi", "countries" : 1, "regions": 1, "subregions": 1, \
		"subregions_list" : ['Eastern Asia'], "countries_list" : ['China'], "regions_list" : ['Asia'], "coords" : [(35.0, 105.0)]}

nok = {"code" : "NOK", "name" : "Norway Kroner", "countries" : 3, "regions": 1, "subregions": 1, \
		"subregions_list" : ['Northern Europe'], "countries_list" : ['Bouvet Island', 'Norway', 'Svalbard and Jan Mayen'], "regions_list" : ['Europe'], \
		"coords" : [(78.0, 20.0), (62.0, 10.0), (-54.43333333, 3.4)]}

usd = {"code" : "USD", "name" : "US Dollar", "countries" : 19, "regions": 4, "subregions": 8, \
		"subregions_list" : ['Caribbean', 'Central America', 'Eastern Africa', 'Micronesia', 'Northern America', 'Polynesia', 'South America', 'South-Eastern Asia'], \
		"countries_list" : ['American Samoa', 'Bonaire', 'British Indian Ocean Territory', 'British Virgin Islands', 'East Timor', 'Ecuador', 'El Salvador', \
			'Federated States of Micronesia', 'Guam', 'Haiti', 'Marshall Islands', 'Northern Mariana Islands', 'Palau', 'Panama', 'Puerto Rico', \
			'Turks and Caicos Islands', 'United States', 'United States Minor Outlying Islands', 'Zimbabwe'], \
		"regions_list" : ['Africa', 'Americas', 'Asia', 'Oceania'], \
		"coords" : [(18.431383, -64.62305), (21.75, -71.58333333), (-14.33333333, -170.0), (-8.83333333, 125.91666666), (9.0, 168.0), (7.5, 134.5), (38.0, -97.0), \
			(13.46666666, 144.78333333), (6.91666666, 158.25), (19.0, -72.41666666), (9.0, -80.0), (-20.0, 30.0), (13.83333333, -88.91666666), (-6.0, 71.5), (-2.0, -77.5), (12.15, -68.266667), (18.25, -66.5), (15.2, 145.75)]}


