import argparse
import sys
import re


parser = argparse.ArgumentParser(description='''
    A tool that performs frequency counting, and cleanup of
    a word list produced by a tokenizer like fast-tokenizer''')

optional = parser.add_argument_group('optional arguments')

optional.add_argument('--min-freq', help='minimun number of occurances (default = 1)',
                      dest='min_freq', type=int, default=1)

optional.add_argument('--no-print-freq', help="don't print fequency count",
                      dest='no_print_freq',action='store_true')

optional.add_argument('--min-capital-freq',help='''minimun number of occurances 
       for words containing only capital letters (default = 1)''',dest='min_cap_freq',type=int,default = 1)

optional.add_argument('--sort-on-freq',help='sort on word frequency',
                      dest='sort_on_freq',action='store_true')

args = parser.parse_args()

words = {}

min_freq_count = args.min_freq

in_file = sys.stdin
line = in_file.readline()

# συν διαλυτικά
se_tonismena = {
	'α' : 'ά',
	'ε' : 'έ',
	'η' : 'ή',
	'ι' : 'ί',
	'ο' : 'ό',
	'ω' : 'ώ',
	'υ' : 'ύ',
	'ϋ' : 'ΰ',
	'ϊ' : 'ΐ'
}

# first pass, put words into dictionary

while line != '':
	line = line.strip()
	if line.strip() in words:
		words[line] += 1
	elif line != '':
		words[line] = 1
	line = in_file.readline()

# second pass, remove probably wrong words
word_list = []

for x,y in words.items():
	
	should_be_put = True
	
	if y < min_freq_count:
		continue
	# remove words with no accent and at least 2 sylables
	elif re.fullmatch(r"[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΫΪαβγδεζηθικλμνξοπρστυφχψωςϋϊ]*[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΫΪαεηιυοωϋϊ]+[βγδζθκλμνξπρστφχψς]+[αεηιυοωϋϊ]+[αβγδεζηθικλμνξοπρστυφχψωςϋϊ]*",x,re.UNICODE) is not None:
		continue
	# remove words with probably wrong capital letters (at least 2 in the beginning) or with non capital in the middle
	elif re.search(r'([ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΆΈΉΊΌΎΏ]{2,}[αβγδεζηθικλμνξοπρστυφχψωςάέήίόύώΐΰϋϊἱ]|[αβγδεζηθικλμνξοπρστυφχψωςάέήίόύώΐΰϋϊἱ][ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΆΈΉΊΌΎΏΫΪ])',x,re.UNICODE) is not None:
		continue
	# not possible letter combinations in Greek
	elif re.search(r'(τπ|λλλ|σσσ|κκκ|τττ|ρρρ|γγγ|θθ|ηη|μμμ|ννν|ςς|ζζ|ξξ|ooo|πππ|σ$)', x, re.UNICODE) is not None:
		continue
	elif re.fullmatch(r'[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΆΈΉΊΌΎΏΫΪ]+', x, re.UNICODE) is not None and y < args.min_cap_freq:
		continue
	# τόνος πριν την προ παραλήγουσα
	elif re.search(r'[ΆΈΉΊΌΎΏέάώήίύόΐΰ].*[βγδζθκλμνξπρστφχψ].*[έάώήίύόαεηιυοωϋϊΐΰ].*[βγδζθκλμνξπρστφχψ].*[έάώήίύόαεηιυοωϋϊΐΰ].*[βγδζθκλμνξπρστφχψ].*[έάώήίύόαεηιυοωϋϊΐΰ]', x, re.UNICODE):
		continue
	# οι τόνοι δεν πρέπει να είναι δίπλα δίπλα
	elif re.search(r'[ΆΈΉΊΌΎΏέάώήίύόΐΰ][βγδζθκλμνξπρστφχψ]*[έάώήίύόΐΰ]', x, re.UNICODE) is not None:
		continue
	# τόνος σε λέξη με τουλάχιστον 2 κεφαλαία
	elif re.search(r'[ΆΈΉΊΌΎΏΫΪ].*[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΆΈΉΊΌΎΏ]|[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ].*[ΆΈΉΊΌΎΏΫΪ]', x, re.UNICODE) is not None:
		continue
	# if there is the same word in lower case, skip it	
	elif x != x.lower():
		if x.lower() in words: 
			continue
		lowered = x.lower()

		if lowered[-1] == 'σ':
			lowered = lowered[:len(lowered)-1] + 'ς'

		for i in range(len(lowered)):
			if lowered[i] in se_tonismena:
				tmp = lowered[:i] + se_tonismena[lowered[i]] + lowered[i+1:]
				# print(x,tmp)
				if tmp in words:
					should_be_put = False
				
				# first character can be upper
				tmp = lowered[0].upper() + lowered[1:i] + se_tonismena[lowered[i]] + lowered[i+1:]
				if tmp in words:
					should_be_put = False

	if should_be_put:
		word_list.append((x,y))

for x,y in sorted(word_list,key=lambda x: -x[1] if args.sort_on_freq else x[0]):
	if args.no_print_freq:
		print(x)
	else:
		print(x,y)
