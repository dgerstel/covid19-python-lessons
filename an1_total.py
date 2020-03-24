from menu import read_data
data, CASES = read_data()
################################################################################
# 1) I want to see:
# - a sum of all the cases per city {city : sum of cases}
# - world sum
################################################################################
# Prepare a report dictionary (empty)
report = {}
# For each line in the dataset
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

# # Pretty print
# import pprint
# pp = pprint.PrettyPrinter(width=80)
# pp.pprint(report)

world_sum = sum(v for k,v in report.items())
print(80*'*')
print("Total confirmed world cases:", world_sum)
