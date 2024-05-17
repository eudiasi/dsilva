valor_compra = float (input("digite o valor da compra"))
if valor_compra >=100:
    desconto = valor_compra * 0.1
    valor_final = valor_compra - desconto
    print("parabéns voçe ganhou um desconto de 10%")
    print("valor final da compra: R$", valor_final)
else:
    print("Infelizmente, voce nao ganhou desconto")
    print("valor final da compra: R$" , valor_compra)