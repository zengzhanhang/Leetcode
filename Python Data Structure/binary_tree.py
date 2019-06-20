class treeNode():
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, value=None, left=None, right=None):
        """
        treeNode constructure
        """
        self.value = value
        self.left = left
        self.right = right
        self.parent = None # pointer to parent node in tree
    
class binary_search_tree:
    def __init__(self):
        self.root=None

    def insert(self, value):
        if self.root:
            self._insert(value, self.root)
        else:
            self.root = treeNode(value)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = treeNode(value)
                cur_node.left.parent = cur_node
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = treeNode(value)
                cur_node.right.parent = cur_node
            else:
                self._insert(value, cur_node.right)
        else: #value = cur_node.value
            print("Value already in tree!")

    def printTree(self):
        if self.root:
            self._printTree(self.root)
        else:
            print("ERROR: empty tree")
            return None
    
    def _printTree(self, cur_node): # Inorder traversal print tree
        if cur_node:
            self._printTree(cur_node.left)
            print(str(cur_node.value))
            self._printTree(cur_node.right)

    def printTree_preorder(self):
        if self.root:
            self._printTree_preorder(self.root)
        else:
            print("ERROR: empty tree")
            return None

    def _printTree_preorder(self, cur_node):
        if cur_node:
            print(str(cur_node.value))
            self._printTree_preorder(cur_node.left)
            self._printTree_preorder(cur_node.right)

    def printTree_postorder(self):
        if self.root:
            self._printTree_postorder(self.root)
        else:
            print("ERROR: empty tree")
            return None

    def _printTree_postorder(self, cur_node):
        if cur_node:
            self._printTree_postorder(cur_node.left)
            self._printTree_postorder(cur_node.right)
            print(cur_node.value)


    def height(self):
        if self.root:
            return self._height(self.root)
        else:
            return 0

    def _height(self, cur_node, cur_height=0):
        if cur_node == None: 
            return cur_height
        else:
            left_height = self._height(cur_node.left, 1+cur_height)
            right_height = self._height(cur_node.right, 1+cur_height)            
            return max(left_height, right_height)

    def search(self, value):
        if self.root:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right:
            return self._search(value, cur_node.right)
        else:
            return False

    def find(self, value):
        if self.root:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left:
            return self._find(value, cur_node.left)
        elif value > cur_node.value and cur_node.right:
            return self._find(value, cur_node.right)


    def levelOrder(self):
        if self.root:
            return self._levelOrder(self.root)
        else:
            print("ERROR: empty tree")
            return None

    def _levelOrder(self, cur_node):
        queue = list([cur_node])
        node_traversaled = list()
        while len(queue) > 0:
            cur_node = queue.pop(0)
            # print(cur_node.value)
            node_traversaled.append(cur_node.value)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return node_traversaled

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        # Protect against deleting a node not found in the tree
        if node == None or self.find(node.value) == None:
            print("Value to be deleted not found in tree!")
            return None
        
        # return the node with minum value in the tree rooted at input node
        def min_value_node(cur_node):
            current = cur_node
            while current.left:
                current = current.left
            return current

        # return number of children for the spsified node
        def num_children(cur_node):
            total = 0
            if cur_node.left:
                total += 1
            if cur_node.right:
                total += 1
            return total

        # get the parent node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        n_children = num_children(node)

        # break operation into different cases based on the 
        # structure of the tree & node to be deleted

        # CASE 1 (node with no children)
        if n_children == 0:
            
            # Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
            if node_parent != None:
                if node_parent.left  == node:
                    node_parent.left == None
                else:
                    node_parent.right == None
            else:
                self.root == None

        # CASE 2 (node with single child)
        if n_children == 1:

            #get the single child node
            if node.left:
                child = node.left
            else:
                child  = node.right

            # Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
            if node_parent != None:
                # replace the node to be deleted with its child
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

        # CASE 3 (node with two childrend)
        if n_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right)
            
            # copy the inorder successor's value to the node formerly
			# holding the value we wished to delete
            node.value = successor.value

			# delete the inorder successor now that it's value was
			# copied into the other node
            self.delete_node(successor)


def buildTree(tree, num_elements=10, max_int=1000):
    from random import randint
    for _ in range(num_elements):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

if __name__ == "__main__":
    tree = binary_search_tree()
    tree = buildTree(tree)

    print("print tree: ")
    tree.printTree()
    print("\nprint tree in Preoder-manner: ")
    tree.printTree_preorder()

    print("\nprint tree in Postorder-manner: ")
    tree.printTree_postorder()

    print("\nprint tree in level order")
    print(tree.levelOrder())

    print("Tree height is: {}".format(str(tree.height())))
    # print(tree.search(300))
    # print(tree.search(10001))


    # print("=" * 60)
    # tree2 = binary_search_tree()
    # tree2.insert(5)
    # tree2.insert(11)
    # tree2.insert(1)
    # tree2.insert(7)
    # tree2.insert(3)
    # tree2.insert(29)
    # tree2.insert(6)
    # tree2.insert(8)
    # tree2.insert(2)

    # print(tree2.search(29))
    # print(tree2.search(19))
