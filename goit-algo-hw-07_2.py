class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_in_tree(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root.value

# Приклад використання:
# Створюємо дерево:
#         10
#       /    \
#      5     15
#     / \      \
#    3   8     20
root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(8)
root.right = TreeNode(15)
root.right.right = TreeNode(20)

print("Мінімальне значення в дереві:", find_min_in_tree(root))
