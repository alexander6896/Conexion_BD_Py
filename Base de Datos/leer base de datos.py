import MySQLdb

db = MySQLdb.connect(host="192.168.1.67",    # tu host, usualmente localhost
                     port=3306,
                     user="alexander",         # tu usuario
                     passwd="vladimir",  # tu password
                     db="regitstro")        # el nombre de la base de datos

cursor = db.cursor()
print"Cual es el No. de control"
nocontrol=input()
print"El no control es: ",nocontrol

#Consulta hacia la Base de Datos
sql = "Select * From persona where dni='%s'" % nocontrol

cursor.execute(sql)
result = cursor.fetchall()
impreso = result
print impreso
#if result is not None:
  #  for row in result:
 #       print row
#else:
#    print"no hay datos en la tabla"
#print(cursor)

#Se cierra la conexion a la base de datos
cursor.close()
