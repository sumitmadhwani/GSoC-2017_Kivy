'''
iOS Spell Checker
-----------------
'''

from plyer.facades import SpellCheck
from pyobjus import autoclass
from pyobjus.dylib_manager import load_framework

load_framework('/System/Library/Frameworks/UIKit.framework')
UITextChecker = autoclass('UITextChecker')


class iOSSpellCheck(SpellCheck):

    def __init__(self):
        self.uitextchecker = UITextChecker.alloc().init()

    def _get_suggestions(self, text):
        self.search_range = NSRange(0, len(text))
        return text


def instance():
    return iOSSpellCheck()
