from time import ctime
from datetime import datetime

# Read data from file
#CASES = input("Type which cases you want to analyse (Confirmed|Deaths|Recovered): ")
CASES='Confirmed'
f = open('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-{}.csv'.format(CASES), 'r')
data = f.readlines()
f.close()
################################################################################
# 1) I want to see:
# - a sum of all the cases per city {city : sum of cases}
# - world sum
################################################################################
# Prepare a report dictionary (empty)
report = {}
# For each line except the first one (header) and the last one (bad formatting for Boston)
for line in data[1:]:
	# e.g. Chongqing,Mainland China,1/3/2020,30.05718,107.874,5,6,9,27,27,57,57,75,75,110,110,110,132,132,132,147,147,147,165,182,211,238,247,300,337,337,366
	#print(line)
	line = line.replace('"', '')
	line = line.replace('\n','') # each line = str
	line_list = line.split(',') # string to list
	#print(line_list)
	city = line_list[0:2] #e.g. ['Chongqing', 'Mainland China']
	# make string from 2 list elements (string glued with ',')
	city = ", ".join(city) # e.g. 'Chongqing, Mainland China'
	if city[0] == ',': # e.g. ', Iraq'
		city = city[2:] # e.g. 'Iraq'
	#print(city)
	coordinates = line_list[2:4]
	tot_cases = line_list[-1]
	# For empty tot_cases:
	if tot_cases == '':
		tot_cases = 0
	else:
		tot_cases = int(tot_cases)
	# We're interested only in {city : sum of tot_cases}
	# Let's add this city and its number of tot_cases to the dictionary
	report[city] = tot_cases
	#print(city, ' : ', report[city])
print(80*'*')
print("Total cases as for**{}**".format(data[0].replace('\n','').split(',')[-1]))
print(report) # OK, but ugly!
print(80*'*')

# # Pretty print
# import pprint
# pp = pprint.PrettyPrinter(width=80)
# pp.pprint(report)

world_sum = sum(v for k,v in report.items())
print(80*'*')
print("Total confirmed world cases:", world_sum)
print(80*'*')
exit()

################################################################################
# 2) I want to see how the total confirmed cases changes from day to day.
#    Make a sum of columns for each day
################################################################################
# Let's start with an empty list
world_cases_per_day_cummul = {}
n_days = len(data[1].split(',')[4:])
print("N days:", n_days)
dates = []
for day in range(n_days):
	# Get the date of today
	date = data[0].split(',')[4+day].split(' ')[0] # e.g. 1/21/2020
	#dates.append(date)
	print('date:', date)
	# Take only one record per day
	# if date in world_cases_per_day_cummul.keys():
	# 	continue
	# Let's start counting that day with 0
	world_cases_per_day_cummul[date] = 0
	# We'll be updating that value
	# refering to that day with
	# world_case_per_day_cummul[date]
	for city in data[1:-1]:
		city = city.replace('\n', '')
		city = city.split(',')
		cases_today = city[4+day] # get fields [4,5,6,7,...] on the days [0,1,2,...]
		if cases_today == '':
			cases_today=0
		print('cases today:', cases_today)
		cases_today = int(float(cases_today))
		world_cases_per_day_cummul[date] += cases_today 
print(world_cases_per_day_cummul)

# The above list is cummulative, but we want per day list
world_cases_per_day = {world_cases_per_day_cummul[i+1]-world_cases_per_day_cummul[i] for i in range(n_days-1)}
print(world_cases_per_day)

days = list(world_cases_per_day_cummul.keys())
days.sort(key=lambda date: datetime.strptime(date, '%m/%d/%y'))
print("days sorted:", days)
#world_cases_per_day = {days[i+1] : world_cases_per_day_cummul[days[i+1]]-world_cases_per_day_cummul[days[i]] for i in range(len(days)-1)}
for i in range(len(days)-1):
	print('day:', days[i+1])
	print('cumul today:', world_cases_per_day_cummul[days[i+1]])
	print('cumul tomorrow:', world_cases_per_day_cummul[days[i]])
	print(days[i+1], '\t:\t',world_cases_per_day_cummul[days[i+1]]-world_cases_per_day_cummul[days[i]])
print(world_cases_per_day)

# Visualisation
from matplotlib import pyplot as plt
wcpdc_list = [world_cases_per_day_cummul[d] for d in days[1:]]
wcpd_list = [world_cases_per_day[d] for d in days[1:]]
plt.plot(days[1:], wcpd_list, 'bo', label='New cases')
plt.plot(days[1:], wcpdc_list, 'go', label='Cummulative')
plt.xlabel('date', fontsize=18, labelpad=100)
plt.ylabel('Number of people', fontsize=18)
plt.xticks(fontsize=7, rotation=45)
plt.title(CASES+" cases of 2019-nCov", fontsize=18)
plt.legend()
plt.show()
