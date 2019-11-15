# ZooHackathon Brasil - 2019

Our solution is based on an Kivy developed App, a platform that enable their users do report Wildlife Traffic crimes. The report is made through occurrence classifications (TAG's), photos, GPS location and some minor information. Each report sustain a DataBase which is then presented in a Power BI Dashboard to the responsible Organizations, such as IBAMA and PRF in Brazil, by ordering the most relevant occurrences to help these agents do prioritize and enhance their actions and decisions.

<br>
<img src="https://github.com/lucashueda/zoohackadosparsa/blob/master/tela_inicial.jpg?raw=true">
<br>

The App uses a Machine Learning Algorithm to recognize Animal species. In this case, it was trained to differentiate the 22 most trafficked birds species in Brazil. To create the model, it is utilized a Microsoft Azure tool, training it with almost 100 photos per bird specie. The model achieved a 95% Accuracy and a 86% Recall, with a threshold of 75%. It means that the model predicted 86% images with a class certainty over 75% and 95% of these predictions where correct.

<br>
<img src="https://github.com/lucashueda/zoohackadosparsa/blob/master/species_recognition.jpg?raw=true">
<br>

## Getting Started

Follow these instructions to run the App:

### Prerequisites

First, you need to Download Python 3.7.4 in your computer. You can get it here: https://www.python.org/downloads/
You then need to install pip. You can follow the instructions in this link: https://pip.pypa.io/en/stable/installing/
If you want to see and use the Power BI Dashboard, please download the Power BI Desktop here: https://powerbi.microsoft.com/en-us/desktop/

### Installing
Clone this repository in a local folder.

Install the all the requirements packages in "requirements.txt" with de CMD command:

```
pip install -r requirements.txt
```

## Get Running

### The App

To run the App, use the command:

```
python kivy_screens.py
```

### The Dashboard

To use the Dashboard, first install Power BI Desktop in your computer. To get the most use of this tool please watch some Power BI introduction videos or tutorials: https://docs.microsoft.com/en-us/power-bi/guided-learning/

Open the Power BI and explore the Dashboard and its functionalities.

To Update the Dashboard constatly with the App outputs, please direct the table Source to the base_aves.csv file in the current folder.
You can do this by:

```
-> Click on edit queries
-> Select the current table
-> Click on the gear next to Source, in the right side
-> Choose the base_aves.csv file address
```

## Build With

* [Microsoft Azure](https://www.customvision.ai/) - Model building tool
* [Kivy](https://kivy.org/) - Python App Framework
* [Power BI](https://powerbi.microsoft.com/) - Data Visualization tool

## Authors

* **Alexandre Massao Tamaoki** - Applied Mathematics - Undergradute (massao.tamaoki@gmail.com)
* **Camila Sayuri Hanazono** - Applied Mathematics - Undergradute (camilahanazono@gmail.com)
* **Igor Carneiro Figueredo** - Physics - Undergradute (igorcfig@gmail.com)
* **Lucas Hideki Ueda** - Applied Mathematics - Graduate (lucashueda@gmail.com)

## References

[1] IBAMA, Esforços para o combate ao tráfico de animais silvestres no Brasil (Publicação
traduzida do original “Efforts to Combat Wild Animals Trafficking in Brazil.
Biodiversity, Book 1, chapter XX, 2012” - ISBN 980-953-307-201-7), http://www.ibama.gov.br/sophia/cnia/periodico/esforcosparaocombateaotraficodeanimais.pdf

[2] Coordenação-Geral de Fiscalização Ambiental (CGFis), Autos de Infração - Dados Abertos do IBAMA, http://dadosabertos.ibama.gov.br/dataset/autos-de-infracao
