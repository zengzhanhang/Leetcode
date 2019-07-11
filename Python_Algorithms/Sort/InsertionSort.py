class SortAlgorithms():
    
    def __init__(self):
        """
        None
        """

    def InsertionSort(self, int_array: int):
        for i in range(len(int_array)-1):
            cur_idx = i+1
            while cur_idx > 0 and int_array[cur_idx] < int_array[cur_idx-1]:
                int_array[cur_idx-1], int_array[cur_idx] = int_array[cur_idx], int_array[cur_idx-1]
                cur_idx -= 1
        return int_array

    def _generateRandomArray(self, num_elements, max_value):
        from random import randint
        res = []
        for _ in range(num_elements):
            res.append(randint(num_elements, max_value))
        return res

if __name__ == "__main__":
    s = SortAlgorithms()
    randomInput = s._generateRandomArray(10, 100)
    print("The original input is: {}".format(randomInput))
    sortedOutput = s.InsertionSort(randomInput)
    print("The sorted output is: {}".format(sortedOutput))