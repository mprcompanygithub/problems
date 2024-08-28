class DFS:
    def dfs_rec(self,adj,i,visited):
        visited[i]=True
        # print(visited)
        print(i,end=" ")
        for j in adj[i]:
            if not visited[j]:
                self.dfs_rec(adj,j,visited)

    def dfs(self,adj):
        visited={ i:False for i in adj}
        # print(visited)
        for i in adj:
            if not visited[i]:
                self.dfs_rec(adj,i,visited)
def addingAdjacentElement(adj,u,v):
    if u not in adj:
        adj[u]=[]
    if v not in adj:
        adj[v]=[]
    adj[u].append(v)
    adj[v].append(u)
# nodes is important
nodes = 5
adjacent_element={}
# initialise values
# n=[["A","B"], ["A", "C"], ["B", "C"], ["B", "D"],["C","D"],["C","E"],["E","D"]]
n=[["A","B"],["A","C"],["A","D"],["B","E"],["B","F"],["C","F"]]
for i in n:
    addingAdjacentElement(adjacent_element,i[0],i[1])
print(adjacent_element)
dfs=DFS()
dfs.dfs(adjacent_element)