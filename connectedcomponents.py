def dfs(graph, start, visited, component):
    visited.add(start)
    component.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited, component)

def connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)

    return components

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C'],
    'H': ['I'],
    'I': ['H']
}

print(connected_components(graph))


