#!usr/bin/python3.4

# randIndex.py
# A program that calculates the Rand index based on two files with clusters and labels
# By: Mart Busger op Vollenbroek
# Completed on: 02-12-2014

import sys

class File():
	def __init__(self, cluster):
		self.cluster = cluster

	def setLabel(self, label):
		self.label = label

	def Cluster(self):
		return self.cluster

	def Label(self):
		return self.label

def main():
	file1 = open(sys.argv[1], "r")
	file2 = open(sys.argv[2], "r")

	objectList = []
	for line in file1:
		objectList.append(File(line))

	labels = []
	for line in file2:
		labels.append(line)

	for i in range(len(objectList)):
		objectList[i].setLabel(labels[i])

	file1.close()
	file2.close()

	TP = 0
	TN = 0
	FP = 0
	FN = 0

	for obj1 in objectList:
		for obj2 in objectList:
			if obj1 != obj2:
				if obj1.Cluster() == obj2.Cluster():
					if obj1.Label() == obj2.Label():
						TP += 1
					else:
						FP += 1
				else:
					if obj1.Label() == obj2.Label():
						FN += 1
					else:
						TN += 1

	randIndex = (TP + TN) / (TP + FP + FN + TN)
	print(randIndex)


if __name__ == '__main__':
	main()
