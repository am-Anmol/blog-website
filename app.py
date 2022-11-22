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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/savedetails',methods=['POST'])

def savedetails():
    UN = request.form['full_name']
    EMAIL = request.form['email']
    PSS = request.form['password']

    
    
    Username = UN
    Email = EMAIL
    Password = PSS
    
 


    
    

app.run(debug=True)