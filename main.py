from bs4 import BeautifulSoup as bs
import requests
from flask import Flask, render_template, request
from random import randint
import os


def choose_img():
    number = randint(1, 5)
    return f'CraqueDaniel{number}.jpg'


def choose_img2():
    number = randint(1, 5)
    return f'Renan{number}.jpg'


def phrase_maker():
    global data2
    number = randint(0, 5)
    number1 = randint(0, 1)
    index = randint(1, 2)
    url = 'https://www.pensador.com/autor/craque_daniel/'
    page = requests.get(url)
    html = page.content
    soup = bs(html, 'html.parser')
    data = soup.find('div', class_='phrases-list')
    data1 = data.findAll('p', class_='frase fr')
    data2 = data.findAll('p', class_='frase fr0')
    if index == 1:
        return (data2[number1]).get_text()
    else:
        return (data1[number]).get_text()


def phrase_maker2():
    number = randint(0, 5)
    url = 'https://www.pensador.com/autor/choque_de_cultura/'
    page = requests.get(url)
    html = page.content
    soup = bs(html, 'html.parser')
    data = soup.findAll('p', class_='frase fr')
    a = []
    for i in data:
        if 'Renan' in i.get_text():
            a.append(i.get_text())

    return a[number]


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file1():
    return render_template('index.html', nome=phrase_maker(), data=choose_img())


@app.route('/renan', methods=['GET', 'POST'])
def upload_file2():
    return render_template('renanPage.html', nome=phrase_maker2(), data=choose_img2())


app.run(host='0.0.0.0', port=80, debug=True)



