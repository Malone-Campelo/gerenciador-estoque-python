import os
from time import sleep

estoque = [
    { "produto": "Cuscuz", "quantidade": 2, "valor": 0.99 },
    { "produto": "Arroz", "quantidade": 2, "valor": 25.00 },
    { "produto": "Açucar", "quantidade": 5, "valor": 3.99 }
]

vendas = []

def mostrar_menu():
    print("""
[ 1 ] Realizar Venda
[ 2 ] Adicionar Produto
[ 3 ] Atualizar Produto
[ 4 ] Estoque
[ 5 ] Mostrar Lucro do Dia
[ 0 ] Sair
""")

def realizar_venda():
    while True:
        produto = input("Nome do produto (ou 'Voltar' para encerrar): ")
        if produto.lower() == "voltar":
            break
        quantidade = int(input("Qtd: "))
        produto_encontrado = False
        for item in estoque:
            if item["produto"].strip().lower() == produto:
                if item["quantidade"] >= quantidade:
                    item["quantidade"] -= quantidade
                    total_venda = quantidade * item['valor']
                    vendas.append(total_venda)
                    print(f"Venda realizada: {produto} x {quantidade} = {total_venda:.2f}R$")
                    produto_encontrado = True
                else:
                    print("Quantidade em estoque insuficiente.")
                break
        if not produto_encontrado:
            print("Produto não encontrado no estoque.")
        sleep(2)

def adicionar_produtos():
    while True:
        produto = input("Inserir produto (ou 'voltar' para encerrar): ")
        if produto.lower() == "voltar":
            break
        quantidade = int(input("Qtd: "))
        preco = float(input("Valor R$: "))
        print("--" * 30)
        print(f"Produto: {produto}")
        print(f"Quantidade: {quantidade}")
        print(f"Valor: {preco:.2f}R$")
        confirmacao = input("As informações estão corretas? (s/n): ").lower()
        print("Aguarde...")
        sleep(2)
        if confirmacao == "s":
            if quantidade > 0 and preco > 0:
                estoque.append({"produto": produto, "quantidade": quantidade, "valor": preco})
                print("Produto adicionado com sucesso!")
            else:
                print("ERRO: quantidade ou preço inválido!")
        else:
            print("Operação cancelada.")
        sleep(2)

def atualizar_produto():
    produto = input("Nome do produto (ou 'voltar' para cancelar): ")
    if produto.lower() == 'voltar':
        return
    quantidade = int(input("Qtd: "))
    preco = float(input("Preço: "))
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor: {preco:.2f}R$")
    confirmacao = input("As informações estão corretas? (s/n): ").lower()
    print("Atualizando....")
    sleep(2)
    if confirmacao == "s":
        if quantidade >= 0 and preco >= 0:
            produto_encontrado = False
            for item in estoque:
                if item['produto'].lower() == produto.lower():
                    item['quantidade'] = quantidade
                    item['valor'] = preco
                    produto_encontrado = True
                    print("Atualizado com sucesso!")
                    break
            if not produto_encontrado:
                print("Produto não encontrado no estoque.")
        else:
            print("ERRO, quantidade ou valor incorreto.")
    else:
        print("Operação cancelada.")
    sleep(2)

def exibir_estoque():
    print("\nEstoque atual:")
    for item in estoque:
        print(f"Produto: {item['produto']} | Quantidade: {item['quantidade']} | Valor: {item['valor']:.2f} R$")
    input("\nPressione Enter para voltar ao menu...")

def mostrar_lucro():
    total_lucro = sum(vendas)
    print(f"\nLucro total do dia: {total_lucro:.2f}R$")
    input("\nPressione Enter para voltar ao menu...")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    mostrar_menu()
    escolha = input("Escolha a opção: ")
    if escolha == '1':
        realizar_venda()
    elif escolha == '2':
        adicionar_produtos()
    elif escolha == '3':
        atualizar_produto()
    elif escolha == '4':
        exibir_estoque()
    elif escolha == '5':
        mostrar_lucro()
    elif escolha == '0':
        print("Saindo do sistema...")
        sleep(1)
        break
    else:
        print("Opção inválida. Tente novamente.")
        sleep(2)