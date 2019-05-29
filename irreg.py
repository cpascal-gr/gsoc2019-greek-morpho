form parse import wword
#TODO είμαι,έχω
def add_irreg_words():
	#Αρθρα
	wword('ο','ο','DET',case='Nom',definite='Def',gender='Masc',number='Sing',prontype='Art')
	wword('του','ο','DET',case='Gen',definite='Def',gender='Masc',number='Sing',prontype='Art')
	wword('τον','ο','DET',case='Acc',definite='Def',gender='Masc',number='Sing',prontype='Art')
	wword('οι','ο','DET',case='Nom',definite='Def',gender='Masc',number='Plur',prontype='Art')
	wword('των','ο','DET',case='Gen',definite='Def',gender='Masc',number='Plur',prontype='Art')
	wword('τους','ο','DET',case='Acc',definite='Def',gender='Masc',number='Plur',prontype='Art')

	wword('η','ο','DET',case='Nom',definite='Def',gender='Fem',number='Sing',prontype='Art')
	wword('της','ο','DET',case='Gen',definite='Def',gender='Fem',number='Sing',prontype='Art')
	wword('τη','ο','DET',case='Acc',definite='Def',gender='Fem',number='Sing',prontype='Art')
	wword('την','ο','DET',case='Acc',definite='Def',gender='Fem',number='Sing',prontype='Art')
	wword('οι','ο','DET',case='Nom',definite='Def',gender='Fem',number='Plur',prontype='Art')
	wword('των','ο','DET',case='Gen',definite='Def',gender='Fem',number='Plur',prontype='Art')
	wword('τις','ο','DET',case='Acc',definite='Def',gender='Fem',number='Plur',prontype='Art')

	wword('το','ο','DET',case='Nom',definite='Def',gender='Neut',number='Sing',prontype='Art')
	wword('του','ο','DET',case='Gen',definite='Def',gender='Neut',number='Sing',prontype='Art')
	wword('το','ο','DET',case='Acc',definite='Def',gender='Neut',number='Sing',prontype='Art')
	wword('τα','ο','DET',case='Nom',definite='Def',gender='Neut',number='Plur',prontype='Art')
	wword('των','ο','DET',case='Gen',definite='Def',gender='Neut',number='Plur',prontype='Art')
	wword('τα','ο','DET',case='Acc',definite='Def',gender='Neut',number='Plur',prontype='Art')

	#Σύνδεσμοι
	#Παρατακτικοί
	wword('και','και','CCONJ')
	wword('κι','κι','CCONJ')
	wword('ούτε','ούτε','CCONJ')
	wword('μήτε','μήτε','CCONJ')
	wword('ουδέ','ουδέ','CCONJ')
	wword('ή','ή','CCONJ')
	wword('είτε','είτε','CCONJ')
	wword('αν και','αν και','CCONJ')
	wword('αλλά','αλλά','CCONJ')
	wword('μα','μα','CCONJ')
	wword('παρά','παρά','CCONJ')
	wword('όμως','όμως','CCONJ')
	wword('ωστόσο','ωστόσο','CCONJ')
	wword('ενώ','ενώ','CCONJ')
	wword('μολονότι','μολονότι','CCONJ')
	wword('μόνο','μόνο','CCONJ')
	wword('λοιπόν','λοιπόν','CCONJ')
	wword('ώστε','ώστε','CCONJ')
	wword('άρα','άρα','CCONJ')
	wword('επομένως','επομένως','CCONJ')
	wword('οπότε','οπότε','CCONJ')
	wword('δηλαδή','δηλαδή','CCONJ')

	#Υποτακτικοί
	wword('ότι','ότι','SCONJ')
	wword('πως','πως','SCONJ')
	wword('που','που','SCONJ')
	wword('άμα','άμα','SCONJ')
	wword('όταν','όταν','SCONJ')
	wword('ενώ','ενώ','SCONJ')
	wword('καθώς','καθώς','SCONJ')
	wword('αφού','αφού','SCONJ')
	wword('αφότου','αφότου','SCONJ')
	wword('πριν','πριν','SCONJ')
	wword('μόλις','μόλις','SCONJ')
	wword('προτού','προτού','SCONJ')
	wword('ώσπου','ώσπου','SCONJ')
	wword('ωσότου','ωσότου','SCONJ')
	wword('σαν','σαν','SCONJ')
	wword('γιατί','γιατί','SCONJ')
	wword('επειδή','επειδή','SCONJ')
	wword('αφού','αφού','SCONJ')
	wword('τι','τι','SCONJ')
	wword('αν','αν','SCONJ')
	wword('εάν','εάν','SCONJ')
	wword('άμα','άμα','SCONJ')
	wword('να','να','SCONJ')
	wword('για να','για να','SCONJ')
	wword('ώστε','ώστε','SCONJ')
	wword('αν και','αν και','SCONJ')
	wword('μολονότι','μολονότι','SCONJ')
	wword('μη','μη','SCONJ')
	wword('μην','μην','SCONJ')
	wword('μήπως','μήπως','SCONJ')
	wword('παρά','παρά','SCONJ')
