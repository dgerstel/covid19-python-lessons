# NOT WORKING

for i in range(len(data)):
	data[i] = data[i].replace('"','').replace('\n','')
	if data[i][0] == ',':
		data[i] = data[i][1:]

# Now, the same exercise but for the whole world
def get_city(row):
	row=row.replace('"','')
	row = row.split(',')
	city = row[0:2]
	city = ', '.join(city)
	if city[0] == ',':
		city = city[2:]
	return city

def get_cases_list(row):
	# TODO: fix USA (Seattle reads coordinates)
	return [int(x) for x in row.replace('"','').replace('\n','').split(',')[4:]]

data2D = {get_city(row) : get_cases_list(row) for row in data[1:]}
for i in range(len(days)):
	d = days[i]
	sum_today = 0
	for city in data2D:
		sum_today += data2D[city][i]
	world_daily.append(sum_today)
print(world_daily)
exit()

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


# Let's start with an empty list
hubei_daily = []

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
