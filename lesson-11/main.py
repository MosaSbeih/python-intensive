import random
import cProfile


class Node:

    def __init__(self, value=None) -> None:

        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self) -> None:

        self.root = None

    def insert(self, value):

        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):

        if not current_node.right and current_node.value < value:
            current_node.right = Node(value)
        elif not current_node.left and current_node.value > value:
            current_node.left = Node(value)
        elif current_node.right and current_node.value < value:
            self._insert(current_node.right, value)
        elif current_node.left and current_node.value > value:
            self._insert(current_node.left, value)

    def search(self, target: int) -> bool:

        if self.root.value == target:
            return True
        else:
            return self._search(self.root, target)

    def _search(self, current_node, target):

        if current_node:
            if current_node.right and target == current_node.right.value:
                return True
            elif current_node.left and target == current_node.left.value:
                return True
            elif target > current_node.value:
                return self._search(current_node.right, target)
            elif target < current_node.value:
                return self._search(current_node.left, target)

        return False


if __name__ == "__main__":

    cp = cProfile.Profile()

    # small tree
    small_binary_tree = BinarySearchTree()

    for _ in range(1000):
        small_binary_tree.insert(random.randint(0, 99))

    cp.enable()
    print("Was the target found: ", small_binary_tree.search(23))
    cp.disable()
    cp.print_stats()

    # big tree
    big_binary_tree = BinarySearchTree()

    for _ in range(10000000):
        big_binary_tree.insert(random.randint(0, 99))

    cp.enable()
    print("Was the target found: ", big_binary_tree.search(23))
    cp.disable()
    cp.print_stats()
