class SortAlgorithms():
    
    def __init__(self):
        """
        None
        """

    def MergeSort(self, int_array: int):
        length = len(int_array)
        if length < 2:
            return int_array
        
        mid = int(len(int_array)/2)
        left = int_array[:mid]
        right = int_array[mid:]
        return self._merge(self.MergeSort(left), self.MergeSort(right))
        
    def _merge(self, left, right):
        res = []
        while len(left)>0 and len(right)>0:
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        
        while left:
            res.append(left.pop(0))
        while right:
            res.append(right.pop(0))

        return res


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
    sortedOutput = s.MergeSort(randomInput)
    print("The sorted output is: {}".format(sortedOutput))