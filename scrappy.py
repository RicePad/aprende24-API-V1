# #create a tuple of nodes
# nodes = ('A', 'B', 'C', 'D', 'E')

# #create a double dicitionary of distances
# distances = {
#   'C': {"A": 1, "B": 7, "D": 2},
#   'A': {"B": 3, "C": 1},
#   'D': {"B": 5, "C": 2, "E": 7},
#   'B': {"A": 3, "B": 7, "B": 5},
#   'E': {"B": 1, "D": 7},
#   }

# #loop through a dictionary of array
# unvisited = {node: float("inf") for node in nodes }
# #create an empty dictionary 
# visited = {}
# #choose a start point
# current = "C"
# #set distance 
# currentDistance = 0 
# #set starting and distance in dictionary
# unvisited[current] = currentDistance

# #Djikstra's Algorithm:

# while True:
#     for neighbour, distance in distances[current].items():
#         print("k:{0}, v:{1}".format(neighbour, distance))

#         if neighbour not in unvisited: continue
#         newDistance = currentDistance + distance
        
#         if unvisited[neighbour] is float("inf") or unvisited[neighbour] > newDistance:
#             unvisited[neighbour] = newDistance
#     visited[current] = currentDistance
#     print("visited", visited)

#     del unvisited[current]
#     print("unvisited:", unvisited)      

#     if not unvisited: break
#     candidates = [node for node in unvisited.items() if node[1]]
#     print("candidates:", candidates)

#     current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
#     print("current:", current)
#     print("currentDistance:", currentDistance)
# print(visited)


from collections import deque
2	
3	def person_is_seller(name):
4	      return name[-1] == 'm'
5	
6	graph = {}
7	graph["you"] = ["alice", "bob", "claire"]
8	graph["bob"] = ["anuj", "peggy"]
9	graph["alice"] = ["peggy"]
10	graph["claire"] = ["thom", "jonny"]
11	graph["anuj"] = []
12	graph["peggy"] = []
13	graph["thom"] = []
14	graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]

    while search_queue:
        person = search_queue.pop_left()

        if person not in searched:
            if person_is_seller(person):
                print("person is seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
    