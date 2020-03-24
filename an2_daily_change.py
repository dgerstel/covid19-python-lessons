from menu import read_data
from datetime import datetime
import matplotlib.dates as md
data, CASES = read_data()
COUNTRY = input("Which country?")
################################################################################
# 2) I want to see how the total confirmed cases changes from day to day for a given city
# (start with one city e.g. Hubei, Mainland China)
################################################################################
# Select the row with the Hubei data only
for row in data[1:]:
	if COUNTRY in row and row[0]==',':
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
# Convert string-type date to datetime-type date
days = [datetime.strptime(d,'%m/%d/%y').date() for d in days]
plt.plot(days, hubei_daily, 'bo', label='New cases')
line = plt.plot(days, hubei_cummulative, 'go', label='Cummulative')
# plt.plot(days, [0 if d != '3/9/20' else 60000 for d in days], '|', color='black', label='Confinement starts')
# plt.plot(days, [0 if d != '3/21/20' else 60000 for d in days], '|', color='green', label='Increase rate slows down')
# y=0 for clarity
plt.plot(days, [0 for x in days])
plt.xlabel('date', fontsize=18, labelpad=100)
plt.ylabel('Number of people', fontsize=18)
#plt.yscale('log')
# Confinement begins
conf_start = datetime.strptime('09/03/2020', '%d/%m/%Y').date()
conf_middle = datetime.strptime('13/03/2020', '%d/%m/%Y').date()
slowing = datetime.strptime('21/03/2020', '%d/%m/%Y').date()
plt.axvline(datetime.strptime('09/03/2020', '%d/%m/%Y').date(), color='black', label='Confinement starts')
plt.axvline(datetime.strptime('21/03/2020', '%d/%m/%Y').date(), color='yellow', label='Increase rate slows down')
plt.text(x=datetime.strptime('15/03/2020', '%d/%m/%Y').date(), y=50000, color='red', s='12 days')
period = md.date2num(slowing) - md.date2num(conf_start)
plt.arrow(conf_start, 5000, dx=period, dy=0, shape='full', head_width=1000, head_length=0.05)
plt.annotate('12 days', xy=(conf_middle,5050))#, arrowprops=dict(arrowstyle='<->'))
plt.legend()
plt.xticks(fontsize=7, rotation=45)
plt.title("COVID-19 {} cases in {}".format(CASES, COUNTRY), fontsize=18)
plt.legend()
plt.show()

