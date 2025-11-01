from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello from GitHub Build!")

if _name_ == "_main_":
    MyApp().run()
