# this is a program that will take in a bunch of tree banks and then give a relative word order of verb and bject 

#its a bunch of info delimited by tabs, \t. 
#Word Id \t Form \t Lemma \t POS tag \t lang specific POS tag \t Feature \t head of current word \t U Dep relation \t misc

# languages: afrikaans, croation, czech ,estonian, hungarian, kazakh, latvian, persian, portuguese, serbian

import matplotlib.pyplot as plt

af = "ud-treebanks-v2.11/UD_Afrikaans-AfriBooms/af_afribooms-ud-dev.conllu"
hr = "ud-treebanks-v2.11/UD_Croatian-SET/hr_set-ud-dev.conllu"
cs= "ud-treebanks-v2.11/UD_Czech-CLTT/cs_cltt-ud-dev.conllu"
et = "ud-treebanks-v2.11/UD_Estonian-EWT/et_ewt-ud-dev.conllu"
hu = "ud-treebanks-v2.11/UD_Hungarian-Szeged/hu_szeged-ud-train.conllu"
kk = "ud-treebanks-v2.11/UD_Kazakh-KTB/kk_ktb-ud-test.conllu"
lv = "ud-treebanks-v2.11/UD_Latvian-LVTB/lv_lvtb-ud-dev.conllu"
fa = "ud-treebanks-v2.11/UD_Persian-PerDT/fa_perdt-ud-dev.conllu"
pt = "ud-treebanks-v2.11/UD_Portuguese-Bosque/pt_bosque-ud-dev.conllu"
sr = "ud-treebanks-v2.11/UD_Serbian-SET/sr_set-ud-dev.conllu"


banks=[af, hr, cs, et, hu, kk, lv, fa, pt, sr]
labels=["af", "hr", "cs", "et", "hu", "kk", "lv", "fa", "pt", "sr"]

# Ratio lists
obj_verb_ratio=[]
verb_obj_ratio=[]

for i in range(0, len(banks)):
	#set bank coutners to 0
	obj_verb=0
	verb_obj=0
	
	#open the treebank and read all the lines
	treebank=open(banks[i], encoding="utf8")
	lines=treebank.readlines()
	treebank.close()

	for line in lines:
	#if its a comment or newline skip 
		if line[0] =="#" or line[0]=="\n":
			#print(line,"skipped")
			continue

		word_info=line.split('\t') #split line into columns

		#if its an object check where the verb is
		if word_info[7] == "obj":
			if word_info[0]>word_info[6]:
				verb_obj+=1
			else:
				obj_verb+=1

	#print(obj_verb, verb_obj)
	total=obj_verb+verb_obj

	obj_verb_ratio.append(obj_verb/total)
	verb_obj_ratio.append(verb_obj/total)

plt.xlabel("Object-Verb")
plt.ylabel("Verb-Object")
plt.title("Relative word order of verb and object")

plt.scatter(obj_verb_ratio, verb_obj_ratio)

for i in range(0, len(obj_verb_ratio)):
	plt.annotate(labels[i], 
		(obj_verb_ratio[i], verb_obj_ratio[i]),
		textcoords= "offset points",
		xytext=(0,10),
		ha="center")
	
plt.savefig("obj_verb_ratios.png")

