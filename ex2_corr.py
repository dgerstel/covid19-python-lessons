from menu import read_data
from datetime import datetime
import matplotlib.dates as md
data, CASES = read_data()
################################################################################
# 2) I want to see how the total confirmed cases changes from day to day for a given city
# (start with one city e.g. Hubei, Mainland China)
################################################################################
# Attention: le menu.py a changé
# Select the row with the Hubei data only
COUNTRY = ',France'
for row in data[1:]:
	if COUNTRY in row and row[0]==',':
		hubei_row = row
		break

# Clean it up
hubei_row = hubei_row.replace('\n','')
hubei_row_list = hubei_row.split(',')

# Creer une liste cummulative des cas
hubei_cummulative = []
for x in hubei_row_list[4:]:
	hubei_cummulative.append(int(x))
print(hubei_cummulative)
# For the first day, cummulative <=> daily
hubei_daily = [hubei_cummulative[0]]
for i in range(1, len(hubei_cummulative)):
	delta = hubei_cummulative[i]-hubei_cummulative[i-1]
	hubei_daily.append(delta)

# We need dates for each day
days = data[0]
days = days.replace('\n','')
days = days.split(',')
days = days[4:]
# Ou dans une seule ligne :
#days = data[0].replace('\n','').split(',')[4:]

# Affichez `date : +nombre de cas`
for i in range(len(hubei_cummulative)):
	print(days[i], ' : ', hubei_cummulative[i], '(+', hubei_daily[i], ')', sep='')
