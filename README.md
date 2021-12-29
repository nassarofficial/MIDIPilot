# MIDIPilot
### A Neural DSP Quad Cortex MIDI extension app.

This project was initiated to give extra control capabilities through MIDI to Neural DSP's Quad Cortex. MIDIPilot currently enables you to turn on stomp effects through an external MIDI pedal (Voodoo Lab Ground Control Pro) while "remaining" in scene mode. Right now this program is very simple and what it does is send a series of MIDI CC messages to achieve the result needed. This program of course can be edited to work with any other MIDI pedal.

I have an idea on several features to make this a lot easier for people who are not necassary technical, but it all depends on the interaction I get. Also this is just a quick shortcut to the scene/stomp switching. But I have a pretty groundbreaking feature that I am working on that I will reveal once I make some progress.
### Requirements
* Raspberry PI (preferrably V4 if you want to support upcoming new features)
* MIDI TO USB Dongle: [TIE Studio MIDI 1i1o ](https://tie-products.com/en/produkt/midi-1i1o/) (I am pretty sure any decent MIDI TO USB dongle would work)
* USB C cable for powering the Rapberry Pi
* [SD card with Noob OS](https://www.amazon.com/Raspberry-Pi-32GB-Preloaded-NOOBS/dp/B01LXR6EOA)
* Micro HDMI to HDMI cable or whatever display connecter (to connect your Raspberry Pi to a display).
* USB mouse or keyboard, or one of them to setup the bluetooth ones.


### Installation
After inserting the micro SD, connecting the Raspberry Pi to the display connector, USB C for power, and mouse and keyboard. Connect to a Wifi network or use lan to connect to the internet. Then, open a terminal window and run the following:

1. Clone the repo into your user directory (/home/pi/):
`git clone https://github.com/nassarofficial/MIDIPilot.git`

1. `cd MIDIPilot/`
1. Change permissions on the installation bash script. The bash script basically copies and inserts a service so the program runs on startup once the raspberry is booted.
`sudo chmod +x install.sh`
1. Run `./install.sh`
1. Reboot.
2. Now shred! 🤘🤘

### Contribution
Feel free to post recommendations or features in the issues section. I dont have any contribution guidelines yet as I am not sure if there will be significant activity worth the effort.

<div align="center">
    <a href="https://github.com/nassarofficial">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.linkedin.com/in/ahmed-nassar-1317a3a6/">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-linkedin.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://twitter.com/asnassar">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-twitter.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.instagram.com/nassarofficial/">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-instagram.png" width="3%"/>
    </a>
</div>
