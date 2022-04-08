from flask import Flask, render_template, request
import os

app = Flask(__name__)

class Calculadora:
    def __init__(self, valor1, valor2, operacao):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacao = operacao

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == 'POST':
        calculo = Calculadora(request.form['valor1'], request.form['valor2'], request.form['operacao'])
        if calculo.operacao == "Adição":
            resultado = int(calculo.valor1) + int(calculo.valor2)
        elif calculo.operacao == "Subtração":
            resultado = int(calculo.valor1) - int(calculo.valor2)
        elif calculo.operacao == "Multiplicação":
            resultado = int(calculo.valor1) * int(calculo.valor2)
        elif calculo.operacao == "Divisão":
            resultado = int(calculo.valor1) / int(calculo.valor2)
        else:
            return "Não é possível realizar a operação."
        
        resposta = f"O resultado da {calculo.operacao} entre {calculo.valor1} e {calculo.valor2} é {resultado}."
        return render_template('calculadora.html', resposta = resposta)
    return render_template('calculadora.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '127.0.0.1', port = port, debug = True)