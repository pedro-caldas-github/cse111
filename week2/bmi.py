def bmi():

    altura = float(input("digite a altura: "))
    peso = float(input("digite o peso: "))

    imc = peso/(altura ** 2)

    return imc

resultado = bmi()

print(f"O seu IMC é: {resultado}")