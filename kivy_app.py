from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width',  500)
Config.set('graphics', 'height', 760)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (500, 760)
        play: True
    ToggleButton:
        text: 'Tirar e classificar foto'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '58dp'
    Button:
        text: 'Denunciar tráfico'
        size_hint_y: None
        height: '58dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()