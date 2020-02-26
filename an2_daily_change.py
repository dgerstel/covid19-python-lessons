from menu import read_data
data, CASES = read_data()
################################################################################
# 2) I want to see how the total confirmed cases changes from day to day for a given city
# (start with one city e.g. Hubei, Mainland China)
################################################################################
# Select the row with the Hubei data only
for row in data[1:]:
	if 'Hubei' in row:
		hubei_row = row
		break
# Clean it up
hubei_row = hubei_row.replace('\n','')
hubei_row_list = hubei_row.split(',')
hubei_cummulative = [int(x) for x in hubei_row_list[4:]]
print(hubei_cummulative)
# For the first day, cummulative <=> daily
hubei_daily = [hubei_cummulative[0]]
for i in range(1, len(hubei_cummulative)):
	delta = hubei_cummulative[i]-hubei_cummulative[i-1]
	hubei_daily.append(delta)
# We need dates for each day
days = data[0].replace('\n','').split(',')[4:]
for i in range(len(hubei_cummulative)):
	print(days[i], ' : ', hubei_cummulative[i], '(+', hubei_daily[i], ')', sep='')

# Let's visualise the daily change
from matplotlib import pyplot as plt
plt.plot(days, hubei_daily, 'bo', label='New cases')
plt.plot(days, hubei_cummulative, 'go', label='Cummulative')
# y=0 for clarity
plt.plot(days, [0 for x in days])
plt.xlabel('date', fontsize=18, labelpad=100)
plt.ylabel('Number of people', fontsize=18)
plt.xticks(fontsize=7, rotation=45)
plt.title("COVID-19 {} cases in Hubei".format(CASES), fontsize=18)
plt.legend()
plt.show()

