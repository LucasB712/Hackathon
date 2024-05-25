import sqlite3
import random

# Função para conectar ao banco de dados SQLite
def conectar_bd():
    conn = sqlite3.connect('perguntas_respostas.db')
    return conn


# Função para gerar uma pergunta do banco de dados
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
        
    return num1, num2, operador, resposta

# Função para verificar a resposta do usuário
def verificar_resposta(resultado, resposta_usuario):
    return resultado == resposta_usuario

def main():
    conn = conectar_bd()
    cursor = conn.cursor()

    while True:
        print("+.Adicao\n")
        print("-.Subtracao\n")
        print("x.Multiplicacao\n")
        print("/.Divisao\n")
        print("Digite 'sair' a qualquer momento para sair.\n")

        numero = input("Digite sua opção: ")

        if numero == 'sair' :
            print("obrigado por jogar")
            return 0;

        pergunta = gerar_pergunta(cursor, numero)
        num1, num2, operador, resultado = pergunta
        print(f"Quanto é {num1} {operador} {num2}?")
        resposta_usuario = input("Sua resposta: ")

        if resposta_usuario.lower() == 'sair':
            print("Obrigado por jogar. Até mais!")
            break

        try:
            resposta_usuario = int(resposta_usuario)
        except ValueError:
            print("Por favor, digite uma resposta válida.")
            continue

        if verificar_resposta(resultado, resposta_usuario):
            print("Correto! Parabéns!")
        else:
            print(f"Incorreto. A resposta correta é {resultado}.")
        
if __name__ == "__main__":
    main()