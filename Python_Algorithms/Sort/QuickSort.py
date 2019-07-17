class SortAlgorithms():
    
    def __init__(self):
        """
        None
        """

    def quickSort(self, int_array: int) -> int:
        if len(int_array) < 2:
            return int_array
        
        mid = int(len(int_array)/2)
        pivot = int_array[mid]
        left, right, p = [], [], []
        while int_array:
            if int_array[-1] < pivot:
                left.append(int_array.pop())
            elif int_array[-1] > pivot:
                right.append(int_array.pop())
            else:
                p.append(int_array.pop())
        return self.quickSort(left) + p + self.quickSort(right)

    def _generateRandomArray(self, num_elements, max_value):
        from random import randint
        res = []
        for _ in range(num_elements):
            res.append(randint(0, max_value))
        return res


if __name__ == "__main__":
    s = SortAlgorithms()
    randomInput = s._generateRandomArray(10, 100)
    print("The original input is: {}".format(randomInput))
    sortedOutput = s.quickSort(randomInput)
    print("The sorted output is: {}".format(sortedOutput))