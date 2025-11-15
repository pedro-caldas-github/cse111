def main():
    """	Provides the user input loop. The loop asks the user for a password to test. 
    If that password is anything but "q" or "Q" call the password_strength function 
    and report the results to the user. If the user enters "q" or "Q", quit the program.
    """

    a = input("type your password: ")

    while a != "q" or "Q":
        print(f"This is your password: {a} ")
        a = input("type your password: ")


    pass
def word_in_file(word, filename, case_sensitive):

    """This function reads a file (specified by the filename parameter) in which each line of the file 
    contains a single word. If the word passed in the word parameter matches a word in 
    the file the function returns a true otherwise it returns a false. If the parameter 
    case_sensitive is true a case sensitive match is performed. If case_sensitive is false a 
    case insensitive match is performed. The case_sensitive parameter should default to False"""

    with open("toppasswords.txt", "r") as arquivo:
        valores_do_txt = []

        for item in arquivo:
            valores_do_txt.append(item.strip())
            print(valores_do_txt)


    pass
def word_has_character(word, character_list):
    pass
def word_complexity(word):
    pass
def password_strength(password, min_length, strong_length):
    pass

if __name__ == "__main__":
    main()

# open(filename, "r",encoding="utf-8")

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]