#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys


TotalLogements=0
oldarr=None
#print "Type de logement\tNombre de logements"
for line in sorted(sys.stdin, key=lambda line: line.split('\t')[3]):
#for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) ==5:
		arr, nombreLogement,annee,nature,commentaire=data
	if len(data) ==4:
		arr, nombreLogement,annee,nature=data
	if len(data) ==3:
		arr, nombreLogement,annee=data
	
	if oldarr and oldarr != nature:
		print "Type de logements:{0}\t\tNombre de logements:{1}".format(oldarr,TotalLogements)
		TotalLogements=0
	oldarr=nature
	TotalLogements += int(nombreLogement)
if oldarr != None:
	print "Type de logements:",oldarr,"\t\tNombre de logements:", TotalLogements