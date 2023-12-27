import random
from collections import Counter, defaultdict


def gerar_codigo(tamanho=9):
    letras = [*"QWERTYUIOPASDFGHJKLZXCVBNM"]
    numeros = range(10)

    codigo = ""

    for i in range(tamanho):
        if i % 2 == 0:
            caracter = letras[random.randrange(0, len(letras))]
        else:
            caracter = str(numeros[random.randrange(0, len(numeros))])

        codigo += caracter

    return codigo


def gerar_lista_usuarios(tamanho=1000000):
    lista = []
    for i in range(tamanho):
        codigo = gerar_codigo()
        lista.append({"id": i, "nome": f"Usuário {codigo}", "conexoes": []})
    return lista


def gerar_lista_conexoes(lista_usuarios):
    conexoes = []
    for seq, usuario in enumerate(lista_usuarios):
        for _ in range(random.randrange(0, 6)):
            index = random.randrange(0, len(lista_usuarios))
            if index == seq:
                if index == len(lista_usuarios) - 1:
                    index = index - 1
                else:
                    index = index + 1

            usuario_rel = lista_usuarios[index]
            conexoes.append((usuario["id"], usuario_rel["id"]))

    return conexoes


def gerar_lista_interesses(lista_usuarios):
    opcoes_interesses = ["Aprendizado de Máquina",
                         "Análise de Dados",
                         "Processamento de Linguagem Natural (PNL)",
                         "Big Data",
                         "Bancos de Dados",
                         "Estatística",
                         "Ciência Reprodutiva",
                         "Engenharia de Recursos",
                         "Desenvolvimento de Software",
                         "Ética em Ciência de Dados",
                         "Reconhecimento de Padrões",
                         "Otimização de Modelos",
                         "Visualização de Dados Interativa",
                         "IoT (Internet of Things) e Ciência de Dados",
                         "Processamento de Imagens",
                         "Processamento de Sinais",
                         "Análise de Redes Sociais",
                         "Mineração de Texto",
                         "Análise de Séries Temporais",
                         "Aprendizado por Reforço",
                         "Análise de Fraudes",
                         "Análise de Cliente e Segmentação de Mercado",
                         "Análise de Sentimento em Mídias Sociais",
                         "Aprendizado Não Supervisionado",
                         "Aprendizado Semissupervisionado"]

    interesses_usuario = []

    for seq, usuario in enumerate(lista_usuarios):
        interesses = []
        for _ in range(random.randrange(0, 5)):
            index = random.randrange(0, len(opcoes_interesses))
            interesse = opcoes_interesses[index]
            if interesse not in interesses:
                interesses.append(interesse)
                interesses_usuario.append((usuario["id"], interesse))

    return interesses_usuario


def gerar_lista_salarios(tamanho=1000):
    lista = []
    for i in range(tamanho):
        salario = random.randrange(40000, 100000)
        experiencia = random.randrange(10, 100) / 10.0
        lista.append((salario, experiencia))
    return lista



