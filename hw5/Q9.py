V = 5
INF = 99999

graph= [[0, 4, 2, 5, INF], \
       [INF, 0, 1, INF, 4], \
       [1, 3, 0, 1, 2], \
       [-2, INF, INF, 0, 2], \
       [INF, -3, 3, 1, 0]]

def FloydWarshall():
    dist = [[None for y in range(V)] for x in range(V)]
    omitElement = [0, INF]

    for i in range(5):
        for j in range(5):
            if graph[i][j] not in omitElement:
                dist[i][j]=j

    for k in range(V):
        for i in range(V):
            for j in range(V):
                # get the min value of the distance
                if (graph[i][k] + graph[k][j]) < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    dist[i][j] = dist[i][k]

    # print(graph)
    # print(dist)
    return graph, dist

def main():
    graph, dist = FloydWarshall()
    print("Output")
    for i in range(V):
        for j in range(V):
            if i == j:
                print("({0},{1}) : distance = {2}, path = {0} -> {1}".format(i+1, j+1, graph[i][j]))
            else:
                path = [i]
                while path[-1] != j:
                    path.append(dist[path[-1]][j])
                print("({0},{1}) : distance = {2}, path = {3}".format(i+1, j+1, graph[i][j], ' -> '.join(str(p + 1) for p in path)))

if __name__ == '__main__':
    main()

