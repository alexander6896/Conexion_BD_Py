import MySQLdb 

myDB = MySQLdb.connect(host="192.168.1.67",
                        port=3306,
                        user="alexander",
                        passwd="vladimir",
                        db="regitstro") 
cHandler = myDB.cursor() 
cHandler.execute("SHOW DATABASES") 
results = cHandler.fetchall() 
for items in results: 
    print items[0] 