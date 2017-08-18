from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from plyer import spellcheck

Builder.load_string('''
<SpellCheckInterface>:
    orientation: 'vertical'
    BoxLayout:
        Label:
            text: 'Input Text'
        TextInput:
            id: inputtext
    Button:
        text: 'Get Suggestions'
        on_press: root.get_suggestions(inputtext.text)
    Label:
        id: label_sug
''')


class SpellCheckInterface(BoxLayout):
    '''Root Widget'''

    label_sug = ObjectProperty()

    def get_suggestions(self, text):
        self.suggestions = spellcheck.get_suggestions(text)
        self.label_sug.text = self.suggestions


class SpellCheckApp(App):

    def build(self):
        return SpellCheckInterface()

if __name__ == "__main__":
    SpellCheckApp().run()
