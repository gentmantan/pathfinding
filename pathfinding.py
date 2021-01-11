graph_a = [[0, 1, 0, 0, 0], [0, 0, 0 ,0, 0], [0, 0, 0 ,0, 0], [0, 0, 0 ,0, 0]]

class Bfssearch:
    def __init__(self, graph):
        self.graph = graph
        self.pos = [(2, 2, 0)]
        self.postoadd = [] 
        self.numstep = 0
        self.checked = set()

    def maincheck(self):
        while self.pos:
            for x in self.pos[0]:                
                if x in self.checked:
                    print("Already checked")
                    del x
                           

                if x[0] == 0:
                    print("Left is bounded for " + str(x))
                elif self.graph[x[0]-1][x[1]] == 1:
                    #Check if left is blocked
                    print("Left is blocked for " + str(x))
                else:
                    self.postoadd.append((x[0]-1, x[1], x[2]+1))
                    print("Appended new at left")            
                
                if x[0] == len(self.graph)-1:
                    print("Right is bounded for " + str(x))
                elif self.graph[x[0]+1][x[1]] == 1:
                    #Check if right is blocked
                    print("Right is blocked for " + str(x))
                else:
                    self.pos.append((x[0]+1, x[1], x[2]+1))
                    print("Appended new at right")

 #           if x[1] == 0:
  #              print("Up is bounded for " + str(x)
   #         elif self.graph[x[0]][x[1]-1] == 1:
    #            print("Up is blocked for " + str(x))
     #       else:
      #          self.pos.append((x[0], x[1]-1, x[2]+1))
       #         print("Appended new at up")

        #    if x[1] == len(self.graph[0]):

            self.checked.add(x)
            del x

            
            # if self.graph[x[0]][x[1]-1] == 1 or x[1] == 0:
            #     #Check if up is blocked
            #     print("Up is blocked for " + str(x))
            #     self.checked.add(x)
            
            
            # if self.graph[x[0]][x[1]-1] == 1 or \
            # x[1] == len(self.graph[0]):
            #     #Check if down is blocked
            #     print("Down is blocked for " + str(x))
            #     self.checked.add(x)
        print(self.pos)
        print(self.checked)
                
        

search = Bfssearch(graph_a)
search.maincheck()
