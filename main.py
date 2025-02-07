from collections import deque
print("#################################################################")
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def display(self):
        return self.queue


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print("Remaining elements in the queue:", q.display())
print("Front element:", q.front())
q.dequeue()
q.dequeue()

print("Remaining elements in the queue:", q.display())

print("#################################################################")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)



class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def level_order_traversal(root):

    if not root:
        return

    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            for child in node.children:
                queue.append(child)

        print(current_level)


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node5 = TreeNode(5)
node6 = TreeNode(6)


node5.add_child(TreeNode(7))
node5.add_child(TreeNode(8))
root.add_child(node2)
root.add_child(node3)
root.add_child(node6)
node2.add_child(node5)
node3.add_child(node6)

print("Level order traversal:")
level_order_traversal(root)

print("#################################################################")


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):

        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs_search(self, start, target):
        if start not in self.graph:
            print("Start node not in graph")
            return

        visited = set()

        queue = deque([(start, 0)])
        visited.add(start)

        while queue:
            current, steps = queue.popleft()

            if current == target:
                print("Node found")
                print(f"Steps taken: {steps}")
                return

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))

        print("Node not found")

    def bfs_level_print(self, start):
        if start not in self.graph:
            print("Start node not in graph")
            return

        visited = set()
        current_level = deque([start])
        visited.add(start)
        level = 0

        while current_level:
            print(f"Level {level}:", end=" ")
            next_level = deque()


            for node in current_level:
                print(node, end=" ")

                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_level.append(neighbor)

            print()
            current_level = next_level
            level += 1



g = Graph()

edges = [
    (0, 1), (0, 2), (0, 3),
    (1, 4), (1, 5),
    (2, 6), (2, 7),
    (3, 8), (3, 9),
    (4, 10), (4, 11),
    (5, 12), (5, 13),
    (6, 14), (6, 15),
    (7, 16), (7, 17),
    (8, 18), (8, 19),
    (9, 20), (9, 21)
]

for edge in edges:
    g.add_edge(edge[0], edge[1])

print("BFS Search Test:")
source = 0
destination = 15
g.bfs_search(source, destination)


print("Level-by-level BFS traversal:")
g.bfs_level_print(source)