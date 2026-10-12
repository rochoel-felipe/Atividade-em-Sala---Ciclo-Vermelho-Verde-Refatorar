# ============================================================
# PLANO
# Problema: calculadora de frete de uma loja online.
# Casos de teste (uma variação de comportamento cada):
#   1. Frete padrão:      R$ 10,00 + R$ 2,00 por kg
#   2. Frete expresso:    R$ 25,00 + R$ 4,00 por kg
#   3. Retirada na loja:  sempre R$ 0,00
# Padrão de projeto escolhido: Strategy
# Por quê: cada tipo de frete é uma regra diferente e novos tipos
#          podem surgir; Strategy evita um if/elif crescendo sem parar.
# Tempo planejado: red 25 min | green 25 min | refactor 40 min
# Uso de IA: (preencha se for usar. Ex.: tirar dúvida sobre Strategy)
# ============================================================

from frete import calcular_frete


def test_frete_padrao():
    # 10 + 2 * 3 = 16
    assert calcular_frete("padrao", peso_kg=3) == 16.00


def test_frete_expresso():
    # 25 + 4 * 3 = 37
    assert calcular_frete("expresso", peso_kg=3) == 37.00


def test_retirada_na_loja_e_gratis():
    assert calcular_frete("retirada", peso_kg=3) == 0.00