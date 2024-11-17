import candidatos
import criptografia

#Função para a apuração
def apuracao():
    chave = input("Digite a senha: ")
    
    #Ação com a senha correta
    if chave == "VotacaoUnip2024":
        
        #Realiza a leitura do resultado
        with open("resultados.txt", "r", encoding="utf-8") as arquivo:
                resultado_criptografado = arquivo.read()

        #Verificar se o arquivo está em branco
        if resultado_criptografado == "":
            print(f"\nRelatório de votação.\nURNA 013022\n")
            print(f"\nNão há registro de votos.\n")
        
        #Realiza o relatório de votação
        if criptografia.validar_hash():

            #Realiza a leitura do resultado
            with open("resultados.txt", "r", encoding="utf-8") as arquivo:
                resultado_criptografado = arquivo.read()
            
            #Descriptograva e imprime o resultado
            resultado = criptografia.descriptografar(resultado_criptografado, chave)
            apuracao = eval(resultado)
            total_votos = sum(apuracao.values())
            print(f"\nRelatório de votação.\nURNA 013022")
            if total_votos > 0:
                print(f"\nTotal de votos: {total_votos}\n")
                for nome, votos in apuracao.items():
                    porcentagem = (votos/total_votos) * 100
                    print(f"{nome}: {porcentagem:.2f}% - ({votos} Votos)")
            return True
        
    #Ação com a senha incorreta              
    else:
        print("Senha incorreta!!!\n")
        print(f"Relatório de votação.\nURNA 013022\n")
        with open("resultados.txt", "r", encoding="utf-8") as arquivo:
                resultado_criptografado = arquivo.read()
        if resultado_criptografado == "":
            print(f"Não há registro de votos.")
        else:
            print(resultado_criptografado)
        return False

