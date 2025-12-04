from white_space import WhiteSpaces

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    ws = WhiteSpaces(sentence)
    words = ws.make_list()
    ws.repetitions(words)
