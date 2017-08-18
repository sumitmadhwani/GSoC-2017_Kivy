'''
Spell Checker
=============

The spell checker can be used to check for misspelled words. This API also
helps to get a list of words that are possible valid repacements for
misspelled word or possible completions for a partially entered word.

The :class:`SpellCheck` provides access to public methods to use spell
checker in your device.

'''


class SpellCheck(object):
    '''
    Spell Check facade.
    '''

    def get_suggestions(self, text):
        return self._get_suggestions(text)

    #private

    def _get_suggestions(self, text):
        raise NotImplementedError()
