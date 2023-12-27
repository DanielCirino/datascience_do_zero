from collections import Counter, defaultdict

from fabrica_dados import interesses_usuarios, usuarios


def usuarios_que_se_interessam_por(tema):
    return [id_usuario
            for id_usuario, interesse in interesses_usuarios
            if interesse == tema]


print(len(usuarios_que_se_interessam_por("Big Data")))

ids_usuario_por_interesse = defaultdict(list)
interesses_por_id_usuario = defaultdict(list)

for id_usuario, interesse in interesses_usuarios:
    ids_usuario_por_interesse[interesse].append(id_usuario)
    interesses_por_id_usuario[id_usuario].append(interesse)

def usuarios_com_mesmos_interesses(usuario):
    return Counter(id_usuario_interessado
                   for interesse in interesses_por_id_usuario[usuario["id"]]
                   for id_usuario_interessado in ids_usuario_por_interesse[interesse]
                   if id_usuario_interessado != usuario["id"])


print(usuarios_com_mesmos_interesses(usuarios[56]))