#import libraries
from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
import time
app=Flask(__name__)
app.secret_key = "4db8b51a4017e427f3ea5c2137c450f767dce1bf"  

#code for connection
app.config['MYSQL_HOST'] = 'localhost'#hostname
app.config['MYSQL_USER'] = 'root'#username
app.config['MYSQL_PASSWORD'] = '1234'#password

app.config['MYSQL_DB'] = 'blogdata'#database name

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/savedetails',methods=['GET', 'POST'])

def savedetails():
    if request.method == "POST":
            UN = request.form['full_name']
            EMAIL = request.form['email']
            PSS = request.form['password']
            cur = mysql.connection.cursor()
            
            
            Name = UN
            Email = EMAIL
            Password = PSS
            cur.execute("INSERT INTO User(Name, Email, Password) VALUES (%s, %s, %s)", (Name, Email, Password))
            mysql.connection.commit()
            cur.close()
            return 'success'
    
@app.route('/add')
def add():
    return render_template('addblog.html')

@app.route('/saveblog',methods=['GET', 'POST'])
def saveblog():
    if request.method == "POST":
            BT = request.form['blogtitle']
            BC = request.form['blogcontent']
            IMG = request.form['blogimage']
            cur = mysql.connection.cursor()
            
            
            blogTitle = BT
            blogDesc = BC
            blogImg = IMG
            createTime = time.strftime('%Y-%m-%d %H:%M:%S')
            UserId = session['userid']
            isActive = 'true'
            cur.execute("INSERT INTO blogs(blogTitle, blogDesc, blogImg, createTime, UserId, isActive) VALUES (%s, %s, %s, %s, %s, %s)", (blogTitle, blogDesc, blogImg, createTime, UserId, isActive))
            mysql.connection.commit()
            cur.close()
            return render_template('home.html')


@app.route('/logged',methods=['GET', 'POST'])

def loggedin():
    if request.method == "POST":
            EMAIL = request.form['email']
            PSS = request.form['password']
            cur = mysql.connection.cursor()

            cur.execute('SELECT * FROM user WHERE email = %s AND password = %s', (EMAIL, PSS,))
            account = cur.fetchone()
            if account:
                session['loggedin'] = True
                session['userid']=account[0]
                session['email'] = account[2]
                return redirect("/home")
            
            else:
                return 'Incorrect username/password!'
    

@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM blogs where isActive='true'")
    blog = cur.fetchall()
    return render_template('home.html',blogData=blog)

@app.route('/logout')  
def logout():
   session.pop('email', None)
   session.pop('userid', None)
   return render_template('index.html')

app.run(debug=True)