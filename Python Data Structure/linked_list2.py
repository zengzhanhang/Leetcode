# class Node:
#     def __init__(self, value=):
#         self.value = value
#         self.node = None

class linked_list:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def append(self, value):
        new_node = linked_list(value)
        if self.next != None:
            cur_node = self.next
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_node
        else:
            self.next = new_node

    def length(self):
        total = 0
        if self.next:
            cur_node = self.next
            total += 1
            while cur_node.next != None:
                cur_node = cur_node.next
                total += 1
        return total


    def display(self):
        lst = []
        if self.next != None:
            cur_node = self.next
            lst.append(cur_node.value)
            while cur_node.next != None:
                cur_node = cur_node.next
                lst.append(cur_node.value)
        print(lst)

    # def get(self, inx):
    #     if self.next != None:
    #         cur_node = 
    #     cur_inx = 0



def main():
    my_list = linked_list()

    my_list.display()

    my_list.append(2)
    my_list.append(19)
    my_list.append(10)

    print(my_list.length())
    my_list.display()

if __name__ == "__main__":
    main()