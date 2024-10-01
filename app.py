from flask import Flask, render_template, request

app = Flask(__name__)
# Definição de vagas
vagas_disponiveis = {
    "Técnico em Administração": {
        "Cota 2": 1, "Cota 3": 3, "Cota 4": 1, "Cota 5": 10, 
        "Cota 6": 1, "Cota 7": 3, "Cota 8": 1, "Cota 9": 10, "Cota 1": 27, "Cota 10": 3
    },
    "Técnico em Informática": {
        "Cota 2": 1, "Cota 3": 3, "Cota 4": 1, "Cota 5": 10, 
        "Cota 6": 1, "Cota 7": 3, "Cota 8": 1, "Cota 9": 10, "Cota 1": 27, "Cota 10": 3
    }
}

# Função que determina a cota
def determinar_cota(tipo_escola, renda_familiar, autodeclaracao, pcd):
    if pcd == "sim":
        if tipo_escola == "pública":
            if renda_familiar == "inferior":
                if autodeclaracao in ["negro", "preto", "pardo", "indígena", "quilombola"]:
                    return "Cota 2"  # Retorna apenas o código da cota
                else:
                    return "Cota 4"
            else:
                if autodeclaracao in ["negro", "preto", "pardo", "indígena", "quilombola"]:
                    return "Cota 6"
                else:
                    return "Cota 8"
        else:
            return "Cota 10"
    else:
        if tipo_escola == "pública":
            if renda_familiar == "inferior":
                if autodeclaracao in ["negro", "preto", "pardo", "indígena", "quilombola"]:
                    return "Cota 3"
                else:
                    return "Cota 5"
            else:
                if autodeclaracao in ["negro", "preto", "pardo", "indígena", "quilombola"]:
                    return "Cota 7"
                else:
                    return "Cota 9"
        else:
            return "Cota 1"

# Rota principal para exibir o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Função para calcular vagas
def calcular_vagas(curso, cota):
    if curso in vagas_disponiveis and cota in vagas_disponiveis[curso]:
        return vagas_disponiveis[curso][cota]
    else:
        return 0  # Retorna 0 se não houver vagas correspondentes

# Rota para processar o formulário
@app.route('/resultado', methods=['POST'])
def resultado():
    # Capturar os dados do formulário, incluindo o curso
    curso = request.form['curso']  # Capturando o curso
    tipo_escola = request.form['tipo_escola']
    renda_familiar = request.form['renda_familiar']
    autodeclaracao = request.form['autodeclaracao']
    pcd = request.form['pcd']

    # Lógica para calcular a cota
    cota = determinar_cota(tipo_escola, renda_familiar, autodeclaracao, pcd)

    # Lógica para determinar o número de vagas com base na cota e no curso
    vagas = calcular_vagas(curso, cota)

    # Enviar dados para o template
    return render_template('resultado.html', cota=cota, curso=curso, vagas=vagas)

import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Obtém a porta do ambiente, padrão para 5000
    app.run(host="0.0.0.0", port=port)  # Inicia o servidor no host e porta apropriados
