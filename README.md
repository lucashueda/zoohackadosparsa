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

First, you need to Download Python 3.6, 3.7 or 3.8 in your computer. You can get it here: https://www.python.org/downloads/
You then need to install pip. You can follow the instructions in this link:https://pip.pypa.io/en/stable/installing/

### Installing
Clone this repository in a local folder.

Install the all the requirements packages in "requirements.txt" with de CMD command:

```
pip install -r requirements.txt
```

Also, install the Kivy, OpenCV, Geoforge and Azure API packages:

```
conda install kivy -c conda-forge
pip install opencv-python geocoder azure-cognitiveservices-vision-computervision
```

To run the App, use the command:

```
python kivy_screens.py
```

# Referências

[1] IBAMA, Esforços para o combate ao tráfico de animais silvestres no Brasil (Publicação
traduzida do original “Efforts to Combat Wild Animals Trafficking in Brazil.
Biodiversity, Book 1, chapter XX, 2012” - ISBN 980-953-307-201-7), http://www.ibama.gov.br/sophia/cnia/periodico/esforcosparaocombateaotraficodeanimais.pdf

[2] Coordenação-Geral de Fiscalização Ambiental (CGFis), Autos de Infração - Dados Abertos do IBAMA, http://dadosabertos.ibama.gov.br/dataset/autos-de-infracao

___________________________________________________________________________________________________________________________________

# Boas práticas de desenvolvimento


## Definindo um ambiente de desenvolvimento no seu computador LOCAL

O passo a passo descrito aqui será utilizado para mantermos a boa prática na gestão do desenvolvimento da solução.

- 1º passo) Instale o Anaconda (python 3.7) e o "gitbash"
- 2º passo) Crie um "conda enviroment" utilizando o seguinte código no terminal do Anaconda (anaconda prompt):
```
conda create --name zoohack
```
Ele pedirá para digitar "y" ou "n", digite "y" é aperte enter. Esse código criará um ambiente com o nome "zoohack"

- 3º passo) Ative o ambiente com o comando: 
```
 conda activate zoohack
```

A partir desse código sua linha do terminal deverá constar o seguinte prefixo:
<br>
![Screenshot](https://github.com/lucashueda/zoohackadosparsa/blob/master/tutorial_git_activate.png?raw=true)
<br>

## Como clonar o repositório e iniciá-lo

Agora que você já criou um ambiente produtivo isolado no seu computador (que inicialmente só possui pacotes do Anaconda) vamos mostrar como utilizar do repositório e alterá-lo da maneira mais assertiva.

- 1º passo) Abra o terminal do git (gitbash na busca do windows)
- 2º passo) Navegue utilizando "cd dir" até o local onde deseja clonar o repositório
- 3º passo) Execute o código:
```
git clone https://github.com/lucashueda/zoohackadosparsa.git
```
- 4º passo) Uma pasta com o nome "zoohackadosparsa" deverá ter sido criado no diretório em que seu terminal está. Entre pelo terminal na pasta clonada com o código: "cd zoohackadosparsa". Mantenha aberto para a próxima etapa do tutorial "Como trabalhar com o repositório".

## Como trabalhar com o repositório

- 1º passo) Dentro do diretório salvo na sua máquina (através do terminal do gitbash). Basicamente o 4º passo do tutorial acima. Execute o seguinte código:
```
git pull
```
Esse comando atualizará arquivos do repositório que não existem na sua pasta clonada ainda. 
- 2º passo) Adicione seus arquivos dentro da pasta física do seu computador (ou seja, coloque os documentos dentro da pastinha la que tem no seu computador) e execute a seguinte sequência de comandos.
```
git add *
git commit -m "descrição das atualizações realizadas"
git push
```
Pronto agora suas atualizações subiram para o repositório no site: https://github.com/lucashueda/zoohackadosparsa

## !!!!!!!!!!!!! Branchs!!!!!!!!!!!!

Para que possamos trabalhar independentemente e mantermos nosso MVP funcional cada um trabalhará em uma branch, que nada mais é que uma cópia temporal do código no momento que um repositório foi criado, para isso faremos os seguintes passos:

- 1º passo) Sempre que for executar os passos do tutorial acima "Como trabalhar com o repositório" troca para sua branch específica, executando:
```
git checkout seunome
```
seunome = {cami, xandao, para, flango} cada um terá sua branch no repositório.
- ~~2º passo) Em seguida você rodará o seguinte código:
```
git merge master
```
- 3º passo) Repita o tutorial acima para atualizar seus arquivos.


No fim de tudo darei um merge em todas as branchs para juntar nossos trabalhos. Não execute o passo 2 ainda pois só será necessário num final próximo, pode ir realizando só os códigos do tutorial "Como trabalhar com o repositório" dentro da sua **própria branch**.
