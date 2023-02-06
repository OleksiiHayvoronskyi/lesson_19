import matplotlib.pyplot as plt
import networkx as nx

# Завдання 2. Напишіть функцію знаходження найкоротшого маршруту між двома
# населеними пунктами, яка приймає як аргумент об’єкт графу і пару населених
# пунктів, а повертає маршрут і його протяжність.

print('--- Task 2 ---')


# Функція пошуку найкоротшого шляху.
def find_shortest_path(graph, start, goal):
    explored = []

    # Черга проходження.
    queue = [[start]]

    # Перевіряє, чи є початковий вузол шуканою точкою.
    if start == goal:
        print("The same node")
        return

    # Цикл обходження графа.
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Перевіряє, чи є сусідній вузол шуканою точкою.
                if neighbour == goal:
                    print(f'The shortest path from {start} up to {goal} is',
                          new_path)
                    return
            explored.append(node)
    print("So sorry, this path doesn't exist :(")
    return


if __name__ == "__main__":
    # Граф.
    graph = {
         'Hadiach': ['Zinkiv', 'Lebedyn'],
         'Zinkiv': ['Hadiach', 'Myrhorod', 'Lebedyn'],
         'Lebedyn': ['Zavodske', 'Myrhorod'],
         'Myrhorod': ['Zinkiv', 'Hadiach', 'Lebedyn']
    }

    G = nx.Graph(graph)
    # G.add_nodes_from([('Hadiach', 'Zinkiv'), ('Lebedyn', 'Myrhorod')])
    # G.add_edges_from([('Hadiach', 'Zinkiv'), ('Hadiach', 'Myrhorod'),
    #                   ('Zavodske', 'Zinkiv'), ('Myrhorod', 'Zinkiv')])
    print(nx.shortest_path_length(G, 'Hadiach', 'Zinkiv', weight='weight'))

    nx.draw(G, with_labels=True, font_weight='bold', font_size=10,
            font_color='blue', node_color='y', width=1.5, edge_color="grey")
    plt.show()

    # Викликаю функцію.
    find_shortest_path(graph, 'Zinkiv', 'Zavodske')

