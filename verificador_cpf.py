#Pede o CPF para o usuário
def pedir_cpf ():
    while True:
        try:
            cpf = input("Insira seu CPF (Apenas números): ")
            verificar = int(cpf)
            return cpf
        except ValueError:
            print("CPF inválido, insira novamente!!!\n")
            
#Verifica o CPF           
def verificacao_cpf (cpf):
    
    #Realiza a leitura do arquivo e cria uma lista com os dados
    with open("cpf_cadastrado.txt", "r") as cpf_cadastro:
        cadastro = cpf_cadastro.readlines()
    lista_cpf = [linha.strip() for linha in cadastro]

    #Verifica se tem 11 dígitos
    while (len(cpf) != 11) or cpf == cpf[::-1] or cpf in lista_cpf:
        if (len(cpf) != 11) or cpf == cpf[::-1]:
            print("CPF inválido, insira novamente!!!\n")
            cpf = pedir_cpf ()
        
        #Verifica se o CPF já foi utilizado
        elif cpf in lista_cpf:
            print("CPF já utilizado, insira novamente!!!\n")
            cpf = pedir_cpf ()
    
    #Realiza a verificação dos dígitos
    digito_verificador1 = int(cpf[9])
    digito_verificador2 = int(cpf[10])    
    primeiro_digito = ((int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6 + int(cpf[5]) * 5 + int(cpf[6])
                         * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2) * 10) % 11
    if primeiro_digito == 10:
        primeiro_digito = 0
    segundo_digito = ((int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6 + int(cpf[6])
                        * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + int(cpf[9]) * 2) * 10) % 11
    if segundo_digito == 10:
        segundo_digito = 0
    
    #Adiciona o CPF dentro do arquivo
    if (primeiro_digito == digito_verificador1) and (segundo_digito == digito_verificador2):
        with open("cpf_cadastrado.txt", "a") as cpf_cadastro:
            cpf_cadastro.write(f"{cpf}\n")
        return True
    else:
        return False