def get_positive_value(prompt_text):

    value = float(input("Input the value"))

    while value < 0:
        print("please input a positive value: ")
        value = float(input("Input the value: "))

    return value

largura = get_positive_value("qual a largura do retangulo")
altura = get_positive_value("qual a altura do retangulo")

print(largura*altura)








