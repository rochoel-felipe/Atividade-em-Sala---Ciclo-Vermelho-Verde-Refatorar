# ============================================================
# PADRÃO DE PROJETO APLICADO: Strategy
#
# Participantes (conforme o domínio):
#   - Strategy (interface):      EstrategiaFrete
#   - ConcreteStrategy:          FretePadrao, FreteExpresso, RetiradaNaLoja
#   - Context:                   calcular_frete (escolhe e usa a estratégia)
# ============================================================

from abc import ABC, abstractmethod


class EstrategiaFrete(ABC):
    """Strategy: contrato que todo tipo de frete deve seguir."""

    @abstractmethod
    def calcular(self, peso_kg):
        pass


class FretePadrao(EstrategiaFrete):
    """ConcreteStrategy: R$ 10,00 + R$ 2,00 por kg."""

    def calcular(self, peso_kg):
        return 10.00 + 2.00 * peso_kg


class FreteExpresso(EstrategiaFrete):
    """ConcreteStrategy: R$ 25,00 + R$ 4,00 por kg."""

    def calcular(self, peso_kg):
        return 25.00 + 4.00 * peso_kg


class RetiradaNaLoja(EstrategiaFrete):
    """ConcreteStrategy: sempre grátis."""

    def calcular(self, peso_kg):
        return 0.00


ESTRATEGIAS = {
    "padrao": FretePadrao(),
    "expresso": FreteExpresso(),
    "retirada": RetiradaNaLoja(),
}


def calcular_frete(tipo, peso_kg):
    """Context: delega o cálculo para a estratégia do tipo escolhido."""
    return ESTRATEGIAS[tipo].calcular(peso_kg)

# ============================================================
# AUTOAVALIAÇÃO
# Critérios feitos:
#   1. Testes em arquivo separado, um teste por variação
#   2. Três commits, um por fase (red, green, refactor)
#   3. Commit red contém só os testes
#   4. Strategy nomeado, participantes com nomes do domínio
#   5. Suíte passa após refatoração, saída em resultado_testes.txt
#
# O que mudou entre verde e refatorado:
#   O if/elif único virou uma classe por tipo de frete. Para criar
#   um novo tipo agora basta uma nova classe e uma linha no dicionário,
#   sem mexer nas regras dos outros tipos.
#
# Parte que deu mais trabalho: entender e aplicar os conceitos de red green refatorar
#
# Uso de IA: Utilizei para tirar duvidas do Strategy, e subir no github
# ============================================================