# 03-PiLamp
Control a Philips HUE lamp with a raspberry using rotary encoders


Requires Python Phue Library, to install sudo pip-3 install phue. More information about the library can be found here https://github.com/studioimaginaire/phue

GPIOZERO does not include a rotary encoder class yet, were  using a version of the rotary encoder class which seems will be at some point included in a release of GPIO zero: https://github.com/RPi-Distro/python-gpiozero/pull/482/files/4a92c12f4110241867bab3fa4129490c658435cf..9039f42f9899eaaf77e35c3f4c84f27c5e211c97#diff-cb7fa96ad9b747a72f2b2b10e5956cf1
