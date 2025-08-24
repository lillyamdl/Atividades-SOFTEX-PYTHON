valor_hora = float(input("Valor recebido por hora trabalhada: "))
quant_hora = int(input("Qntd de hrs trabalhadas: "))
sala_brut = valor_hora * quant_hora
desc_renda = 11/100
desc_INSS = 9/100
desc_sind = 4/100
def sala_liq(sala_brut):
    desc_total = desc_renda  + desc_INSS + desc_sind
    desconto = sala_brut * desc_total
    salario = sala_brut - desconto
    print(f"Salario bruto: R${sala_brut:.2f}")
    print(f"IR(11%) : R$ {desc_renda:.2f}")
    print(f"INSS(%9) : R$ {desc_INSS: .2f}")
    print(f"Sindicato(4%) : R$ {desc_sind:.2f}")
    print(f"Salario liquido: R$ {salario:.2f}")
    return salario

print(sala_liq(sala_brut))
