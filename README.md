# ZooHackathon Brasil - 2019

Repositório de códigos para o zoohactkathon 2019. A solução se baseia num aplicativo desenvolvido em kivy que possibilita que usuários façam denúncias de possíveis atos ilícitos envolvendo animais silvestre, essa denúncia é feita através de fotos e localização pelo aplicativo e chega à fiscais ambientais em um dashboard em Power BI, ordenando casos mais relevantes para que eles possam atuar de forma mais assertiva.

<br>
![Screenshot](https://github.com/lucashueda/zoohackadosparsa/blob/master/tela_inicial.jpg?raw=true)
<br>

O aplicativo ainda consta com um algoritmo de reconhecimento de espécies de aves, mais especificamente as 20 espécies mais tráficadas no Brasil. O modelo foi treinado na plataforma Microsoft Azure e obteve acurácia de 95% no problema de 20 classes, utilizando uma base coletada através do google images com cerca de 100 imagens para cada espécie.

<br>
![Screenshot](https://github.com/lucashueda/zoohackadosparsa/blob/master/species_recognition.jpg?raw=true)
<br>

# Como usar

Instale os pacotes do "requirements.txt" com o comando:
```
pip install -r requirements.txt
```

Instale também o kivy, opencv, geoforge e azure apis:
```
conda install kivy -c conda-forge
pip install opencv-python geocoder azure-cognitiveservices-vision-computervision
```


Para rodar o app basta rodar:

```
python kivy_screens.py
```

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
