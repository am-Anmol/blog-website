import re
from flask import *
app=Flask(__name__)

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