def math4(num1, num2):
    
    soma = num1 + num2
    dif = num1 - num2
    multi = num1 * num2
    div = num1 / num2

    return f"{num1} + {num2} = {soma}\n{num1} - {num2} = {dif}\n{num1} * {num2} = {multi}\n{num1} / {num2} = {div}"

num_fora1 = int(input("Digite 1 nº inteiro: "))
num_fora2 = int(input("Digite outro nº inteiro: "))

if(num_fora2 != 0):
    print(math4(num_fora1, num_fora2))
else:
    print("Não é possível dividir por zero!")

