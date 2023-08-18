def main():
    n = int(input())
    total = 0

    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

    cupom = input()  # Lê o cupom de desconto

    if cupom == "10%":
        total_com_desconto = total * 0.9
    elif cupom == "20%":
        total_com_desconto = total * 0.8
    else:
        total_com_desconto = total

    print(f"Valor total: {total_com_desconto:.2f}")


if __name__ == "__main__":
    main()
