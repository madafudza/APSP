def dijkstra_basic(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        # Находим вершину с минимальным расстоянием
        min_dist = float('inf')
        min_index = -1
        for v in range(n):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_index = v

        visited[min_index] = True

        # Обновляем расстояния до соседей
        for neighbor, weight in graph[min_index]:
            if not visited[neighbor] and dist[min_index] + weight < dist[neighbor]:
                dist[neighbor] = dist[min_index] + weight

    return dist
