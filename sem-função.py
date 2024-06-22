from time import sleep
estoque = [
    { "produto": "Lapis", "quantidade": 2, "valor": 0.50 },
]

print("""
[ 1 ] Realizar Venda
[ 2 ] Adicionar Produto
[ 3 ] Atualizar Produto
[ 4 ] Estoque
[ 0 ] Sair
""")

while True:
    escolha = input("Escolha a opção: ")
    if escolha == '2':
        produto = input("Inserir produto: ")
        quantidade = int(input("Qtd: "))
        preco = float(input("Valor R$: "))

        # Verificação e confirmação
        print(f"\nConfirme as informações:")
        print(f"Produto: {produto}")
        print(f"Quantidade: {quantidade}")
        print(f"Valor: {preco:.2f}R$")
        confirmacao = input("As informações estão corretas? (s/n): ").lower()
        print("Adicionando produto.....")
        sleep(2)

        if confirmacao == "s":
            if quantidade > 0 and preco > 0:
                estoque.append({"produto": produto, "quantidade": quantidade, "valor": preco})
                print("Adicionado com sucesso!")
            else:
                print("ERRO: quantidade ou preço inválido!")
        else:
            print("Operação cancelada.")
    
    elif escolha == '3':
        # Atualizar produto
        produto = input("Nome do produto (ou 'voltar' para cancelar): ")
        if produto.lower() == 'voltar':
            continue
        quantidade = int(input("Qtd: "))
        preco = float(input("Preço: "))

        # Verificação e confirmação
        print(f"\nConfirme as informações:")
        print(f"Produto: {produto}")
        print(f"Quantidade: {quantidade}")
        print(f"Valor: {preco:.2f}R$")
        confirmacao = input("As informações estão corretas? (s/n): ").lower()
        print("Atualizando....")
        sleep(2)

        if confirmacao == "s":
            if quantidade > 0 and preco > 0:
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
    
    elif escolha == '4':
        # Exibir estoque
        print("\nEstoque atual:")
        for item in estoque:
            print(f"Produto: {item['produto']}, Quantidade: {item['quantidade']}, Valor: {item['valor']:.2f}R$")
    
    elif escolha == '0':
        print("Saindo do sistema")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
