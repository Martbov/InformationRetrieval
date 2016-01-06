#!/usr/bin/Python3.4

# Store_data.py
# Rolf Kuipers & Mart Busger op Vollenbroek
# Information Retrieval, Rijksuniversiteit Groningen

from Brief import Brief
import pandas as pd
import pickle

def main():
	# Maak gebruik van pandas-module om kolommen uit csv. bestand te halen
	df = pd.read_csv('corpus.csv')
	ID = df['User Number']
	motivatie = df['Motivatie']
	maatschap = df['Maatschappelijkebetrokkenheid']
	extraversie = df['csel_extr']
	innovatie = df['csel_inno']
	stabiliteit = df['csel_stab']
	vriendelijkheid = df['csel_vrie']
	zorgvuldigheid = df['csel_zrgv']

	# Helaas werkte (door index-range fouten) alle object in 1 loop creëren met alle attributen niet.
	# Daarom eerst alleen het ID toevoegen en daarna alle andere aspecten d.m.v. Setters. 
	brief_dic = []
	for num in ID:
		brief_dic.append(Brief(num))
	for i in range(len(motivatie)):
		tekst = motivatie[i] + maatschap[i]
		brief_dic[i].setTekst(tekst)
		brief_dic[i].setInnovatie(innovatie[i])
		brief_dic[i].setExtraversie(extraversie[i])
		brief_dic[i].setStabiliteit(stabiliteit[i])
		brief_dic[i].setVriendelijkheid(vriendelijkheid[i])
		brief_dic[i].setZorgvuldigheid(zorgvuldigheid[i])
		
	pickle.dump(brief_dic, open("data.pickle", 'wb'))

main()