# AlexaRobot

# Hardware Set Up

**The GoPiGo:** The body of the robot. Assembly instructions here: https://www.dexterindustries.com/GoPiGo/get-started-with-the-gopigo3-raspberry-pi-robot/1-assemble-gopigo3/

**Raspberry Pi 3:** The brains of the AlexaRobot.

**The Speaker for the Raspberry Pi:** In order to hear the response of Alexa there needs to be a speaker connected to the Raspberry Pi. 

**A USB Microphone:** In order to speak with the AlexaRobot there needs to be a microphone. 

**Micro SD Card:** There needs to be an micro SD card in order to download and install Dexter Industries software. You 
must install the image on the Raspberry Pi using your PC. Here's a link: https://www.dexterindustries.com/howto/install-raspbian-for-robots-image-on-an-sd-card/

# Software Set Up

**AlexaPi:** In order to use the Alexa Voice Services to listen to commands, you must use the AlexaPi project software. Set up instructions here: https://github.com/alexa-pi/AlexaPi

**If This Then That(IFTTT):** IFTTT is a sevice that lets the AlexaRobot connect different parts of the internet together. There is a need for IFTTT because Alexa cannot return text strings to the Raspberry Pi. IFTTT helps connect the AlexaPi responses back to the Raspberry Pi. 

**Ngrok:** Ngrok is a service that allows you to connect to your Raspberry Pi through any network.  With Ngrok, you don’t need to be on the same local network as your Pi to SSH in or to access a web server.  ngrok will help us pipe information back from IFTTT to the Pi. IFTTT needs an internet-based URL to contact, so we’ll use ngrok to make our server accessible to the outside world.

