#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys


TotalLogements=0
oldarr=None
print "Arrondissement\tNombre de logements"
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) ==5:
		arr, nombreLogement,annee,nature,commentaire=data
	if len(data) ==4:
		arr, nombreLogement,annee,nature=data
	if len(data) ==3:
		arr, nombreLogement,annee=data
	
	if oldarr and oldarr != arr:
		print "{0}\t\t{1}".format(oldarr,TotalLogements)
		TotalLogements=0
	oldarr=arr
	TotalLogements += int(nombreLogement)
if oldarr != None:
	print oldarr,"\t\t", TotalLogements