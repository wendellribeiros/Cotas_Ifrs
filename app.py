from flask import Flask, render_template, request

app = Flask(__name__)

# Função que determina a cota
def determinar_cota(tipo_escola, renda_familiar, autodeclaracao, pcd):
    if pcd == "sim":
        if tipo_escola == "pública":
            if renda_familiar == "inferior":
                if autodeclaracao in ["negro", "preto", "pardo", "indígena", "quilombola"]:
                    return "Cota 2 - PcD, escola pública, PPIQ, renda ≤ 1 salário mínimo"
                else:
                    return "Cota 4 - PcD, escola pública, renda ≤ 1 salário mínimo"
            else:
                if autodeclaracao in ["negro", "preto", "pardo", "indígena", "quilombola"]:
                    return "Cota 6 - PcD, escola pública, PPIQ, independente de renda"
                else:
                    return "Cota 8 - PcD, escola pública, independente de renda"
        else:
            return "Cota 10 - PcD, acesso universal"
    else:
        if tipo_escola == "pública":
            if renda_familiar == "inferior":
                if autodeclaracao in ["negro", "preto", "pardo", "indígena", "quilombola"]:
                    return "Cota 3 - Escola pública, PPIQ, renda ≤ 1 salário mínimo"
                else:
                    return "Cota 5 - Escola pública, renda ≤ 1 salário mínimo"
            else:
                if autodeclaracao in ["negro", "preto", "pardo", "indígena", "quilombola"]:
                    return "Cota 7 - Escola pública, PPIQ, independente de renda"
                else:
                    return "Cota 9 - Escola pública, independente de renda"
        else:
            return "Cota 1 - Acesso Universal"
# Rota principal para exibir o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o formulário
@app.route('/resultado', methods=['POST'])
def resultado():
    tipo_escola = request.form['tipo_escola']
    renda_familiar = request.form['renda_familiar']
    autodeclaracao = request.form['autodeclaracao']
    pcd = request.form['pcd']

    cota = determinar_cota(tipo_escola, renda_familiar, autodeclaracao, pcd)

    return render_template('resultado.html', cota=cota)

import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Obtém a porta do ambiente, padrão para 5000
    app.run(host="0.0.0.0", port=port)  # Inicia o servidor no host e porta apropriados

