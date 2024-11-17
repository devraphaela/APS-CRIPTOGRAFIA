import criptografia

#Realiza a leitura do arquivo
with open("resultados.txt", "r", encoding="utf-8") as arquivo:
    resultado_txt = arquivo.read()

#Ação caso o arquivo esteja vazio
if resultado_txt == "":
    resultado = {
    "Ivan Soares": 0,
    "Raphael Gomes": 0,
    "Samantha Alves": 0,
    "Branco": 0,
    "Nulo": 0}

#Descriptograva o arquivo e transforma em dicionário
else:
    chave = "VotacaoUnip2024"
    resultado_crip = criptografia.descriptografar(resultado_txt, chave)
    resultado = eval(resultado_crip)

 #Contabiliza os votos
def contador_votos(voto):
    if voto == 10:
        resultado["Ivan Soares"] += 1
    elif voto == 17:
        resultado["Raphael Gomes"] += 1
    elif voto == 21:
        resultado["Samantha Alves"] += 1
    elif voto == 0:
        resultado["Branco"] += 1
    elif voto == 1:
        resultado["Nulo"] += 1
    return resultado

#Salva e criptografa o resultado.
def salvar_resultado():
    resultados = str(resultado)
    hash_resultados = criptografia.gerar_hash(resultados)
    chave = "VotacaoUnip2024"
    votos_criptografados = criptografia.criptografar(resultados, chave)
    with open("resultados.txt", "w", encoding="utf-8") as arquivo_crip:
        arquivo_crip.write(str(votos_criptografados))
    with open("hash.txt", "w", encoding="utf-8") as arquivo_hash:
        arquivo_hash.write(str(hash_resultados))
    
    
    
