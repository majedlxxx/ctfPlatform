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
	conn=sqlite3.connect("ctf.db")
	cursor=conn.execute("select * from account;")
	users=cursor.fetchall()
	return users

def validateLogin(username,password):
	conn=sqlite3.connect("ctf.db")
	command='select username from account where username="'+username+'" and password="'+password+'";'
	print(command)
	cursor=conn.execute(command)
	return len(cursor.fetchall())>0





#select username from account where username="input1" and password="hash(input2)";
#username:	
	#majed"; --
	#" or 1=1; --
	#majed" and password=(select password from account where username="majed"); -- 

#select username from account where username="input" and password="32250170a0dca92d53ec9624f336ca24";
#"(select username from account where password="32250170a0dca92d53ec9624f336ca24")"
#"

