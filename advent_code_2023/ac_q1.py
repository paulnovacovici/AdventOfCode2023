new_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.is_complete = False

    def add_child(self, child_node):
        """Add a child node to this node"""
        self.children.append(child_node)

    def find_child(self, value):
        for child in self.children:
            if value == child.value:
                return child
        return None

    def prefix_complete(self, cand):
        cur = self
        for i, c in enumerate(cand):
            if cur.is_complete:
                return cand[:i]
            cur = cur.find_child(c)
            if cur is None:
                return None

    def __repr__(self):
        return f"TreeNode({self.value})"

    def __str__(self, level=0):
        """String representation to visualize the tree"""
        ret = "\t" * level + repr(self) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


def create_tree(values):
    sentinel = TreeNode(None)

    for value in values:
        cur = sentinel
        for c in value:
            child_node = cur.find_child(c)
            if child_node is None:
                child_node = TreeNode(c)
                cur.add_child(child_node)
            cur = child_node
        cur.is_complete = True

    return sentinel


def number(value):
    for i, num in enumerate(new_nums):
        if num == value:
            return i + 1


def process_line(tree, line):
    a = []
    for i, c in enumerate(line):
        if c >= "0" and c <= "9":
            a.append(c)
        num = tree.prefix_complete(line[i:])
        if num:
            a.append(str(number(num)))

    return int(a[0] + a[-1])


def process_file():
    tree = create_tree(new_nums)
    with open("ac_q1.txt", "r") as file:
        acc = 0
        for line in file:
            # Process each line here
            print(line)
            print(process_line(tree, line))
            acc += process_line(tree, line)
        print(acc)


# print(node.prefix_complete("six"))
process_file()
