class Min_Max:
    def __init__(self, arr):
        if not isinstance(arr, list):
            raise TypeError("arr must be a list")
        if not all(isinstance(x, (int, float)) for x in arr):
            raise ValueError("All elements in arr must be numbers")
        self.arr = arr
    def min_max(self):
        max_number = self.arr[0]
        min_number = self.arr[0]
        for i in range(len(self.arr)):
            if (self.arr[i]<min_number):
                min_number = self.arr[i]
            elif (self.arr[i]>max_number):
                max_number = self.arr[i]
        return [min_number,max_number]