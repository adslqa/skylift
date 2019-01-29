# Skylift V1.0 Jan 2019

SkyLift is a low-cost DIY Wi-FI geolocation spoofing device. It uses the ESP8266 to broadcast Wi-Fi Beacon Frames that exploit a longstanding (2008) vulnerability in Wi-Fi geolocation services. 

Version 1.0 includes improvements:

- only two commands are needed to go from GPS coords to Arduino firmware
- job files to process Wigle request, coversion to Arduino, and iOS scan conversion
- removed vendors (not really useful)
- improved timing
- reduced SSID names to 6 characters to improve speed (ESP seems to slow down when handling too many array operations and then broadcast timing accuracy slips)
- added notebook for plotting lat/lon (needs more work)


Documentation for the previous version can be found [docs/README_v1.md]

## Getting Started

 Setup virutal environment

- `git clone https://github.com/adamhrv/skylift`
- `cd skylift`
- `virtualenv --no-site-packages -p python3 venv `
- `source venv/bin/activate`
- `pip install -r requirments`

Download test data from Wigle

- first you'll need to register on <Wigle.net>
- `cp env-sample env`
- add your credentials to an env file in `env/wigle.env`
- `source env/wigle.env`
- setup a job in the `data/jobs/wigle.csv` file
- `cd skylift`
- run `python cli_jobs.py wigle`

Covnert Wigle Data to Arduino Sketch

- edit `data/jobs/arduino.csv` to add file names from Wigle scan outputs
- `python cli_jobs arduino`
- copy the networks folder into your Arudino sketch



------------------------

## TODO

- add notes on creating job files
- add Wigle app export processor
- add instructions for Arduino sketch


## Research 

- <http://www.rfwireless-world.com/Terminology/WLAN-beacon-frame.html>
- <http://www.rfwireless-world.com/Articles/WLAN-MAC-layer-protocol.html>
- <http://www.sharetechnote.com/html/WLAN_Beacon.html>
- <http://www.sharetechnote.com/html/WLAN_FrameStructure.html#MAC_Header_Ex_01>
- <https://www.saltwaterc.eu/forging-an-802-11-beacon-frame.html>
- <http://www.zytrax.com/tech/wireless/802_mac.htm>
- <https://witestlab.poly.edu/blog/802-11-wireless-lan-2/>
- <https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/>
- <https://en.wikipedia.org/wiki/List_of_WLAN_channels>
- Japan: 12, 13, 14. Most of world is: 12, 13. US is only 1 - 11

------

