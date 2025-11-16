from storage import salvar_dados

def registrar_item(dados, id_item, nome, preco):
    item = {
        "id": id_item,
        "nome": nome,
        "preco": preco
    }
    dados["itens"].append(item)
    salvar_dados(dados)
    return item


def realizar_pedido(dados, numero, cliente):
    pedido = {
        "numero": numero,
        "cliente": cliente,
        "itens": [],
        "status": "pendente"
    }
    dados["pedidos"].append(pedido)
    salvar_dados(dados)
    return pedido


def adicionar_item_pedido(dados, numero, id_item, quantidade):
    # Busca o pedido
    for pedido in dados["pedidos"]:
        if pedido["numero"] == numero:
            pedido["itens"].append({
                "id_item": id_item,
                "quantidade": quantidade
            })
            salvar_dados(dados)
            return True  # Sucesso

    return False  # Pedido não encontrado


def aceitar_pedido(dados, numero):
    # Procura o pedido e atualiza o status
    for pedido in dados["pedidos"]:
        if pedido["numero"] == numero:
            pedido["status"] = "aceito"
            salvar_dados(dados)
            return True  # Sucesso

    return False  # Pedido não encontrado
