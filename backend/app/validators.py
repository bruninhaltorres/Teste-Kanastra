from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_valido(nome):
    if all(char.isalpha() or char.isspace() for char in nome):
        return True
    return False 