#import libraries
from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
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
                return 'Logged in successfully!'+session['email']
            
            else:
                return 'Incorrect username/password!'
    

@app.route('/home')
def home():
    return render_template('home.html')

app.run(debug=True)