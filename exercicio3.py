valor = float(input("Qual foi o valor da compra?"))
quantidade_parcela = int(input("Gostaria de parcelar em quantas vezes?"))

valor_parcelado = valor / quantidade_parcela
print(f"Compra de R$ {valor:.2f} em {quantidade_parcela}x de R${valor_parcelado}")
for parcela in range (1,quantidade_parcela +1):
    print(f"Essa parcela {parcela} vale: {valor_parcelado:.2f}")
