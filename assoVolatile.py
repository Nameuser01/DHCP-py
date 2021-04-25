#!/usr/bin/env python3
#-*-coding:utf-8-*-
import time
import random
import threading

def attribution():
	addr1 = dnsTable("www.siteweb.com")
	addr2 = dnsTable("www.serveur.com")
	addr3 = dnsTable("www.machine17.com")
	addr1.start()
	time.sleep(5)
	addr2.start()
	time.sleep(10)
	addr3.start()
	#On place un délais avant de lancer chaque thread pour que chaque nom de machine soit séparé de son ip de manière différé dans le temps

class dnsTable(threading.Thread):
	def __init__(self, nom):
		threading.Thread.__init__(self)
		assert isinstance (nom, str) and (len(nom) > 0)
		self.nom = nom
		self.a = {}
		self.ttl = 10 #le ttl vaut 10 pour des raisons pratiques

	def run(self):
		ip = ("192" + "." + "168" + "." + str(random.randint(0,255)) + "." + str(random.randint(1,253)))#host-id 16 bits, masque de 255.255.0.0
		#sur un service dns plus important il faudra penser à faire un système qui vérifie si l'adresse ip est disponible ou non
		self.a[self.nom] = ip
		for cle,valeur in self.a.items():
			print("- {} est attribué au nom {}".format(valeur, cle))
		time.sleep(self.ttl)
		del self.a[self.nom]
		#Si les valeurs ont bien été removed, alors la boucle suivante n'affiche rien
		for cle,valeur in self.a.items():
			print("! {} est toujours liée au nom {}".format(valeur, cle))


attribution()