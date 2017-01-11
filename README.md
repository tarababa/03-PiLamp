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
Hue or Saturation can be changed by turning the rotary encoder, changing whether Hue or Saturation is affected is acomplished by pressing down on the shaft of the rotary encoder.

#Requirements
### Python Philips HUE Library
The interface between the Raspberry PI and the Philips HUE bridge is established through the ![Python Phue Library](https://github.com/studioimaginaire/phue). To install ```sudo pip-3 install phue```.
### Python Rotary Encoder Classes
As the ![GPIOZero library](https://github.com/RPi-Distro/python-gpiozero) does not include a rotary encoder classes yet, we are  using a version of the rotary encoder classes written by ![Paulo Mateus](https://github.com/PedalPi/Physical/issues/1). The rotary encoder classes have been included in the repository of the PiLamp project (![rotaryEncoder.py](https://github.com/tarababa/03-PiLamp/blob/master/rotaryEncoder.py). 

## Run PiLamp.py on startup
Edit /etc/rc.local and add the following lines. (Obviously they must match the path to the `PiLamp.py` script).

```
# Run PiLamp.py
(python3 /home/pi/03-PiLamp/PiLamp.py)&
```
