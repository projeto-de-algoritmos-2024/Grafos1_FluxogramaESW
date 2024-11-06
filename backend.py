# backend.py
"""from flask import Flask, request, jsonify
import networkx as nx
from networkx.algorithms.traversal.depth_first_search import dfs_predecessors
from networkx.algorithms.traversal.breadth_first_search import bfs_predecessors

app = Flask(__name__)

# Inicializar o grafo usando seu código existente
G = nx.DiGraph()
# Adicione as arestas e nós como você já configurou no seu projeto
# Criação das Arestas

# partindo de Cálculo 1
G.add_edge("Cálculo 1 - MAT0025", "Cálculo 2 - MAT0026")
G.add_edge("Cálculo 2 - MAT0026", "Métodos Numéricos para Engenharia - FGA0160")

# volta para calculo 1
G.add_edge("Cálculo 1 - MAT0025", "Probabilidade e Estatística Aplicada à Engenharia - FGA0157")

# partindo de algoritmos e programação de computadores
G.add_edge("Algoritmo e Programação de Computadores - CIC0004", "Orientação a Objetos - FGA0154")
G.add_edge("Orientação a Objetos - FGA0154", "Métodos de Desenvolvimento de Software - FGA0312")
G.add_edge("Métodos de Desenvolvimento de Software - FGA0312", "Requisitos de Software - FGA0313")
G.add_edge("Requisitos de Software - FGA0313", "Testes de Software - FGA0314")
G.add_edge("Testes de Software - FGA0314", "Gerência de Configuração e Evolução de Software - FGA0317")

# volta para testes de software
G.add_edge("Testes de Software - FGA0314", "Técnicas de Programação em Plataformas Emergentes - FGA0242")

# volta para metodos de desenvolvimento de software (lembrar que pode ligar com testes de software)
G.add_edge("Métodos de Desenvolvimento de Software - FGA0312", "Interação Humano Computador - FGA0173")
G.add_edge("Interação Humano Computador - FGA0173", "Qualidade de Software 1 - FGA0315")

# volta para requisitos de software
G.add_edge("Requisitos de Software - FGA0313", "Arquitetura e Desenho de Software - FGA0208")
G.add_edge("Arquitetura e Desenho de Software - FGA0208", "Técnicas de Programação em Plataformas Emergentes - FGA0242")
G.add_edge("Técnicas de Programação em Plataformas Emergentes - FGA0242", "Engenharia de Produto de Software - FGA0316")

# volta para orientação a objetos
G.add_edge("Orientação a Objetos - FGA0154", "Paradigmas de Programação - FGA0210")

# volta para algoritmos e programação de computadores
G.add_edge("Algoritmo e Programação de Computadores - CIC0004", "Desenvolvimento de Software - FGA0084")

# volta para algoritmos e programação de computadores
G.add_edge("Algoritmo e Programação de Computadores - CIC0004", "Estrutura de Dados 1 - FGA0146")
G.add_edge("Estrutura de Dados 1 - FGA0146", "Compiladores 1 - FGA0003")
G.add_edge("Compiladores 1 - FGA0003", "Paradigmas de Programação - FGA0210")

# volta para estrutura de dados 1
G.add_edge("Estrutura de Dados 1 - FGA0146", "Projeto e Análise de Algoritmos - FGA0124")

# volta para estrutura de dados 1
G.add_edge("Estrutura de Dados 1 - FGA0146", "Estrutura de Dados 2 - FGA0030")
G.add_edge("Estrutura de Dados 2 - FGA0030", "Programação para Sistemas Paralelos e Distribuídos - FGA0244")

# partindo de introdução a algebra linear (lembrar de PED)
G.add_edge("Introdução à Álgebra Linear - MAT0031", "Teoria de Eletrônica Digital 1 - FGA0073")
G.add_edge("Teoria de Eletrônica Digital 1 - FGA0073", "Fundamentos de Arquiteturas de Computadores - FGA0142")
G.add_edge("Fundamentos de Arquiteturas de Computadores - FGA0142", "Fundamentos de Sistemas Operacionais - FGA0170")
G.add_edge("Fundamentos de Sistemas Operacionais - FGA0170", "Fundamentos de Redes de Computadores - FGA0211")
G.add_edge("Fundamentos de Redes de Computadores - FGA0211", "Programação para Sistemas Paralelos e Distribuídos - FGA0244")

# volta para fundamentos de sistemas operacionais
G.add_edge("Fundamentos de Sistemas Operacionais - FGA0170", "Fundamentos de Sistemas Embarcados - FGA0103")

# volta para introdução a algebra linear (lembrar de PED)
G.add_edge("Introdução à Álgebra Linear - MAT0031", "Teoria de Eletrônica Digital 1 - FGA0073")

# partindo de engenharia economica
G.add_edge("Engenharia Econômica - FGA0133", "Gestão da Produção e Qualidade - FGA0173")
G.add_edge("Gestão da Produção e Qualidade - FGA0173", "Qualidade de Software 1 - FGA0315")

# partindo de matemática discreta 2
G.add_edge("Matemática Discreta 1 - FGA0085", "Matemática Discreta 2 - FGA0108")
G.add_edge("Matemática Discreta 2 - FGA0108", "Sistema de Banco de Dados 1 - FGA0137")
G.add_edge("Sistema de Banco de Dados 1 - FGA0137", "Sistema de Banco de Dados 2 - FGA0060")

# partindo de projeto integrador 1
G.add_edge("Projeto Integrador 1 - FGA0150", "Projeto Integrador de Engenharia 2 - FGA0250")

# partindo de trabalho de conclusão de curso 1
G.add_edge("Trabalho de Conclusão de Curso 1 - FGA0287", "Trabalho de Conclusão de Curso 2 - FGA0290")

@app.route('/pre_requisitos', methods=['GET'])
def pre_requisitos():
    disciplina = request.args.get('disciplina')
    metodo = request.args.get('metodo', 'dfs')  # Padrão é DFS
    
    if metodo == 'dfs':
        predecessors = dfs_predecessors(G, source=disciplina)
    else:  # método BFS
        predecessors = bfs_predecessors(G, source=disciplina)
    
    caminho_pre_requisitos = list(predecessors.keys())

    # Retornar os pré-requisitos como uma lista de nós/disciplinas
    return jsonify({"pre_requisitos": caminho_pre_requisitos})

# No backend, ajuste a chave para ser compatível com o frontend
def format_chave(disciplina, pre_req):
    return f"{pre_req}, {disciplina}"

if __name__ == '__main__':
    app.run(debug=True)"""


























from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Carregar as coordenadas das setas do arquivo JSON
with open('coordenadas.json') as f:
    coordenadas_disciplinas = json.load(f)


# Exemplo de grafo de disciplinas com pré-requisitos
grafo_disciplinas = {
    "Cálculo 2 - MAT0026": ["Cálculo 1 - MAT0025"],
    "Métodos Numéricos para Engenharia - FGA0160": ["Cálculo 2 - MAT0026"],
    "Probabilidade e Estatística Aplicada à Engenharia - FGA0157": ["Cálculo 1 - MAT0025"],
    "Orientação a Objetos - FGA0154": ["Algoritmo e Programação de Computadores - CIC0004"],
    "Métodos de Desenvolvimento de Software - FGA0312": ["Orientação a Objetos - FGA0154"],
    "Requisitos de Software - FGA0313": ["Métodos de Desenvolvimento de Software - FGA0312"],
    "Testes de Software - FGA0314": ["Requisitos de Software - FGA0313"],
    "Gerência de Configuração e Evolução de Software - FGA0317": ["Testes de Software - FGA0314"],
    "Técnicas de Programação em Plataformas Emergentes - FGA0242": ["Testes de Software - FGA0314"],
    "Interação Humano Computador - FGA0173": ["Métodos de Desenvolvimento de Software - FGA0312"],
    "Qualidade de Software 1 - FGA0315": ["Interação Humano Computador - FGA0173"],
    "Arquitetura e Desenho de Software - FGA0208": ["Requisitos de Software - FGA0313"],
    "Técnicas de Programação em Plataformas Emergentes - FGA0242": ["Arquitetura e Desenho de Software - FGA0208"],
    "Engenharia de Produto de Software - FGA0316": ["Técnicas de Programação em Plataformas Emergentes - FGA0242"],
    "Paradigmas de Programação - FGA0210": ["Orientação a Objetos - FGA0154"],
    "Desenvolvimento de Software - FGA0084": ["Algoritmo e Programação de Computadores - CIC0004"],
    "Estrutura de Dados 1 - FGA0146": ["Algoritmo e Programação de Computadores - CIC0004"],
    "Compiladores 1 - FGA0003": ["Estrutura de Dados 1 - FGA0146"],
    "Paradigmas de Programação - FGA0210": ["Compiladores 1 - FGA0003"],
    "Projeto e Análise de Algoritmos - FGA0124": ["Estrutura de Dados 1 - FGA0146"],
    "Estrutura de Dados 2 - FGA0030": ["Estrutura de Dados 1 - FGA0146"],
    "Programação para Sistemas Paralelos e Distribuídos - FGA0244": ["Estrutura de Dados 2 - FGA0030"],
    "Introdução à Álgebra Linear - MAT0031": ["Teoria de Eletrônica Digital 1 - FGA0073"],
    "Fundamentos de Arquiteturas de Computadores - FGA0142": ["Teoria de Eletrônica Digital 1 - FGA0073"],
    "Fundamentos de Sistemas Operacionais - FGA0170": ["Fundamentos de Arquiteturas de Computadores - FGA0142"],
    "Fundamentos de Redes de Computadores - FGA0211": ["Fundamentos de Sistemas Operacionais - FGA0170"],
    "Programação para Sistemas Paralelos e Distribuídos - FGA0244": ["Fundamentos de Redes de Computadores - FGA0211"],
    "Fundamentos de Sistemas Embarcados - FGA0103": ["Fundamentos de Sistemas Operacionais - FGA0170"],
    "Gestão da Produção e Qualidade - FGA0173": ["Engenharia Econômica - FGA0133"],
    "Qualidade de Software 1 - FGA0315": ["Gestão da Produção e Qualidade - FGA0173"],
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
    dfs(disciplina)

    return pre_requisitos


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

if __name__ == '__main__':
    app.run(debug=True)

