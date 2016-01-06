#!/usr/bin/Python3.4

# Brief.py
# Rolf Kuipers & Mart Busger op Vollenbroek
# Information Retrieval, Rijksuniversiteit Groningen

import nltk
from nltk import stem
#from nltk.corpus import stopwords

class Brief:
	def __init__(self, ID):
		self.ID = ID

	def setTekst(self, tekst):
		self.tekst = tekst

		tokens = nltk.word_tokenize(self.tekst)
		#newtokens = [w for w in tokens if w.lower() not in stopwords.words('dutch')]
		#snowball = stem.snowball.DutchStemmer()
		porter = stem.porter.PorterStemmer()
		stemming = [porter.stem(i) for i in tokens]
		self.tekst = " ".join(stemming)

	def setInnovatie(self, innovatie):
		self.innovatie = float(innovatie)

		if self.innovatie < 3.0:
			self.innoclass = 'non-innovatief'
		if self.innovatie == 3.0:
			self.innoclass = 'neutraal'
		if self.innovatie > 3:
			self.innoclass = 'innovatief'

	def getInnoClass(self):
		return self.innoclass

	def setExtraversie(self, extraversie):
		self.extraversie = float(extraversie)

		if self.extraversie < 3.0:
			self.extraclass = 'introvert'
		if self.extraversie == 3.0:
			self.extraclass = 'neutraal'
		if self.extraversie > 3.0:
			self.extraclass = 'extravert'

	def getExtraClass(self):
		return self.extraclass

	def setVriendelijkheid(self,vriendelijkheid):
		self.vriendelijkheid = float(vriendelijkheid)

		if self.vriendelijkheid < 3.0:
			self.vriendclass = 'onvriendelijk'
		if self.vriendelijkheid == 3.0:
			self.vriendclass = 'neutraal'
		if self.vriendelijkheid > 3.0:
			self.vriendclass = 'vriendelijk'

	def getVriendClass(self):
		return self.vriendclass

	def setStabiliteit(self, stabiliteit):
		self.stabiliteit = float(stabiliteit)

		if self.stabiliteit < 3.0:
			self.stabclass = 'instabiel'
		if self.stabiliteit == 3.0:
			self.stabclass = 'neutraal'
		if self.stabiliteit > 3.0:
			self.stabclass = 'stabiel'

	def getStabClass(self):
		return self.stabclass

	def setZorgvuldigheid(self,zorgvuldigheid):
		self.zorgvuldigheid = float(zorgvuldigheid)

		if self.zorgvuldigheid < 3.0:
			self.zorgclass = 'onzorgvuldig'
		if self.zorgvuldigheid == 3.0:
			self.zorgclass = 'neutraal'
		if self.zorgvuldigheid > 3.0:
			self.zorgclass = 'zorgvuldig'

	def getZorgClass(self):
		return self.zorgclass

	def Tekst(self):
		return self.tekst

	def Extraversie(self):
		return self.extraversie

	def Innovatie(self):
		return self.innovatie

	def Vriendelijkheid(self):
		return self.vriendelijkheid

	def Stabiliteit(self):
		return self.stabiliteit

	def Zorgvuldigheid(self):
		return self.zorgvuldigheid

