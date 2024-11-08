from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Carregar as coordenadas das setas do arquivo JSON
with open('coordenadas.json') as f:
    coordenadas_disciplinas = json.load(f)


# Exemplo de grafo de disciplinas com pré-requisitos
grafo_disciplinas = {
    "Algoritmo e Programação de Computadores - CIC0004": [],
    "Cálculo 2 - MAT0026": ["Cálculo 1 - MAT0025"],
    "Métodos Numéricos para Engenharia - FGA0160": ["Cálculo 2 - MAT0026"],
    "Probabilidade e Estatística Aplicada à Engenharia - FGA0157": ["Cálculo 1 - MAT0025"],
    "Orientação a Objetos - FGA0154": ["Algoritmo e Programação de Computadores - CIC0004"],
    "Métodos de Desenvolvimento de Software - FGA0312": ["Orientação a Objetos - FGA0154"],
    "Requisitos de Software - FGA0313": ["Métodos de Desenvolvimento de Software - FGA0312"],
    "Testes de Software - FGA0314": ["Requisitos de Software - FGA0313"],
    "Gerência de Configuração e Evolução de Software - FGA0317": ["Testes de Software - FGA0314"],
    "Interação Humano Computador - FGA0173": ["Métodos de Desenvolvimento de Software - FGA0312"],
    "Qualidade de Software 1 - FGA0315": ["Interação Humano Computador - FGA0173", "Gestão da Produção e Qualidade - FGA0173"],
    "Arquitetura e Desenho de Software - FGA0208": ["Requisitos de Software - FGA0313"],
    "Técnicas de Programação em Plataformas Emergentes - FGA0242": ["Arquitetura e Desenho de Software - FGA0208", "Testes de Software - FGA0314"],
    "Engenharia de Produto de Software - FGA0316": ["Técnicas de Programação em Plataformas Emergentes - FGA0242"],
    "Paradigmas de Programação - FGA0210": ["Orientação a Objetos - FGA0154"],
    "Desenvolvimento de Software - FGA0084": ["Algoritmo e Programação de Computadores - CIC0004"],
    "Estrutura de Dados 1 - FGA0146": ["Algoritmo e Programação de Computadores - CIC0004"],
    "Compiladores 1 - FGA0003": ["Estrutura de Dados 1 - FGA0146"],
    "Paradigmas de Programação - FGA0210": ["Compiladores 1 - FGA0003", "Orientação a Objetos - FGA0154"],
    "Projeto e Análise de Algoritmos - FGA0124": ["Estrutura de Dados 1 - FGA0146"],
    "Estrutura de Dados 2 - FGA0030": ["Estrutura de Dados 1 - FGA0146"],
    "Programação para Sistemas Paralelos e Distribuídos - FGA0244": ["Estrutura de Dados 2 - FGA0030", "Fundamentos de Redes de Computadores - FGA0211"],
    "Teoria de Eletrônica Digital 1 - FGA0073": ["Introdução à Álgebra Linear - MAT0031"],
    "Fundamentos de Arquiteturas de Computadores - FGA0142": ["Teoria de Eletrônica Digital 1 - FGA0073"],
    "Fundamentos de Sistemas Operacionais - FGA0170": ["Fundamentos de Arquiteturas de Computadores - FGA0142"],
    "Fundamentos de Redes de Computadores - FGA0211": ["Fundamentos de Sistemas Operacionais - FGA0170"],
    "Fundamentos de Sistemas Embarcados - FGA0103": ["Fundamentos de Sistemas Operacionais - FGA0170"],
    "Gestão da Produção e Qualidade - FGA0173": ["Engenharia Econômica - FGA0133"],
    "Matemática Discreta 2 - FGA0108": ["Matemática Discreta 1 - FGA0085"],
    "Sistema de Banco de Dados 1 - FGA0137": ["Matemática Discreta 2 - FGA0108"],
    "Sistema de Banco de Dados 2 - FGA0060": ["Sistema de Banco de Dados 1 - FGA0137"],
    "Projeto Integrador de Engenharia 2 - FGA0250": ["Projeto Integrador 1 - FGA0150"],
    "Trabalho de Conclusão de Curso 2 - FGA0290": ["Trabalho de Conclusão de Curso 1 - FGA0287"]
}

    # Adicione o restante das disciplinas e seus pré-requisitos


# Função para calcular os pré-requisitos usando DFS
def calcular_pre_requisitos(disciplina):
    visitados = set()  # Para armazenar disciplinas visitadas e evitar loops
    pre_requisitos = []  # Para armazenar os pares (prerequisito, disciplina)

    def dfs(disc):
        # Para cada pré-requisito da disciplina atual, se não foi visitado, faça DFS
        for pre in grafo_disciplinas.get(disc, []):
            if pre not in visitados:
                visitados.add(pre)
                pre_requisitos.append((pre, disc))  # Adiciona o par (prerequisito, disciplina)
                dfs(pre)  # Continua a busca recursivamente

    # Inicia a DFS a partir da disciplina fornecida
    visitados.add(disciplina)
    dfs(disciplina)

    return pre_requisitos

# Função para calcular as disciplinas sequentes usando BFS
def calcular_disciplinas_sequentes(disciplina):
    sequentes = []
    visitados = set()

    # Verificar todas as disciplinas no grafo
    for disc, prereqs in grafo_disciplinas.items():
        # Verifica se a disciplina fornecida é um pré-requisito de alguma outra disciplina
        if disciplina in prereqs and disc not in visitados:
            sequentes.append(disc)
            visitados.add(disc)

    print(f"Disciplinas sequentes de {disciplina}: {sequentes}")
    return sequentes

# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para obter os pré-requisitos de uma disciplina
@app.route('/pre_requisitos', methods=['POST'])
def pre_requisitos():
    data = request.get_json()
    disciplina = data['disciplina']
    pre_requisitos = calcular_pre_requisitos(disciplina)
    coordenadas = [coordenadas_disciplinas.get(f"{pre_req[0]}, {pre_req[1]}") for pre_req in pre_requisitos]
    return jsonify({'pre_requisitos': coordenadas})

# Rota para obter as disciplinas sequentes de uma disciplina
@app.route('/disciplinas_sequentes', methods=['POST'])
def disciplinas_sequentes():
    data = request.get_json()
    disciplina = data['disciplina']
    sequentes = calcular_disciplinas_sequentes(disciplina)
    coordenadas = [coordenadas_disciplinas.get(f"{disciplina}, {seq}") for seq in sequentes]
    print("Dados das disciplinas sequentes:", sequentes)

    return jsonify({'sequentes': coordenadas})

if __name__ == '__main__':
    app.run(debug=True)

