# AlexaRobot

## Hardware Set Up

**What You'll Need** 

* **A Micro SD Card:** There needs to be an micro SD card in order to download and install Dexter Industries software for the AlexaRobot (GoPiGo3). You must install Raspbian for Robots on an micro SD Card for the Raspberry Pi. Here's a link on how to install the image: https://www.dexterindustries.com/howto/install-raspbian-for-robots-image-on-an-sd-card/

* **A Raspberry Pi 3:** The brains of the AlexaRobot.

* **The GoPiGo3:** The body of the robot. Assembly instructions here: https://www.dexterindustries.com/GoPiGo/get-started-with-the-gopigo3-raspberry-pi-robot/1-assemble-gopigo3/

* **A Speaker for the Raspberry Pi:** In order to hear the response of Alexa there needs to be a speaker connected to the Raspberry Pi. Here's the speaker that I used: https://www.dexterindustries.com/product/speaker-for-the-raspberry-pi/

* **A USB Microphone:** In order to speak with the AlexaRobot there needs to be a microphone. Here's the one that I used:  https://www.amazon.com/gp/product/B01MQ2AA0X/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1

* **8 AA Batteries:** The robot is powered with 8 AA batteries.

**Instructions:** The first step is to assemble the GoPiGo3 Robot for the Raspberry Pi. Next, you will mount the microphone to one of the USB ports on the Raspberry Pi.  Finally, you should mount the speaker for the Raspberry Pi to the top of the GoPiGo3 and hold it in place with a ziptie.  Again, the robot is powered with 8 AA batteries.

## Software Set Up

### AlexaPi 
In order to use the Alexa Voice Services to listen to commands, you must use the AlexaPi project software. Set up instructions here: https://github.com/alexa-pi/AlexaPi

**If This Then That(IFTTT):** IFTTT is a sevice that lets the AlexaRobot connect different parts of the internet together. There is a need for IFTTT because Alexa cannot return text strings to the Raspberry Pi. IFTTT helps connect the AlexaPi responses back to the Raspberry Pi. 

**Ngrok:** Ngrok is a service that allows you to connect to your Raspberry Pi through any network.  With Ngrok, you don’t need to be on the same local network as your Pi to SSH in or to access a web server.  ngrok will help us pipe information back from IFTTT to the Pi. IFTTT needs an internet-based URL to contact, so we’ll use ngrok to make our server accessible to the outside world.

![AlexaRobot1](https://user-images.githubusercontent.com/39312485/56705225-1e61a780-66de-11e9-9aa6-f000b35b334a.png)
