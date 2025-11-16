from storage import carregar_dados, salvar_dados
from menu import (
    exibir_menu,
    registrar_item_menu,
    listar_itens_menu,
    realizar_pedido_menu,
    adicionar_item_menu,
    aceitar_pedido_menu,
    listar_pedidos_ordenados_menu
)

def main():
    # Carrega dados + árvores AVL
    dados, arvore_itens, raiz_itens, arvore_pedidos, raiz_pedidos = carregar_dados()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            raiz_itens = registrar_item_menu(dados, arvore_itens, raiz_itens)
            salvar_dados(dados)  # salva automaticamente

        elif opcao == "2":
            listar_itens_menu(dados)

        elif opcao == "3":
            raiz_pedidos = realizar_pedido_menu(dados, arvore_pedidos, raiz_pedidos)
            salvar_dados(dados)

        elif opcao == "4":
            adicionar_item_menu(dados)
            salvar_dados(dados)

        elif opcao == "5":
            aceitar_pedido_menu(dados)
            salvar_dados(dados)

        elif opcao == "6":
            listar_pedidos_ordenados_menu(dados)

        elif opcao == "0":
            print("Saindo...")
            salvar_dados(dados)
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
