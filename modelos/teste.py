
import re  # biblioteca para manipulação de strings (regex)

# =========================
# FUNÇÕES DE VALIDAÇÃO
# =========================

def validar_cnh(cnh):
    # Remove todos os caracteres que não são números (ex: ".", "-", espaços)
    cnh = re.sub(r'\D', '', cnh)

    # Verifica se a CNH tem exatamente 11 dígitos
    if len(cnh) != 11:
        return False

    # Verifica se todos os dígitos são iguais (ex: 11111111111)
    if cnh == cnh[0] * 11:
        return False

    # Cálculo do Primeiro Dígito Verificador (DV1)
    soma = 0
    # Pesos de 9 até 1
    for i in range(9):
        soma += int(cnh[i]) * (9 - i)

    resto1 = soma % 11
    
    # Define o valor do decremento para o próximo cálculo
    # Se o resto for > 9, o dígito é 0 e o decremento é 2
    if resto1 > 9:
        v_dsc = 2
        dig1 = 0
    else:
        v_dsc = 0
        dig1 = resto1

    # Cálculo do Segundo Dígito Verificador (DV2)
    soma = 0
    # Pesos de 1 até 9
    for i in range(9):
        soma += int(cnh[i]) * (1 + i)

    resto2 = soma % 11
    
    # Aplicação da regra do decremento
    dig2 = resto2 - v_dsc
    
    # Ajustes finais para o segundo dígito
    if dig2 < 0:
        dig2 += 11
    if dig2 > 9:
        dig2 = 0

    # Comparação Final
    # Verifica se os dígitos calculados batem com os informados
    return str(dig1) == cnh[9] and str(dig2) == cnh[10]

    
def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10

    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])


def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
    return re.match(padrao, email) is not None
