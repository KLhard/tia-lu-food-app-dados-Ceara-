import json
from avl import AVLTree

ARQUIVO = "dados.json"


def carregar_dados():
    # Carrega o arquivo JSON ou cria estrutura vazia
    try:
        with open(ARQUIVO, "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = {
            "itens": [],
            "pedidos": []
        }

    # === Carregar itens na AVL ===
    arvore_itens = AVLTree()
    raiz_itens = None

    for item in dados["itens"]:
        raiz_itens = arvore_itens.insert(raiz_itens, item["id"], item)

    # === Carregar pedidos na AVL ===
    arvore_pedidos = AVLTree()
    raiz_pedidos = None

    for pedido in dados["pedidos"]:
        raiz_pedidos = arvore_pedidos.insert(raiz_pedidos, pedido["numero"], pedido)

    return dados, arvore_itens, raiz_itens, arvore_pedidos, raiz_pedidos


def salvar_dados(dados):
    # Salva os dados no arquivo JSON
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
