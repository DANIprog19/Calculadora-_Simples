# Calculadora Simples

## Descrição:

Esse é um projeto de uma calculadora que realiza as quatro operações básicas, no entanto o seu diferencial é que o seu código além de ser feito na linguagem Python, ela utiliza uma biblioteca de interface gráfica chamada **tkinter**.
Para usá-la basta importar a sua biblioteca em seu código e abreviar a sua nomenclatura da seguinte forma:

```python
import tkinter as tk
```

Além disso foi usado outras bibliotecas como **messagebox** para a abertura de uma nova janela indicando o erro da divisão por 0, além de usar a biblioteca **winsound** para trazer o som de erro dentro dessa função, sendo feita assim:

```python
from tkinter import messagebox
import winsound

        winsound.MessageBeep(winsound.MB_ICONHAND)
        messagebox.showinfo("ERRO","VALOR INDIVISÍVEL!")
```

Esse projeto foi feito do zero, com o intuito de ser código livre para que outros usuários da plataforma ou da rede possam contribuir com seus conhecimentos nele.

## Como Instalar?

Para usar ele basta ter a versão mais recente do Python(3.13) instalada em sua máquina, sendo a biblioteca **tkinter** padrão dentro do ambiente Python.

## Formas de contribuir

Existem diversas formas de contribuir nesse projeto, sendo elas:

1. Aprimorar o layout
2. Ajustar os widgets
3. Alinhar os botões e os Labels
4. Criar novas janelas para erros ou mensagens ao usuário.

## Licença Usada

**GNU (General Public Licence V3.0)**
