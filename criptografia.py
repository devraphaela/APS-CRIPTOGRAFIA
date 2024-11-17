import hashlib

# Função de hash
def gerar_hash(chave):
    return hashlib.sha256(chave.encode()).hexdigest()

# Criptografia
def criptografar(texto, chave):
    resultado = ''.join(chr((ord(char) + len(chave)) % 256) for char in texto)
    return resultado

# Descriptografia
def descriptografar(texto_criptografado, chave):
    resultado = ''.join(chr((ord(char) - len(chave)) % 256) for char in texto_criptografado)
    return resultado

#Valida o documento
def validar_hash():
    with open("resultados.txt", "r", encoding="utf-8") as arquivo:
        resultado_criptografado = arquivo.read()
        chave = "VotacaoUnip2024"
        dados_desencriptados = descriptografar(resultado_criptografado, chave)
        hash_resultado = gerar_hash(dados_desencriptados)
    with open("hash.txt", "r", encoding="utf-8") as arquivo_hash:
        hash_original = str(arquivo_hash.read().strip())
    return hash_original == hash_resultado

