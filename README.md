# AlexaRobot

## Hardware Set Up

**What You'll Need** 

* **The GoPiGo3:** The body of the robot. Assembly instructions here: https://www.dexterindustries.com/GoPiGo/get-started-with-the-gopigo3-raspberry-pi-robot/1-assemble-gopigo3/

* **A Micro SD Card:** There needs to be an micro SD card in order to download and install Dexter Industries software for the AlexaRobot (GoPiGo3). You must install Raspbian for Robots on an micro SD Card for the Raspberry Pi. Here's a link on how to install the image: https://www.dexterindustries.com/howto/install-raspbian-for-robots-image-on-an-sd-card/

* **A Raspberry Pi 3:** The brains of the AlexaRobot.

* **A Speaker for the Raspberry Pi:** In order to hear the response of Alexa there needs to be a speaker connected to the Raspberry Pi. Here's the speaker that I used: https://www.dexterindustries.com/product/speaker-for-the-raspberry-pi/

* **A USB Microphone:** In order to speak with the AlexaRobot there needs to be a microphone. Here's the one that I used:  https://www.amazon.com/gp/product/B01MQ2AA0X/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1

* **8 AA Batteries:** The robot is powered with 8 AA batteries.

**Instructions:** The first step is to assemble the GoPiGo3 Robot for the Raspberry Pi. Next, you will mount the microphone to one of the USB ports on the Raspberry Pi.  Finally, you should mount the speaker for the Raspberry Pi to the top of the GoPiGo3 and hold it in place with a ziptie.  Again, the robot is powered with 8 AA batteries.

## Software Set Up

![AlexaRobot1](https://user-images.githubusercontent.com/39312485/56705659-d6dc1b00-66df-11e9-9c69-d4ad678c526a.png)


### Set Up AlexaPi 
In order to use the Alexa Voice Services to listen to commands, you must use the AlexaPi project software. Set up instructions here: https://github.com/alexa-pi/AlexaPi. Just follow the "Installation Guide" at the bottom of the GitHub. 

### Set Up If This Then That(IFTTT)
IFTTT is a sevice that lets the AlexaRobot connect different parts of the internet together. There is a need for IFTTT because Alexa cannot return text strings to the Raspberry Pi. IFTTT helps connect the AlexaPi responses back to the Raspberry Pi. 

First, you will need to set up an IFTTT account. The account is free. Here is a link to IFTTT: https://ifttt.com/join

Next, in IFTTT, you will want to set up your applets.  You will need an applet for each command you want to send to the GoPiGo3. First, connect Amazon Alexa to your IFTTT Account. Link here: https://ifttt.com/amazon_alexa. Then you'll do the following to create an applet that will handle a single command:

**1.** Create an IFTTT applet for your first command. Link Here: https://ifttt.com/create. Click on the "this" in the "if this then that" link in the center of the page. You will create an Alexa applet.

![1](https://user-images.githubusercontent.com/39312485/56707816-71405c80-66e8-11e9-9a13-349e4ea70326.JPG)

**2.** Select "Say a Specific Phrase".

![2](https://user-images.githubusercontent.com/39312485/56707845-8f0dc180-66e8-11e9-81c4-d464af4986ec.JPG)


**3.** Specify the command. Say "forward".

![3](https://user-images.githubusercontent.com/39312485/56707863-a51b8200-66e8-11e9-8d17-abcd8cfa41ef.JPG)


**4.** Next, select “That”.

**5.** You will use the action service “Webhooks”.

![5](https://user-images.githubusercontent.com/39312485/56707894-c0868d00-66e8-11e9-8f0f-c2e36ba3eda1.JPG)


**6.**  Click “Make a web request” and specify the information.

![6](https://user-images.githubusercontent.com/39312485/56707913-d1370300-66e8-11e9-8482-21edb8a61484.JPG)

**7.** The URL is either your provided ngrok url, or your custom domain. For me, I purchase a domain name, which will be explained in the "connect to ngrok" set up. For now, just enter in “ngrok.io”.

![7](https://user-images.githubusercontent.com/39312485/56707926-e01db580-66e8-11e9-9f36-8dfbcf94b23f.JPG)


**8.** Your applet will be doing a “GET” method, the content will be text. You do not have to put anything in the body, but I just entered what phrase I am saying

**9.**  Click “Create Action” and then “Finish”.

You will need to do this for all the moves you want your Amazon Alexa controlled robot to make. In this project, you will make six: one for “Forward”, “Backward”, “Left”, “Stop”, “Right”, and “Dance”.









### Connect to ngrok 
Ngrok is a service that allows you to connect to your Raspberry Pi through any network.  With ngrok, you don’t need to be on the same local network as your Pi to SSH in or to access a web server. Ngrok will help us pipe information back from IFTTT to the Pi. IFTTT needs an internet-based URL to contact, so we’ll use ngrok to make our server accessible to the outside world.

### Set Up the Flask Server
