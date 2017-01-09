from rotaryEncoder import RotaryEncoderClickable
from signal import pause
from phue import Bridge

IP_ADDRESS_BRIDGE = '10.0.0.102'
PI_LIGHT          = '3.14 Lamp'
HUE               = 'Hue'
SATURATION        = 'Saturation'
colorMode         = HUE     

bridge = Bridge (IP_ADDRESS_BRIDGE)

#get list of lights
light_names = bridge.get_light_objects('name')
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
