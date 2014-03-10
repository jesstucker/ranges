import re


range_list = []
rangey = range(1,10000)
for each in rangey:
	if each > 0 and each < 1000:
		range_list.append({each: '100s'})
	elif each >= 1000 and each < 2000:
		range_list.append({each: '1000s'})
	elif each >= 2000 and each < 3000:
		range_list.append({each: '2000s'})
	elif each >= 3000 and each < 4000:
		range_list.append({each: '3000s'})
	elif each >= 4000 and each < 5000:
		range_list.append({each: '4000s'})
	elif each >= 5000 and each < 6000:
		range_list.append({each: '5000s'})
	elif each >= 6000 and each < 7000:
		range_list.append({each: '6000s'})
	elif each >= 7000 and each < 8000:
		range_list.append({each: '7000s'})
	elif each >= 8000 and each < 9000:
		range_list.append({each: '8000s'})
	elif each >= 9000 and each < 10000:
		range_list.append({each: '9000s'})

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

A_M = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
main_N = ['N','NA','NB','NC','ND','NE',]
NK_S = ['NK','NX',
		'P','PA','PB','PC','PD','PE','PF','PG','PH','PJ','PK','PL','PM','PN','PQ','PR','PS','PT','PZ',
		'Q','QA','QB','QC','QD','QE','QH','QK','QL','QM','QP','QR',
		'R','RA','RB','RC','RD','RE','RF','RG','RJ','RK','RL','RM','RS','RT','RV','RX','RZ',
		'S','SB','SD','SF','SH','SK',]
T_TP = ['T','TA','TC','TD','TE','TF','TG','TH','TJ','TK','TL','TN','TP',]
# TR = ['TR',]
TS_Z = ['TS','TT','TX',
		'U','UA','UB','UC','UD','UE','UF','UG','UH',
		'V','VA','VB','VC','VD','VE','VF','VG','VK','VM',
		'Z','ZA']

def categorize(empty_list, array):
	for callnumber in array:
		letter = find.alpha(callnumber)
		if letter[0] in A_M:
			empty_list.append(callnumber + ' |' + letter[0])
		elif letter in main_N:
			number = int(find.num(callnumber))
			category = merged_dictionary[number]
			empty_list.append(callnumber + ' |' + letter + category)
		elif letter == 'NE':
			empty_list.append(callnumber + ' |NE')
		elif letter in NK_S:
			empty_list.append(callnumber + ' |NK-S')
		elif letter in T_TP:
			empty_list.append(callnumber + ' |T-TP')
		elif letter == 'TR':
			empty_list.append(callnumber + ' |TR')
		elif letter in TS_Z:
			empty_list.append(callnumber + ' |TS-Z')


