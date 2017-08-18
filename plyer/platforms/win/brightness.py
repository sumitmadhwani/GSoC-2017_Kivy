'''
Windows Brightness
------------------
'''

from plyer.facades import Brightness
import ctypes
from ctypes.wintypes import DWORD, WCHAR, HANDLE


class WinBrightness(Brightness):

    def __init__(self):
        self.win_id = ctypes.windll.user32.GetForegroundWindow()
        print "win_id =" + str(self.win_id)
        MONITOR_DEFAULTTOPRIMARY = 1
        self.monitor_id = ctypes.windll.user32.MonitorFromWindow(
            self.win_id,
            MONITOR_DEFAULTTOPRIMARY)
        print "monitor id = " + str(self.monitor_id)
        self.count = DWORD()
        self.num_of_physical_monitors = ctypes.windll.dxva2.GetNumberOfPhysicalMonitorsFromHMONITOR(
            self.monitor_id,
            ctypes.byref(self.count))
        print "num of physical monitors = " + str(self.num_of_physical_monitors)
        print "count = " + str(self.count.value)
        self.physical_array = (_PHYSICAL_MONITOR * self.count.value)()
        self.physical_monitor = ctypes.windll.dxva2.GetPhysicalMonitorsFromHMONITOR(
            self.monitor_id,
            self.count.value,
            self.physical_array)
        print "physical monitor = " + str(self.physical_monitor)
        print "physical array = " + str(self.physical_array)
        self.max_bri = DWORD()
        self.min_bri = DWORD()
        self.curr_bri = DWORD()
        # for physical in self.physical_array:
        #     print "physical handle = " + str(physical.handle)
        #     print "handle description =" + str(physical.description)
        #     brightness = ctypes.windll.dxva2.GetMonitorBrightness(physical.handle, self.min_bri, self.curr_bri, self.max_bri)
        #     print brightness
        #     print "min bri = " + str(self.min_bri)
        #     print "curr bri = " + str(self.curr_bri)
        #     print "max bri = " + str(self.max_bri)
            # ctypes.windll.dxva2.DestroyPhysicalMonitor(physical.handle)

    def _current_level(self):
        return 0

    def _set_level(self, level):
            for physical in self.physical_array:
                print "physical handle = " + str(physical.handle)
                print "handle description =" + str(physical.description)
                brightness = ctypes.windll.dxva2.GetMonitorBrightness(physical.handle, ctypes.byref(self.min_bri), ctypes.byref(self.curr_bri), ctypes.byref(self.max_bri))
                print brightness
                print "min bri = " + str(self.min_bri.value)
                print "curr bri = " + str(self.curr_bri.value)
                print "max bri = " + str(self.max_bri.value)
                set_bri = ctypes.windll.dxva2.SetMonitorBrightness(physical.handle, int(level))
                print set_bri

class _PHYSICAL_MONITOR(ctypes.Structure):
    _fields_ = [('handle', HANDLE),
                ('description', WCHAR * 128)]


def instance():
    return WinBrightness()
