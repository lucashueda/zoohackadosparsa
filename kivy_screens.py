## Import de libs pro appe setando tamanho do app

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from kivy.properties import StringProperty
import datetime as dt
import csv
import numpy as np

from kivy.config import Config
Config.set('graphics', 'width',  500)
Config.set('graphics', 'height', 760)

## import de bibliotecas para fazer requisição do modelo
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
import urllib3

global project_id, predictor, publish_iteration_name

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"

# Replace with a valid key
prediction_key ="90f450b8b0e54914ac6b6ab84474d445"
prediction_resource_id = "/subscriptions/15fcdbb1-44c2-45b4-bcd5-b6d1ae0e5aad/resourceGroups/ZooHack/providers/Microsoft.CognitiveServices/accounts/ZooHackathon"
project_id = "bc6aa156-c15c-4033-a406-7b1b3eea8e2d"
publish_iteration_name = "Iteration6"

predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

## Função que prevê a espécie a partir do caminho de uma imagem
def species_predict(file_path):
    global project_id, predictor, publish_iteration_name
    try:
        pred = ""
        with open(file_path, "rb") as image_contents:
            results = predictor.classify_image(project_id, publish_iteration_name, image_contents.read(),verify=False)
            for prediction in results.predictions[0:1]:
                pred += prediction.tag_name + ": {0:.2f}%\r\n".format(prediction.probability * 100)
            return pred                    
    except:
        return "Imagem não pode ser lida"



## Definindo o kv que definirá a estrutura do app
Builder.load_string("""
#:import SlideTransition kivy.uix.screenmanager.SlideTransition

<Principal>:
    BoxLayout:
		background_color: 1, 1,1, .85

    	padding: 10
    	spacing: 70
    	orientation: 'vertical'

    	ActionBar:
        	ActionView:
	    		ActionPrevious:
	    			title: 'Início'
	    		ActionButton:
	    			text: 'Menu'

    	Image:
	        source: 'figs/capa2.jpg'

    	GridLayout:
    		spacing: 50
    		padding: 20

	    	cols: 1
	        Button:
	        	background_normal: ''
	    		background_color: 1, .3, .0, .85
	            text: 'Denunciar'
	            height: '75dp'
	            size_hint_y: None
		        on_release:
	        		app.root.transition = SlideTransition(direction='down')
	        		app.root.current = 'forms'
	        Button:
	        	background_normal: ''
	    		background_color: 1, .0, .4, .85
	            text: 'Reconhecer espécie'
	            height: '75dp'
	            size_hint_y: None
		        on_release:
	        		app.root.transition = SlideTransition(direction='up')
	        		app.root.current = 'cameraclick'


<Formulario>:
    BoxLayout:


    	padding: 10
    	spacing: 70
    	orientation: 'vertical'

    	ActionBar:
        	ActionView:
	    		ActionPrevious:
	    			title: 'Formulário'
	    			on_release: app.root.current = 'main'
	    		ActionButton:
	    			text: 'Menu'
	    			on_release: app.root.current = 'main'


        GridLayout:
            spacing: 70
            padding: 20

            cols: 1

            Label:
                id: label
                text: "Escolha a opção que mais se adequa à sua denúncia:"
                font_size: 20

            ToggleButton:
                id: my_toggle1
                text: 'Venda de animal'    
                height: '75dp'
                on_state: my_toggle1.state = "down" if my_toggle2.state == "normal" or my_toggle3.state == "normal" else "normal"

            ToggleButton:
                id: my_toggle2
                text: 'Animal em cativeiro'    
                height: '75dp'
                on_state: my_toggle2.state = "down" if my_toggle1.state == "normal" or my_toggle3.state == "normal" else "normal"

            ToggleButton:
                id: my_toggle3
                text: 'Maus tratos'    
                height: '75dp'
                on_state: my_toggle3.state = "down" if my_toggle2.state == "normal" or my_toggle1.state == "normal" else "normal"

            TextInput:
                text: 'Escreva um comentário.'
                size_hint_x: 20
                height: '75dp'


    	GridLayout:
    		spacing: 10
    		padding: 10

	    	cols: 1

	        Button:
	        	background_normal: ''
                background_color: 1, .3, .0, .85
	            text: 'Enviar localização'
	            height: '75dp'
		        on_release:
	        		app.root.transition = SlideTransition(direction='left')
	        		app.root.current = 'gps'
	        Button:
	        	background_normal: ''
                background_color: 1, .0, .4, .85
	            text: 'Enviar sem localização'
	            height: '75dp'
	            on_release:
	        		app.root.transition = SlideTransition(direction='right')
	            	app.root.current = 'fim'


<CameraClick>:

	BoxLayout:

		orientation: 'vertical'

    	padding: 20
    	spacing: 20

    	ActionBar:
    	    ActionView:
	    		ActionPrevious:
	    			title: 'Câmera'
	    			on_release: app.root.current = 'main'
	    		ActionButton:
	    			text: 'Menu'
	    			on_release: app.root.current = 'main'

		Camera:
		    id: camera
            resolution: (640, 640)
            size: (640, 640)
            play: True

    	GridLayout:
	    	cols: 1
	    	spacing: 50
    		padding: 10

	        Label:
	        	id: label
		        text: root.results
                font_size: 32

		    ToggleButton:
		        text: 'Tirar e classificar foto'    
				height: '75dp'
		        on_press: 
		        	camera.play = not camera.play
		        	root.capture()

            Button:
                background_normal: ''
                background_color: 1, .0, .4, .85
                text: 'Enviar'
                on_release:
                    app.root.transition = SlideTransition(direction='right')
                    app.root.current = 'fim'
		        


<GPS>:
    
    BoxLayout:

        orientation: 'vertical'

        padding: 5
        spacing: 5

    	ActionBar:
    		ActionView:
	    		ActionPrevious:
	    			title: 'GPS'
	    			on_release: app.root.current = 'forms'
	    		ActionButton:
	    			text: 'Menu'
	    			on_release: app.root.current = 'main'

        Image:
            source: 'figs/localizacao.png'

        GridLayout:

            cols: 1
            spacing: 10
            padding: 10

            ToggleButton:
                text: 'Pegar minha localização'    
                height: '75dp'
                on_press: 
                    root.build()
            Button:
            	background_normal: ''
                background_color: 1, .3, .0, .85
                text: 'Tirar foto do animal'
    	        on_release:
            		app.root.transition = SlideTransition(direction='left')
            		app.root.current = 'cameraclick'
            Button:
            	background_normal: ''
                background_color: 1, .0, .4, .85
                text: 'Enviar sem foto'
                on_release:
            		app.root.transition = SlideTransition(direction='right')
                	app.root.current = 'fim'

<Fim>:

    BoxLayout:
        orientation: "vertical"


        padding: 10
        spacing: 70


        ActionBar:
            ActionView:
                ActionPrevious:
                    title: 'Fim'
                    on_release: app.root.current = 'main'
                ActionButton:
                    text: 'Menu'
                    on_release: app.root.current = 'main'

        Image:
            source: 'figs/fim.jpg'

""")


global lat, lng, hora, dia, especia, grupo, qtde, data, municipio, UF, caracteristica

now = dt.datetime.now()
hora = now.strftime("%H:%M:%S")
dia = now.strftime("%d/%m/%Y")
data = now.strftime("%d/%m/%Y %H:%M:%S")
cites = 'N'

grupo = 'Ave'
qtde = 1
caracteristica = 'Vivo'
municipio = ''
UF = ''

## Declarando as telas
class Principal(Screen):
    pass

class CameraClick(Screen):

    results = StringProperty()

    def capture(self):
        global especia
        camera = self.ids['camera']
        camera.export_to_png("img.png")
        self.results = species_predict('img.png')
        especia = self.results.split(":")[0]
        print(self.results)

class Formulario(Screen):
    pass

class GPS(Screen):

    def build(self):
        global lat, lng, municipio, UF
        import geocoder
        g = geocoder.ip('me')
        municipio = g[0].city.upper()
        UF = 'SP'
        # mapview = MapView(zoom=1, lat=g.lat, lon=g.lng)
        # return mapview
        lat = str(g.lat).replace(".",",")
        lng = str(g.lng).replace(".",",")
        print(lat, lng)

class Fim(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Principal(name='main'))
sm.add_widget(CameraClick(name='cameraclick'))
sm.add_widget(Formulario(name='forms'))
sm.add_widget(GPS(name='gps'))
sm.add_widget(Fim(name='fim'))

class Jhony32App(App):

    def build(self):
        return sm

if __name__ == '__main__':
    Jhony32App().run()
    with open('D:\\zoohackadosparsa\\base_aves.csv','a') as fd:
        writer = csv.writer(fd, delimiter=';')
        writer.writerow([np.random.randint(30000), data, municipio, UF, '', '', lat, lng, data, dia, hora, qtde, grupo, '', especia, cites, caracteristica, ''])