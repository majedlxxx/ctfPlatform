import sqlite3
def saveUser(nu):
	conn=sqlite3.connect("ctf.db")
	#insert into account values("majed","pass12");
	command='insert into account(username,password) values("'
	command+=nu["username"]
	command+='","'
	command+=nu["password"]
	command+='");'
	conn.execute(command)
	conn.commit()
	conn.close()
                                                                                                       
def listUsers():
	users=open("database","r").read().split("\n")
	return users

saveUser({"username":"majed","password":"pass123"})