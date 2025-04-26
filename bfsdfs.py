from collections import deque

def bfs(adj_matrix, start, goal):
    n = len(adj_matrix)
    visited = []

    queue = deque([start])
    visited.append(start)
    bfs_order = []

    while queue:
        node = queue.popleft()
        bfs_order.append(node)

        print(f"Current node: {node}")
        print(f"Open list: {list(queue)}")
        print(f"Closed list: {visited}\n")

        if node == goal:
            return bfs_order

        for neighbor, is_connected in enumerate(adj_matrix[node]):
            if is_connected and neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

    return bfs_order

def dfs(adj_matrix, start, goal, visited=None, dfs_order=None):
    if visited is None:
        visited = []
        dfs_order = []

    visited.append(start)
    dfs_order.append(start)

    print(f"Current node: {start}")
    print(f"Open list: {dfs_order}")
    print(f"Closed list: {visited}\n")

    if start == goal:
        return dfs_order

    for neighbor, is_connected in enumerate(adj_matrix[start]):
        if is_connected and neighbor not in visited:
            result = dfs(adj_matrix, neighbor, goal, visited, dfs_order)
            if result is not None:
                return result

    dfs_order.pop()
    return None

def input_adj_matrix():
    n = int(input("Enter the number of nodes: "))
    adj_matrix = []
    print("Enter the adjacency matrix row by row:")
    for i in range(n):
        row = list(map(int, input().split()))
        adj_matrix.append(row)
    return adj_matrix

# Main Execution
adj_matrix = input_adj_matrix()
start_node = int(input("Enter the start node: "))
goal_node = int(input("Enter the goal node: "))

print("\nBFS Traversal:", bfs(adj_matrix, start_node, goal_node))
print("-----------------------------------\n")
print("DFS Traversal:", dfs(adj_matrix, start_node, goal_node))
