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
TR = ['TR',]
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


def categorize2(empty_list):
	for callnumber in array:
		letter = find.alpha(callnumber)
		number = int(find.num(callnumber))
		if letter[0] in A_M:
			empty_list.append(callnumber + ' |' + letter[0])
		if letter == 'N':
			# the merged dictionary is going to have to change for more rules
			category = merged_dictionary[number] 



N_dict = {"N123": "N100-999"}

N_range = range(1,1000)

for each in N_range:
	print 'N' + str(each)



# Yes...
N100s_range = ['N' + str(each) for each in range(1,1000)]
empt = []
for each in N100s_range:
	empt.append({each: "N1-999"})
N100s_dict = dict((k,v) for d in empt for (k,v) in d.items())
# Only works for 2.7 
# N100s_dict = { k: v for d in empt for k, v in d.items() }





def tranche(letter, min, max, label):
	the_range = [letter + str(each) for each in range(min, max)]
	empt_list = []
	for each in the_range:
		empt_list.append({each: label})
	the_dict = dict((k,v) for d in empt_list for (k,v) in d.items())
	return the_dict


N0100 = tranche('N', 1, 1000, 'N1-999')
N1000 = tranche('N', 1000, 6000, 'N1000-5999')
N6000 = tranche('N', 6000, 7000, 'N6000-6999')
N7000 = tranche('N', 7000, 8000, 'N7000-7999')
N8000_9000 = tranche('N', 8000, 10000, 'N8000-9999')

NA0100 = tranche('NA', 1, 1000, 'NA1-999' )
NA1000 = tranche('NA', 1000, 2000, 'NA1000-1999')
NA2000 = tranche('NA', 2000, 3000, 'NA2000-2999')
NA3000 = tranche('NA', 3000, 4000, 'NA3000-3999')
NA4000 = tranche('NA', 4000, 5000, 'NA4000-4999')
NA5000 = tranche('NA', 5000, 6000, 'NA5000-5999')
NA6000 = tranche('NA', 6000, 7000, 'NA6000-6999')
NA7000 = tranche('NA', 7000, 8000, 'NA7000-7999')
NA8000 = tranche('NA', 8000, 9000, 'NA8000-8999')
NA9000 = tranche('NA', 9000, 10000, 'NA9000-9999')

NB0100 = tranche('NB', 1, 1000, 'NB1-999')
NB1000 = tranche('NB', 1000, 10000, 'NB1000-9999')

NC0100 = tranche('NC', 1, 1000, 'NC1-999')
NC1000 = tranche('NC', 1000, 10000, 'NC1000-9999')

ND0100 = tranche('ND', 1, 200, 'ND1-199')
ND0200 = tranche('ND', 200, 300, 'ND200-299')
ND0300 = tranche('ND', 300, 400, 'ND300-399')
ND0400 = tranche('ND', 400, 500, 'ND400-499')
ND0500 = tranche('ND', 500, 600, 'ND500-599')
ND0600 = tranche('ND', 600, 700, 'ND600-699')
ND0700 = tranche('ND', 700, 800, 'ND700-799')
ND0800 = tranche('ND', 800, 900, 'ND800-899')
ND0900 = tranche('ND', 900, 1000, 'ND900-999')
ND1000 = tranche('ND', 1000, 10000, 'ND1000-9999')

TR1_500 = tranche('TR', 1, 600, 'TR1-599')
TR600_900 = tranche('TR', 600, 1000, 'TR600-999')


tranches = [
	N0100, N1000, N6000, N7000, N8000_9000,
	NA0100, NA1000, NA2000, NA3000, NA4000,
	NA5000, NA6000, NA7000, NA8000, NA9000,
	NB0100, NB1000,
	NC0100, NC1000,
	ND0100, ND0200, ND0300, ND0400, ND0500,
	ND0600, ND0700, ND0800, ND0900, ND1000,
	TR1_500, TR600_900,
]

master_dictionary = dict((k,v) for d in tranches for (k,v) in d.items())




