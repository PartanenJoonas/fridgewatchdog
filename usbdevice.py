import serial
import time
from datetime import datetime
import mysql.connector
from camera import Camera

#yhdistetään tietokantaan ja tehdään camera kirjastosta olio
#määritetään sarjaportti, jotta saadaan nucleolta dataa
cnx = mysql.connector.connect(user='admin', password='admin', host='localhost', database='testidb')
cur = cnx.cursor()
cm = Camera()

time.sleep (1)

ser=serial.Serial("/dev/ttyACM0",9600)

state = 0

#while-loop lukemaan sarjaportilta dataa ja päivittämään ne tietokantaan
while True:
    
    
    data_raw = ser.readline().decode().strip()
    
    data = str(data_raw)
    
    #jos valo käy päällä otetaan kuva
    if data == "on":
        if state == 1:
            #nothing
            print("a")
        else:       
            cm.take_picture()
            state = 1
        
    elif data == "off":
        if state == 0:
            #nothing
            print("b")
        else:
            state = 0
    else:
        
        #jos sarjaportilta tulee ulos lämpötila-arvo, se päivitetään tietokantaan
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         
        data = float(data)
        cur.execute("INSERT into testi (date_time, temp) values (%s,%s)", (timestamp, data))
            
        cnx.commit()
        print(str(data) + " " + timestamp)
    
    