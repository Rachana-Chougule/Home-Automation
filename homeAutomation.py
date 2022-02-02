import RPi.GPIO as GPIO
import time
import math
import datetime
GPIO.setwarnings(False)
l1 = 3
l2 = 5
l3 = 7
l4 = 8
f1 = 10
f2 = 12
f3 = 16
f4 = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(l1, GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
GPIO.setup(l3, GPIO.OUT)
GPIO.setup(l4,GPIO.OUT)
GPIO.setup(f1, GPIO.OUT)
GPIO.setup(f2,GPIO.OUT)
GPIO.setup(f3, GPIO.OUT)
GPIO.setup(f4,GPIO.OUT)
# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError
from ubidots import ApiClient
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_tRxW896ap1jEiK8aJA8L1V3JRe2C'
# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'anushkapatil322'
# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try:
 light1 = aio.feeds('light1')
 light2 = aio.feeds('light2')
 light3 = aio.feeds('light3')
 light4 = aio.feeds('light4')
 fan1 = aio.feeds('fan1')
 fan2 = aio.feeds('fan2')
 fan3 = aio.feeds('fan3')
 fan4 = aio.feeds('fan4')
except RequestError:
 feed1 = Feed(name="light1")
 feed2 = Feed(name="light2")
 feed3 = Feed(name="light3")
 feed4 = Feed(name="light4")
 feed5 = Feed(name="fan1")
 feed6 = Feed(name="fan2")
 feed7 = Feed(name="fan3")
 feed8 = Feed(name="fan4")
 light1 = aio.create_feed(feed1)
 light2 = aio.create_feed(feed2)
 light3 = aio.create_feed(feed3)
 light4 = aio.create_feed(feed4)
 fan1 = aio.create_feed(feed5)
 fan2 = aio.create_feed(feed6)
 fan3 = aio.create_feed(feed7)
 fan4 = aio.create_feed(feed8)

def initialize():
 print("Initializing the smart home ")
 GPIO.output(l1, GPIO.LOW)
 GPIO.output(l2, GPIO.LOW)
 GPIO.output(l3, GPIO.LOW)
 GPIO.output(l4, GPIO.LOW)
 GPIO.output(f1, GPIO.LOW)
 GPIO.output(f2, GPIO.LOW)
 GPIO.output(f3, GPIO.LOW)
 GPIO.output(f4, GPIO.LOW)
 return
initialize()
while True:
 data1 = aio.receive(light1.key)
 if int(data1.value) == 1:
 print('received <- Light 1 ON\n')
 GPIO.output(l1, GPIO.HIGH)
 elif int(data1.value) == 0:
 print('received <- Light 1 OFF\n')
 GPIO.output(l1, GPIO.LOW)
 time.sleep(0.5)
 data2 = aio.receive(light2.key)
 if int(data2.value) == 1:
 print('received <- Light 2 ON\n')
 GPIO.output(l2, GPIO.HIGH)
 elif int(data2.value) == 0:
 print('received <- Light 2 OFF\n')
 GPIO.output(l2, GPIO.LOW)
 time.sleep(0.5)

 data3 = aio.receive(light3.key)
 if int(data3.value) == 1:
 print('received <- Light 3 ON\n')
 GPIO.output(l3, GPIO.HIGH)
 elif int(data3.value) == 0:
 print('received <- Light 3 OFF\n')
 GPIO.output(l3, GPIO.LOW)
 time.sleep(0.5)
 data4 = aio.receive(light4.key)
 if int(data4.value) == 1:
 print('received <- Light 4 ON\n')
 GPIO.output(l4, GPIO.HIGH)
 elif int(data4.value) == 0:
 print('received <- Light 4 OFF\n')
 GPIO.output(l4, GPIO.LOW)
 time.sleep(0.5)
 data5 = aio.receive(fan1.key)
 if int(data5.value) == 1:
 print('received <- Fan 1 ON\n')
 GPIO.output(f1, GPIO.HIGH)
 elif int(data5.value) == 0:
 print('received <- Fan 1 OFF\n')
 GPIO.output(f1, GPIO.LOW)
 time.sleep(0.5)
 data6 = aio.receive(fan2.key)
 if int(data6.value) == 1:
 print('received <- Fan 2 ON\n')
 GPIO.output(f2, GPIO.HIGH)
 elif int(data6.value) == 0:
 print('received <- Fan 2 OFF\n')
 GPIO.output(f2, GPIO.LOW)
 time.sleep(0.5)
 data7 = aio.receive(fan3.key)
 if int(data7.value) == 1:
 print('received <- Fan 3 ON\n')
 GPIO.output(f3, GPIO.HIGH)
 elif int(data7.value) == 0:
 print('received <- Fan 3 OFF\n')
 GPIO.output(f3, GPIO.LOW)
 time.sleep(0.5)
 data8 = aio.receive(fan4.key)
 if int(data8.value) == 1:
 print('received <- Fan 4 ON\n')
 GPIO.output(f4, GPIO.HIGH)
 elif int(data8.value) == 0:
 print('received <- Fan 4 OFF\n')
 GPIO.output(f4, GPIO.LOW)
 time.sleep(0.5)