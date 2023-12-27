from collections import Counter

from fabrica_dados import (usuarios,
                           conexoes)



for i, j in conexoes:
    usuarios[i]["conexoes"].append(usuarios[j])
    usuarios[j]["conexoes"].append(usuarios[i])


def numero_de_conexoes(usuario):
    return len(usuario["conexoes"])


total_de_conexoes = sum([numero_de_conexoes(usuario) for usuario in usuarios])
total_usuarios = len(usuarios)

nivel_rede = total_de_conexoes / total_usuarios

print(total_usuarios, total_de_conexoes, nivel_rede)

conexoes_por_usuario = [(usuario["id"], len(usuario["conexoes"])) for usuario in usuarios]
usuarios_mais_conectados = sorted(conexoes_por_usuario,
                                  key=lambda usuario: usuario[1],
                                  reverse=True)

print(usuarios_mais_conectados[:10])


def nao_e_o_mesmo(usuario, outro_usuario):
    return usuario["id"] != outro_usuario["id"]


def nao_sao_conexoes(usuario, outro_usuario):
    return all(nao_e_o_mesmo(conexao, outro_usuario) for conexao in usuario["conexoes"])


def conexoes_de_conexoes(usuario):
    return Counter(
        coac["id"]
        for conexao in usuario["conexoes"]
        for coac in conexao["conexoes"]
        if nao_e_o_mesmo(usuario, coac) and nao_sao_conexoes(usuario, coac)
    )


id_mais_conectado = usuarios_mais_conectados[5][0]

print(conexoes_de_conexoes(usuarios[id_mais_conectado]))





