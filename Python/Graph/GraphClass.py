class Graph:
    def __init__(self, vertex_num = None):
        self.vtx_num = 0
        self.adj_list = [] # Adjacent vertex of a specific vertice
        self.vtx_arr = [] # True/False array that tells whether an vertex indice is existing or not
        if vertex_num:
            self.vtx_num = vertex_num
            self.vtx_arr = [True] * self.vtx_num
            self.adj_list = [[] for _ in range(self.vtx_num)] 
            # self.adj_list = [[]] * self.vtx_num 
    def is_empty(self):
        if self.vtx_num == 0:
            return True
        else: return False
    def add_vertex(self):
        for i in range(len(self.vtx_arr)):
            if self.vtx_arr[i] == False:
                self.vtx_num+=1
                self.vtx_arr[i] = True
                return i
        self.adj_list.append([])
        self.vtx_num += 1
        self.vtx_arr.append(True)
        return self.vtx_num - 1
    def delete_vertex(self,v):
        if v >= self.vtx_num:
            raise Exception(f"There is no vertex of {v}")
        if self.vtx_arr[v]:
            self.adj_list[v] = []
            self.vtx_num -= 1
            self.vtx_arr[v] = False
            for adj in self.adj_list: # deleting vertice 'v' from other adjacent list
                for vertex in adj:
                    if vertex == v:
                        adj.remove(vertex)
    def add_edge(self,u,v):
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        else:
            print("The specified edge already exists.")
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)
        else:
            print("The specified edge already exists.")
    def delete_edge(self,u,v):
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)
        else:
            print("There is no such edge")
        if u in self.adj_list[v]:
            self.adj_list[v].remove(u)
        else:
            print("There is no such edge")
    def adj(self,v):
        return self.adj_list[v]

if __name__ == "__main__":
    MyG = Graph(4)
    MyG.add_edge(0,1)
    MyG.add_edge(0,2)
    MyG.add_edge(0,3)
    MyG.add_edge(1,2)
    MyG.add_edge(2,3)
    MyG.add_edge(3,0)
    for vtx in range(len(MyG.vtx_arr)):
        if MyG.vtx_arr[vtx] == True:
            print(MyG.adj(vtx))