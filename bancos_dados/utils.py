import json
import os # para verificar se um arquivo existe (sistema operacional)

def ler_dados(arquivo):
    # Verifica se o arquivo existe dentro da pasta bancos_dados
    caminho = os.path.join("bancos_dados", arquivo)

    # Se o arquivo não existir, retorna lista vazia e nem tenta abrir
    if not os.path.exists(caminho) :
        return [] 
    
    # Abre o arquivo normalmente
    with open(arquivo, "r", encoding="utf-8") as f :
        return json.load(f) # transforme o txt json em uma lista python
    

def salvar_dados(arquivo, dados):
    caminho = os.path.join("bancos_dados", arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        # indent=4 para ser legível, ensure_ascii=False para aceitar acentos
        json.dump(dados, f, indent=4, ensure_ascii=False)