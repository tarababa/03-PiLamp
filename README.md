# 03-PiLamp
Control a Philips HUE lamp with a Raspberry PI using rotary encoders. The python program was written by Aurora Taraba, the video below shows the script in action.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=3mecB9uydR0" target="_blank"><img src="http://img.youtube.com/vi/3mecB9uydR0/0.jpg" alt="Philips HUE controlled with Raspberry PI" width="480"  border="10" /></a>

The image below shows how the Rasperry PI Zero and the rotary encoders where put together.
<img src="https://github.com/tarababa/03-PiLamp/blob/master/img/RPiAndRotaryEncoders.JPG" alt="PiLamp Conroller" width="480">

#Functions
Both rotary encoders are of the "clickable" variety i.e. they have a switch which is activated when pressing down on the shaft of the rotary encoder.

##On/Off & Brightness
The lamp can be toggled on/off by pressing down on the shaft of the rotary encoder. Turning the rotary encoder changes the brightness of the light.

##Hue/Saturation
Hue or Saturation can be changed by turning the rotary encoder, changing whether Hue or Saturation is affected is accomplished by pressing down on the shaft of the rotary encoder.

#Requirements
### Python Philips HUE Library
The interface between the Raspberry PI and the Philips HUE bridge is established through the ![Python Phue Library](https://github.com/studioimaginaire/phue). To install ```sudo pip-3 install phue```.
### Python Rotary Encoder Classes
As the ![GPIOZero library](https://github.com/RPi-Distro/python-gpiozero) does not include a rotary encoder classes yet, we are  using a version of the rotary encoder classes written by ![Paulo Mateus](https://github.com/PedalPi/Physical/issues/1). The rotary encoder classes have been included in the repository of the PiLamp project (![rotaryEncoder.py](https://github.com/tarababa/03-PiLamp/blob/master/rotaryEncoder.py)). 

## Run PiLamp.py on startup
Edit /etc/rc.local and add the following lines. (Obviously they must match the path to the `PiLamp.py` script).

```
# Run PiLamp.py
python3 /home/pi/03-PiLamp/PiLamp.py > /dev/null 2>&1 &
```

We ran into a couple of problems when trying to start the PiLamp.py script automatically using this method:

* When attempting to create the bridge object the phue library looks for a configuration file containing username, IP address etc. When none is provided this config file goes into the user's home directory. When starting on boot rc.local is run as root, it is not a good idea to have the config file in the home directory of root thus we explicitely specificy the path and name of the configuration file when creating the bridge. The directory the PiLamp.py file resides in is used for the configuration file.
```Python
PHUE_CONFIG_FILE  =  os.path.dirname(os.path.realpath(__file__))+'/.python_hue'
...
...
bridge = Bridge (ip = IP_ADDRESS_BRIDGE, config_file_path = PHUE_CONFIG_FILE )
```

* When getting the list of light objects from the bridge a "Network unreachable" error is raised when running PiLamp.py on boot probably because the network is not quite ready at that point in time. A try/except section was added to catch this situation and retry until the network is ready and the light objects list can be obtained. A bit crude perhaps but it works.
```python
  #get list of lights
  done = False
  while not done:
    try:  
      light_names = bridge.get_light_objects('name')
      done = True
    except OSError as e:
      # an IOError exception occurred (socket.error is a subclass)
      if e.errno == 101: #Network is unreachable
        print('Network unreachable, going to try again to get light objects')
      else: 
        raise            #all is lost
```
