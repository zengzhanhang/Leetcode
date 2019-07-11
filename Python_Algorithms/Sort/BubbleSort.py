class SortAlgorithms():
    
    def __init__(self):
        """
        None
        """

    def BubbleSort(self, int_array: int, print_opt=False):
        for _ in range(len(int_array)-1):
            for j in range(len(int_array)-1):
                if int_array[j] > int_array[j+1]:
                    int_array[j], int_array[j+1] = int_array[j+1], int_array[j]
            if print_opt == True:
                print(int_array)
        return int_array

    def SelectionSort(self, int_array: int, print_opt = False):
        idx = len(int_array)-1
        while idx > 0:
            max_idx, max_element = 0, int_array[0]
            for i, num in enumerate(int_array[:idx+1]):
                if num > max_element:
                    max_idx, max_element = i, num
            int_array[idx], int_array[max_idx] = int_array[max_idx], int_array[idx]
            idx -= 1
            if print_opt == True:
                print(int_array)
        return int_array

    def BubbleSort2(self, int_array: int, print_opt = False):
        for i in range(len(int_array)-1):
            for j in range(i, len(int_array)):
                if int_array[i] > int_array[j]:
                    int_array[i], int_array[j] = int_array[j], int_array[i]
            if print_opt == True:
                print(int_array)
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
    sortedOutput = s.BubbleSort(randomInput, print_opt=True)
    print("The sorted output is: {}".format(sortedOutput))