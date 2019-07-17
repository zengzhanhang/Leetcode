class SortAlgorithms():
    def __init__(self):
        pass

    def bubbleSort(self, int_array: int) -> int:
        for _ in range(len(int_array)):
            for j in range(len(int_array)-1):
                if int_array[j] > int_array[j+1]:
                    int_array[j], int_array[j+1] = int_array[j+1], int_array[j]
        return int_array

    def insertionSort(self, int_array: int) -> int:
        right = len(int_array)-1
        while right > 0:
            max_value = 0
            for i in range(right+1):
                if int_array[i] > max_value:
                    max_idx = i
                    max_value = int_array[i]
            int_array[max_idx], int_array[right] = int_array[right], int_array[max_idx]
            right -= 1
        return int_array

    def mergeSort(self, int_array: int) -> int:
        
        def _merge(left, right):
            res = []
            while left and right:
                if left[0] < right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
            while left:
                res.append(left.pop(0))
            while right:
                res.append(right.pop(0))
            return res
        
        if len(int_array) < 2:
            return int_array
        
        mid = int(len(int_array)/2)
        left = int_array[:mid]
        right = int_array[mid:]
        return _merge(self.mergeSort(left), self.mergeSort(right))

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

    def _generateRandomArray(self, num_elements: int, max_values: int) -> int:
        from random import randint
        
        res = []
        for _ in range(num_elements):
            res.append(randint(0, max_values))
        return res


if __name__ == "__main__":
    sa = SortAlgorithms()

    randomInput = sa._generateRandomArray(10, 100)
    print("The original random input is: {}".format(randomInput))
    
    # bubbleOutput = sa.bubbleSort(randomInput)
    # print("The bubble sorted output is: {}".format(bubbleOutput))
    
    # insertionOutput = sa.insertionSort(randomInput)
    # print("The insertion sorted output is: {}".format(insertionOutput))
    
    # mergeOutput = sa.mergeSort(randomInput)
    # print("The merge sorted output is: {}".format(mergeOutput))

    # randomInput = [5,1,1,2,0,0]
    quickOutput = sa.quickSort(randomInput)
    print("The quick sorted output is: {}".format(quickOutput))