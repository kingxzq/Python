import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
#防止字体警告
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 将边列表转换为有向或无向图的邻接矩阵
def edge_list_to_adj_matrix(edge_list, directed=True):
    num_nodes = max(max(x[:2]) for x in edge_list) + 1
    adj_matrix = np.zeros((num_nodes, num_nodes))

    for edge in edge_list:
        start, end, weight = edge[:3]
        adj_matrix[start][end] = weight
        if not directed:
            adj_matrix[end][start] = weight

    return adj_matrix


# 将有向或无向图的邻接矩阵转换为边列表
def adj_matrix_to_edge_list(adj_matrix):
    edge_list = []
    num_nodes = len(adj_matrix)

    for i in range(num_nodes):
        for j in range(num_nodes):
            if adj_matrix[i][j] != 0:
                edge_list.append([i, j, adj_matrix[i][j]])

    return edge_list


# 绘制有向或无向图
def draw_graph(edge_list, directed=True):
    G = nx.DiGraph() if directed else nx.Graph()

    for edge in edge_list:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


# 将边列表转换为有向或无向图
def edge_list_to_graph(edge_list, directed=True):
    G = nx.DiGraph() if directed else nx.Graph()

    for edge in edge_list:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    return G


# 将无向图的邻接矩阵转换为边列表
def adj_matrix_to_undirected_edge_list(adj_matrix):
    edge_list = []
    num_nodes = len(adj_matrix)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):  # Iterate only over the upper triangle to avoid duplicate edges
            if adj_matrix[i][j] != 0:
                edge_list.append([i, j, adj_matrix[i][j]])

    return edge_list


# 将无向图的边列表转换为图
def undirected_edge_list_to_graph(edge_list):
    G = nx.Graph()

    for edge in edge_list:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    return G


# 计算最小生成树并打印
def calculate_and_print_mst(graph, directed=True):
    if directed:
        # 将有向图转换为无向图（忽略边的方向）
        undirected_graph = graph.to_undirected()
        mst = nx.minimum_spanning_tree(undirected_graph)
    else:
        mst = nx.minimum_spanning_tree(graph)

    print(f"{'有向图' if directed else '无向图'} 的最小生成树:")
    for edge in mst.edges(data=True):
        print(edge)

    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 绘制最小生成树
    pos = nx.spring_layout(mst)
    labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw(mst, pos, with_labels=True)
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
    plt.title(f"{'有向图' if directed else '无向图'} 的最小生成树")
    plt.show()





# 有向图示例
directed_edge_list = [[0, 1, 2], [1, 2, 1], [2, 0, 3], [2, 1, 4]]
directed_adj_matrix = edge_list_to_adj_matrix(directed_edge_list)
draw_graph(directed_edge_list, directed=True)

# 无向图示例
undirected_edge_list = [[0, 1, 2], [1, 2, 1], [2, 0, 3], [3, 0, 4]]
undirected_adj_matrix = edge_list_to_adj_matrix(undirected_edge_list, directed=False)
draw_graph(undirected_edge_list, directed=False)

# 打印有向图的点邻接矩阵
print("有向图的点邻接矩阵:")
print(directed_adj_matrix)

# 打印无向图的点邻接矩阵
print("无向图的点邻接矩阵:")
print(undirected_adj_matrix)

# 生成有向图并画出
generated_directed_graph = edge_list_to_graph(directed_edge_list, directed=True)
pos_directed = nx.spring_layout(generated_directed_graph)

# 绘制图
nx.draw(generated_directed_graph, pos_directed, with_labels=True)

# 绘制边的权值
edge_labels = nx.get_edge_attributes(generated_directed_graph, 'weight')
nx.draw_networkx_edge_labels(generated_directed_graph, pos_directed, edge_labels=edge_labels)

plt.title("有向图")
plt.show()

# 生成无向图并画出
undirected_generated_graph = undirected_edge_list_to_graph(undirected_edge_list)
pos_undirected = nx.spring_layout(undirected_generated_graph)

# 绘制图
nx.draw(undirected_generated_graph, pos_undirected, with_labels=True)

# 绘制边的权值
edge_labels_undirected = nx.get_edge_attributes(undirected_generated_graph, 'weight')
nx.draw_networkx_edge_labels(undirected_generated_graph, pos_undirected, edge_labels=edge_labels_undirected)

plt.title("无向图")
plt.show()


# 计算并打印有向图的最小生成树
calculate_and_print_mst(generated_directed_graph, directed=True)

# 计算并打印无向图的最小生成树
calculate_and_print_mst(undirected_generated_graph, directed=False)
