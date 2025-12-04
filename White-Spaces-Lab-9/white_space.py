class WhiteSpaces:
    def __init__(self,sentence):
        self.sentence = sentence
    def make_list(self):
        arr = self.sentence.split()
        print(arr)
        return arr
    def repetitions(self,arr):
        counted = set()  # keep track of words already processed
        for i in range(len(arr)):
            if arr[i] not in counted:  # only count if not already done
                same = 0
                for j in range(len(arr)):
                    if arr[i] == arr[j]:
                        same += 1
                print(arr[i], "is repeated", same, "number of times")
                counted.add(arr[i])