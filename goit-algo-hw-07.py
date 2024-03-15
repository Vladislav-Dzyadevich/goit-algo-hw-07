class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_in_tree(root):
    if root is None:
        return None
    while root.right is not None:
        root = root.right
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

print("Максимальне значення в дереві:", find_max_in_tree(root))
