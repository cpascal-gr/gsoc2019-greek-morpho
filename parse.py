#TODO gender detection needs work
# detect only {{αθ}} for both genders
# τρίχα λάθος γένος
# Πρόσθεσε γένος ακόμα και αν δεν βρέθηκε πίνακας
from html.parser import HTMLParser
from html.entities import name2codepoint
import sys
import re
import sqlite3

conn = sqlite3.connect('dict.db')
cur = conn.cursor()

# http://nlp.ilsp.gr/nlp/tagset_examples/tagset_en/
# Add Mood = Διάθεση
#	Indicative ενεργετική
#	υποτακτική
#	Imperative προστακτική
# Person 1 , 2 , 3
# Tense χρονος
#	Present
#	Past
#	Future
# Aspect ποιόν ενέργειας
#	Imperfective εξακολοθητικοί
#	Perfective συνοπτικοί
# Voice
#	Active
#	Passive
# Οι μετοχές είναι ρήματα με γένος,πτώση,αριθμό
# Article
#	Definite
#	Indefinite
# Τα επίθετα έχουν και βαθμό Degree
# Τα prounouns πρέπει να μπουν


'''Abbr
Aspect
Case
Definite
Degree
Foreign
Gender
Mood
Number
NumType
Person
Poss
PronType
SpaceAfter
Tense
VerbForm
Voice'''

with open("scema.sql") as file:
	script = file.read()
	cur.executescript(script)
	conn.commit()

# TODO πχ αγαπημένος (υποστήριξη περισσότερων από ένα μέρος του λόγου)
def parse_code(lemma,code):
	res = re.search("=== Ετυμολογία ===\n[^\s]*\s*(?P<ETM>[^=\n]+?)\n",code,re.UNICODE)
	if res != None:
		string = "INSERT INTO etymology VALUES (\'%s\',\'%s\')" % (esc(lemma),esc(res.group("ETM")))
		cur.execute(string)
	else:
		print("ETYMOLOGY NOT FOUND")
	res = re.search("=== (Ουσιαστικό|Ρήμα|Επίθετο|Μετοχή|Κύριο\sόνομα|Πολυλεκτικός\sόρος) ===\n+[^\n]*\n+(?P<DEF>[^=]+?)(\n+==|\Z)",code,re.DOTALL|re.UNICODE)
	if res != None:
		string = "INSERT INTO def VALUES (\'%s\',\'%s\')" % (esc(lemma),esc(res.group("DEF")))
		cur.execute(string)
	else:
		print("DEFINITION NOT FOUND")
		print(code)

def get_forms(s):
	if 'a' in s:# if <a href ...> </a>
		s = re.search(r"\>([ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψωςάέήίόύώΐΰϋϊἱΆΈΉΊΌΎΏΫΪ()]+)\<\/a\>", s).group(0)
	all_forms = re.findall(r"[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψωςάέήίόύώΐΰϋϊἱΆΈΉΊΌΎΏΫΪ()]+", s)
	res = []
	for i in all_forms:
		# print("form=",i)
		if '(' in i:
			tmp = ''
			j = 0
			while i[j] != '(':
				tmp += i[j]
				j+=1
			if tmp != '':
				res += [tmp]
			if j > len(i):
				break
			j+=1
			while i[j] != ')':
				tmp += i[j]
				j += 1
			res += [tmp]
		else:
			res += [i]
	return res

def esc(s):
	return s.translate(str.maketrans({"'":  r"''"}))

def wword(form,lemma,pos,*args, **kwargs):
	gender = kwargs.get('gender',None)
	ptosi = kwargs.get('ptosi',None)
	number = kwargs.get('number',None)
	person = kwargs.get('person',None)
	aspect = kwargs.get('aspect',None)
	tense = kwargs.get('tense',None)
	mood = kwargs.get('mood',None)
	verbform = kwargs.get('verbform',None)
	voice = kwargs.get('voice',None)
	definite = kwargs.get('definite',None)
	prontype = kwargs.get('prontype',None)
	tags = kwargs.get('tags',None)
	degree = kwargs.get('degree',None)
	poss = kwargs.get('poss',None)
	greek_pos = kwargs.get('greek_pos',None)
	freq = kwargs.get('freq',0)

	string = "INSERT INTO words VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d)"%(esc(form),esc(lemma),pos,greek_pos,gender,ptosi,number,person,tense,aspect,mood,verbform,voice,definite,degree,prontype,poss,tags,freq)
	#print(string)
	cur.execute(string)

def is_complete(lemma,pos):
	s = "SELECT form FROM words WHERE form = \'%s\' AND tags <> 'Incomplete' AND (true" % esc(lemma)
	for i in pos:
		s += " OR pos = \'%s\' " % esc(i)
	cur.execute(s+')')
	l = cur.fetchall()
	if len(l) != 0:
		return True
	return False

def form_exists(form,pos):
	cur.execute("SELECT form FROM words WHERE (form = \'%s\' AND pos = \'%s\')" % (esc(form),esc(pos)))
	l = cur.fetchall()
	if len(l) != 0:
		return True
	return False

if False:
	ptoseis = {
		"ονομαστική": "nom",
		"γενική": "gen",
		"αιτιατική": "acc",
		"κλητική": "voc"
	}

	arithmoi = {
		"ενικός" : "sg",
		"πληθυντικός" : "pl",
		0 : 'sg',
		1 : 'pl'
	}

	gender = {
		0 : "m",
		1 : "f",
		2 : "nt"
	}
else:
	ptoseis = {
		"ονομαστική": "Nom",
		"γενική": "Gen",
		"αιτιατική": "Acc",
		"κλητική": "Voc"
	}

	arithmoi = {
		"ενικός" : "Sing",
		"πληθυντικός" : "Plur",
		0 : 'Sing',
		1 : 'Plur'
	}

	gender = {
		0 : "Masc",
		1 : "Fem",
		2 : "Neut"
	}
"""
pos_transl = {
	"adj" : "ADJ", #Επίθετα
	"n" : "NOUN", #
	"vblex" : "VERB"
	"np" : "PROPN" #Κύριο όνομα
	"adv" : "ADV" #
	"prn" : "PRON"#Αντωνυμίες
	"pr" : "ADP" #Προθέσεις
	"det" : "DET"#Αρθρα
	"num" : "NUM"#αριθμητικά
	"cnjcoo" : "CCONJ"#Παρατακτικοί
	"cnjsub" : "SCONJ"#Υποτακτικοί
	"κατι":"PUNCT"#Σημεία στίξης
	"κατι και εδω":"PART"#Μόρια
}"""

def print_forms(s,lemma,pos,genos,ptwsi,arithmos,degree,greek_pos,tag):
	if s.strip() == '':
		return
	if 'PolyTerm' in tag:
		tmp = [s]
	else:
		tmp = get_forms(s)
	for i in tmp:
		if pos == 'VERB':
			 # Εδώ είναι οι μετοχές -μένος
			wword(i.strip(),lemma,pos,gender=genos,ptosi=ptwsi,number=arithmos,degree=degree,greek_pos=greek_pos,aspect='Perf',verbform='Part',voice='Pass',tags=tag)
		else:
			wword(i.strip(),lemma,pos,gender=genos,ptosi=ptwsi,number=arithmos,degree=degree,greek_pos=greek_pos,tags=tag)
	
# Μερικά επίθετα έχουν μόνο ένα γένος πχ αβάζος
class AdjParser(HTMLParser):
	i = False
	td = False
	th = False
	ptosi = "ERROR"
	arithmos = "ERROR"
	part = 'ADJ'
	genos = 0
	word = ''
	lemma = ''
	tag = ''
	detected = False
	degree = None
	greek_pos = None
	grc = False
	def handle_starttag(self, tag, attrs):
		for first,second in attrs:
			if first == "id" and second == "Αρχαία_ελληνικά_(grc)":
				self.grc = True
			if first == "class" and second == "mw-parser-output":#Start of parsing
				self.grc = False
				self.detected = False
		if self.grc == True:
			return
		if self.td and tag == "br":
			self.prop_print()
			return
		if self.i == True:
			if tag == "td":
				self.td = True
			if tag == "th":
				self.th = True
		
		for first,second in attrs:
			if first == "id" and second == "Αρχαία_ελληνικά_(grc)":
				self.grc = True

		if tag == "table":#detect table
			for first,second in attrs:
				if first == "style" and second == "float:right;border:1px solid #AAAACC;margin-left:0.5em;margin-bottom:0.5em;text-align:center;":
					print(' parsable table detected',end='')
					self.detected = True
					self.i = True

	def handle_endtag(self, tag):

		if tag == "table":
			self.i = False

		if self.td and tag == "br":
			self.prop_print()
			return

		if self.td == True and tag == "td":#element print end
			self.td = False
			self.prop_print()
			self.genos+=1
		if tag == "th":
			self.genos = 0
			self.th = False


	def handle_data(self, data):
		data = data.strip()
		if self.i == True:
			if self.th == True and data in ["ενικός","πληθυντικός"]:
				self.arithmos = arithmoi[data]
			if self.td == True and data != "" and data != "\n":
				if data in ["ονομαστική","γενική","αιτιατική","κλητική"]:
					self.ptosi = ptoseis[data]
					self.td = False
				else:
					self.word += data
					self.pr = True

	def prop_print(self):
		g = gender[self.genos%3]
		print_forms(self.word,self.lemma,self.part,g,self.ptosi,self.arithmos,self.degree,self.greek_pos,self.tag)
		self.word = ''


class NounParser(HTMLParser):
	i = False
	td = False
	th = False
	ptosi = "ERROR"
	arithmos = "ERROR"
	degree = None
	greek_pos = None
	genos = 0
	word = ''
	lemma = ''
	detected = False
	grc = False
	total_numbers = 1
	cur_arithmos = 0
	part = 'ERROR'
	tag = 'ERROR'

	def handle_starttag(self, tag, attrs):
		for first,second in attrs:
			if first == "id" and second == "Αρχαία_ελληνικά_(grc)":
				self.grc = True
			if first == "class" and second == "mw-parser-output":
				self.grc = False
				self.total_numbers = 0
				self.cur_arithmos = 0
				self.detected = False
		if self.grc == True:
			return

		if self.i == True:
			if tag == "td":
				self.td = True
				#βγάλε την παρατήρηση στο τέλος πχ Ανδρέας
				for first,second in attrs:
					if first == "style" and second == "background:#d9ebff; font-size: 90%; font-style: italic;":
						self.td = False
			if tag == "th":
				self.th = True
		
		for first,second in attrs:
			if first == "id" and second == "Αρχαία_ελληνικά_(grc)":
				self.grc = True

		if tag == "table":#detect table
			for first,second in attrs:
				if first == "style" and second == "float:right;border:1px solid #AAAACC;margin-left:0.5em;margin-bottom:0.5em;text-align:right;":
					print(' parsable table detected',end='')
					self.detected = True
					self.i = True

	def handle_endtag(self, tag):
		if tag == "table":
			self.i = False

		if self.td == True and tag == "td":#element print end
			self.td = False
			self.prop_print()
			self.cur_arithmos += 1
		if tag == "th":
			self.th = False

	def handle_data(self, data):
		data = data.strip()
		if self.i == True:
			if self.th == True and data in ["ενικός","πληθυντικός"]:
				self.arithmos = arithmoi[data]
				self.total_numbers += 1
			if self.td == True and data != "" and data != "\n":
				if data in ["ονομαστική","γενική","αιτιατική","κλητική"]:
					self.ptosi = ptoseis[data]
					self.td = False
				else:
					self.word += data
					self.pr = True

	def prop_print(self):
		g = gender[self.genos]
		if self.total_numbers == 1:
			ar = self.arithmos
		else:
			ar = arithmoi[self.cur_arithmos%2]
		print_forms(self.word,self.lemma,self.part,g,self.ptosi,ar,self.degree,self.greek_pos,self.tag)
		self.word = ''

NotDetectedNoun = open("NotDetectedNoun.dic","a")
TableNotGender = open("TableNotGender.dic","a")

#TODO θυλικό μονο στον ενικό
def parse_noun(html,lemma,part,tag):
	pn = NounParser()
	pn.lemma = lemma
	pn.part = part
	pn.tag = tag
	result = re.finditer("\<font color=\"#002000\"\>\<i\>(?P<GENOS>.*?)\</i\>\<\/font\>",html,re.DOTALL|re.UNICODE)
	genos = 'ERROR'
	detected = False
	h_found = False
	aklito = False
	for match in result:
		m = match.group('GENOS')
		m = m.strip()
		if genos == m:#detect only one time
			continue
		print(' ' + m,end='')
		if m in ['ουδέτερο','ουδέτερο μόνο στον ενικό','ουδέτερο μόνο στον πληθυντικό'] and detected == False:
			detected = True
			genos = pn.genos = 2
		elif m in[ 'θηλυκό','θηλυκό μόνο στον ενικό','θηλυκό μόνο στον πληθυντικό'] and (detected == False or h_found == True):
			genos = pn.genos = 1
			detected = True
		elif m in ['αρσενικό','αρσενικό μόνο στον πληθυντικό','αρσενικό μόνο στον ενικό']and detected == False:
			detected = True
			genos = pn.genos = 0
		elif m == 'άκλιτο':
			aklito = True
		elif m == 'ή':
			h_found = True
			continue
		else:
			continue
		pn.feed(html)

	if aklito and genos != 'ERROR':
		for ptosi in ["Nom","Gen","Acc","Voc"]:
			for arith in ["Sing","Plur"]:
				wword(lemma,lemma,part,gender=gender[genos],ptosi=ptosi,number=arith)

	if detected == False:
		parsable_tables = re.findall("float:right;border:1px solid #AAAACC;margin-left:0.5em;margin-bottom:0.5em;text-align:right;",html,re.DOTALL|re.UNICODE)
		if len(parsable_tables) != 0:
			print("[["+lemma+"]]",file=TableNotGender)
	if pn.detected == False and not aklito:
		print('[[' + lemma + ']]',file=NotDetectedNoun);
		wword(lemma,lemma,part,tags='Incomplete')
