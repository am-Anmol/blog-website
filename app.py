#import libraries
from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
app=Flask(__name__)

#code for connection
app.config['MYSQL_HOST'] = 'localhost'#hostname
app.config['MYSQL_USER'] = 'root'#username
app.config['MYSQL_PASSWORD'] = 'root'#password

app.config['MYSQL_DB'] = 'blogdata'#database name

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

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

    
    

app.run(debug=True)