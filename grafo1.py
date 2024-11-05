import networkx as nx

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













