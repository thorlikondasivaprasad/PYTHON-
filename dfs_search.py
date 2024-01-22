def push(stack, val):
    stack.append(val)

def pop(stack):
    if not stack:
        return None
    return stack.pop()

def dfs(graph, start, target):
    stack = []
    visited = []

    push(stack, start)
    visited.append(start)

    while stack:
        current_node = pop(stack)
        if current_node == target:
            return True

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                push(stack, neighbor)
                visited.append(neighbor)

    return False

graph = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f', 'g'],
    'd': [],
    'e': [],
    'f': [],
    'g': []
}

root_node = input("Enter root node: ")
target_node = input("Enter target node: ")

if root_node not in graph or target_node not in graph:
    print("Invalid input. The entered node(s) do not exist in the graph.")
else:
    result = dfs(graph, root_node, target_node)

    if result:
        print(f"Target {target_node} found.")
    else:
        print(f"Target {target_node} not found.")
