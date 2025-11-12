# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Serialize: Tree -> String
    def serialize(self, root):
        def dfs(node):
            if not node:
                vals.append("N")  # 'N' represents null
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        vals = []
        dfs(root)
        return ",".join(vals)

    # Deserialize: String -> Tree
    def deserialize(self, data):
        vals = data.split(",")
        self.index = 0

        def dfs():
            if vals[self.index] == "N":
                self.index += 1
                return None
            node = TreeNode(int(vals[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Helper function to print tree in level order
from collections import deque
def print_level_order(root):
    if not root:
        print("Empty tree")
        return
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("N")
    print("Level Order:", " -> ".join(result))


# ---- Main program ----
if __name__ == "__main__":
    codec = Codec()

    # Create example binary tree:
    #        1
    #       / \
    #      2   3
    #         / \
    #        4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Serialize the tree
    serialized = codec.serialize(root)
    print("\nSerialized Tree String:")
    print(serialized)

    # Deserialize the string back to tree
    deserialized = codec.deserialize(serialized)
    print("\nDeserialized Tree (Level Order):")
    print_level_order(deserialized)
