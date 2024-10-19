import os
os.system ("cls || clear")


def calcular_inss(salario_base):
    if salario_base <= 1100.00:
        return salario_base * 0.075
    elif salario_base <= 2203.48:
        return salario_base * 0.09
    elif salario_base <= 3305.22:
        return salario_base * 0.12
    elif salario_base <= 6433.57:
        return salario_base * 0.14
    else:
        return 854.36  # Teto máximo do INSS


def calcular_irrf(salario_base, dependentes):
    deducao_dependente = 189.59 * dependentes
    base_irrf = salario_base - deducao_dependente - calcular_inss(salario_base)
    
    if base_irrf <= 2259.20:
        return 0.0
    elif base_irrf <= 2826.65:
        return base_irrf * 0.075
    elif base_irrf <= 3751.05:
        return base_irrf * 0.15
    elif base_irrf <= 4664.68:
        return base_irrf * 0.225
    else:
        return base_irrf * 0.275

def calcular_folha_pagamento():
 
    matricula = input("Informe a matrícula do funcionário: ")
    senha = input("Informe a senha: ")
    salario_base = float(input("Informe o salário base (em R$): "))
    vale_transporte = input("Deseja receber vale transporte? (s/n): ").lower()
    vale_refeicao = float(input("Informe o valor do vale refeição fornecido pela empresa (em R$): "))
    dependentes = 1  # Considerando apenas 1 dependente
    
   
    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, dependentes)
 
    vt = salario_base * 0.06 if vale_transporte == 's' else 0.0
  
    vr = vale_refeicao * 0.20
  
    plano_saude = 150.00 * dependentes
   
    salario_liquido = salario_base - (inss + irrf + vt + vr + plano_saude)
    
    print("\n======= Resumo da Folha de Pagamento =======")
    print(f"\nSalário Base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {vt:.2f}")
    print(f"Desconto Vale Refeição: R$ {vr:.2f}")
    print(f"Desconto Plano de Saúde: R$ {plano_saude:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Chama a função principal
calcular_folha_pagamento()
