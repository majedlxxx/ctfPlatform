from flask import Flask, request, jsonify, render_template                                                                       
import os           
import hashlib
import sqlite3

def hash(string):
	hashedPass=hashlib.md5(string.encode()).digest()
	hashedPass=hashedPass.hex()
	return hashedPass

def saveUser(nu):
	database=open("database","a")
	database.write(nu["username"]+":"+nu["password"]+"\n")
	database.close()
                                                                                                       
def listUsers():
	users=open("database","r").read().split("\n")
	return users

                                                                                                           
app = Flask(__name__)       
@app.route("/",methods=['GET'])
def home():
	return "<h1>Hello</h1>"

@app.route("/user",methods=["GET"])
def user():
	return open("user.html", "r").read()

@app.route("/login" , methods=['POST'])
def login():
	form=request.form
	username=form["username"]
	password=form["password"]
	password=hash(password)
	print("*"*10)
	print(username+":"+password)
	print(listUsers())
	if (username+":"+password) in listUsers():
		return "<h1>You have logged in successfuly</h1>"
	else:
		return '<h1>Invalid credentials</h1><a href="/user">try again</a>'



@app.route("/admin",methods=['GET'])
def admin():
	return open("admin.html","r").read()

@app.route("/newuser",methods=['POST'])
def newUser():
	data=request.form
	username=data["username"]
	pass1=data["password"]
	pass2=data["password2"]
	adminpass=data["adminpass"]
	users=listUsers()
	for user in users:
		if username in user:#use:pass
			return "User already exists"
	if pass1!=pass2:
		return "Passwords didn't match"

	hashedPass=hash(pass1)
	nu={}
	nu["username"]=username
	nu["password"]=hashedPass
	saveUser(nu)
	return "New user has been successfuly created"


if __name__ == '__main__':
  app.run('0.0.0.0')











                                                                                 
# @app.route('/admin', methods=['GET'])                                                                                                  
# def adminPanel():                                                                                                     
#   return open("admin.html").read()                                                                                          

# @app.route('/newuser',methods=['POST'])
# def newUser():
#   return "new user"     

# @app.route("/", methods=['GET'])
# def homePage():
# 	print(request.username)
#   return open("ctf.html").read()   

# @app.route("/login", methods=['GET'])
# def challenge1():
#   return open("index.html").read()                                                                                                        

# @app.route("/ff", methods=['GET'])
# def challenge2():
#   return "flag{y0u've_found_@noth3r_one}" 

# # @app.route('/admin', methods=['GET', 'POST'])                                                                     
# # def codeSubmit():                                                                                                
# #     if request.method == 'POST':                                                                                 
# #         language= request.get_json()['language']                                                                 
# #         code= request.get_json()['code']                                                                         
# #         print(code)
# #         print(language)
# #         '''
# #         os.system("rm code.py")
# #         open("code.py","w").write(code)
# #         result= str(subprocess.check_output('python3 code.py' , shell=True))[2:-1]
# #         print(result)
# #         return jsonify({'result': result})
# #         '''
# #     else:
# #         return "hello"

