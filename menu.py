from pedido import (
    registrar_item,
    realizar_pedido,
    adicionar_item_pedido,
    aceitar_pedido
)
from ordenacao import insertion_sort


def exibir_menu():
    print("\n===== SISTEMA DE RESTAURANTE =====")
    print("1 – Registrar item")
    print("2 – Listar itens")
    print("3 – Realizar pedido")
    print("4 – Adicionar item ao pedido")
    print("5 – Aceitar pedido")
    print("6 – Listar pedidos ordenados")
    print("0 – Sair")
    return input("Escolha: ")


def registrar_item_menu(dados, arvore_itens, raiz_itens):
    try:
        id_item = int(input("ID do item: "))
        nome = input("Nome: ").strip()

        if not nome:
            print("Nome inválido!")
            return raiz_itens

        preco = float(input("Preço: "))

        novo_item = registrar_item(dados, id_item, nome, preco)

        # Inserir na AVL de itens
        raiz_itens = arvore_itens.insert(raiz_itens, novo_item["id"], novo_item)

        print("Item registrado com sucesso!")
        return raiz_itens

    except ValueError:
        print("Erro: entrada inválida!")
        return raiz_itens


def listar_itens_menu(dados):
    print("\n--- ITENS ---")

    if not dados["itens"]:
        print("Nenhum item cadastrado.")
        return

    for item in dados["itens"]:
        print(f"{item['id']} - {item['nome']} - R$ {item['preco']:.2f}")


def realizar_pedido_menu(dados, arvore_pedidos, raiz_pedidos):
    try:
        numero = int(input("Número do pedido: "))
        cliente = input("Nome do cliente: ").strip()

        if not cliente:
            print("Nome inválido!")
            return raiz_pedidos

        novo_pedido = realizar_pedido(dados, numero, cliente)

        # Inserir na AVL de pedidos
        raiz_pedidos = arvore_pedidos.insert(raiz_pedidos, novo_pedido["numero"], novo_pedido)

        print("Pedido criado com sucesso!")
        return raiz_pedidos

    except ValueError:
        print("Erro: entrada inválida!")
        return raiz_pedidos


def adicionar_item_menu(dados):
    try:
        numero = int(input("Número do pedido: "))
        id_item = int(input("ID do item: "))
        quantidade = int(input("Quantidade: "))

        if quantidade <= 0:
            print("Quantidade deve ser maior que zero.")
            return

        adicionar_item_pedido(dados, numero, id_item, quantidade)
        print("Item adicionado ao pedido!")

    except ValueError:
        print("Erro: entrada inválida!")


def aceitar_pedido_menu(dados):
    try:
        num = int(input("Número do pedido: "))
        aceitar_pedido(dados, num)
        print("Pedido aceito!")
    except ValueError:
        print("Erro: entrada inválida!")


def listar_pedidos_ordenados_menu(dados):
    print("\n--- PEDIDOS ORDENADOS POR NÚMERO ---")

    if not dados["pedidos"]:
        print("Nenhum pedido registrado.")
        return

    ordenados = insertion_sort(dados["pedidos"], "numero")

    for p in ordenados:
        print(f"#{p['numero']} - Cliente: {p['cliente']} - Itens: {len(p['itens'])}")
