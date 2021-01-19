import time
from datetime import datetime
import mysql.connector

from picamera import PiCamera
import RPi.GPIO as GPIO

#Raspberry pin config 
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)


class Camera:
    
    #initializing camera
    def __init__ (self):
    
    
        self.camera = PiCamera()
        self.camera.resolution = (1920, 1080)
        

    
    def take_picture(self):
        
        self.camera.start_preview()
        
        time.sleep(2)
            
        self.camera.capture("/your picture location here.jpeg")
        
        self.camera.stop_preview()
