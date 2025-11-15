with open("toppasswords.txt", "r") as arquivo:
    valores_do_txt = []

    for item in arquivo:
        valores_do_txt.append(item.strip())
        print(valores_do_txt)