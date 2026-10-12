def calcular_frete(tipo, peso_kg):
    if tipo == "padrao":
        return 10.00 + 2.00 * peso_kg
    elif tipo == "expresso":
        return 25.00 + 4.00 * peso_kg
    elif tipo == "retirada":
        return 0.00