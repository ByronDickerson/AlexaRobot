# AlexaRobot

This is my senior project dealing with the intergration of the GoPiGo3 robot with the Alexa Voice Services.

I saw a tutorial online on how to create a robot that can be controlled by Alexa and thought it would be interesting to attempt. Credit is to DexterIndustries for creating their Alexa controlled robot. Their Alexa controlled robot is a bit out of date so I had to change a quite a bit in order to get the robot to work. Also, above is the code for my flask.py file

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

**7.** The URL is either your provided ngrok url, or your custom domain. For me, I purchased a domain name, which will be explained in the "connect to ngrok" set up. For now, just enter in “ngrok.io”.

![7](https://user-images.githubusercontent.com/39312485/56707926-e01db580-66e8-11e9-9f36-8dfbcf94b23f.JPG)


**8.** Your applet will be doing a “GET” method, the content will be text. You do not have to put anything in the body, but I just entered what phrase I am saying

**9.**  Click “Create Action” and then “Finish”.

You will need to do this for all the moves you want your Amazon Alexa controlled robot to make. In this project, you will make six: one for “Forward”, “Backward”, “Left”, “Stop”, “Right”, and “Dance”.

### Connect to ngrok 
Ngrok is a service that allows you to connect to your Raspberry Pi through any network.  With ngrok, you don’t need to be on the same local network as your Pi to SSH in or to access a web server. Ngrok will help us pipe information back from IFTTT to the Pi. IFTTT needs an internet-based URL to contact, so we’ll use ngrok to make our server accessible to the outside world.

First, set up an account with ngrok. Link here: https://dashboard.ngrok.com/user/signup. You can get away with a free account, but it will be much easier to set up your robot with a paid account. A paid account will allow you to set up named servers, rather than ngrok’s randomly assigned server. Also, everytime you restart your tunnel to connect to your server, you will have to reconfigure you applets url's with the new randomly assigned server. That can be really annoying and really time consuming. 

Next, install ngrok on your Raspberry Pi.  On your Pi, in the command line, type:

```
 mkdir ~/ngrok
 cd ~/ngrok
 sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
 unzip ngrok-stable-linux-arm.zip
```
This should install all the software.  You will next need to get your token; this will authorize your Raspberry Pi to ngrok.  If you login to your ngrok account, you will see step 3 (Connect your account), with your token already populated.  It should start with “./ngrok authtoken”.  Copy the command, and paste it into your command line.

**Test out ngrok:**  You can type the following into the command line:

```
./ngrok http 80
```

You should see a server start up. 

![server](https://user-images.githubusercontent.com/39312485/56708873-6b4c7a80-66ec-11e9-82fc-ddb33ea2e990.JPG)

When an IP address appears, try typing this into your browser.  You should see your default server on Port 80 come up.  With Raspbian for Robots, you should see the Raspbian for Robots entrance page show up.

You will start your server with the following command:

```
 ./ngrok http -subdomain=YourDomainName 5000
```

Where “YourDomainName” is a reserved domain set up with our basic account on ngrok.  If you go with the free account, you’ll now need to go back and re-enter the domain name that ngrok gave your Pi above into each of your IFTTT commands.

### Set Up the Flask Server

The final step in setting up your Amazon Alexa controlled robot is setting up the Flask server on the Raspberry Pi.

You'll set up a Flask server in Python to listen to IFTTT.  I am assume you’re running Raspbian for Robots, which has the Python package manager Pip already installed.  To install Flask on the Raspberry Pi, you’ll simply need to type the following into your command line:

```
sudo pip install flask
```

That’s pretty much it.  Flask should be installed.  You can try running the flask server that dexterindustries has provided in their github code and see what happens.

You can find the file by either updating your GoPiGo3 directory, or by simply running:

```
sudo wget https://raw.githubusercontent.com/DexterInd/GoPiGo/master/Projects/Alexabot/alexabot-flask-app.py
```

Then run the server:
```
python alexabot-flask-app.py
```

You should see something like this:

![flask](https://user-images.githubusercontent.com/39312485/56709160-bf0b9380-66ed-11e9-8272-f449424ef55c.JPG)

To get a general idea of how the code works on the Flask server, I’ve set up each command to listen to a specific Flask URL.  For example, if you were to call, in your web browser, “http://alexabot.ngrok.io/forward” we get the response in our browser back “Alexabot moved forward!”. You can check out the code above.

### Running the Amazon Alexa Controlled Robot

Now, with all the services set up, we should be able to say a command like “Alexa trigger forward”, Alexa will alert IFTTT, which will send an HTTP message through ngrok back to our GoPiGo and post to the web server running in Flask.  The Flask program will command the GoPiGo to move forward.

The quickstart to get running with Alexabot are to first start AlexaPi:
```
sudo python /opt/AlexaPi/src/main.py
```
Next, start ngrok in a separate window:

```
sudo ~/ngrok/ngrok http -subdomain=dexterindustries -log=stdout 5000 > log.txt &
```

Finally, start the Flask server:
```
sudo python alexabot-flask-app.py
```

Now when you say "Alexa" she will say "Yes"..... you will say "Trigger Forward" and the AlexaRobot should move forward. You can do the same thing for all 6 commands created in your applets.  
