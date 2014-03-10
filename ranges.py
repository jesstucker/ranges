import re
import sys
from xlrd import open_workbook


workbook = open_workbook('ranges_tally_2010-13.xls')
oten = workbook.sheet_by_index(0)
oeleven = workbook.sheet_by_index(1)
testy = oeleven.col_values(0)
testy.pop(0)


testlist = ['N72.A75 F67 2011',
'TR140.A73 S87 2011',
'DS749.5 .F58 2011',
'ND245.5.A28 N69 2011',
'TR647 .J3428 2011',
'NA5235.O259 S55 2011',
'NB1002 .P35 2011',
'NK7149.A1 D56 2011',
'DH811.G49 S23 2011',
'PN6727.C565 D43 2011',
'PN6727 .D34 2011',
'ND623.A795 Z46 2011',]

range_list = []
rangey = range(1,10000)
for each in rangey:
	if each > 0 and each < 1000:
		range_list.append({each: 'hundreds'})
	elif each >= 1000 and each < 2000:
		range_list.append({each: 'thousands'})
	elif each >= 2000 and each < 3000:
		range_list.append({each: 'two thousands'})
	elif each >= 3000 and each < 4000:
		range_list.append({each: 'three thousands'})
	elif each >= 4000 and each < 5000:
		range_list.append({each: 'four thousands'})
	elif each >= 5000 and each < 6000:
		range_list.append({each: 'five thousands'})
	elif each >= 6000 and each < 7000:
		range_list.append({each: 'six thousands'})
	elif each >= 7000 and each < 8000:
		range_list.append({each: 'seven thousands'})
	elif each >= 8000 and each < 9000:
		range_list.append({each: 'eight thousands'})
	elif each >= 9000 and each < 10000:
		range_list.append({each: 'nine thousands'})

merged_dictionary = {k: v for d in range_list for k, v in d.items() }


class FindElement:
	def alpha(self, callnumber_string):
		p = r'^[A-Z]{1,3}'
		alpha_part = re.findall(p, callnumber_string)
		try:
			return alpha_part[0]
		except:
			return ("")

	def num(self, callnumber_string):
		p = r'[0-9]{1,4}'
		number_part = re.findall(p, callnumber_string)
		try:
			return number_part[0]
		except:
			return ("")

find = FindElement()



first_list = []

def categorize(slist, empty_list):
	for i in slist:
		alpha = find.alpha(i)
		numeric = int(find.num(i))
		numeric_category = merged_dictionary[numeric]
		empty_list.append(alpha + str(numeric) + " | " + alpha + " " + numeric_category + "\n")




# f = open('range_test.txt', 'w')
# first_list = str(first_list)
# f.write(first_list)
# f.close()


