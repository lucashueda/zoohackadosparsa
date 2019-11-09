# ZooHackathon Brasil - 2019

Repositório de códigos para o zoohactkathon 2019.

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
![Screenshot](https://github.com/lucashueda/zoohackadosparsa/blob/master/tutorial_git_activate.png?raw=true)

## Como clonar o repositório e iniciá-lo

Agora que você já criou um ambiente produtivo isolado no seu computador (que inicialmente só possui pacotes do Anaconda) vamos mostrar como utilizar do repositório e alterá-lo da maneira mais assertiva.

- 1º passo) Abra o terminal do git (gitbash na busca do windows)
- 2º passo) Navegue utilizando "cd dir" até o local onde deseja clonar o repositório
- 3º passo) Execute o código:
```
git clone https://github.com/lucashueda/zoohackadosparsa.git
```
- 4º passo) Uma pasta com o nome "zoohackadosparsa" deverá ter sido criado no diretório em que seu terminal está. Entre pelo terminal na pasta clonada com o código: "cd zoohackadosparsa".
- 5º passo) 
