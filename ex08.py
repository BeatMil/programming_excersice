class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


def bst_numbers_sum(root, num=0):
    numbers = [] # store numbers in string
    history = []
    # been_to = []
    pointer = None # location of where we are
    check_right = False
    while True: # check left most side
        if root.left and pointer == None: # first time
            numbers.append(root.value)
            history.append(root)
            pointer = root.left

        if pointer.left and history.count(pointer.left) == 0:
            # check left side
            # and if already gone there then do else
            numbers.append(pointer.value)
            history.append(pointer)
            pointer = pointer.left
        # elif pointer.left and history.count(pointer.left) >= 0:
        elif pointer.right and history.count(pointer.right) == 0:
            # check right side
            # and if already gone there then do else
            pointer = pointer.right
            numbers.append(pointer.value)
            history.append(pointer)
        else:
            numbers.append(pointer.value)
            history.append(pointer)
            print("Time to go back up")
            pointer = history[-2]
    # print for debug purpose
    print("Pointer: %s" % pointer)
    print("History: %s" % history)
    print("LEN History: %s" % len(history))
    # print("Been_to: %s" % been_to)
    print("Numbers: %s" % numbers)
    for i in numbers:
        print(str(i),end="")

# n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  / \
# 4   5
#/
#6

bst_numbers_sum(n1)
# 262
# Explanation: 124 + 125 + 13 = 262
