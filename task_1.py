import matplotlib.pyplot as plt
import networkx as nx

# Завдання 1. Використовуючи дані з файлу cities.csv, створіть список типу:
# cities = ['city 1', 'city 2', km]...]. З отриманого списку створіть граф.
# Візуалізуйте отриманий граф.

print('--- Task 1 ---')

G = nx.Graph()

# Визанчаю вузли та ребра (1-варіант).
G.add_edge('Hadiach', 'Zinkiv', weight=45)
G.add_edge('Hadiach', 'Lebedyn', weight=80)
G.add_edge('Hadiach', 'Myrhorod', weight=200)
G.add_edge('Hadiach', 'Zavodske', weight=100)
G.add_edge('Lokhvytsia', 'Hadiach', weight=35)
G.add_edge('Hadiach', 'Lokhvytsia', weight=40)
G.add_edge('Lebedyn', 'Zavodske', weight=175)
G.add_edge('Zinkiv', 'Lebedyn', weight=90)
G.add_edge('Zinkiv', 'Zavodske', weight=150)
G.add_edge('Lokhvytsia', 'Myrhorod', weight=100)


# Визанчаю вузли (2-варіант).
# cities = [('Hadiach', 'Zinkiv', 45), ('Hadiach', 'Lebedyn', 60),
#           ('Hadiach', 'Myrhorod', 61), ('Hadiach', 'Zavodske', 67),
#           ('Lokhvytsia', 'Hadiach', 81), ('Hadiach', 'Lokhvytsia', 94)]
##
# # Визанчаю список ребер.
# edges = [('Hadiach', 'Zinkiv'), ('Zinkiv', 'Lebedyn'),
#          ('Lebedyn', 'Zavodske'), ('Hadiach', 'Zavodske'),
#          ('Myrhorod', 'Zavodske'), ('Lokhvytsia', 'Hadiach'),
#          ('Hadiach', 'Vorozhba')]

# Додаю інформацію в об’єкт графа.
# G.add_nodes_from(cities)
# G.add_edges_from(edges)


# Тип візуалізації circular_layout.
pos=nx.circular_layout(G)
# Візуалізую граф.
nx.draw(G, pos, with_labels=True, font_weight='bold', font_size=10,
        font_color='blue', node_color='y', node_shape='o', width=2,
        edge_color="grey")
edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight)
plt.show()
print('Graph is ready. Look at right!')
