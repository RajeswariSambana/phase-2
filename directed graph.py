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

obj=graph()
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    obj.addedge(a,b)    
obj.bfs()



