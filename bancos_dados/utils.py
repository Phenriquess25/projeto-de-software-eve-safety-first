import json
import os # para verificar se um arquivo existe (sistema operacional)

def ler_dados(arquivo):
    # Se o arquivo não existir, retorna lista vazia e nem tenta abrir
    if not os.path.exists(arquivo) :
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([], f)
    
    # Abre o arquivo normalmente
    with open(arquivo, "r", encoding="utf-8") as f :
        return json.load(f) # transforme o txt json em uma lista python
    

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        # indent=4 para ser legível, ensure_ascii=False para aceitar acentos
        json.dump(dados, f, indent=4, ensure_ascii=False)
