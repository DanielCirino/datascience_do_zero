from collections import defaultdict

from fabrica_dados import gerar_lista_salarios

salarios = gerar_lista_salarios()


def faixa_experiencia(anos):
    if anos < 3:
        return "a) até 3 anos"
    elif anos < 6:
        return "b) de 3 a 5 anos"
    else:
        return "c) mais de 5 anos"


salarios_por_experiencia = defaultdict(list)
for salario, experiencia in salarios:
    faixa = faixa_experiencia(experiencia)
    salarios_por_experiencia[faixa].append(salario)

media_salarial_por_faixa = {
    faixa: sum(salarios) / len(salarios)
    for faixa, salarios in salarios_por_experiencia.items()
}

print(media_salarial_por_faixa)
