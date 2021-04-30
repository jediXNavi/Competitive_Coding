from data_structures import BinaryTree

tree = BinaryTree('')

def preorder(tree):
    if tree:
        print(tree.get_root())
        preorder(tree.get_left())
        preorder(tree.get_right())