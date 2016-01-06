import pickle
from Brief import Brief
import uuid
import os.path

def main(): 
	# Geef elk document de juiste klasse.

	data = pickle.load(open('data.pickle', 'rb'))
	
	path1 = '/home/rolf/Dropbox/InformationRetrieval/onzorgvuldig'
	path2 = '/home/rolf/Dropbox/InformationRetrieval/zorgvuldig'
	for obj in data:
		f = uuid.uuid4()
		if obj.getZorgClass() == 'onzorgvuldig':
			name = os.path.join(path1, f.hex)
			bestand = open(name, 'w')
			bestand.write(obj.Tekst())
			bestand.close()
		if obj.getZorgClass() == 'zorgvuldig':
			name = os.path.join(path2,f.hex)
			bestand = open(name, 'w')
			bestand.write(obj.Tekst())
			bestand.close()
		

main()