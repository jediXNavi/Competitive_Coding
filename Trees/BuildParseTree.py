from data_structures import Stack, BinaryTree


def parseTree(expression):
    tokens = expression.split()
    tree_holder = Stack()
    main_tree = BinaryTree('')
    tree_holder.push(main_tree)
    currentTree = main_tree
    for val in tokens:
        if val == '(':
            currentTree.add_left('')
            tree_holder.push(currentTree)
            currentTree = currentTree.get_left()

        elif val not in '+-*/':
            currentTree.set_root_val(val)
            parent = tree_holder.pop()
            currentTree = parent

        elif val in '+-*/':
            currentTree.set_root_val(val)
            currentTree.add_right('')
            tree_holder.push(currentTree)
            currentTree = currentTree.get_right()

        elif val == ')':
            currentTree = tree_holder.pop()
        else:
            raise ValueError

    return main_tree








