class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_values_in_tree(root):
    if root is None:
        return 0
    return root.value + sum_of_values_in_tree(root.left) + sum_of_values_in_tree(root.right)

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

print("Сума всіх значень в дереві:", sum_of_values_in_tree(root))
