def calcular_media(notas):
    """Calcula média de uma lista de notas"""
    if not notas:
        return 0
    return sum(notas) / len(notas)


def verificar_aprovacao(media):
    """Diz se o aluno foi aprovado ou não"""
    if media >= 7:
        return "Aprovado ✅"
    elif media >= 5:
        return "Recuperação ⚠️"
    else:
        return "Reprovado ❌"