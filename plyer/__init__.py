'''
Plyer
=====

'''

__all__ = ('barometer', 'brightness', 'compass', 'fingerprint',
			'gamerotation', 'geomagneticrotation', 'gravity', 'gyroscope',
			'light', 'networkinfo', 'proximity', 'smsreceive',
			'spatialorientation', 'spellcheck', 'temperature',
			'useracceleration')

__version__ = '1.3.1dev'


from plyer import facades
from plyer.utils import Proxy

#: Barometer proxy to :class:`plyer.facades.Barometer`
barometer = Proxy('barometer', facades.Barometer)

#: Brightness proxy to :class:`plyer.facades.Brightness`
brightness = Proxy('brightness', facades.Brightness)

#: Compass proxy to :class:`plyer.facades.Compass`
compass = Proxy('compass', facades.Compass)

#: Fingerprint proxy to :class:`plyer.facades.Fingerprint`
fingerprint = Proxy('fingerprint', facades.Fingerprint)

#: GameRotation proxy to :class:`plyer.facades.GameRotation`
gamerotation = Proxy('gamerotation', facades.GameRotation)

#: GeomagneticRotation proxy to :class:`plyer.facades.GeomagneticRotation`
geomagneticrotation = Proxy('geomagneticrotation', facades.GeomagneticRotation)

#: Gravity proxy to :class:`plyer.facades.Gravity`
gravity = Proxy('gravity', facades.Gravity)

#: Gyroscope proxy to :class:`plyer.facades.Gyroscope`
gyroscope = Proxy('gyroscope', facades.Gyroscope)

#: Light proxy to :class:`plyer.facades.Light`
light = Proxy('light', facades.Light)

#: NetworkInfo proxy to :class:`plyer.facades.NetworkInfo`
networkinfo = Proxy('networkinfo', facades.NetworkInfo)

#: Proximity proxy to :class:`plyer.facades.Proximity`
proximity = Proxy('proximity', facades.Proximity)

#: SmsReceive proxy to :class:`plyer.facades.SmsReceive`
smsreceive = Proxy('smsreceive', facades.SmsReceive)

#: SpatialOrientation proxy to :class:`plyer.facades.SpatialOrientation`
spatialorientation = Proxy('spatialorientation', facades.SpatialOrientation)

#: SpellCheck proxy to :class:`plyer.facades.SpellCheck`
spellcheck = Proxy('spellcheck', facades.SpellCheck)

#: Temperature proxy to :class:`plyer.facades.Temperature`
temperature = Proxy('temperature', facades.Temperature)

#: UserAcceleration proxy to :class:`plyer.facades.UserAcceleration`
useracceleration = Proxy('useracceleration', facades.UserAcceleration)
