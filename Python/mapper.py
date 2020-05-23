#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys

for line in sys.stdin:
	data = line.strip().split(";")
	if len(data) == 15:
		identifiant,adresse,code_postal,ville,annee,bailleur,nombre_total_logements,nombre_logements_PLA_I,nombre_logements_PLUS,nombre_logements_PLUS_CD,nombre_logements_PLS,mode_realisation,commentaires,arrondissement,nature_programme=data
		print "{0}\t{1}\t{2}\t{3}\t{4}".format(arrondissement,nombre_total_logements,annee,nature_programme,commentaires)

