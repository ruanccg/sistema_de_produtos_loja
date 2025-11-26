# ============================================================
#                   SISTEMA DE PRODUTOS
# ============================================================

codigos = [] # Essa lista irá armazenar os códigos dos produtos como inteiro
nomes = []  # Essa lista irá armazenar os nomes dos produtos como string
precos = [] # Essa lista irá armazenar os preços dos produtos como float
quantidades = [] # Essa lista irá armazenar as quantidades dos produtos como inteiro

ARQUIVO = "produtos_com_dados.csv" #Aqui criamos uma variável que irá armazenar o documento externo que contém os produtos em estoque

def carregar_produtos(): #Aqui vamos abrir a função para carregar produtos e salvar dentro do arquivo externo
    try: 
        f = open(ARQUIVO, "r", encoding="utf-8") # Aqui usamos a função open para abrir o arquivo e ler, usamos também o encoding para compreender as acentuações
        for linha in f:
            linha = linha.replace("\n", "")
            if linha == "":
                continue

            partes = linha.split(";")
            if len(partes) != 4:
                continue

            codigos.append(int(partes[0]))
            nomes.append(partes[1])
            precos.append(float(partes[2]))
            quantidades.append(int(partes[3]))

        f.close()
        print(len(codigos), "produto(s) carregado(s).")

    except FileNotFoundError:
        print("Arquivo não encontrado. Sistema iniciará vazio.")


def salvar_produtos():
    f = open(ARQUIVO, "w", encoding="utf-8")
    i = 0
    while i < len(codigos):
        linha = str(codigos[i]) + ";" + nomes[i] + ";" + str(precos[i]) + ";" + str(quantidades[i]) + "\n"
        f.write(linha)
        i = i + 1
    f.close()
    print("Produtos salvos no arquivo.")


# ============================================================
#                    FUNÇÕES DE APOIO
# ============================================================
def ler_inteiro(msg):
    valor = input(msg)
    while valor.isdigit() == False:
        print("Digite um número inteiro válido!")
        valor = input(msg)
    return int(valor)


def ler_float(msg):
    valor = input(msg)
    valido = False

    while valido == False:
        valido = True
        pontos = 0

        for ch in valor:
            if ch == ".":
                pontos = pontos + 1
                if pontos > 1:
                    valido = False
            elif ch.isdigit() == False:
                valido = False

        if valor == "":
            valido = False

        if valido == False:
            print("Digite um número válido (ex: 10 ou 10.50):")
            valor = input(msg)

    return float(valor)


# ============================================================
#                     CRUD DE PRODUTOS
# ============================================================
def cadastrar_produto():
    print("\n=== CADASTRAR PRODUTO ===")

    codigo = ler_inteiro("Código do produto: ")

    if codigo in codigos:
        print("ERRO: já existe produto com esse código!")
        return

    nome = input("Nome do produto: ")
    while nome == "":
        print("Nome não pode ser vazio!")
        nome = input("Nome do produto: ")

    preco = ler_float("Preço: ")

    quantidade = ler_inteiro("Quantidade em estoque: ")

    if quantidade < 0:
        print("ERRO: quantidade não pode ser negativa!")
        return

    codigos.append(codigo)
    nomes.append(nome)
    precos.append(preco)
    quantidades.append(quantidade)

    salvar_produtos()
    print("Produto cadastrado com sucesso!")


def listar_produtos():
    print("\n=== LISTAGEM DE PRODUTOS ===")

    if len(codigos) == 0:
        print("Nenhum produto cadastrado.")
        return

    i = 0
    while i < len(codigos):
        print(
            "Código:", codigos[i],
            "| Nome:", nomes[i],
            "| Preço: R$", round(precos[i], 2),
            "| Quantidade:", quantidades[i]
        )
        i = i + 1


def buscar_produto():
    print("\n=== BUSCAR PRODUTO ===")

    codigo = ler_inteiro("Código do produto: ")

    i = 0
    while i < len(codigos):
        if codigos[i] == codigo:
            print("Encontrado!")
            print("Código:", codigos[i],
                  "| Nome:", nomes[i],
                  "| Preço: R$", round(precos[i], 2),
                  "| Quantidade:", quantidades[i])
            return
        i = i + 1

    print("Produto NÃO encontrado.")


def atualizar_produto():
    print("\n=== ATUALIZAR PRODUTO ===")

    codigo = ler_inteiro("Digite o código do produto: ")

    i = 0
    while i < len(codigos):
        if codigos[i] == codigo:

            print("Produto atual:")
            print("Nome:", nomes[i])
            print("Preço: R$", round(precos[i], 2))
            print("Quantidade:", quantidades[i])

            novo_nome = input("Novo nome (enter mantém): ")
            if novo_nome != "":
                nomes[i] = novo_nome

            novo_preco = input("Novo preço (enter mantém): ")
            if novo_preco != "":
                # validar preço manualmente
                valido = False
                while valido == False:
                    valor = novo_preco
                    valido = True
                    pontos = 0
                    for ch in valor:
                        if ch == ".":
                            pontos = pontos + 1
                            if pontos > 1:
                                valido = False
                        elif ch.isdigit() == False:
                            valido = False
                    if valor == "":
                        valido = False
                    if valido == False:
                        print("Preço inválido!")
                        novo_preco = input("Novo preço (enter mantém): ")
                precos[i] = float(novo_preco)

            nova_qtd = input("Nova quantidade (enter mantém): ")
            if nova_qtd != "":
                while nova_qtd.isdigit() == False:
                    print("Quantidade inválida!")
                    nova_qtd = input("Nova quantidade: ")
                quantidades[i] = int(nova_qtd)

            salvar_produtos()
            print("Produto atualizado com sucesso!")
            return

        i = i + 1

    print("Produto não encontrado.")


def remover_produto():
    print("\n=== REMOVER PRODUTO ===")

    codigo = ler_inteiro("Código do produto a remover: ")

    i = 0
    while i < len(codigos):
        if codigos[i] == codigo:
            del codigos[i]
            del nomes[i]
            del precos[i]
            del quantidades[i]
            salvar_produtos()
            print("Produto removido com sucesso!")
            return
        i = i + 1

    print("Produto não encontrado.")


# ============================================================
#                        RELATÓRIOS
# ============================================================
def relatorio_estoque_baixo():
    print("\n=== RELATÓRIO: ESTOQUE BAIXO ===")

    limite = ler_inteiro("Listar produtos com quantidade <= ")

    caminho = "arquivos_csv_relatorios/relatorio_estoque_baixo.txt"
    f = open(caminho, "w", encoding="utf-8")

    f.write("RELATÓRIO: ESTOQUE BAIXO\n")
    f.write("Quantidade menor ou igual a: " + str(limite) + "\n\n")

    achou = False
    i = 0
    while i < len(codigos):
        if quantidades[i] <= limite:
            linha = (
                "Código: " + str(codigos[i]) +
                " | Nome: " + nomes[i] +
                " | Quantidade: " + str(quantidades[i]) + "\n"
            )
            print(linha, end="")
            f.write(linha)
            achou = True
        i += 1

    if achou == False:
        print("Nenhum produto com estoque baixo.")
        f.write("Nenhum produto com estoque baixo.\n")

    f.close()
    print("\nRelatório salvo em:", caminho)


def relatorio_ordenar_por_preco():
    print("\n=== RELATÓRIO: PRODUTOS ORDENADOS POR PREÇO ===")

    if len(codigos) == 0:
        print("Nenhum produto cadastrado.")
        return

    # bubble sort
    n = len(codigos)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if precos[j + 1] < precos[j]:

                aux = codigos[j]
                codigos[j] = codigos[j + 1]
                codigos[j + 1] = aux

                aux = nomes[j]
                nomes[j] = nomes[j + 1]
                nomes[j + 1] = aux

                aux = precos[j]
                precos[j] = precos[j + 1]
                precos[j + 1] = aux

                aux = quantidades[j]
                quantidades[j] = quantidades[j + 1]
                quantidades[j + 1] = aux

            j += 1
        i += 1

    caminho = "arquivos_csv_relatorios/relatorio_ordenado_preco.txt"
    f = open(caminho, "w", encoding="utf-8")
    f.write("RELATÓRIO: PRODUTOS ORDENADOS POR PREÇO\n\n")

    i = 0
    while i < len(codigos):
        linha = (
            "Código: " + str(codigos[i]) +
            " | Nome: " + nomes[i] +
            " | Preço: R$" + str(round(precos[i], 2)) +
            " | Quantidade: " + str(quantidades[i]) + "\n"
        )
        print(linha, end="")
        f.write(linha)
        i += 1

    f.close()
    print("\nRelatório salvo em:", caminho)


def relatorio_total_itens():
    print("\n=== RELATÓRIO: TOTAL DE ITENS EM ESTOQUE ===")

    total = 0
    i = 0
    while i < len(quantidades):
        total += quantidades[i]
        i += 1

    print("Total de itens no estoque:", total)

    caminho = "arquivos_csv_relatorios/relatorio_total_itens.txt"
    f = open(caminho, "w", encoding="utf-8")
    f.write("RELATÓRIO: TOTAL DE ITENS EM ESTOQUE\n\n")
    f.write("Total de itens: " + str(total) + "\n")
    f.close()

    print("\nRelatório salvo em:", caminho)

# ============================================================
#                      MENU PRINCIPAL
# ============================================================
def menu():
    while True:
        print("\n===== SISTEMA DE LOJA =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar produto")
        print("5 - Remover produto")
        print("6 - Relatório: estoque baixo")
        print("7 - Relatório: ordenar por preço")
        print("8 - Relatório: total de itens em estoque")
        print("0 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            buscar_produto()
        elif opc == "4":
            atualizar_produto()
        elif opc == "5":
            remover_produto()
        elif opc == "6":
            relatorio_estoque_baixo()
        elif opc == "7":
            relatorio_ordenar_por_preco()
        elif opc == "8":
            relatorio_total_itens()
        elif opc == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# ============================================================
#                    PROGRAMA PRINCIPAL
# ============================================================
carregar_produtos()
menu()
