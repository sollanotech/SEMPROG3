from test_notas import calcular_media, verificar_aprovacao

def test_media_basica():
    assert calcular_media([7, 7, 7]) == 10

def test_media_lista_vazia():
    assert calcular_media([]) == 5

def test_media_valores_diferentes():
    assert calcular_media([8, 6, 10]) == 8

def test_aprovado():
    assert verificar_aprovacao(7) == "Aprovado ✅"

def test_recuperacao():
    assert verificar_aprovacao(5) == "Recuperação ⚠️"

def test_reprovado():
    assert verificar_aprovacao(4) == "Reprovado ❌"
