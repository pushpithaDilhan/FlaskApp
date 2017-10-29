from flask import Flask,render_template,request,redirect,jsonify
from flaskext.mysql import MySQL
from flask_restful import Resource,Api,reqparse

#add postman chrome extension to check the requests

#create flask app
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'demoapplication'
app.config['MYSQL_PORT'] = '3306'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)
api = Api(app)
conn = mysql.connect()
cur = conn.cursor()

#---------------------------------------------------------------------------------------------------------------------
class GetUser(Resource):
    def get(self,uid):
        cur.execute("SELECT uid,fname,lname,bdate FROM user WHERE uid="+uid)
        rv = cur.fetchone()
        if str(rv)=="None":
            return jsonify({"status":"Not found"})
        else:
            return jsonify({'uid':rv[0],'fname':rv[1],'lname':rv[2],'bdate':rv[3]})

api.add_resource(GetUser, '/api/user/<string:uid>')

class GetUsers(Resource):
    def get(self):
        cur.execute("SELECT uid,fname,lname,bdate FROM user")
        rv = cur.fetchall()
        users = []
        if str(rv)=="None":
            return {"status":"Not found"}
        else:
            for data in rv:
                users.append({'uid':data[0],'fname':data[1],'lname':data[2],'bdate':data[3]})                
            return users

api.add_resource(GetUsers, '/api/users')

@app.route("/")
def main():
    return render_template("index.html")
#----------------------------------------------------------------------------------------------------------------
@app.route("/adduser",methods=['GET','POST'])
def adduser():
    if request.method == 'POST':
        return do_register(request)
    else:
        return render_template("adduser.html")
def do_register(request):
    fname = request.form['fname']
    lname = request.form['lname']
    bdate = request.form['bday']
    username = request.form['uname']
    password = request.form['pwd']
    cur.execute("SELECT MAX(uid) FROM user")
    rv = cur.fetchone()
    uid = int(rv[0])+1      
    cur.execute("INSERT INTO user ( uid, fname, lname, bdate, username, password ) VALUES (%s, %s, %s, %s, %s, %s)",(str(uid),fname,lname,bdate,username,password))
    conn.commit()
    return redirect("/")

@app.route("/remove/<string:uid>",methods=['GET'])
def removeUser(uid): 
    cur.execute("DELETE FROM user WHERE uid= %s",(uid)) 
    conn.commit()
    return redirect("/viewusers")

@app.route("/adduser/<string:uid>",methods=['GET','POST'])
def updateUser(uid):
    if request.method == 'POST':
        return do_update(request,uid)
    else:
        cur.execute("SELECT uid,fname,lname,bdate,username FROM user WHERE uid="+uid)
        rv = cur.fetchone()
        return render_template("adduser.html",user={'uid':rv[0],'fname':rv[1],'lname':rv[2],'bdate':rv[3],'username':rv[4]})  

def do_update(request,uid):
    cur.execute("DELETE FROM user WHERE uid= %s",(uid))
    fname = request.form['fname']
    lname = request.form['lname']
    bdate = request.form['bday']
    username = request.form['uname']
    password = request.form['pwd']
    cur.execute("INSERT INTO user ( uid, fname, lname, bdate, username, password ) VALUES (%s, %s, %s, %s, %s, %s)",(str(uid),fname,lname,bdate,username,password))
    conn.commit()
    return redirect("/viewusers") 

@app.route("/viewusers")
def viewUsers():
    usersAPI = GetUsers()
    return render_template("viewusers.html",users = usersAPI.get())

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_login(request)
    else:
        return render_template("login.html")

def do_login(request):
    username = request.form['username']
    password = request.form['password']
    role = 'role' in request.form
    error_msg = "Invalid Username or Password"
    if role:
        #admin check
        cur.execute("SELECT fname FROM user WHERE username=%s and password=%s",(username,password))
        rv = cur.fetchone()
        if rv != None:
            return render_template("admindashboard.html",admin = rv[0])
        else:
            return render_template("login.html", error = error_msg)        
    else:
        #user check
        cur.execute("SELECT fname FROM admin WHERE username=%s and password=%s",(username,password))
        rv = cur.fetchone()
        if rv != None:
            return render_template("userdashboard.html" , user = rv[0])
        else:
            return render_template("login.html", error = error_msg)


if __name__ == "__main__":
    app.run(debug=True)
