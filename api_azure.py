#!/usr/bin/env python
# coding: utf-8

import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
import urllib3

global project_id, predictor, publish_iteration_name

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

folder = "C:\\Users\\massa\\Documents\\zoohackadosparsa\\Imagens\\Testes\\"

ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"

# Replace with a valid key
prediction_key ="90f450b8b0e54914ac6b6ab84474d445"
prediction_resource_id = "/subscriptions/15fcdbb1-44c2-45b4-bcd5-b6d1ae0e5aad/resourceGroups/ZooHack/providers/Microsoft.CognitiveServices/accounts/ZooHackathon"
project_id = "bc6aa156-c15c-4033-a406-7b1b3eea8e2d"
publish_iteration_name = "Iteration6"

predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

def species_predict(file_path):
    global project_id, predictor, publish_iteration_name
    try:
        pred = ""
        with open(file_path, "rb") as image_contents:
            results = predictor.classify_image(project_id, publish_iteration_name, image_contents.read(),verify=False)
            for prediction in results.predictions[0:3]:
                pred += "\t" + prediction.tag_name + ": {0:.2f}%\r\n".format(prediction.probability * 100)
            return pred                    
    except:
        return "Imagem não pode ser lida"

