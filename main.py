from kivy.app import App
from kivy.uix.label import Label

class ZahalaApp(App):
    def build(self):
        return Label(text="Zahala Factory Control\nProject Loaded")

ZahalaApp().run()
