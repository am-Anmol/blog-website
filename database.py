from flask import *
app=Flask(__name__)
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'blogdata'

mysql = MySQL(app)

@app.route("/")
def save():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO User(Name,Email,Password) VALUES (%s, %s,%s)", ("Anmol", 'anmol@test.com','123456'))
    mysql.connection.commit()
    cur.close()
    return render_template('index.html')

app.run(debug=True)
