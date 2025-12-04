class List_Of_Words:
    def __init__(self, words):
        if not isinstance(words, list):
            raise TypeError("words must be a list of strings")
        self.words = words

    def repetitions(self):
        lowercase_words = [word.lower() for word in self.words]
        print(f"The list of words in lowercase is: {lowercase_words}")

        counted = []  # list to keep track of already counted words

        for i in range(len(lowercase_words)):
            find = lowercase_words[i]
            if find in counted:  # This will skip if we already counted this word
                continue
            count = 0
            for y in range(len(lowercase_words)):
                if find == lowercase_words[y]:
                    count += 1
            print(f"'{find}' is repeated {count} times")
            counted.append(find) 
