from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

# app=Flask(__name__)
app=Flask(__name__, template_folder='Templates', static_folder='static')


#CONFIG
#db = yaml.load(open('db.yaml'))
db = yaml.safe_load(open('db.yaml'))

app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)



@app.route('/',methods = ['GET','POST'])
def index():
     #  if request.method =='POST':
        
       
     #    userDetails = request.form
     #    #email=userDetails['exampleInputEmail1']
     #    fname = userDetails['fname']
     #    lname=userDetails['lname']
     #   # seat=request.form['seat-level.value']
     #    cur = mysql.connection.cursor()
     #    cur.execute("INSERT INTO customer(email,fname,lname,form-select) Values(%s,%s,%s,%s)",(email,fname,lname,seat))
     #    mysql.connection.commit()
     #    cur.close()
     #    return 'successsss'
      return render_template("index.html")
# def index():
#     # return ('hiii')
#      return "<h1> Welcome to my Website....Enter '/home' at the end of url to navigate to home page</h1>"

@app.route('/contact')

def contact():
     return render_template("contact.html")

@app.route('/login')

def login():
     return render_template("login.html")

@app.route('/booking',methods = ['GET','POST'])

def booking():
     if request.method =='POST':
        
       
        userDetails = request.form
        email=userDetails['email']
        fname = userDetails['fname']
        lname=userDetails['lname']
        seat=userDetails['seattype']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customer(email,firstname,lastname,seattype) Values(%s,%s,%s,%s)",(email,fname,lname,seat))
        mysql.connection.commit()
        cur.close()
        return "<h1>Congratulation you have successfully registered!!!!!  TO Select Seat click or paste it in url http://127.0.0.1:5000/SelectSeat </h1>"
        return render_template("seat.html")
     return render_template("booking.html")


@app.route('/SelectSeat',methods = ['GET','POST'])
def SelectSeat():
     if request.method =='POST':
        
       
        user = request.form
        NoOfSeat=user['NoOfSeat']
        sporttype=user['sporttype']
        seattype=user['seatType']
        cur = mysql.connection.cursor()
     #    cur.execute("INSERT INTO customer.(NoOfSeat,sporttype,seatType) Values(%s,%s,%s)",(NoOfSeat,sporttype,seattype))
        cur.execute("INSERT INTO customer.seat(NoOfSeat,sporttype,seatType) Values(%s,%s,%s)",(NoOfSeat,sporttype,seattype))
          #    cur.execute("INSERT INTO customer(NoOfSeat,sporttype) Values(%s,%s)",(NoOfSeat,sporttype))
        mysql.connection.commit()
        cur.close()
          #return (seattype+ sporttype)*NoOfSeat
        return "<h1>Congratulation your seat has been reserved </h1>"
     return render_template("seat.html")


if __name__ == "__main__":
    app.run(debug=True)
