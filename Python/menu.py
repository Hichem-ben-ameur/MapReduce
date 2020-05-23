#!/usr/bin/env python
import os


def action1():
	    
	commande1 = 'hadoop fs -rm -r -R logements-output1'
	commande2 = 'hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar  -file /home/cloudera/mapper.py    -mapper /home/cloudera/mapper.py  -file /home/cloudera/reducer.py   -reducer /home/cloudera/reducer.py  -input /user/cloudera/logements/* -output /user/cloudera/logements-output1'
	commande3 = 'hadoop fs -tail logements-output1/part-00000'
	os.system(commande1)
	os.system(commande2)
	os.system(commande3)
	print "\n Merci de verifier le dossier '/user/cloudera/logements-output1'"

def action2():

   	commande1 = 'hadoop fs -rm -r -R logements-output2'
	commande2 = 'hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar  -file /home/cloudera/mapper.py    -mapper /home/cloudera/mapper.py  -file /home/cloudera/reducer2.py   -reducer /home/cloudera/reducer2.py  -input /user/cloudera/logements/* -output /user/cloudera/logements-output2 | sort -k4'
	commande3 = 'hadoop fs -tail logements-output2/part-00000'
	os.system(commande1)
	os.system(commande2)
	os.system(commande3)
	print "\n Merci de verifier le dossier '/user/cloudera/logements-output2'"


def no_such_action():
   return

def main():
    actions = {"1": action1, "2": action2}
    while True:
	print "\n"
        print "\t********* Menu **********\n"
	print "Tapez 1 pour calculer le nombre de logements par arrondissement"
	print "Tapez 2 pour calculer le nombre de logements par type (Exemple : logement familial, residence pour etudiants etc ...)"
	print "Tapez 3 pour quitter l'application"
        selection = raw_input("Votre choix: ")
        if "3" == selection:
            return
        toDo = actions.get(selection, no_such_action)
        toDo()

if __name__ == "__main__":
    main()
