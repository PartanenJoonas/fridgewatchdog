from flask import Flask, render_template, request
import mysql.connector
import RPi.GPIO as GPIO
import os
import datetime




app = Flask(__name__)
app.static_folder = 'static'

#Tyhjennetään välimuisti, jotta sisältö päivittyy kokonaan

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


#Yhdistetään tietokantaan

@app.route('/')


def home():
    
    con = mysql.connector.connect(user='admin',
                                  password='admin',
                                  host='localhost',
                                  database='testidb')
    
    
    
        
        
    query1 = ("SELECT * FROM testi ORDER BY row_counter DESC LIMIT 1")
    cur = con.cursor()
    
    cur.execute(query1)
    
    rows = cur.fetchall()
    cur.close()
    con.close()
    
    
    return render_template("index.html", rows=rows)

#Haetaan lämpötila-arvot ja päivämäärät ja laitetaan ne tietokantaan

@app.route('/temps')
def temps():
    #connecting to database located at localhost
    con = mysql.connector.connect(user='admin',
                                  password='admin',
                                  host='localhost',
                                  database='testidb')
    
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    timestamp = timestamp[:17]
    timestamp2 = datetime.datetime.now() - datetime.timedelta(days= 1)

    timestamp2 = str(timestamp2)
    #print(timestamp)
    #print(timestamp2[:18])
    
    timestamp3 = '2020-12-14 22:53:21'
    
    
    
    #creating cursor object
    cur = con.cursor()
    
    #use MySQL query to fetch the last 7 rows
    query1 = ("SELECT * FROM testi ORDER BY row_counter DESC LIMIT 7")
    
    #MySQL query to show testi table
    query2 = ("SELECT * FROM testi")
    
 #cur.execute("INSERT into testi (date_time, temp) values (%s,%s)", (timestamp, data 2020-12-14 22:53:%'))
    query3 = ("SELECT * FROM testi WHERE (date_time LIKE %s);")
    #execute query
    cur.execute(query3, (timestamp +'%',))
    #reading the database
    rows = cur.fetchall()
    cur.close()
    con.close()
    #inserts values into html template
    return render_template("list.html",rows=rows)





if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
    
    
    