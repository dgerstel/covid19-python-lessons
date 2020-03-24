def read_data():
	''' Read data from file based on user's choice.
	Return the dataset and its type of cases.'''
	print(80 * '*')
	while True:
		cases = input("Type which cases you want to analyse ([C]onfirmed|[D]eaths|[R]ecovered): ")
		if cases.lower() == 'c': # 'C'.lower() => 'c'; 'c'.lower() => 'c'
			cases = 'Confirmed'
			break
		elif cases.lower() == 'd':
			cases = 'Deaths'
			break
		elif cases.lower() == 'r':
			cases = 'Recovered'
			break
		else:
			print('Wrong choice! Select one of: C|D|R')
	if cases == 'Confirmed':
		f = open('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', 'r')
	elif cases == 'Deaths':
		f = open('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', 'r')
	else:
		print('WARNING!!! Using deprecated format!!!')
		f = open('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-{}.csv'.format(cases), 'r')
	data = f.readlines() # fichier => liste
	f.close()
	return data, cases # return tuple
	
