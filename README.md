# MapReduce
Ce projet consiste à comprendre et à appliquer le modèle de programmation MapReduce à travers une application qui traite les données relatives au logement social.

# Choix technique
- Le Framework Hadoop qui traite et stock les données volumineuses sur un cluster <br/>
- L’architecture de développement MapReduce qui permettre de traiter des données d’une façon parallèle et distribuée<br/>
- Le langage de développement Python pour la création des déférentes parties de l’application<br/>

# Comment puis-je commencer ?
- L'enregistrement de la base de données <I>logements.txt</I> dans le HDFS:<br/>
    hadoop fs -mkdir -p logements<br/>
    hadoop fs -put Downloads/logements.txt logements<br/>
 <B>Note</B>: La base de données se trouve dans le dossier bdd<br/>
- Téléchargez le dossier <I>Python</I> qui contient les scripts<br/>
- Autorisez l’accès aux scripts :<br/>
    chmod +x /home/cloudera/menu.py<br/>
    chmod +x /home/cloudera/mapper.py <br/>
    chmod +x /home/cloudera/reducer1.py <br/>
    chmod +x /home/cloudera/reducer.py<br/>
- Exécutez le fichier <I>menu.py</I> (c'est le point d'entrée de l'application)
