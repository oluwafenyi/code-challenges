
# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python


class Node:
    next = None


def loop_size(node):
    nodes = {}
    while True:
        nodes.setdefault(node, 0)
        nodes[node] += 1
        if nodes[node] == 2:
            loop_start = node
            break
        node = node.next

    count = 1
    next_node = loop_start.next
    while next_node != loop_start:
        count += 1
        next_node = next_node.next
    return count


node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

assert loop_size(node1) == 3
