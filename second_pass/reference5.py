import re

# A very simple regex finder for alpha and numeric call number parts:
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

# Some simple lists for checking call number letters against:
A_M = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
main_N = ['N','NA','NB','NC','ND',]
# This list is replaced by simpler code in the categorize function:
# NX_S = ['NX',
# 		'P','PA','PB','PC','PD','PE','PF','PG','PH','PJ','PK','PL','PM','PN','PQ','PR','PS','PT','PZ',
# 		'Q','QA','QB','QC','QD','QE','QH','QK','QL','QM','QP','QR',
# 		'R','RA','RB','RC','RD','RE','RF','RG','RJ','RK','RL','RM','RS','RT','RV','RX','RZ',
# 		'S','SB','SD','SF','SH','SK',]
Q_S = ['Q', 'R', 'S']
T_TP = ['T','TA','TC','TD','TE','TF','TG','TH','TJ','TK','TL','TN','TP',]
TR = ['TR',]
TS_Z = ['TS','TT','TX',
		'U','UA','UB','UC','UD','UE','UF','UG','UH',
		'V','VA','VB','VC','VD','VE','VF','VG','VK','VM',
		'Z','ZA']


# This function makes tranche categories clearer and easier to write.  
# No doubt, it's a little obfuscated for my liking, but its benefits
# are palpable; code for writing tranches is made readable. Could even
# have a non-coder write them out.
def tranche(letter, min, max, label):
	# List comprehension for creating an initial list of ranges:
	the_range = [letter + str(each) for each in range(min, max)]
	# List comprehension converts to individual dictionaries with label values:
	with_labels = [{each: label} for each in the_range]
	# Merge the individual dictionaries into one:
	the_dict = dict((k,v) for d in with_labels for (k,v) in d.items())
	return the_dict

# Individual variables return dictionaries containing core call number
# ranges.
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

# List of dictionaries collected for the purpose of merging
# into a master dictionary:
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

# Merging all dictionaries into a master dictionary for reference:
master_dictionary = dict((k,v) for d in tranches for (k,v) in d.items())

# Takes incoming call number list and appends the proper category. Checks
# against the master_dictionary:
def categorize(callnumber_list):
	empty_list = []
	for callnumber in callnumber_list:
		callnumber = callnumber.encode("UTF-8")
		letter = find.alpha(callnumber)
		if letter[0] in A_M:
			empty_list.append(callnumber + ' |' + letter[0])
		elif letter in main_N:
			number = find.num(callnumber)
			key = letter + number
			category = master_dictionary[key]
			empty_list.append(callnumber + ' |' + category)
		elif letter == 'NE':
			empty_list.append(callnumber + ' |NE')
		elif letter == 'NK':
			empty_list.append(callnumber + ' |NK')
		elif letter == 'NX':
			empty_list.append(callnumber + ' |NX')
		elif letter[0] == 'P':
			empty_list.append(callnumber + ' |P')
		elif letter[0] in Q_S: 
			empty_list.append(callnumber + ' |Q-S')
		elif letter in T_TP:
			empty_list.append(callnumber + ' |T-TP')
		elif letter == 'TR':
			number = find.num(callnumber)
			key = letter + number
			category = master_dictionary[key]
			empty_list.append(callnumber + ' |' + category)
		elif letter in TS_Z:
			empty_list.append(callnumber + ' |TS-Z')
		else:
			empty_list.append(callnumber + ' |mybugs')
	return empty_list

# At this point, what you do is simply set a new variable to the categorize
# function, which will return a list of callnumbers appended with the appropriate
# category.  Here is an example:

# if in repl:

# >> category_result = categorize(callnumber_list)
# >> category_result
# >> ['NA4972 .A4 2010 |NA4000-4999'],
# >> 'N6537 .A4 A8 2010 |N6000-6999',
# >> ...
# >> ]



