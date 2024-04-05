import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'passowrd123'

	)

# preparar um objeto
cursorObject = dataBase.cursor()

# Criar datbase
cursorObject.execute("CREATE DATABASE Uivesp")

print("tudo certo até aqui")
