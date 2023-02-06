import matplotlib.pyplot as plt
import networkx as nx

# Завдання 1. Використовуючи дані з файлу cities.csv, створіть список типу:
# cities = ['city 1', 'city 2', km]...]. З отриманого списку створіть граф.
# Візуалізуйте отриманий граф.


G = nx.Graph()

# Вузли.
cities = [('Hadiach', 'Zinkiv', 45), ('Hadiach', 'Lebedyn', 60),
          ('Hadiach', 'Myrhorod', 61), ('Hadiach', 'Zavodske', 67),
          ('Lokhvytsia', 'Hadiach', 81), ('Hadiach', 'Vorozhba', 94)]


# Визанчаю список ребер.
edges = [('Hadiach', 'Zinkiv'), ('Zinkiv', 'Lebedyn'),
         ('Lebedyn', 'Zavodske'), ('Hadiach', 'Zavodske'),
         ('Myrhorod', 'Zavodske'), ('Lokhvytsia', 'Hadiach'),
         ('Hadiach', 'Vorozhba')]

# Додаю інформацію в об’єкт графа.
G.add_nodes_from(cities)
G.add_edges_from(edges)

# Візуалізую граф.
nx.draw(G, with_labels=True, font_weight='light', font_size=8,
        font_color='blue', node_color='y', node_shape='o', width=1.5,
        edge_color="grey")
plt.show()
print('Graph is ready. Look at right!')
