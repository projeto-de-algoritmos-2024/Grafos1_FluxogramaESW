import networkx as nx
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

# Criação dos Nós

# Criando o grafo direcionado
G = nx.DiGraph()

# Adiciona os nós 
# 1° semestre
G.add_node("Cálculo 1 - MAT0025")
G.add_node("Algoritmo e Programação de Computadores - CIC0004")
G.add_node("Desenho Industrial Assistido por Computador - FGA0168")
G.add_node("Engenharia e Ambientes - FGA0302")
G.add_node("Introdução à Engenharia - FGA0163")

# 2° semestre
G.add_node("Cálculo 2 - MAT0026")
G.add_node("Física 1 - IFD0171")
G.add_node("Física 1 Experimental - IFD0173")
G.add_node("Introdução à Álgebra Linear - MAT0031")
G.add_node("Probabilidade e Estatística Aplicada à Engenharia - FGA0157")
G.add_node("Desenvolvimento de Software - FGA0084")

# 3° semestre
G.add_node("Métodos Numéricos para Engenharia - FGA0160")
G.add_node("Engenharia Econômica - FGA0133")
G.add_node("Humanidades e Cidadania - FGA0164")
G.add_node("Teoria de Eletrônica Digital 1 - FGA0073")
G.add_node("Prática de Eletrônica Digital 1 - FGA0071")
G.add_node("Orientação a Objetos - FGA0154")
G.add_node("Matemática Discreta 1 - FGA0085")

# 4° semestre
G.add_node("Gestão da Produção e Qualidade - FGA0173")
G.add_node("Métodos de Desenvolvimento de Software - FGA0312")
G.add_node("Estrutura de Dados 1 - FGA0146")
G.add_node("Fundamentos de Arquiteturas de Computadores - FGA0142")
G.add_node("Matemática Discreta 2 - FGA0108")
G.add_node("Projeto Integrador 1 - FGA0150")

# 5° semestre
G.add_node("Interação Humano Computador - FGA0173")
G.add_node("Requisitos de Software - FGA0313")
G.add_node("Sistema de Banco de Dados 1 - FGA0137")
G.add_node("Fundamentos de Sistemas Operacionais - FGA0170")
G.add_node("Compiladores 1 - FGA0003")
G.add_node("Estrutura de Dados 2 - FGA0030")

# 6° semestre
G.add_node("Qualidade de Software 1 - FGA0315")
G.add_node("Testes de Software - FGA0314")
G.add_node("Arquitetura e Desenho de Software - FGA0208")
G.add_node("Fundamentos de Redes de Computadores - FGA0211")
G.add_node("Sistema de Banco de Dados 2 - FGA0060")
G.add_node("Projeto e Análise de Algoritmos - FGA0124")

# 7° semestre
G.add_node("Técnicas de Programação em Plataformas Emergentes - FGA0242")
G.add_node("Paradigmas de Programação - FGA0210")
G.add_node("Fundamentos de Sistemas Embarcados - FGA0103")
G.add_node("Programação para Sistemas Paralelos e Distribuídos - FGA0244")

# 8° semestre
G.add_node("Engenharia de Produto de Software - FGA0316")
G.add_node("Gerência de Configuração e Evolução de Software - FGA0317")

# 9° semestre
G.add_node("Trabalho de Conclusão de Curso 1 - FGA0287")
G.add_node("Projeto Integrador de Engenharia 2 - FGA0250")

# 10° semestre
G.add_node("Trabalho de Conclusão de Curso 2 - FGA0290")


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

# Lista de disciplinas concluídas
disciplinas_concluidas = set()  # Inicialmente vazia

# Função para verificar disciplinas liberadas usando BFS
def disciplinas_liberadas(grafo, concluidas):
    liberadas = set()
    for disciplina in concluidas:
        # Verifica cada vizinho da disciplina concluída
        for vizinho in grafo.successors(disciplina):
            # Todos os pré-requisitos do vizinho devem estar concluídos
            pre_requisitos = set(grafo.predecessors(vizinho))
            if pre_requisitos.issubset(concluidas):
                liberadas.add(vizinho)
    return liberadas - concluidas  # Remove disciplinas que já foram concluídas

# Inicializando o app Dash
app = dash.Dash(__name__)

# Layout do app
app.layout = html.Div([
    html.H1("Fluxograma de Engenharia de Software - UnB"),
    dcc.Graph(id='graph', config={'displayModeBar': False}),
    html.Div(id='output-container', style={'margin-top': '20px'})
])

# Função para atualizar o grafo e exibir as disciplinas liberadas
@app.callback(
    Output('graph', 'figure'),
    Output('output-container', 'children'),
    Input('graph', 'clickData')  # Detecta clique em um nó
)
def update_graph(clickData):

    global disciplinas_concluidas
    
    # Marca uma disciplina como concluída quando o usuário clica nela
    if clickData:
        selected_course = clickData['points'][0]['text']
        disciplinas_concluidas.add(selected_course)  # Adiciona a disciplina como concluída

    # Obter as disciplinas liberadas
    liberadas = disciplinas_liberadas(G, disciplinas_concluidas)
    liberadas_texto = "Disciplinas liberadas: " + ", ".join(liberadas)

    # Define posições fixas para cada nó, organizadas por semestre
    pos = {
        # 1º Semestre
        "Cálculo 1 - MAT0025": (0, 7),
        "Algoritmo e Programação de Computadores - CIC0004": (0, 5.5),
        "Desenho Industrial Assistido por Computador - FGA0168": (0, 4),
        "Engenharia e Ambientes - FGA0302": (0, 2.5),
        "Introdução à Engenharia - FGA0163": (0, 1),
        
        # 2º Semestre
        "Cálculo 2 - MAT0026": (1.5, 7),
        "Física 1 - IFD0171": (1.5, 5.5),
        "Física 1 Experimental - IFD0173": (1.5, 4),
        "Introdução à Álgebra Linear - MAT0031": (1.5, 2.5),
        "Probabilidade e Estatística Aplicada à Engenharia - FGA0157": (1.5, 1),
        "Desenvolvimento de Software - FGA0084": (1.5, -0.5),
        
        # 3º Semestre
        "Métodos Numéricos para Engenharia - FGA0160": (3, 7),
        "Engenharia Econômica - FGA0133": (3, 5.5),
        "Humanidades e Cidadania - FGA0164": (3, 4),
        "Teoria de Eletrônica Digital 1 - FGA0073": (3, 2.5),
        "Prática de Eletrônica Digital 1 - FGA0071": (3, 1),
        "Orientação a Objetos - FGA0154": (3, -0.5),
        "Matemática Discreta 1 - FGA0085": (3, -1),

        # 4º Semestre
        "Gestão da Produção e Qualidade - FGA0173": (4.5, 7),
        "Métodos de Desenvolvimento de Software - FGA0312": (4.5, 5.5),
        "Estrutura de Dados 1 - FGA0146": (4.5, 4),
        "Fundamentos de Arquiteturas de Computadores - FGA0142": (4.5, 2.5),
        "Matemática Discreta 2 - FGA0108": (4.5, 1),
        "Projeto Integrador 1 - FGA0150": (4.5, -0.5),
        
        # 5º Semestre
        "Interação Humano Computador - FGA0173": (6, 7),
        "Requisitos de Software - FGA0313": (6, 5.5),
        "Sistema de Banco de Dados 1 - FGA0137": (6, 4),
        "Fundamentos de Sistemas Operacionais - FGA0170": (6, 2.5),
        "Compiladores 1 - FGA0003": (6, 1),
        "Estrutura de Dados 2 - FGA0030": (6, -0.5),
        
        # 6º Semestre
        "Qualidade de Software 1 - FGA0315": (7.5, 7),
        "Testes de Software - FGA0314": (7.5, 5.5),
        "Arquitetura e Desenho de Software - FGA0208": (7.5, 4),
        "Fundamentos de Redes de Computadores - FGA0211": (7.5, 2.5),
        "Sistema de Banco de Dados 2 - FGA0060": (7.5, 1),
        "Projeto e Análise de Algoritmos - FGA0124": (7.5, -0.5),
        
        # 7º Semestre
        "Técnicas de Programação em Plataformas Emergentes - FGA0242": (9, 7),
        "Paradigmas de Programação - FGA0210": (9, 5.5),
        "Fundamentos de Sistemas Embarcados - FGA0103": (9, 4),
        "Programação para Sistemas Paralelos e Distribuídos - FGA0244": (9, 2.5),
        
        # 8º Semestre
        "Engenharia de Produto de Software - FGA0316": (10.5, 7),
        "Gerência de Configuração e Evolução de Software - FGA0317": (10.5, 5.5),
        
        # 9º Semestre
        "Trabalho de Conclusão de Curso 1 - FGA0287": (12, 7),
        "Projeto Integrador de Engenharia 2 - FGA0250": (12, 5.5),
        
        # 10º Semestre
        "Trabalho de Conclusão de Curso 2 - FGA0290": (13.5, 7)
    }
    
    # Código para desenhar arestas e nós usando as posições fixas
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1.5, color='#888'),  # Aumentando a espessura e ajustando a cor
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    node_text = []
    node_color = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)

        # Define a cor dos nós
        if node in disciplinas_concluidas:
            node_color.append("lightgreen")  # Concluídas em verde claro
        elif node in liberadas:
            node_color.append("lightblue")  # Liberadas em azul claro
        else:
            node_color.append("lightgrey")  # Não liberadas em cinza claro

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=node_text,
        textposition="middle center",
        hoverinfo='text',
        marker=dict(
            showscale=False,
            symbol="square",
            size=50,
            color=node_color,  # Aplica a lista de cores
            line=dict(width=1, color='#333')
        ),
        textfont=dict(size=10)
    )


    # Construindo a figura
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='Mapa de Disciplinas',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                    ))

    return fig, liberadas_texto


if __name__ == '__main__':
    app.run_server(debug=True)