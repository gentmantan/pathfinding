graph_a = [[0, 1, 2, 0, 0], [0, 0, 0 ,0, 0], [0, 0, 0 ,0, 0], [0, 0, 0 ,0, 0]]

class Bfssearch:
    def __init__(self, graph):
        self.graph = graph
        self.pos = [(2, 2, 0)]
        self.postoadd = [] 
        self.numstep = 0
        self.checked = set()
    def maincheck(self):
        while True:
            for x in self.pos:       
                if self.graph[x[0]][x[1]] == 2:
                    print(x)
                    return x         
                if x in self.checked:
                    print("Already checked")
                    break      

                if x[0] == 0:
                    print("Left is bounded for " + str(x))
                elif self.graph[x[0]-1][x[1]] == 1:
                    #Check if left is blocked
                    print("Left is blocked for " + str(x))
                elif (x[0]-1, x[1]) not in self.checked:
                    self.postoadd.append((x[0]-1, x[1]))
                    print("Appended new at left " + str(x))            
                
                if x[0] == len(self.graph)-1:
                    print("Right is bounded for " + str(x))
                elif self.graph[x[0]+1][x[1]] == 1:
                    #Check if right is blocked
                    print("Right is blocked for " + str(x))
                elif (x[0]+1, x[1]) not in self.checked:
                    self.postoadd.append((x[0]+1, x[1]))
                    print("Appended new at right " + str(x))
                
                if x[1] == 0:
                    print("Up is bounded for " + str(x))
                elif self.graph[x[0]][x[1]-1] == 1:
                    print("Up is blocked for " + str(x))
                elif (x[0], x[1]-1) not in self.checked:
                    self.postoadd.append((x[0]+1, x[1]))

                
                self.checked.add((x[0], x[1]))
            self.pos = self.postoadd
            self.postoadd = []
        print(self.pos)
        print(self.checked)
                
        

search = Bfssearch(graph_a)
search.maincheck()
