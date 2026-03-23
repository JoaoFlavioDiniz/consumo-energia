#Programa é calculadora de consumo elétrico inteligente.
#  O objetivo é ajudar usuários a estimar quanto um aparelho gasta de energia elétrica por mês, com base em dados
#  simples de uso.

aparelho = input("Digite o nome Aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts: "))
horasDia = float(input("Quantas horas o aparelho funciona em média por dia?: "))
consumoMensal = (potencia * horasDia * 30) / 1000
custoEstimado = consumoMensal * 0.75

print("-" * 30) # Linha separadora para organizar o visual
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
# Ajuste no texto para "Custo mensal estimado"
print(f"Custo mensal estimado (R$ 0,75/kWh): R$ {custoEstimado:.2f}")
print("-" * 30)