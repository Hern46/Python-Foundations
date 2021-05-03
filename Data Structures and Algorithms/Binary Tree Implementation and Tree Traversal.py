class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.leftchild = None
        self.rightchild = None

    def insert_left(self, node):
        if self.leftchild == None:
            self.leftchild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insert_right(self, node):
        if self.rightchild == None:
            self.rightchild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.rightchild = self.rightchild
            self.rightchild = t

    def get_root_val(self):
        return self.key

    def set_root_val(self, val):
        self.key = val

    def get_left_child(self):
        return self.leftchild

    def get_right_child(self):
        return self.rightchild

tree = BinaryTree('root')

tree.insert_left('left subtree')
tree.insert_right('right subtree')

def preorder_traversal(tree):
    if tree:
        print(tree.get_root_val())
        preorder_traversal(tree.get_left_child())
        preorder_traversal(tree.get_right_child())

preorder_traversal(tree)
print(' ')

def inorder_traversal(tree):
    if tree:
        preorder_traversal(tree.get_left_child())
        print(tree.get_root_val())
        preorder_traversal(tree.get_right_child())

inorder_traversal(tree)
print(' ')

def postorder_traversal(tree):
    if tree:
        preorder_traversal(tree.get_left_child())
        preorder_traversal(tree.get_right_child())
        print(tree.get_root_val())

postorder_traversal(tree)
