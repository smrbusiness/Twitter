#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb, getpass
conex = MySQLdb.connect("192.168.2.107","root","cMADrid15","TWITTER")
cursor = conex.cursor()

listasi=['S','s','SI','SÍ','Sí','Si','sí','si','Y','y','YES','Yes','yes']
listano=['N','n','NO','No','no']

fallos=3

def addseguidor(consultaseguir, gente):
	cursor.execute(consultaseguir, (seguidor, user))
def addtweet(consultatweet, texto):
	cursor.execute(consultatweet, (user,tweet))
def addborrarusur(consultaborrarusur,texto):	
	cursor.execute(consultaborrarusur, id_usuario)
def addborrarseguir(consultaborrarseguir,texto):	
	cursor.execute(consultaborrarseguir, (id_usuario,usuario))
def dejarseguir(consulta,texto):
	cursor.execute(consultadejarseguir,(id_usuario,user))
def mirartweets(consultamirartweets, texto):
	cursor.execute(consultamirartweets, id_usuario)
def borrartweets(consulta, id_user):
	cursor.execute(consultaborrartweets, id_usuario)
def login(consulta, parametros):
	cursor.execute(consultalogin,(user, contra))
def register(consulta, parametros):
	cursor.execute(consultacrearusur,(ID,Nombre,Clave))
def verseguidores(consulta, nombre):
	cursor.execute(consultaverseguidores,nombre)
def fail(consulta,nombre):
	cursor.execute(consultafallos,user)
def block(consulta,nombre):
	cursor.execute(consultablock,user)
def bloqueo(consulta,nombre):
	cursor.execute(consultabloqueo,user)
def desbloqueo(consulta, nombre):
	cursor.execute(consultadesbloqueo, usuario)
def tweets(consulta,texto):
	cursor.execute(consultatweetseguidos, user)
def usuarios(consulta,texto):
	cursor.execute(consultausuarios,user)
def existe(consulta,texto):
	cursor.execute(consultaexiste,(seguidor,user))
def seguidores(consulta,texto):
	cursor.execute(consultaseguidores,user)
def busqueda(consulta,texto):
	cursor.execute(consultabusqueda,abuscar)
def existe2(consulta,texto):
	cursor.execute(consultaexiste2,seguidor)
def fav(consulta,parametros, cursor, conex):
	cursor.execute(consultafav,(id_fav, user))
	conex.commit()
def vertweets(consultavertweets, texto):
	cursor.execute(consultavertweets, user)
def borradotweets(consulta, id_user):
	cursor.execute(consultaborradotweets, id_tweet)
def verfavs(consulta,texto):
	cursor.execute(consultaverfavs,id_usuario)
	

consultaseguir='insert into seguidores(id_usuario, seguidor) values(%s,%s);' #para seguir a un usuario
consultatweet='insert into tweets (id_usuario,tweet,fecha) values(%s,%s,curdate());' #para tweetear
consultaborrarusur='delete from usuarios where id = %s;' #borrar usuarios de la tabla usuarios
consultaborrarseguir='delete from seguidores where id_usuario=%s or seguidor=%s;' #borra usuarios de la tabla seguidores
consultaborrartweets='delete from tweets where id_usuario=%s;' #borra usuarios de la tabla tweets
consultamirartweets='select id_tweet,id, tweet, fecha from usuarios, tweets where id_usuario=id and id = %s;' #enseña los tweets de un usuario
consultalogin='select count(id) from usuarios where id=%s and Contra=%s;' #comprueba si tu usuario y contraseña son correctos
consultacrearusur="insert into usuarios(id,Nombre,Contra) values(%s,%s,%s);" #crea usuario
consultaverseguidores="select seguidor from seguidores where id_usuario=%s;" #muestra los seguidores de un usuario
consultafallos="insert into conexionesfail(id_usuario,Fecha) values (%s,now());" #graba las conexiones fallidas en conexionesfail
consultablock='update usuarios set Block= "si" where id =%s and id !="admin" ;' #bloquea usuarios
consultabloqueo='select count(Block) from usuarios where id=%s;' #Mira si el usuario esta bloqueado
consultadesbloqueo='update usuarios set Block=null where id=%s;' #Desbloqueo de usuario
consultatweetseguidos='select seguidores.id_usuario ,tweets.tweet, tweets.fecha from seguidores,tweets where seguidores.seguidor=%s and tweets.id_usuario = seguidores.id_usuario;' #tweets de los seguidos
consultausuarios='select id from usuarios where id!="admin" and id!=%s;' #listado de los usuarios a seguir
consultaexiste='select count(id_usuario) from seguidores where id_usuario=%s and seguidor=%s;' #mira si existe el usuario
consultaexiste2='select count(id) from usuarios where id=%s;'
consultadejarseguir='delete from seguidores where id_usuario=%s and seguidor=%s;' #borrar seguidores
consultaseguidores='select * from seguidores where seguidor=%s;'
consultabusqueda='select id_usuario,tweet from tweets where tweet like %s;'
consultafav='insert into favs(id_tweet, id_usuario) values(%s,%s);'
consultatodostweets='select * from tweets'
consultavertweets='select id_tweet,id, tweet, fecha from usuarios, tweets where id_usuario=id and id = %s;'
consultaborradotweets='delete from tweets where id_tweet=%s;'
consultaverfavs='select tweets.tweet, tweets.id_usuario from tweets inner join favs where favs.id_usuario=%s and tweets.id_tweet = favs.id_tweet;'


registro=raw_input("¿Eres un usuario registrado? (si/no): ")
if registro in listasi:
	while fallos != 0:

		user=raw_input('Dime el usuario: ')
		contra=getpass.getpass('Dame la contraseña: ')

		login(consultalogin,(user, contra))
		resultado=cursor.fetchone()
		bloqueo(consultabloqueo,user)
		resultado2=cursor.fetchone()
		if resultado2[0] == 1:
			print "Este usuario esta bloqueado entre con el usuario root y desbloque el usuario "+ user 
		if resultado[0] == 1 and resultado2[0] == 0:
			print 'Acceso permitido'
			if user == 'admin':
				Menuroot = ["","F Borrar usuarios","G Desbloqueo usuarios", ""]
				for i in Menuroot:
					print i
				tecla = raw_input('¿Qué opción quieres?: ')
				if  tecla == 'F' or tecla == 'F': #OK
					bucle = "si"
					while bucle in listasi:
						id_usuario=raw_input('Dame el usuario a borrar: ')
						usuario=raw_input('Por favor confirme ese usuario: ')
						addborrarusur(consultaborrarusur,id_usuario)
						addborrarseguir(consultaborrarseguir,(id_usuario,usuario))
						borrartweets(consultaborrartweets,id_usuario)
						bucle=raw_input('¿Quieres borrar mas usuarios?: ')
					conex.commit()
				if tecla == 'G' or tecla == 'g':
					usuario=raw_input('¿Qué usuario queres desbloquear?: ')
					desbloqueo(consultadesbloqueo, usuario)
					conex.commit()
			else:
				usarprograma = 'si'
				while usarprograma == 'si':
					Menu = ["","----------------------------MENÚ----------------------------","A Seguir a alguien/Dejar de seguir","B Crear/Borrar Tweet","C Mirar tweets ","D Mostrar seguidores","E Tweets de gente a la que sigues","F Buscar tweets","G Dar favorito","H Ver favoritos","S Cerrar sesión","X Cerrar programa","------------------------------------------------------------",""]
					for i in Menu:
						print i
					tecla = raw_input('¿Qué opción quieres?: ')
					if tecla == 'A' or tecla == 'a': 
						bucle = "si"
						while bucle in listasi:
							menu=["","1 - Seguir","2 - Dejar de seguir",""]
							for i in menu:
								print i
							tecla2 = raw_input('¿Qué opcion quieres?: ')
							if tecla2 == "1":
								usuarios(consultausuarios,user)
								jota=cursor.fetchall()
								print "Los usuarios a quienes puedes seguir son: "
								print ""
								for i in jota:
									print i[0]
								seguidor=raw_input('Dime a quien quieres seguir: ')
								existe(consultaexiste,(seguidor,user))
								resultado=cursor.fetchone()
								existe2(consultaexiste2,seguidor)
								resultado2=cursor.fetchone()

								if resultado[0] == 0 and seguidor != user and resultado2[0] == 1:
									addseguidor(consultaseguir,(user, seguidor))
									conex.commit()
								else:
									print "USUARIO NO VALIDO"	
							elif tecla2 == "2":
								seguidores(consultaseguidores,user)
								jota=cursor.fetchall()
								print "Los usuarios a quienes puedes dejar de seguir son: "
								print ""
								for i in jota:
									print i[0]
								id_usuario=raw_input('Dime a quien quieres dejar de seguir: ')
								dejarseguir(consultadejarseguir,(id_usuario,user))
							bucle=raw_input("¿Quieres seguir/dejar de seguir a alguien más?: ")

						conex.commit()

					elif tecla == 'B' or tecla == 'b': #OK
						bucle = "si"
						while bucle in listasi:
							menu=["","1 - Crear tweet","2 - Borrar tweet",""]
							for i in menu:
								print i
							tecla2 = raw_input('¿Qué opción quieres?: ')
							if tecla2 == "1":
								tweet=raw_input('¿Qué tweet quieres poner?: ')
								if len(tweet) <= 140:
									fecha='' 
									addtweet(consultatweet,(user, tweet))
									bucle=raw_input('¿Quieres poner más tweets?: ')
									conex.commit()							
								else:
									print 'Has introducido demasiados caracteres'
							if tecla2 =="2":
								bucle ="si"
								while bucle in listasi:
									resultado=vertweets(consultavertweets,user)
									resultado=cursor.fetchall()
									for fila in resultado:
										print fila[0],"-", fila[1],"-", fila[2]
									id_tweet=input("Indique el número del tweet que quiere borrar: ")
									borradotweets(consultaborradotweets,id_tweet)
									bucle = raw_input("¿Quieres borrar más tweets?: ")

					elif tecla == 'C' or tecla == 'c': #OK
						bucle = "si"
						while bucle in listasi:
							id_usuario=raw_input('¿De que usuarios quieres ver los tweets?: ')
							resultado=mirartweets(consultavertweets,id_usuario)
							resultado=cursor.fetchall()
							for fila in resultado:
								print fila[0],"-", fila[1],"-", fila[2]
							bucle=raw_input("¿Quieres ver mas tweets?: ")
					elif tecla == 'D' or tecla == 'd':
						nombre=raw_input('¿De que usuarios quieres ver los seguidores?: ')
						verseguidores(consultaverseguidores,nombre)
						resultado=cursor.fetchall()
						print "Los seguidores de " + nombre + " son: " 
						for i in resultado:
							print i[0]

					elif tecla== 'e' or tecla == 'E':
						tweets(consultatweetseguidos,user)
						resultado=cursor.fetchall()
						print "Los tweets de las personas a las que sigues son: "
						for i in resultado:
							print i[0],"-",i[1]	

					elif tecla== 'f' or tecla == 'F':		
						abuscar=raw_input("¿Qué palabras quieres buscar? (Entre porcentajes): ")
						busqueda(consultabusqueda,abuscar)
						resultado = cursor.fetchall()
						print "Los resultados de la búsqueda son: "
						print ""
						for i in resultado:
							print i[0],"-",i[1]	
					elif tecla== 'g' or tecla == 'G':
						cursor.execute(consultatodostweets)
						resultado = cursor.fetchall()
						for i in resultado:
							print i[1], "-", i[0], "-", i[2], "-", i[3]     
						print ""
						id_fav=input("Dame la id del tweet al que quieres dar favorito: ")
						cursor.execute(consultafav,(id_fav, user))
						conex.commit()
						print "Favorito guardado"
					elif tecla== "h" or tecla == "H":
						usuarios(consultausuarios,user)
						jota=cursor.fetchall()
						print "Los usuarios de quienes puedes ver los favoritos son: "
						print ""
						for i in jota:
							print i[0]
						id_usuario=raw_input("¿De que usuario quieres ver los favoritos?: ")
						print ""
						verfavs(consultaverfavs,id_usuario)
						resultado=cursor.fetchall()
						for i in resultado:
							print i[0],"-",i[1]
					elif  tecla == 'S' or tecla == 's':
						usarprograma = 'no'
					elif tecla == 'X' or tecla =='x':
						exit()
				
		else:
			print 'Acceso denegado'
			fallos -= 1
			print "Te quedan " + str(fallos) + " intentos"
			fecha=''
			fail(consultafallos,user)
			conex.commit()
			if fallos==0:
				block(consultablock,user)
				print "Este usuario ha sido bloqueado"


elif registro in listano:
	ID = raw_input("Dame tu usuario (@...): ")
	while ID[0] != "@":
		print 'Tu nombre de usuario debe de empezar por @'
		ID = raw_input("Dame tu usuario (@...): ")
	Nombre = raw_input("Dame tu nombre real: ")
	Clave = getpass.getpass("Dame la contraseña que quieres: ")
	Clave2 = getpass.getpass("Confirma la contraseña que quieres: ")
	while Clave != Clave2:
		print "Las claves que has introducido no coinciden"
		Clave = getpass.getpass("Dame la contraseña que quieres: ")
		Clave2 = getpass.getpass("Confirma la contraseña que quieres: ")
	register(consultacrearusur,(ID,Nombre,Clave))
	print "Enhorabuena te has regsitrado satisfactoriamente, vuelve a ejecutar el programa para iniciar sesión. "
else:
	print "Eres tonto macho pero sabes leer o que, que pongas Si o No "

conex.commit()
cursor.close()
conex.close()