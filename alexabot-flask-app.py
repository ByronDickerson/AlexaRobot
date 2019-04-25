#Byron Dickerson
#https://github.com/DexterInd
# This file is the flask server that listens for commands from Alexa.


from flask import Flask #import for the Flask server
from easygopigo3 import EasyGoPiGo3 # import the GoPiGo3 drivers
import time #import time from time library

app = Flask(__name__)

# Create an instance of the GoPiGo3 class.
gpg = EasyGoPiGo3()

@app.route('/')#connect to default ngrok server 
def index():
	return 'Hello world'

@app.route('/forward') #connect to ngrok server for text string for applet
def forward():
	print("Forward!")
	gpg.forward()	# Send the GoPiGo3 Forward
	time.sleep(1)	# for 1 second.
	gpg.stop()	# the stop the GoPiGo3
	return 'AlexaRobot moved forward!'

@app.route('/backward')#connect to ngrok server
def backward():
	print("Backward!")
	gpg.backward()	# Send the GoPiGo3 Backward
	time.sleep(1)	# for 1 second
	gpg.stop()	# and then stop the GoPiGo3.
	return 'Backward!'

@app.route('/left') #connect to ngrok server for text string for applet
def left():
	print("Left!")
	gpg.left()
	time.sleep(1)
	gpg.stop()
	return 'Left!'

@app.route('/right') #connect to ngrok server for text string for applet
def right():
	print("Right!")
	gpg.right()
	time.sleep(1)
	gpg.stop()
	return 'Right!'

@app.route('/dance') #connect to ngrok server for text string for applet
def dance():
	print("Dance!")
	for each in range(0,5):
		gpg.right()
		time.sleep(0.25)
		gpg.left()
		time.sleep(0.25)
		gpg.backward()
		time.sleep(0.25)
	gpg.stop()
	return 'Dance!'

	
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0') #allow flask to run IP addresss
