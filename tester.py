import nltk
from nltk import trigrams

def main():
	tekst = "Het Rijkstraineeship past perfect bij mij , omdat ik mijzelf graag verder wil ontwikkelen en tegelijkertijd mijn steentj kan bijdragen aan het oplossen van maatschappelijk problemen . Tijden mijn studi en werk al onderzoek heb ik mij bezig gehouden met criminologisch en sociologisch vraagstukken rondom criminaliteit en veiligheid . Deze kenni zou ik graag willen toepassen in de praktijk . In plaat van het enkel analyseren van beleid , zoal ik tot nu toe heb gedaan , wil ik ook graag helpen met het ontwikkelen en uitvoeren van beleid . Dit trekt mij aan , omdat ik dan meer kan samenwerken , overleg kan voeren en communicatief en creatief bezig kan zijn dan in mijn huidig werk al onderzoek . Daarnaast geeft het Rijkstraineeship mij de kan om me bezig te ( blijven ) houden met interessant maatschappelijk onderwerpen , zoal veiligheid , criminaliteit en integrati . Ik vind het ook leuk om mij breed te oriënteren op verschillend onderwerpen . Tenslott kan ik mezelf al Rijkstraine ontwikkelen op divers gebieden , zowel inhoudelijk al persoonlijk . Ik wil graag meer leren om nog meer uit mijzelf en mijn werk te kunnen halen . Mijn maatschappelijk betrokkenheid blijkt onder ander uit mijn keuz voor studi en werk . Ik heb sociologi en criminologi gestudeerd met een specialisati in beleid . Voor mijn tweed master heb ik bijvoorbeeld onderzoek gedaan naar de aanpak van mensenhandel door de strafrechtsketen in Nederland . Ook werk ik op dit moment al junior onderzoek en beleidsadviseur van criminaliteit- en veiligheidsbeleid bij een onderzoeksbureau . Mijn maatschappelijk betrokkenheid blijkt ook uit het vrijwilligerswerk dat ik heb gedaan . Zo heb ik in het hoofdbestuur gezeten van CNV Jongeren . Hier heb ik mij onder ander bezig gehouden met leeftijdsdiscriminati van jongeren die werken in supermarkten en discriminati van allochton jongeren bij het vinden van een stage . Ook heb ik een zomerkamp helpen organiseren voor buitenlands jongeren die daar vaak zelf de financiël middelen niet voor hebben . Het doel van dit kamp wa om deze jongeren meer te leren van elkaar cultuur om het onderling begrip tussen landen te bevorderen . Ten slott heb ik vrijwilligerswerk verricht bij de studentenverenig SIB in Utrecht . Ik ben in die tijd voorzitt geweest van Cultura . Hier voor heb ik verschillend culturel uitj georganiseerd naar onder meer musea , buitenlands restaur en film ."
	tokens = nltk.word_tokenize(tekst)
	x = trigrams(tokens)
	string = ""
	for i in x:
		string = string + " " + str(i)



	print(string)

main()