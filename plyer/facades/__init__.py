'''
Facades
=======

Interface of all the features available.

'''
__all__ = ('Barometer', 'Brightness', 'Compass', 'Fingerprint',
			'GameRotation', 'GeomagneticRotation', 'Gravity', 'Gyroscope',
			'Light', 'NetworkInfo', 'Proximity', 'SmsReceive',
			'SpatialOrientation', 'SpellCheck', 'Temperature',
			'UserAcceleration')

from plyer.facades.barometer import Barometer
from plyer.facades.brightness import Brightness
from plyer.facades.compass import Compass
from plyer.facades.fingerprint import Fingerprint
from plyer.facades.gamerotation import GameRotation
from plyer.facades.geomagneticrotation import GeomagneticRotation
from plyer.facades.gravity import Gravity
from plyer.facades.gyroscope import Gyroscope
from plyer.facades.light import Light
from plyer.facades.networkinfo import NetworkInfo
from plyer.facades.proximity import Proximity
from plyer.facades.smsreceive import SmsReceive
from plyer.facades.spatialorientation import SpatialOrientation
from plyer.facades.spellcheck import SpellCheck
from plyer.facades.temperature import Temperature
from plyer.facades.useracceleration import UserAcceleration
