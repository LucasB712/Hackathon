from flask import Flask, render_template, request, jsonify, send_from_directory
import random
import sqlite3

app = Flask(__name__)

def gerar_pergunta(numero):
    operadores = ['+', '-', '*', '/']
    operador = numero
    if operador == '+':
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        resposta = num1 + num2
    elif operador == '-':
        num1 = random.randint(0, 100)
        num2 = random.randint(0, num1)
        resposta = num1 - num2
    elif operador == '*':
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        resposta = num1 * num2
    elif operador == '/':
        num2 = random.randint(1, 10)
        resultado = random.randint(1, 10)
        num1 = num2 * resultado
        resposta = resultado
        
    return [num1, num2, operador, resposta]

def verificar_resposta(pergunta, resposta):
    resultado = pergunta
    return resposta == resultado

def conectar_bd():
    conn = sqlite3.connect('tucoins.db')
    return conn

@app.route('/sub')
def sub(): 
    num1 = random.randint(1, 100)
    num2 = random.randint(1, num1)  # Garantindo que o segundo número seja menor que o primeiro
    # Renderizando o template HTML e passando os números para o template
    return render_template('subtracao.html', num1=num1, num2=num2)
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voltar_tarefas')
def voltar_tarefas():
    return render_template('tarefas.html')

@app.route('/gerar_pergunta', methods=['POST'])
def gerar_pergunta_route():
    numero = request.json['numero']
    pergunta = gerar_pergunta(numero)
    return jsonify({'pergunta': pergunta})

@app.route('/verificar_resposta', methods=['POST'])
def verificar_resposta_route():
    resultado = request.json['resultado']
    resposta_usuario = request.json['resposta_usuario']
    resultado_verificado = verificar_resposta(resultado, resposta_usuario)
    return jsonify({'resultado_verificado': resultado_verificado})

@app.route('/criar_conta')
def criar_conta():
    return render_template('criarConta.html')

@app.route('/tarefas')
def tarefas():
    return render_template('tarefas.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/imagem/<path:path>')
def serve_static_img(path):
    return send_from_directory('static/imagem', path)

@app.route('/js/<path:path>')
def serve_static_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def serve_static_css(path):
    return send_from_directory('static/css', path)


if __name__ == '__main__':
    app.run(debug=True)