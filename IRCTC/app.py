import tkinter as tk
import staticData as s
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, []).append(to_node)
        self.edges.setdefault(to_node, []).append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

class IRCTCRoute:
    def __init__(self):
        self.graph = Graph()
        self.admin_logged_in = False
        for station in s.irctc_stations:
            self.add_station(station)
        for dis in s.random_distances:
            self.add_distance(dis[0],dis[1],dis[2])
            

    def add_station(self, station):
        if station not in self.graph.nodes:
            self.graph.add_node(station)
            return f"Station {station} added successfully."
        else:
            return f"Station {station} already exists."

    def add_distance(self, from_station, to_station, distance):
            if distance < 0:
                print("Invalid distance. Distance cannot be negative.")
            else:
                self.graph.add_edge(from_station, to_station, distance)
                print(f"Distance between {from_station} and {to_station} added successfully.")

    def search_route(self, initial_stop, target_stop):
        if initial_stop not in self.graph.nodes or target_stop not in self.graph.nodes:
            return "Invalid bus stops."
            
        temp=target_stop
        distances, paths = self._dijkstra(initial_stop)
        route = []
        while target_stop in paths:
            route.append(target_stop)
            target_stop = paths[target_stop]
        route.append(initial_stop)
        route.reverse()
        distance = distances[temp]
        # print(f"Shortest route from {initial_stop} to {route[-1]}: {' -> '.join(route)}")
        # print(f"Shortest distance: {distance}")
        return (route,distance)

    def _dijkstra(self, initial_node):
        visited = {initial_node: 0}
        path = {}
        nodes = set(self.graph.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.graph.edges[min_node]:
                weight = current_weight + self.graph.distances[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path


