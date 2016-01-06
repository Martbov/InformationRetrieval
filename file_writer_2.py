# file_creator.py
# Rolf Kuipers & Mart Busger op Vollenbroek
# Information Retrieval, Rijksuniversiteit Groningen

""" Creates files in given dictionary for later use."""

import pickle
from Brief import Brief
import uuid
import os.path
import nltk
from nltk import bigrams
from nltk import trigrams

def main(): 
	# Retrieve pickle data created by data-retriever program.
	data = pickle.load(open('data.pickle', 'rb'))

	# Select path for the two dictionaries.
	# --- In this case the doubles of instabiel/stabiel
	path1 = '/home/rolfkuipers/Dropbox/InformationRetrieval/instabieldouble'
	path2 = '/home/rolfkuipers/Dropbox/InformationRetrieval/stabieldouble'

	# Check every object for the given property
	# --- In this case instabiel or stabiel.
	for obj in data:
		f = uuid.uuid4()
		if obj.getStabClass() == 'instabiel':
			name = os.path.join(path1, f.hex)

		### OPTION 1	-- Normal text ###
			tekst = obj.Tekst()

		### OPTION 2	-- Bigrams ###
			# tekst = ""
			bigram = bigrams(tekst.split())
			for gram in bigram:
				tekst = tekst + " " + str(gram)

		### OPTION 3	-- Trigrams ###
			#trigram = trigrams(obj.Tekst().split())
			#for tri in trigram:
				#tekst = tekst + " " + str(tri)
				
			bestand = open(name, 'w')
			bestand.write(tekst)
			bestand.close()
		if obj.getStabClass() == 'stabiel':
			name = os.path.join(path2,f.hex)
		### OPTION 1	-- Normal text ###
			tekst = obj.Tekst()

		### OPTION 2	-- Bigrams ###
			# tekst = ""
			bigram = bigrams(tekst.split())
			for gram in bigram:
				tekst = tekst + " " + str(gram)

		### OPTION 3	-- Trigrams ###
			#trigram = trigrams(obj.Tekst().split())
			#for tri in trigram:
				#tekst = tekst + " " + str(tri)

			bestand = open(name, 'w')
			bestand.write(tekst)
			bestand.close()
		

main()