import verificador_cpf
import candidatos
import apuracao
import criptografia

#Pede o voto para o usuário
def pedir_voto ():
    while True:
        try:
            voto = int(input("Digite o número correspondente ao seu voto: "))
            return voto
        except ValueError:
            print("Por favor, insira um número válido.\n")

#Pede o CPF para o usuário            
def pedir_cpf ():
    while True:
        try:
            cpf = input("\nInsira seu CPF (Apenas números): ")
            verificar = int(cpf)
            return cpf
        except ValueError:
            print("CPF inválido, insira novamente!!!\n")
    
#Menu da Urna
opcao = "0"
while opcao != "3":
    opcao = input("\nVotar: 1\nApurar os votos: 2\nSair do menu: 3\nDigite o número referente a ação desejada: ")
    opcoes = ("1", "2", "3")
    
    #Verificação dentro da tupla (opcoes)
    while opcao not in opcoes:
        opcao = input("\nOpção não idetificada!!!\n\nVotar: 1\nApurar os votos: 2\nSair do menu: 3\nDigite o número referente a ação desejada: \n")
    
    #Opção 1 (Votar)
    if opcao == "1":
        
        #Cadastro CPF
        cpf = pedir_cpf ()
        cpf_verificado = verificador_cpf.verificacao_cpf (cpf)
        while cpf_verificado is False:
            print("CPF inválido, insira novamente!!!\n")
            cpf = pedir_cpf ()
            cpf_verificado = verificador_cpf.verificacao_cpf (cpf)
            
        #Cadatro voto
        print("\nLista de candidatos:\n")
        print("Ivan Soares: 10\nRaphael Gomes: 17\nSamantha Alves: 21\nBranco: 0\nNulo: 1\n")
        numeros = (10, 17, 21, 33, 0, 1)
        voto = pedir_voto ()
        
        #Verificação dentro da tupla (numeros)
        while voto not in numeros:
            print("Por favor, insira um número válido.\n")
            print("Lista de candidatos:\n")
            print("Ivan Soares: 10\nRaphael Gomes: 17\nSamantha Alves: 21\nBranco: 0\nNulo: 1\n")
            voto = pedir_voto ()
        
        #Contabiliza os votos
        candidatos.contador_votos(voto)
        candidatos.salvar_resultado()
        
    #Opção 2 (Apurar votos)
    elif opcao == "2":
        sim = ("Sim", "SIM", "sim")
        nao = ("Não", "Nao", "não", "nao", "NAO", "NÃO")
        print("\nApós a apuração, o registro será apagado.")
        resposta = input("Deseja continuar? (Sim ou Não): ")
        while resposta not in (sim) and resposta not in nao:
            resposta = input("\nResposta incompatível\nDeseja continuar? (Sim ou Não): ")
        
        if resposta in sim:
            #apuracao.apuracao()
            senha_correta = apuracao.apuracao()
            if senha_correta == True:
                with open("cpf_cadastrado.txt", "w") as limpar_cpf:
                    pass
                with open("resultados.txt", "w", encoding="utf-8") as limpar_resultado:
                    pass
                with open("hash.txt", "w", encoding="utf-8") as limpar_cpf:
                    pass
                print("\nFim da votação")
        elif resposta in nao:
            pass
            
print("\nPrograma encerrado")
        
