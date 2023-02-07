import matplotlib.pyplot as plt
import networkx as nx

# Завдання 2. Напишіть функцію знаходження найкоротшого маршруту між двома
# населеними пунктами, яка приймає як аргумент об’єкт графа і пару населених
# пунктів.


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

        # Перевірка, чи були вже у почтоному вузлі.
        if node not in explored:
            neighbours = graph[node]

            # Перевірка сусіднів вузлів.
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
    G.add_edges_from([
                      ('Zinkiv', 'Lebedyn', {'weight': 50}),
                      ('Hadiach', 'Myrhorod', {'weight': 160}),
                      ('Zavodske', 'Myrhorod', {'weight': 50}),
                      ('Zinkiv', 'Hadiach', {'weight': 80}),
                      ('Myrhorod', 'Zinkiv', {'weight': 140}),
                      ('Myrhorod', 'Lebedyn', {'weight': 40}),
                      ('Hadiach', 'Lebedyn', {'weight': 155}),
                      ('Zavodske', 'Hadiach', {'weight': 95}),
                      ('Zavodske', 'Lebedyn', {'weight': 100})
    ])

    # Тип візуалізації planar_layout.
    pos = nx.planar_layout(G)
    # Візуалізую граф.
    nx.draw(G, pos, with_labels=True, font_weight='bold', font_size=10,
            font_color='blue', node_color='y', width=1.5, edge_color="black")
    edge_weight = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
    plt.show()

    # Викликаю функцію.
    find_shortest_path(graph, 'Zinkiv', 'Zavodske')
