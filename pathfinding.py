graph_a = [[0, 1, 0, 0, 0], [0, 0, 0 ,0, 0], [0, 0, 0 ,0, 0], [0, 0, 0 ,0, 0]]

class Bfssearch:
    def __init__(self, graph):
        self.graph = graph
        self.pos = [(2, 2, 0)]
        self.numstep = 0
        self.checked = set()

    def maincheck(self):
        while self.pos:
            if self.pos[0] in self.checked:
                print("Already checked")
                del self.pos[0]
                break        

            if self.pos[0][0] == 0:
                print("Left is bounded for " + str(self.pos[0]))
            elif self.graph[self.pos[0][0]-1][self.pos[0][1]] == 1:
                #Check if left is blocked
                print("Left is blocked for " + str(self.pos[0]))
            else:
                self.pos.append((self.pos[0][0]-1, self.pos[0][1], self.pos[0][2]+1))
                print("Appended new at left")            
            
            # if self.graph[self.pos[0][0] + 1][self.pos[0][1]] == 1 or \
            # self.pos[0][0] == len(self.graph):
            #     #Check if right is blocked
            #     print("Right is blocked for " + str(self.pos[0]))
            # else:
            #     self.pos.append((self.pos[0][0]+1, self.pos[0][1], self.pos[0][2]+1))
            #     print("Appended new at right")
            
            self.checked.add(self.pos[0])
            del self.pos[0]

            
            # if self.graph[self.pos[0][0]][self.pos[0][1]-1] == 1 or self.pos[0][1] == 0:
            #     #Check if up is blocked
            #     print("Up is blocked for " + str(self.pos[0]))
            #     self.checked.add(self.pos[0])
            
            
            # if self.graph[self.pos[0][0]][self.pos[0][1]-1] == 1 or \
            # self.pos[0][1] == len(self.graph[0]):
            #     #Check if down is blocked
            #     print("Down is blocked for " + str(self.pos[0]))
            #     self.checked.add(self.pos[0])
        print(self.pos)
        print(self.checked)
                
        

search = Bfssearch(graph_a)
search.maincheck()