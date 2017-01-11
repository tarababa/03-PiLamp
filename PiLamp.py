#    Copyright 2017 Aurora Taraba 
#
#    This file is part of the PiLamp project.
#
#    PiLamp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PiLamp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PiLamp.  If not, see <http://www.gnu.org/licenses/>.

from rotaryEncoder import RotaryEncoderClickable
from signal import pause
from phue import Bridge
import logging,traceback
import os 


print('starting[PiLamp]')
try:
  IP_ADDRESS_BRIDGE = '10.0.0.102'
  PHUE_CONFIG_FILE  =  os.path.dirname(os.path.realpath(__file__))+'/.python_hue'
  PI_LIGHT          = '3.14 Lamp'
  HUE               = 'Hue'
  SATURATION        = 'Saturation'
  colorMode         = HUE     
 
  done = False
  while not done:
    try:
      bridge = Bridge (ip = IP_ADDRESS_BRIDGE, config_file_path = PHUE_CONFIG_FILE )
      done = True
    except OSError as e:
      # an IOError exception occurred (socket.error is a subclass)
      if e.errno == 101: #Network is unreachable
        print('Network unreachable, going to try again')
      else: 
        raise            #all is lost

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
      
  #Initialization of brightness, hue and saturation
  brightness  = light_names[PI_LIGHT].brightness 
  hue         = light_names[PI_LIGHT].hue
  saturation  = light_names[PI_LIGHT].saturation 

  def changeBrightness(value):
    global brightness
    brightnessStep = 5
    brightnessMax  = 254
    if value > 0: #clockwise 
      if brightness >= brightnessMax:
        brightness = 0
      elif brightness + brightnessStep > brightnessMax:
        brightness = brightnessMax
      else:
        brightness= brightness + brightnessStep    
    else: #counter clockwise
      if brightness <= 0:
        brightness = brightnessMax
      elif brightness - brightnessStep < 0:
        brightness = 0
      else:
        brightness= brightness - brightnessStep    

    print('brightness[' + str(brightness) + ']')  
    light_names[PI_LIGHT].brightness = brightness
  def onOff():
    if light_names[PI_LIGHT].on == False:
      light_names[PI_LIGHT].on = True
    else:
      light_names[PI_LIGHT].on = False

  def changeColorMode():
    global colorMode
    if colorMode == HUE:
      colorMode = SATURATION
    else:
      colorMode = HUE
    print('colorMode[' + str(colorMode) + ']')

  def changeColor(value):
    global saturation, hue
    saturationStep = 5
    saturationMax  = 254
    hueStep        = 500
    hueMax         = 65535
    if colorMode == SATURATION:
      if value > 0: #clockwise 
        if saturation >= saturationMax:
          saturation = 0
        elif saturation + saturationStep > saturationMax:
          saturation = saturationMax
        else:
          saturation= saturation + saturationStep    
      else: #counter clockwise
        if saturation <= 0:
          saturation = saturationMax
        elif saturation - saturationStep < 0:
          saturation = 0
        else:
          saturation= saturation - saturationStep    
      print('saturation[' + str(saturation) + ']')  
      light_names[PI_LIGHT].saturation = saturation
    else:
      if value > 0: #clockwise 
        if hue >= hueMax:
          hue = 0
        elif hue + hueStep > hueMax:
          hue = hueMax
        else:
          hue= hue + hueStep    
      else: #counter clockwise
        if hue <= 0:
          hue = hueMax
        elif hue - hueStep < 0:
          hue = 0
        else:
          hue= hue - hueStep    
      print('hue[' + str(hue) + ']')  
      light_names[PI_LIGHT].hue = hue
      
        
  encBrightness = RotaryEncoderClickable(pin_a=19, pin_b=26, button_pin=13)
  encBrightness.when_rotated = changeBrightness
  encBrightness.when_pressed = onOff

  encColor = RotaryEncoderClickable(pin_a=27, pin_b=22, button_pin=17)
  encColor.when_rotated = changeColor
  encColor.when_pressed = changeColorMode

  pause()

except:
  print('unexpected error ['+ str(traceback.format_exc()) + ']') 
