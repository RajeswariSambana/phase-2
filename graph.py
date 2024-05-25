class graph:
    def __init__(self):
        self.graph={}

    def addedge(self,a,b):
        if a not in self.graph:
            self.graph[a]=[]
            self.graph[a].append(b)
        else:
            self.graph[a].append(b)
    
    def bfs(self):   # queue
        a=self.graph
        queue=[1]
        visited=set()
        visited.add(1)
        while queue:
            curr=queue.pop(0)
            print(curr,end=" ")
            for i in a[curr]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

    def dfs(self):      #stack
        a=self.graph
        queue=[1]
        visited=set()
        visited.add(1)
        while queue:
            curr=queue.pop()
            print(curr,end=" ")
            for i in a[curr]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)


obj=graph()
obj.addedge(1,2)
obj.addedge(2,1)
obj.addedge(3,2)
obj.addedge(1,3)
obj.addedge(4,2)
obj.addedge(4,5)
print(obj.graph)
obj.bfs()
print()
obj.dfs()