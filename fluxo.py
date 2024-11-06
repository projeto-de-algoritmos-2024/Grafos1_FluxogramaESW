from flask import Flask, send_file, request
import networkx as nx
from PIL import Image, ImageDraw

app = Flask(__name__)

# Criar o grafo e adicionar as disciplinas com pré-requisitos
G = nx.DiGraph()
G.add_edges_from([
    ("Cálculo 1 - MAT0025", "Cálculo 2 - MAT0026"),
    ("Cálculo 2 - MAT0026", "Métodos Numéricos para Engenharia - FGA0160"),

    # volta para calculo 1
    ("Cálculo 1 - MAT0025", "Probabilidade e Estatística Aplicada à Engenharia - FGA0157"),

    # partindo de algoritmos e programação de computadores
    ("Algoritmo e Programação de Computadores - CIC0004", "Orientação a Objetos - FGA0154"),
    ("Orientação a Objetos - FGA0154", "Métodos de Desenvolvimento de Software - FGA0312"),
    ("Métodos de Desenvolvimento de Software - FGA0312", "Requisitos de Software - FGA0313"),
    ("Requisitos de Software - FGA0313", "Testes de Software - FGA0314"),
    ("Testes de Software - FGA0314", "Gerência de Configuração e Evolução de Software - FGA0317"),

    # volta para testes de software
    ("Testes de Software - FGA0314", "Técnicas de Programação em Plataformas Emergentes - FGA0242"),

    # volta para metodos de desenvolvimento de software (lembrar que pode ligar com testes de software)
    ("Métodos de Desenvolvimento de Software - FGA0312", "Interação Humano Computador - FGA0173"),
    ("Interação Humano Computador - FGA0173", "Qualidade de Software 1 - FGA0315"),

    # volta para requisitos de software
    ("Requisitos de Software - FGA0313", "Arquitetura e Desenho de Software - FGA0208"),
    ("Arquitetura e Desenho de Software - FGA0208", "Técnicas de Programação em Plataformas Emergentes - FGA0242"),
    ("Técnicas de Programação em Plataformas Emergentes - FGA0242", "Engenharia de Produto de Software - FGA0316"),

    # volta para orientação a objetos
    ("Orientação a Objetos - FGA0154", "Paradigmas de Programação - FGA0210"),

    # volta para algoritmos e programação de computadores
    ("Algoritmo e Programação de Computadores - CIC0004", "Desenvolvimento de Software - FGA0084"),

    # volta para algoritmos e programação de computadores
    ("Algoritmo e Programação de Computadores - CIC0004", "Estrutura de Dados 1 - FGA0146"),
    ("Estrutura de Dados 1 - FGA0146", "Compiladores 1 - FGA0003"),
    ("Compiladores 1 - FGA0003", "Paradigmas de Programação - FGA0210"),

    # volta para estrutura de dados 1
    ("Estrutura de Dados 1 - FGA0146", "Projeto e Análise de Algoritmos - FGA0124"),

    # volta para estrutura de dados 1
    ("Estrutura de Dados 1 - FGA0146", "Estrutura de Dados 2 - FGA0030"),
    ("Estrutura de Dados 2 - FGA0030", "Programação para Sistemas Paralelos e Distribuídos - FGA0244"),

    # partindo de introdução a algebra linear (lembrar de PED)
    ("Introdução à Álgebra Linear - MAT0031", "Teoria de Eletrônica Digital 1 - FGA0073"),
    ("Teoria de Eletrônica Digital 1 - FGA0073", "Fundamentos de Arquiteturas de Computadores - FGA0142"),
    ("Fundamentos de Arquiteturas de Computadores - FGA0142", "Fundamentos de Sistemas Operacionais - FGA0170"),
    ("Fundamentos de Sistemas Operacionais - FGA0170", "Fundamentos de Redes de Computadores - FGA0211"),
    ("Fundamentos de Redes de Computadores - FGA0211", "Programação para Sistemas Paralelos e Distribuídos - FGA0244"),

    # volta para fundamentos de sistemas operacionais
    ("Fundamentos de Sistemas Operacionais - FGA0170", "Fundamentos de Sistemas Embarcados - FGA0103"),

    # volta para introdução a algebra linear (lembrar de PED)
    ("Introdução à Álgebra Linear - MAT0031", "Teoria de Eletrônica Digital 1 - FGA0073"),

    # partindo de engenharia economica
    ("Engenharia Econômica - FGA0133", "Gestão da Produção e Qualidade - FGA0173"),
    ("Gestão da Produção e Qualidade - FGA0173", "Qualidade de Software 1 - FGA0315"),

    # partindo de matemática discreta 2
    ("Matemática Discreta 1 - FGA0085", "Matemática Discreta 2 - FGA0108"),
    ("Matemática Discreta 2 - FGA0108", "Sistema de Banco de Dados 1 - FGA0137"),
    ("Sistema de Banco de Dados 1 - FGA0137", "Sistema de Banco de Dados 2 - FGA0060"),

    # partindo de projeto integrador 1
    ("Projeto Integrador 1 - FGA0150", "Projeto Integrador de Engenharia 2 - FGA0250"),

    # partindo de trabalho de conclusão de curso 1
    ("Trabalho de Conclusão de Curso 1 - FGA0287", "Trabalho de Conclusão de Curso 2 - FGA0290"),
])

# Definir caminhos detalhados para as setas entre disciplinas
# Cada caminho é uma lista de pontos intermediários, do ponto de início ao ponto final
caminhos_setas = {
    ("Cálculo 1 - MAT0025", "Cálculo 2 - MAT0026"): [(135, 167), (182, 167)],
    #("MAT0026", "FGA160"): [(150, 55), (175, 75), (250, 55)],
    #("FGA146", "FGA108"): [(100, 155), (150, 165), (200, 155)],
    # Adicione todos os caminhos necessários

    ("Cálculo 2 - MAT0026", "Métodos Numéricos para Engenharia - FGA0160"): [(277, 167 ), (324, 167)],

    # volta para calculo 1
    ("Cálculo 1 - MAT0025", "Probabilidade e Estatística Aplicada à Engenharia - FGA0157"): [(135, 200), (144, 200), (144, 472), (180, 472), (180, 494), (174, 494), (174, 667), (182, 667)],

    ("Algoritmo e Programação de Computadores - CIC0004", "Orientação a Objetos - FGA0154"): [(135, 257), (168, 257), (168, 606), (291, 606), (291, 788), (324, 788)],
    ("Orientação a Objetos - FGA0154", "Métodos de Desenvolvimento de Software - FGA0312"): [(418, 755), (431, 755), (431, 290), (466, 290)],
    ("Métodos de Desenvolvimento de Software - FGA0312", "Requisitos de Software - FGA0313"): [(560, 290), (607, 290)],
    ("Requisitos de Software - FGA0313", "Testes de Software - FGA0314"): [(701, 290), (749, 209)],
    ("Testes de Software - FGA0314", "Gerência de Configuração e Evolução de Software - FGA0317"): [(843, 277), (853, 277), (835, 238), (1000, 238), (1000, 290), (1032, 290)],

    # volta para testes de software
    ("Testes de Software - FGA0314", "Técnicas de Programação em Plataformas Emergentes - FGA0242"): [(843, 257), (865, 257), (865, 167), (890, 167)],

    # volta para metodos de desenvolvimento de software (lembrar que pode ligar com testes de software)
    ("Métodos de Desenvolvimento de Software - FGA0312", "Interação Humano Computador - FGA0173"): [(560, 257), (583, 257), (583, 213), (572, 213), (572, 167), (607, 167)],
    ("Interação Humano Computador - FGA0173", "Qualidade de Software 1 - FGA0315"): [(701, 167), (749, 167)],

    # volta para requisitos de software
    ("Requisitos de Software - FGA0313", "Arquitetura e Desenho de Software - FGA0208"): [(701, 297), (721, 297), (721, 389), (749, 389)],
    ("Arquitetura e Desenho de Software - FGA0208", "Técnicas de Programação em Plataformas Emergentes - FGA0242"): [(843, 389), (870, 389), (870, 200), (890, 200)],
    ("Técnicas de Programação em Plataformas Emergentes - FGA0242", "Engenharia de Produto de Software - FGA0316"): [(984, 167), (1032, 167)],

    # volta para orientação a objetos
    ("Orientação a Objetos - FGA0154", "Paradigmas de Programação - FGA0210"): [(418, 788), (442, 788), (442, 476), (856, 476), (856, 290), (890, 290)],

    # volta para algoritmos e programação de computadores
    ("Algoritmo e Programação de Computadores - CIC0004", "Desenvolvimento de Software - FGA0084"): [(135, 290), (162, 290), (162, 790), (182, 790)],

    # volta para algoritmos e programação de computadores
    ("Algoritmo e Programação de Computadores - CIC0004", "Estrutura de Dados 1 - FGA0146"): [(135, 323), (177, 323), (177, 357), (440, 357), (440, 419), (466, 219)],
    ("Estrutura de Dados 1 - FGA0146", "Compiladores 1 - FGA0003"): [(560, 387), (579, 387), (579, 667), (607, 667)],
    ("Compiladores 1 - FGA0003", "Paradigmas de Programação - FGA0210"): [(701, 667), (712, 667), (712, 607), (873, 607), (873, 323), (890, 323)],

    # volta para estrutura de dados 1
    ("Estrutura de Dados 1 - FGA0146", "Projeto e Análise de Algoritmos - FGA0124"): [(560, 419), (579, 419), (579, 729), (710, 729), (710, 757), (748, 757)],

    # volta para estrutura de dados 1
    ("Estrutura de Dados 1 - FGA0146", "Estrutura de Dados 2 - FGA0030"): [(560, 452), (579, 452), (579, 789), (606, 789)],
    ("Estrutura de Dados 2 - FGA0030", "Programação para Sistemas Paralelos e Distribuídos - FGA0244"): [(700, 789), (719, 789), (719, 736), (861, 736), (861, 577), (889, 577)],

    # partindo de introdução a algebra linear (lembrar de PED)
    ("Introdução à Álgebra Linear - MAT0031", "Teoria de Eletrônica Digital 1 - FGA0073"): [(277, 243), (323, 543)],
    ("Teoria de Eletrônica Digital 1 - FGA0073", "Fundamentos de Arquiteturas de Computadores - FGA0142"): [(417, 544), (466, 544)],
    ("Fundamentos de Arquiteturas de Computadores - FGA0142", "Fundamentos de Sistemas Operacionais - FGA0170"): [(560, 544), (607, 544)],
    ("Fundamentos de Sistemas Operacionais - FGA0170", "Fundamentos de Redes de Computadores - FGA0211"): [(701, 544), (748, 544)],
    ("Fundamentos de Redes de Computadores - FGA0211", "Programação para Sistemas Paralelos e Distribuídos - FGA0244"): [(842, 544), (889, 544)],

    # volta para fundamentos de sistemas operacionais
    ("Fundamentos de Sistemas Operacionais - FGA0170", "Fundamentos de Sistemas Embarcados - FGA0103"): [(701, 512), (737, 512), (737, 489), (863, 489), (863, 422), (889, 442)],

    # volta para introdução a algebra linear (lembrar de PED)
    #("Introdução à Álgebra Linear - MAT0031", "Teoria de Eletrônica Digital 1 - FGA0073"): [(737, 489), (863, 489)],

    # partindo de engenharia economica
    ("Engenharia Econômica - FGA0133", "Gestão da Produção e Qualidade - FGA0173"): [(418, 257), (427, 257), (427, 239), (421, 239), (421, 218), (427, 218), (427, 167), (466, 167)],
    ("Gestão da Produção e Qualidade - FGA0173", "Qualidade de Software 1 - FGA0315"): [(560, 200), (595, 200), (595, 219), (727, 219), (727, 200), (749, 200)],

    # partindo de matemática discreta 1
    ("Matemática Discreta 1 - FGA0085", "Matemática Discreta 2 - FGA0108"): [(417, 910), (453, 910), (453, 667), (466, 667)],
    ("Matemática Discreta 2 - FGA0108", "Sistema de Banco de Dados 1 - FGA0137"): [(560, 649), (587, 649), (587, 419), (607, 419)],
    ("Sistema de Banco de Dados 1 - FGA0137", "Sistema de Banco de Dados 2 - FGA0060"): [(701, 419), (724, 419), (724, 667), (748, 667)],

    # partindo de projeto integrador 1
    ("Projeto Integrador 1 - FGA0150", "Projeto Integrador de Engenharia 2 - FGA0250"): [(560, 912), (1177, 912)],

    # partindo de trabalho de conclusão de curso 1
    ("Trabalho de Conclusão de Curso 1 - FGA0287", "Trabalho de Conclusão de Curso 2 - FGA0290"): [(1269, 790), (1316, 790)],
   
}

@app.route('/highlight_path', methods=['POST'])
def highlight_path():
    data = request.json
    start_node = data.get("disciplina")

    # Verificar se a disciplina está no grafo
    if start_node not in G:
        return {"error": "Disciplina não encontrada no grafo"}, 400

    # Buscar apenas as dependências diretas da disciplina
    path_edges = list(G.in_edges(start_node))  # Usamos in_edges para encontrar dependências que entram na disciplina

    # Depuração: Verifique o que foi encontrado nos in_edges
    print(f"Caminhos encontrados para {start_node}: {path_edges}")

    # Carregar a imagem original do fluxograma
    img = Image.open("fluxoSFW.png")
    draw = ImageDraw.Draw(img)

    # Desenhar o caminho de cada seta usando os pontos intermediários
    for u, v in path_edges:
        # Apenas desenhar os caminhos para as dependências diretas (entrando na disciplina)
        if (u, v) in caminhos_setas:
            pontos = caminhos_setas[(u, v)]
            print(f"Pontos encontrados para a aresta ({u}, {v}): {pontos}")
            # Desenhar linha entre cada par de pontos no caminho
            for i in range(len(pontos) - 1):
                draw.line([pontos[i], pontos[i + 1]], fill="red", width=5)

    # Salvar e retornar a imagem destacada
    img.save("fluxograma_destacado.png")
    return send_file("fluxograma_destacado.png", mimetype="image/png")


if __name__ == '__main__':
    app.run(debug=True)
