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
		"languages_list" : ["Norwegian", "Norwegian Bokmål", "Norwegian Nynorsk"], "currencies_list" : ["NOK"], \
		"borders_list" : ["Finland", "Sweden", "Russia"]} 


#regions
americas = {"name": "Americas", "area": 42247698, "population": 983832674, "subregions": 4, \
			"countries": 56, "languages": 11, "currencies": 43, \
			"subregions_list" : ['Caribbean', 'Central America', 'Northern America', 'South America'], \
			"countries_list" : ['Anguilla', 'Antigua and Barbuda', 'Argentina', 'Aruba', 'Barbados', 'Belize', \
				'Bermuda', 'Bolivia', 'Bonaire', 'Brazil', 'British Virgin Islands', 'Canada', 'Cayman Islands', \
				'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Curaçao', 'Dominica', 'Dominican Republic', 'Ecuador', \
				'El Salvador', 'Falkland Islands', 'French Guiana', 'Greenland', 'Grenada', 'Guadeloupe', 'Guatemala', \
				'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Martinique', 'Mexico', 'Montserrat', 'Nicaragua', 'Panama', \
				'Paraguay', 'Peru', 'Puerto Rico', 'Saint Barthélemy', 'Saint Kitts and Nevis', 'Saint Lucia', \
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
		"countries_list" : ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', '\
			China', 'East Timor', 'Georgia', 'Hong Kong', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', \
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
		  	'Åland Islands'], \
		  "languages_list" : ['Albanian', 'Armenian', 'Belarusian', 'Bokmål, Norwegian', 'Bosnian', 'Bulgarian', 'Catalan', 'Croatian', \
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
			  		'Lithuania', 'Norway', 'Republic of Ireland', 'Svalbard and Jan Mayen', 'Sweden', 'United Kingdom', 'Åland Islands'], \
			  "languages_list" : ['Bokmål, Norwegian', 'Danish', 'English', 'Estonian', 'Faroese', 'Finnish', 'French', 'Icelandic', 'Irish', \
			  		'Latvian', 'Lithuanian', 'Manx', 'Norwegian', 'Norwegian Nynorsk', 'Swedish'], \
			  "currencies_list" : ['DKK', 'EUR', 'GBP', 'ISK', 'NOK', 'SEK']}


#languages
chinese = {"name" : "Chinese", "iso" : "zh", "countries" : 5, "regions" : 1, "subregions": 2, \
			"subregions_list" : ['Eastern Asia', 'South-Eastern Asia'], \
			"countries_list" : ['China', 'Hong Kong', 'Macau', 'Singapore', 'Taiwan'], "regions_list" : ['Asia']}

english = {"name" : "English", "iso" : "en", "countries" : 89, "regions" : 15, "subregions": 18, \
		   "subregions_list" : ['Australia and New Zealand', 'Caribbean', 'Central America', 'Eastern Africa', \
		   		'Eastern Asia', 'Melanesia', 'Micronesia', 'Middle Africa', 'Northern Africa', 'Northern America', \
		   		'Northern Europe', 'Polynesia', 'South America', 'South-Eastern Asia', 'Southern Africa', 'Southern Asia', \
		   		'Southern Europe', 'Western Africa'], \
		   	"countries_list" : ['American Samoa', 'Anguilla', 'Antigua and Barbuda', 'Australia', 'Barbados', 'Belize', 'Bermuda', \
		   		'Botswana', 'British Indian Ocean Territory', 'British Virgin Islands', 'Cameroon', 'Canada', 'Cayman Islands', \
		   		'Christmas Island', 'Cocos (Keeling) Islands', 'Cook Islands', 'Curaçao', 'Dominica', 'Eritrea', 'Falkland Islands', \
		   		'Federated States of Micronesia', 'Fiji', 'Ghana', 'Gibraltar', 'Grenada', 'Guam', 'Guernsey', 'Guyana', \
		   		'Heard Island and McDonald Islands', 'Hong Kong', 'India', 'Isle of Man', 'Jamaica', 'Jersey', 'Kenya', 'Kiribati', \
		   		'Lesotho', 'Liberia', 'Malawi', 'Malta', 'Marshall Islands', 'Mauritius', 'Montserrat', 'Namibia', 'Nauru', \
		   		'New Zealand', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Pakistan', 'Palau', 'Papua New Guinea', \
		   		'Philippines', 'Pitcairn Islands', 'Puerto Rico', 'Republic of Ireland', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', \
		   		'Saint Lucia', 'Saint Martin', 'Saint Vincent and the Grenadines', 'Samoa', 'Seychelles', 'Sierra Leone', 'Singapore', \
		   		'Sint Maarten', 'Solomon Islands', 'South Africa', 'South Georgia', 'South Sudan', 'Sudan', 'Swaziland', 'Tanzania', \
		   		'The Bahamas', 'The Gambia', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', \
		   		'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Vanuatu', 'Zambia', 'Zimbabwe'],\
		   	"regions_list" : ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']}

norwegian = {"name" : "Norwegian", "iso" : "no", "countries" : 2, "regions" : 1, "subregions": 1, \
			 "subregions_list" : ['Northern Europe'], "countries_list" : ['Norway', 'Svalbard and Jan Mayen'], "regions_list" : ['Europe']}


#currencies
cny = {"code" : "CNY", "name" : "Yuan Renminbi", "countries" : 1, "regions": 1, "subregions": 1, \
		"subregions_list" : ['Eastern Asia'], "countries_list" : ['China'], "regions_list" : ['Asia']}

nok = {"code" : "NOK", "name" : "Norway Kroner", "countries" : 3, "regions": 1, "subregions": 1, \
		"subregions_list" : ['Northern Europe'], "countries_list" : ['Bouvet Island', 'Norway', 'Svalbard and Jan Mayen'], "regions_list" : ['Europe']}

usd = {"code" : "USD", "name" : "US Dollar", "countries" : 19, "regions": 4, "subregions": 8, \
		"subregions_list" : ['Caribbean', 'Central America', 'Eastern Africa', 'Micronesia', 'Northern America', 'Polynesia', 'South America', 'South-Eastern Asia'], \
		"countries_list" : ['American Samoa', 'Bonaire', 'British Indian Ocean Territory', 'British Virgin Islands', 'East Timor', 'Ecuador', 'El Salvador', \
			'Federated States of Micronesia', 'Guam', 'Haiti', 'Marshall Islands', 'Northern Mariana Islands', 'Palau', 'Panama', 'Puerto Rico', \
			'Turks and Caicos Islands', 'United States', 'United States Minor Outlying Islands', 'Zimbabwe'], \
		"regions_list" : ['Africa', 'Americas', 'Asia', 'Oceania']}


