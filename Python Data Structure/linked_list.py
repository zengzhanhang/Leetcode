class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        new_node = Node(value)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        self.length += 1

    # def length(self):
    #     cur_node = self.head
    #     total = 0
    #     while cur_node.next != None:
    #         total += 1
    #         cur_node = cur_node.next
    #     return total

    def display(self):
        lst = []
        cur_node = self.head
        while cur_node != None:
            lst.append(cur_node.value)
            cur_node = cur_node.next
        print(lst)

    def get(self, idx):
        if idx >= self.length:
            print("ERROR: 'get' index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while cur_idx < idx:
            cur_node = cur_node.next
            cur_idx += 1
        return cur_node.value

    def remove(self, idx):
        if idx >= self.length:
            print("ERROR: 'get' index out of range")
            return
        cur_idx = 0
        cur_node = self.head
        while cur_idx < idx:
            last_note = cur_node
            cur_node = cur_node.next
            cur_idx += 1
        last_note.next = cur_node.next

def main():
    my_list = linked_list()

    my_list.display()

    my_list.append(2)
    my_list.append(19)
    my_list.append(10)
    my_list.append(3)
    my_list.append(5)
    my_list.append(7)

    print(my_list.length)
    my_list.display()

    print(my_list.get(3))
    my_list.remove(2)
    my_list.display()

    
if __name__ == "__main__":
    main()