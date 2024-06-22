# Lista
estoque = [
    { "produto": "Lapis", "quantidade": 1, "valor": 0.50 },
]
# Função para adicionar, nome produto, quantidade e valor
def adicionar_produto(estoque):
    produto = input("Inserir produto: ")
    quantidade = int(input("Qtd: "))
    preco = float(input("Valor R$: "))
    
    # Verificação e confirmação
    print(f"\nConfirme as informações:")
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor: R${preco:.2f}")
    confirmacao = input("As informações estão corretas: s/n:  ").lower()
   
    if confirmacao == "s":
        if quantidade > 0 and preco > 0:
            estoque.append({"produto": produto, "quantidade": quantidade, "valor": preco})
            print("Adicionado com sucesso!")
        else:
            print("ERRO: quantidade inválida! ")
    else:
        print("Operação cancelada.")
        
            
def atualizar_estoque(estoque):
    produto = input("Qual produto deseja ajustar: ").strip().lower
    produto_encontrado = False
    for item in estoque:
        if item["produto"].lower() == produto:
            produto_encontrado = True
            quantidade = int(input("Nova Qtd: "))
            preco = float(input("Preço atualizado: "))
            
     # Verificar e confirmar
    print(f"\nConfirme as informações:")
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor: R${preco:.2f}")
    
    confirmacao = input("As informações estão corretas? (s/n):  ").lower()
    if confirmacao == "s":
        if quantidade >= 0 and preco >= 0:
            item["quantidade"] = quantidade
            item["preço"] = preco
            print("Produto atualizado com sucesso!")
        else:
            print("ERRO, Valor inválido.")
    else:
        print("Operação cancelada!")
        return
print("Produto não encontrado.")

def visualizar_estoque(estoque):
    print("\nEstoque:")
    for item in estoque:
        print(f"produto: {item['produto']} | quantidade: {item['quantidade']} | valor: {item['valor']:.2f}")
    print()

print("{:-^30}".format("Controle de estoque"))
print("""
[ 1 ] Adicionar Produto
[ 2 ] Atualizar Produto
[ 3 ] Estoque
[ 4 ] Sair
""")

while True:
    escolha = (input("Selecione o numero: "))
    
    if escolha == '1':
        adicionar_produto(estoque)
    elif escolha == '2':
        atualizar_estoque(estoque)
    elif escolha == '3':
        visualizar_estoque(estoque)
    elif escolha == '4':
        print("Saindo dos sistema")
        break
    else:
        print("Opção inválida. Tente novamente.")
    